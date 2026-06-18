#!/usr/bin/env python3
"""ProjectForge coherence checker.

Supports root factory projects and generated projects. Root mode validates the
ProjectForge factory contract; generated mode validates the lighter project-local
contract produced by `tools/new_project.py`.
"""
from __future__ import annotations
import argparse, importlib.util, json, sys
from pathlib import Path
try:
    import yaml
except Exception:
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
 'workspace_config.yaml','tools/check_coherence.py','tools/run.py','tools/architecture_reality_audit.py','tools/recover_session.py',
 'architecture/architecture_state.md','architecture/architectureharvest/relevance_map.yaml',
 'architecture/architectureharvest/adoption_candidates.md','architecture/architectureharvest/rejected_candidates.md',
 'architecture/architectureharvest/review_history.md'
]


def has_text(path: Path, needle: str) -> bool:
    return path.exists() and needle.lower() in path.read_text(encoding='utf-8', errors='replace').lower()


def load_yaml_file(path: Path) -> dict:
    if not path.exists() or yaml is None:
        return {}
    data = yaml.safe_load(path.read_text(encoding='utf-8'))
    return data or {}


def metaharvest_provider_config(root: Path) -> dict:
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
    provider.setdefault('required_interface_files', [
        'README.md',
        'CONSTITUTION.md',
        'INTEGRATION.md',
        'source_registry.yaml',
        'retrieval/problem_catalog.yaml',
        'retrieval/retrieval_index.yaml',
        'retrieval/recommendation_rules.yaml',
    ])
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
    active_root = configured_root

    if mode != 'external':
        warns.append('MetaHarvest provider is not configured as external')

    if configured_root and not configured_root.exists():
        if status == 'active':
            blocks.append(f'configured external MetaHarvest provider path does not exist: {configured_root}')
        else:
            warns.append(f'configured external MetaHarvest provider path does not exist: {configured_root}')

    if active_root is None or not active_root.exists():
        blocks.append('no MetaHarvest provider interface path is available')
        return

    for rel in provider.get('required_interface_files') or []:
        if not (active_root / rel).exists():
            blocks.append(f'MetaHarvest provider missing required interface file: {active_root / rel}')


def detect_mode(root: Path) -> str:
    if (root / 'projectforge.yaml').exists():
        return 'root'
    return 'generated'


def check_common(root: Path, blocks: list[str], warns: list[str]) -> None:
    if (root/'logs'/'index').exists(): warns.append('logs/index exists; SQLite indexing should be opt-in, not default')
    if (root/'models'/'hardware_profile.yaml').exists(): warns.append('models/hardware_profile.yaml is redundant; use hardware/profile.yaml')
    if (root/'tools'/'update_folder_summaries.py').exists(): warns.append('legacy update_folder_summaries.py present; use update_context_summaries.py')
    if not has_text(root/'permissions'/'escalation_rules.yaml','push_requires_human_approval'):
        blocks.append('manual GitHub push rule missing from permissions/escalation_rules.yaml')
    if not has_text(root/'confidence'/'confidence_policy.yaml','codex_or_premium_model'):
        blocks.append('Codex-before-human capability escalation missing from confidence policy')
    if (root/'workspace').exists() and (root/'project.yaml').exists():
        py=(root/'project.yaml').read_text(encoding='utf-8', errors='replace').lower()
        if 'meta_project: true' not in py:
            warns.append('project contains workspace/; generated projects should usually use workspace_config.yaml instead')
    v=root/'tools'/'validate_dry_run.py'
    if v.exists():
        import importlib.util
        spec=importlib.util.spec_from_file_location('projectforge_validate_dry_run', v)
        mod=importlib.util.module_from_spec(spec)
        assert spec and spec.loader
        spec.loader.exec_module(mod)
        for report in (root/'simulation'/'dry_runs').glob('*.md') if (root/'simulation'/'dry_runs').exists() else []:
            if report.name in {'README.md','_SUMMARY.md'}:
                continue
            errs=mod.validate(report)
            if errs: blocks.append(f'invalid dry-run report: {report}: {errs[0]}')
    for rel in ['agents/planner.md','agents/coder.md','agents/reviewer.md','agents/auditor.md']:
        p=root/rel
        if p.exists() and 'context used' not in p.read_text(encoding='utf-8', errors='replace').lower():
            warns.append(f'{rel} does not explicitly require Context used reporting')
    for rel in ['agents/coder.md','agents/reviewer.md']:
        p=root/rel
        txt=p.read_text(encoding='utf-8', errors='replace').lower() if p.exists() else ''
        if p.exists() and ('knowledge/components.yaml' not in txt or 'knowledge/dependencies.yaml' not in txt):
            blocks.append(f'{rel} does not enforce knowledge-map checks before structural changes')
    if not has_text(root/'logs'/'logging_policy.yaml', 'raw events') and not has_text(root/'logs'/'logging_policy.yaml', 'raw_operational_record'):
        warns.append('logging policy does not clearly define logs as raw operational records')
    if not has_text(root/'metrics'/'metrics_policy.yaml', 'derived'):
        warns.append('metrics policy does not clearly define metrics as derived evidence')
    if not has_text(root/'recovery'/'continuity_framework.md', 'Standard ProjectForge closeout contract'):
        blocks.append('continuity framework missing standard closeout contract')
    if not has_text(root/'recovery'/'continuity_framework.md', 'Recover project state and continue work'):
        blocks.append('continuity framework missing fresh-session recovery command contract')
    if not has_text(root/'context'/'context_policy.yaml', 'standard_closeout_order'):
        blocks.append('context policy missing standard continuity closeout order')
    if not has_text(root/'context'/'context_policy.yaml', 'standard_closeout_command'):
        blocks.append('context policy missing standard closeout command')
    run_context_health(root, blocks, warns)


def run_context_health(root: Path, blocks: list[str], warns: list[str]) -> None:
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


def check_root(root: Path):
    blocks=[]; warns=[]
    for rel in ROOT_REQUIRED:
        if not (root/rel).exists(): blocks.append(f'missing required file: {rel}')
    check_common(root, blocks, warns)
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
    expected_projects_root = (
        load_yaml_file(root/'projectforge.yaml')
        .get('projectforge', {})
        .get('defaults', {})
        .get('workspace_projects_root')
    )
    configured_projects_root = canonical_paths.get('generated_projects_root')
    if not configured_projects_root:
        blocks.append('workspace policy missing canonical generated projects path')
    elif expected_projects_root and configured_projects_root != expected_projects_root:
        blocks.append('workspace policy generated projects path does not match projectforge.yaml defaults.workspace_projects_root')
    check_metaharvest_provider(root, blocks, warns)
    return blocks, warns


def check_generated(root: Path):
    blocks=[]; warns=[]
    for rel in GENERATED_REQUIRED:
        if not (root/rel).exists(): blocks.append(f'missing required file: {rel}')
    check_common(root, blocks, warns)
    if (root/'tools'/'new_project.py').exists():
        warns.append('generated project contains factory-only tools/new_project.py; prefer parent ProjectForge for scaffolding')
    if not has_text(root/'workspace_config.yaml', 'projectforge_root'):
        blocks.append('workspace_config.yaml must record parent projectforge_root')
    if has_text(root/'state'/'active_goal.md', 'Project:') and not has_text(root/'state'/'active_goal.md', 'Purpose'):
        warns.append('state/active_goal.md appears underpopulated')
    if not has_text(root/'architecture'/'architectureharvest'/'relevance_map.yaml', 'consult_required_during'):
        blocks.append('MetaHarvest compatibility relevance_map.yaml missing consultation trigger list')
    if not has_text(root/'architecture'/'architectureharvest'/'relevance_map.yaml', 'active'):
        blocks.append('MetaHarvest compatibility relevance_map.yaml missing active/staleness statuses')
    return blocks, warns


def check(root: Path, mode: str = 'auto'):
    if mode == 'auto':
        mode = detect_mode(root)
    if mode == 'root':
        return check_root(root)
    if mode == 'generated':
        return check_generated(root)
    raise ValueError(f'unknown mode: {mode}')


def main() -> int:
    ap=argparse.ArgumentParser(); ap.add_argument('--project', default='.'); ap.add_argument('--mode', choices=['auto','root','generated'], default='auto'); ap.add_argument('--json', action='store_true')
    ns=ap.parse_args(); root=Path(ns.project).resolve(); blocks,warns=check(root, ns.mode)
    if ns.json:
        print(json.dumps({'mode': ns.mode if ns.mode != 'auto' else detect_mode(root), 'blocks':blocks,'warnings':warns}, indent=2))
    else:
        for b in blocks: print(f'BLOCK: {b}', file=sys.stderr)
        for w in warns: print(f'WARN: {w}')
        print(f'coherence: {len(blocks)} block(s), {len(warns)} warning(s)')
    return 2 if blocks else 0
if __name__=='__main__': raise SystemExit(main())
