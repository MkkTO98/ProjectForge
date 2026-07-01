#!/usr/bin/env python3
"""ProjectForge coherence checker.

Supports root factory projects and generated projects. Root mode validates the
ProjectForge factory contract; generated mode validates the lighter project-local
contract produced by `tools/new_project.py`.

System 5 responsibility: deterministic structural and project-local invariant
checks only. This tool does not judge project quality, run CI, manage workflow,
or replace human architectural judgment.
"""
from __future__ import annotations

import argparse
import importlib.util
import json
import re
import sys
from pathlib import Path
from typing import Any

try:
    import yaml
except Exception:  # pragma: no cover - optional dependency
    yaml = None

ROOT_REQUIRED = [
    'CONSTITUTION.md','projectforge.yaml','state/active_goal.md','state/project_state.md',
    'state/architecture.md','permissions/allowlist.yaml','permissions/denylist.yaml',
    'permissions/escalation_rules.yaml','context/context_policy.yaml','simulation/dry_run_policy.yaml',
    'metrics/metrics_policy.yaml','recovery/escalation_policy.yaml','recovery/continuity_framework.md','hardware/profile.yaml',
    'automation/orchestration_schedule.yaml','docs/OPERATOR_MANUAL.md','tools/architecture_reality_audit.py','tools/recover_session.py'
]

GENERATED_REQUIRED = [
    'CONSTITUTION.md','AGENTS.md','project.yaml','state/active_goal.md','state/project_state.md',
    'state/architecture.md','permissions/allowlist.yaml','permissions/denylist.yaml',
    'permissions/escalation_rules.yaml','context/context_policy.yaml','simulation/dry_run_policy.yaml',
    'metrics/metrics_policy.yaml','recovery/escalation_policy.yaml','recovery/continuity_framework.md','hardware/profile.yaml',
    'tools/check_coherence.py','tools/run.py','tools/architecture_reality_audit.py','tools/recover_session.py',
    'tools/context_health.py','tools/build_context.py','architecture/architecture_state.md'
]

IDENTITY_SECTIONS = [
    'Project identity','Scope','Explicit non-scope','Responsibility boundaries',
    'Operating principles','Instruction hierarchy','Generated-project independence'
]

PRIORITY_1_FILES = [
    'CONSTITUTION.md','state/active_goal.md','state/project_state.md',
    'state/architecture.md','context/latest_handoff.md'
]

GOVERNANCE_DIRS = [
    'artifacts/tasks','artifacts/decisions','artifacts/reports','artifacts/handoffs'
]
GOVERNANCE_TEMPLATES = {
    'artifacts/tasks/TEMPLATE.md': ['Status:', '## Request', '## Scope', '## Explicit non-scope', '## Methodology slice', '## Governance links', '## Outcome'],
    'artifacts/decisions/TEMPLATE.md': ['Status:', '## Decision', '## Rationale', '## Alternatives considered', '## Consequences', '## Approval boundary'],
    'artifacts/reports/TEMPLATE.md': ['Date:', 'Type:', 'Status:', '## Evidence consulted', '## Findings', '## Methodology observations', '## Follow-up governance'],
}
APPROVAL_TERMS = ['destructive', 'external publication', 'remote push', 'paid resources', 'credential', 'production data', 'major scope', 'architecture changes']
FORBIDDEN_GENERATED_TERMS = ['ProjectForge', 'EIP', 'MacroForge', 'KnowledgeForge', 'MetaHarvest', 'ArchitectureHarvest', 'architectureharvest']
UNRESOLVED_PLACEHOLDERS = ['{' + 'project_name}', '{' + 'identity_']
METHODOLOGY_TERMS = ['bounded implementation slice', 'explicit non-goals', 'implementation boundary', 'readiness', 'success criteria', 'verification expectations', 'expected evidence', 'post-slice decision', 'Evidence-gated architectural evolution']
METHODOLOGY_FORBIDDEN = ['scrum', 'kanban', 'sprint', 'issue tracker', 'workflow engine', 'quality management system', 'ci/cd']


def read(path: Path) -> str:
    return path.read_text(encoding='utf-8', errors='replace') if path.exists() else ''


def has_text(path: Path, needle: str) -> bool:
    return needle.lower() in read(path).lower()


def load_yaml_file(path: Path) -> dict[str, Any]:
    if not path.exists() or yaml is None:
        return {}
    data = yaml.safe_load(path.read_text(encoding='utf-8'))
    return data or {}


def add_evidence(evidence: list[dict[str, Any]], check: str, files: list[str], detail: str) -> None:
    evidence.append({'check': check, 'files_checked': files, 'detail': detail})


def require_text(path: Path, needles: list[str], blocks: list[str], label: str) -> None:
    text = read(path).lower()
    for needle in needles:
        if needle.lower() not in text:
            blocks.append(f'{label} missing required text: {needle}')


GENERATED_INDEPENDENCE_SCAN_FILES = [
    'CONSTITUTION.md', 'AGENTS.md', 'project.yaml',
    'state/active_goal.md', 'state/project_state.md', 'state/architecture.md',
    'context/context_policy.yaml', 'context/latest_handoff.md',
    'instructions/GENERAL_INSTRUCTIONS.md', 'instructions/WORK_EXECUTION_METHODOLOGY.md',
    'artifacts/tasks/TEMPLATE.md', 'artifacts/decisions/TEMPLATE.md', 'artifacts/reports/TEMPLATE.md',
]


def iter_project_text_files(root: Path):
    # Generated-project independence is an authority/context invariant, not a
    # ban on historical tool names in copied local helper scripts or summaries.
    for rel in GENERATED_INDEPENDENCE_SCAN_FILES:
        path = root / rel
        if path.exists() and path.is_file():
            yield path


def check_identity_contract(root: Path, blocks: list[str], warns: list[str], evidence: list[dict[str, Any]], *, base: str = '') -> None:
    constitution = root / base / 'CONSTITUTION.md'
    agents = root / base / 'AGENTS.md'
    require_text(constitution, IDENTITY_SECTIONS, blocks, f'{base}CONSTITUTION.md' if base else 'CONSTITUTION.md')
    if agents.exists() and 'constitution.md' not in read(agents).lower():
        blocks.append(f'{base}AGENTS.md does not point to CONSTITUTION.md as identity authority')
    add_evidence(evidence, 'identity structural contract', [str(Path(base) / 'CONSTITUTION.md'), str(Path(base) / 'AGENTS.md')], 'checked identity sections, instruction hierarchy, independence doctrine, and AGENTS pointer')


def check_generated_independence(root: Path, blocks: list[str], evidence: list[dict[str, Any]]) -> None:
    hits: list[str] = []
    placeholder_hits: list[str] = []
    for path in iter_project_text_files(root):
        rel = str(path.relative_to(root)).replace('\\', '/')
        text = read(path)
        for term in FORBIDDEN_GENERATED_TERMS:
            if term.lower() in text.lower():
                hits.append(f'{rel}: {term}')
        for marker in UNRESOLVED_PLACEHOLDERS:
            if marker in text:
                placeholder_hits.append(f'{rel}: {marker}')
    if hits:
        blocks.append('generated project contains forbidden external-authority references: ' + '; '.join(hits[:20]))
    if placeholder_hits:
        blocks.append('generated project contains unresolved template placeholders: ' + '; '.join(placeholder_hits[:20]))
    add_evidence(evidence, 'generated-project independence scan', ['**/*.{md,yaml,yml,json,toml,txt,py}'], f'forbidden_reference_hits={len(hits)}, unresolved_placeholder_hits={len(placeholder_hits)}')


def context_priority_files_from_policy(root: Path) -> list[str]:
    policy = load_yaml_file(root / 'context' / 'context_policy.yaml').get('context_policy', {})
    priority = policy.get('context_loading_hierarchy', {}).get('priority_1', {})
    return list(priority.get('files') or [])


def check_context_contract(root: Path, blocks: list[str], evidence: list[dict[str, Any]], *, base: str = '') -> None:
    prefix = Path(base)
    if not base:
        for rel in PRIORITY_1_FILES:
            if not (root / prefix / rel).exists():
                blocks.append(f'missing required startup file: {prefix / rel}')
    policy_files = context_priority_files_from_policy(root / prefix)
    if policy_files and policy_files != PRIORITY_1_FILES:
        blocks.append(f'context policy priority_1 files do not match canonical startup files: {policy_files}')
    for rel in ['tools/build_context.py', 'tools/recover_session.py', 'tools/context_health.py']:
        if not (root / prefix / rel).exists():
            blocks.append(f'missing required context/recovery tool: {prefix / rel}')
    agents = root / prefix / 'AGENTS.md'
    if agents.exists():
        require_text(agents, ['not mandatory startup context', 'Repository-wide exploration is not default startup behavior'], blocks, f'{prefix / "AGENTS.md"}')
    add_evidence(evidence, 'context and recovery structural contract', [str(prefix / rel) for rel in PRIORITY_1_FILES] + [str(prefix / 'context/context_policy.yaml')], 'checked startup files, policy priority_1 consistency, active_context boundary, and required recovery/context tools')


def check_governance_contract(root: Path, blocks: list[str], evidence: list[dict[str, Any]], *, base: str = '') -> None:
    prefix = Path(base)
    for rel in GOVERNANCE_DIRS:
        if not (root / prefix / rel).is_dir():
            blocks.append(f'missing governance directory: {prefix / rel}')
    for rel, headings in GOVERNANCE_TEMPLATES.items():
        p = root / prefix / rel
        if not p.exists():
            blocks.append(f'missing governance template: {prefix / rel}')
            continue
        require_text(p, headings, blocks, str(prefix / rel))
    agents = root / prefix / 'AGENTS.md'
    if agents.exists():
        require_text(agents, APPROVAL_TERMS, blocks, str(prefix / 'AGENTS.md'))
    add_evidence(evidence, 'governance structural contract', [str(prefix / rel) for rel in GOVERNANCE_DIRS] + [str(prefix / rel) for rel in GOVERNANCE_TEMPLATES], 'checked governance directories, template headings, and approval boundary terms')


def check_methodology_contract(root: Path, blocks: list[str], evidence: list[dict[str, Any]], *, base: str = '') -> None:
    prefix = Path(base)
    methodology = root / prefix / 'instructions' / 'WORK_EXECUTION_METHODOLOGY.md'
    if not methodology.exists():
        blocks.append(f'missing methodology file: {prefix / "instructions/WORK_EXECUTION_METHODOLOGY.md"}')
    else:
        require_text(methodology, METHODOLOGY_TERMS, blocks, str(prefix / 'instructions/WORK_EXECUTION_METHODOLOGY.md'))
        require_text(methodology, ['does not define project identity', 'context loading', 'governance record lifecycles', 'validation policy', 'deterministic validators'], blocks, str(prefix / 'instructions/WORK_EXECUTION_METHODOLOGY.md'))
        text = read(methodology).lower()
        for term in METHODOLOGY_FORBIDDEN:
            if term in text and f'not {term}' not in text and f'not a {term}' not in text:
                blocks.append(f'methodology file contains prohibited workflow/platform concept outside a clear anti-goal: {term}')
    for rel in ['AGENTS.md', 'instructions/GENERAL_INSTRUCTIONS.md']:
        p = root / prefix / rel
        if p.exists() and 'work_execution_methodology.md' not in read(p).lower():
            blocks.append(f'{prefix / rel} does not reference WORK_EXECUTION_METHODOLOGY.md')
    for rel, needle in [('artifacts/tasks/TEMPLATE.md', '## Methodology slice'), ('artifacts/reports/TEMPLATE.md', '## Methodology observations')]:
        if not has_text(root / prefix / rel, needle):
            blocks.append(f'{prefix / rel} missing methodology section: {needle}')
    add_evidence(evidence, 'work execution methodology structural contract', [str(prefix / 'instructions/WORK_EXECUTION_METHODOLOGY.md'), str(prefix / 'AGENTS.md'), str(prefix / 'artifacts/tasks/TEMPLATE.md'), str(prefix / 'artifacts/reports/TEMPLATE.md')], 'checked methodology file, references, template sections, separation wording, and prohibited workflow concepts')


def metaharvest_provider_config(root: Path) -> dict[str, Any]:
    cfg = load_yaml_file(root / 'projectforge.yaml').get('projectforge', {})
    provider = dict(cfg.get('metaharvest_provider') or {})
    policy = load_yaml_file(root / 'context' / 'context_policy.yaml').get('context_policy', {})
    ah = policy.get('architecture_harvest') or {}
    if ah:
        provider.setdefault('provider', ah.get('provider'))
        provider.setdefault('status', ah.get('provider_status'))
        provider.setdefault('path', ah.get('root_location'))
        provider.setdefault('compatibility', {})
        provider['compatibility'].setdefault('generated_project_path', ah.get('generated_project_location'))
    provider.setdefault('provider', 'external')
    provider.setdefault('status', 'active')
    provider.setdefault('path', '/home/mkkto/srv/EIP/projects/MetaHarvest')
    provider.setdefault('required_interface_files', ['README.md','CONSTITUTION.md','INTEGRATION.md','source_registry.yaml','retrieval/problem_catalog.yaml','retrieval/retrieval_index.yaml','retrieval/recommendation_rules.yaml'])
    return provider


def resolve_provider_path(root: Path, value: str | None) -> Path | None:
    if not value:
        return None
    path = Path(value)
    return path if path.is_absolute() else root / path


def check_metaharvest_provider(root: Path, blocks: list[str], warns: list[str]) -> None:
    provider = metaharvest_provider_config(root)
    compatibility = provider.get('compatibility') or {}
    generated_path = compatibility.get('generated_project_path') or provider.get('generated_project_location')
    if generated_path != 'architecture/architectureharvest':
        blocks.append('MetaHarvest generated-project compatibility path must remain architecture/architectureharvest')
    mode = provider.get('provider')
    status = provider.get('status')
    configured_root = resolve_provider_path(root, provider.get('path'))
    if mode != 'external':
        warns.append('MetaHarvest provider is not configured as external')
    if configured_root and not configured_root.exists():
        if status == 'active':
            blocks.append(f'configured external MetaHarvest provider path does not exist: {configured_root}')
        else:
            warns.append(f'configured external MetaHarvest provider path does not exist: {configured_root}')
    if configured_root is None or not configured_root.exists():
        blocks.append('no MetaHarvest provider interface path is available')
        return
    for rel in provider.get('required_interface_files') or []:
        if not (configured_root / rel).exists():
            blocks.append(f'MetaHarvest provider missing required interface file: {configured_root / rel}')


def detect_mode(root: Path) -> str:
    return 'root' if (root / 'projectforge.yaml').exists() else 'generated'


def check_common(root: Path, blocks: list[str], warns: list[str], evidence: list[dict[str, Any]]) -> None:
    if (root/'logs'/'index').exists(): warns.append('logs/index exists; SQLite indexing should be opt-in, not default')
    if (root/'models'/'hardware_profile.yaml').exists(): warns.append('models/hardware_profile.yaml is redundant; use hardware/profile.yaml')
    if (root/'tools'/'update_folder_summaries.py').exists(): warns.append('legacy update_folder_summaries.py present; use update_context_summaries.py')
    if not has_text(root/'permissions'/'escalation_rules.yaml','push_requires_human_approval'):
        blocks.append('manual GitHub push rule missing from permissions/escalation_rules.yaml')
    if not has_text(root/'confidence'/'confidence_policy.yaml','codex_or_premium_model'):
        blocks.append('Codex-before-human capability escalation missing from confidence policy')
    if (root/'workspace').exists() and (root/'project.yaml').exists():
        py=read(root/'project.yaml').lower()
        if 'meta_project: true' not in py:
            warns.append('project contains workspace/; generated projects should usually avoid embedded parent workspaces')
    v=root/'tools'/'validate_dry_run.py'
    if v.exists():
        spec=importlib.util.spec_from_file_location('projectforge_validate_dry_run', v)
        mod=importlib.util.module_from_spec(spec)
        assert spec and spec.loader
        spec.loader.exec_module(mod)
        checked = 0
        for report in (root/'simulation'/'dry_runs').glob('*.md') if (root/'simulation'/'dry_runs').exists() else []:
            if report.name in {'README.md','_SUMMARY.md'}:
                continue
            checked += 1
            errs=mod.validate(report)
            if errs: blocks.append(f'invalid dry-run report: {report}: {errs[0]}')
        add_evidence(evidence, 'dry-run report structural validation', ['simulation/dry_runs/*.md'], f'checked_reports={checked}')
    for rel in ['agents/planner.md','agents/coder.md','agents/reviewer.md','agents/auditor.md']:
        p=root/rel
        if p.exists() and 'context used' not in read(p).lower():
            warns.append(f'{rel} does not explicitly require Context used reporting')
    for rel in ['agents/coder.md','agents/reviewer.md']:
        p=root/rel
        txt=read(p).lower()
        if p.exists() and ('knowledge/components.yaml' not in txt or 'knowledge/dependencies.yaml' not in txt):
            blocks.append(f'{rel} does not enforce knowledge-map checks before structural changes')
    if not has_text(root/'logs'/'logging_policy.yaml', 'raw events') and not has_text(root/'logs'/'logging_policy.yaml', 'raw_operational_record'):
        warns.append('logging policy does not clearly define logs as raw operational records')
    if not has_text(root/'metrics'/'metrics_policy.yaml', 'derived'):
        warns.append('metrics policy does not clearly define metrics as derived evidence')
    if not has_text(root/'recovery'/'continuity_framework.md', 'Standard project closeout contract'):
        blocks.append('continuity framework missing standard closeout contract')
    if not has_text(root/'recovery'/'continuity_framework.md', 'Recover project state and continue work'):
        blocks.append('continuity framework missing fresh-session recovery command contract')
    if not has_text(root/'context'/'context_policy.yaml', 'standard_closeout_order'):
        blocks.append('context policy missing standard continuity closeout order')
    if not has_text(root/'context'/'context_policy.yaml', 'standard_closeout_command'):
        blocks.append('context policy missing standard closeout command')
    run_context_health(root, blocks, warns, evidence)


def run_context_health(root: Path, blocks: list[str], warns: list[str], evidence: list[dict[str, Any]]) -> None:
    checker = root / 'tools' / 'context_health.py'
    if not checker.exists():
        warns.append('tools/context_health.py missing; context-size hygiene is not automated')
        return
    spec = importlib.util.spec_from_file_location('projectforge_context_health', checker)
    assert spec and spec.loader
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    report = mod.check(root)
    blocks.extend(f'context health: {item}' for item in report.get('blocks', []))
    warns.extend(f'context health: {item}' for item in report.get('warnings', []))
    add_evidence(evidence, 'context health validation', report.get('files_checked', []), f"blocks={len(report.get('blocks', []))}, warnings={len(report.get('warnings', []))}, measured={len(report.get('measured', []))}")


def check_root(root: Path):
    blocks: list[str] = []
    warns: list[str] = []
    evidence: list[dict[str, Any]] = []
    for rel in ROOT_REQUIRED:
        if not (root/rel).exists(): blocks.append(f'missing required file: {rel}')
    check_common(root, blocks, warns, evidence)
    if not has_text(root/'automation'/'orchestration_schedule.yaml', 'check_coherence'):
        blocks.append('automation schedule does not run check_coherence')
    if not has_text(root/'automation'/'orchestration_schedule.yaml', 'validate_dry_run'):
        blocks.append('automation schedule does not run validate_dry_run')
    if not has_text(root/'automation'/'orchestration_schedule.yaml', 'review_metrics'):
        blocks.append('automation schedule does not run review_metrics')
    if not has_text(root/'automation'/'orchestration_schedule.yaml', 'architecture_reality_audit'):
        blocks.append('automation schedule does not run architecture_reality_audit')
    workspace_policy = load_yaml_file(root/'workspace'/'workspace_policy.yaml').get('workspace_policy', {})
    canonical_paths = workspace_policy.get('canonical_paths') or {}
    expected_projects_root = load_yaml_file(root/'projectforge.yaml').get('projectforge', {}).get('defaults', {}).get('workspace_projects_root')
    configured_projects_root = canonical_paths.get('generated_projects_root')
    if not configured_projects_root:
        blocks.append('workspace policy missing canonical generated projects path')
    elif expected_projects_root and configured_projects_root != expected_projects_root:
        blocks.append('workspace policy generated projects path does not match projectforge.yaml defaults.workspace_projects_root')
    check_metaharvest_provider(root, blocks, warns)
    # Root factory validation checks the generated-project template contract without treating templates as active project state.
    base = 'templates/_shared_project'
    check_identity_contract(root, blocks, warns, evidence, base=base)
    check_context_contract(root, blocks, evidence, base=base)
    check_governance_contract(root, blocks, evidence, base=base)
    check_methodology_contract(root, blocks, evidence, base=base)
    return blocks, warns, evidence


def check_generated(root: Path):
    blocks: list[str] = []
    warns: list[str] = []
    evidence: list[dict[str, Any]] = []
    for rel in GENERATED_REQUIRED:
        if not (root/rel).exists(): blocks.append(f'missing required file: {rel}')
    check_common(root, blocks, warns, evidence)
    if (root/'tools'/'new_project.py').exists():
        warns.append('generated project contains factory-only tools/new_project.py')
    if has_text(root/'state'/'active_goal.md', 'Project:') and not has_text(root/'state'/'active_goal.md', 'Purpose'):
        warns.append('state/active_goal.md appears underpopulated')
    check_identity_contract(root, blocks, warns, evidence)
    check_context_contract(root, blocks, evidence)
    check_governance_contract(root, blocks, evidence)
    check_methodology_contract(root, blocks, evidence)
    check_generated_independence(root, blocks, evidence)
    return blocks, warns, evidence


def check(root: Path, mode: str = 'auto'):
    if mode == 'auto':
        mode = detect_mode(root)
    if mode == 'root':
        blocks, warns, _ = check_root(root)
        return blocks, warns
    if mode == 'generated':
        blocks, warns, _ = check_generated(root)
        return blocks, warns
    raise ValueError(f'unknown mode: {mode}')


def check_with_evidence(root: Path, mode: str = 'auto') -> dict[str, Any]:
    if mode == 'auto':
        mode = detect_mode(root)
    if mode == 'root':
        blocks, warns, evidence = check_root(root)
    elif mode == 'generated':
        blocks, warns, evidence = check_generated(root)
    else:
        raise ValueError(f'unknown mode: {mode}')
    return {
        'mode': mode,
        'command': 'python3 tools/check_coherence.py --project <project> --json',
        'project': str(root.resolve()),
        'blocks': blocks,
        'warnings': warns,
        'evidence': evidence,
    }


def main() -> int:
    ap=argparse.ArgumentParser(); ap.add_argument('--project', default='.'); ap.add_argument('--mode', choices=['auto','root','generated'], default='auto'); ap.add_argument('--json', action='store_true')
    ns=ap.parse_args(); root=Path(ns.project).resolve(); report=check_with_evidence(root, ns.mode)
    if ns.json:
        print(json.dumps(report, indent=2))
    else:
        for b in report['blocks']: print(f'BLOCK: {b}', file=sys.stderr)
        for w in report['warnings']: print(f'WARN: {w}')
        print(f"coherence: {len(report['blocks'])} block(s), {len(report['warnings'])} warning(s)")
    return 2 if report['blocks'] else 0
if __name__=='__main__': raise SystemExit(main())
