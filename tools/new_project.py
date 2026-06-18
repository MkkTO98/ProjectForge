#!/usr/bin/env python3
"""ProjectForge project initializer.

Creates a new project from shared components + template, records accepted setup
answers as decisions, and records unanswered items as deferred decision artifacts.

Hermes is the preferred interviewer. Treat `config/setup_questionnaire.yaml` as
a coverage map for Hermes-led adaptive questioning, then call this tool with
`--answers-json` to render the scaffold noninteractively. The terminal interview
remains as a manual fallback for non-Hermes operation.
"""
from __future__ import annotations
import argparse, datetime as dt, json, re, shutil, subprocess, sys
from pathlib import Path
try:
    import yaml
except Exception:
    yaml = None

UNDECIDED_DEFAULT = {"", "?", "unsure", "undecided", "ask later", "project specific", "project-specific", "later"}
SKIP_DIRS = {"__pycache__", ".pytest_cache", ".mypy_cache", ".ruff_cache", "htmlcov", "dist", "build"}
SKIP_SUFFIXES = (".pyc", ".pyo", ".pyd")
SKIP_NAMES = {".coverage"}
FALLBACK_QUESTIONS = [
    {"id":"purpose", "text":"What is the project's primary purpose?", "severity":"L3", "required_for_bootstrap": True, "section": "identity"},
    {"id":"success", "text":"What counts as success for v1?", "severity":"L3", "required_for_bootstrap": True, "section": "identity"},
    {"id":"autonomy", "text":"Agent autonomy?", "severity":"L3", "required_for_bootstrap": True, "section": "operating_model"},
]


def slugify(name: str) -> str:
    s = re.sub(r"[^a-zA-Z0-9]+", "_", name.strip().lower()).strip("_")
    return s or "project"


def load_yaml(path: Path):
    if yaml is None:
        raise RuntimeError("PyYAML required. Run with uvx --with pyyaml or install pyyaml in a venv.")
    return yaml.safe_load(path.read_text(encoding='utf-8')) or {}


def load_questions(base: Path):
    cfg = base/'config'/'setup_questionnaire.yaml'
    if not cfg.exists() or yaml is None:
        return FALLBACK_QUESTIONS, UNDECIDED_DEFAULT
    data = load_yaml(cfg).get('questionnaire', {})
    undecided = set(data.get('policy', {}).get('undecided_values', [])) or UNDECIDED_DEFAULT
    questions=[]
    for section in data.get('sections', []):
        for q in section.get('questions', []):
            q = dict(q); q['section'] = section.get('id','general'); questions.append(q)
    return questions or FALLBACK_QUESTIONS, {str(x).lower() for x in undecided}


def load_sufficiency_policy(base: Path) -> dict:
    path = base/'config'/'sufficiency_policy.yaml'
    if not path.exists() or yaml is None:
        return {}
    return load_yaml(path).get('sufficiency_policy', {})


def is_unresolved(value, undecided_values: set[str]) -> bool:
    return str(value if value is not None else '').strip().lower() in undecided_values


def validate_answers(answers: dict, questions: list[dict], undecided_values: set[str], policy: dict, allow_deferred_required: bool) -> list[str]:
    qids = {q['id'] for q in questions}
    must_pause = [qid for qid in policy.get('must_pause_if_unresolved', []) if qid in qids or qid in answers]
    unresolved = [qid for qid in must_pause if qid not in answers or is_unresolved(answers.get(qid), undecided_values)]
    if unresolved and not allow_deferred_required:
        return unresolved
    return []


def should_skip_template_artifact(path: Path) -> bool:
    parts = set(path.parts)
    return bool(parts & SKIP_DIRS) or path.name in SKIP_NAMES or path.name.endswith(SKIP_SUFFIXES) or path.name.endswith(".egg-info")


def copy_tree_render(src: Path, dst: Path, mapping: dict[str,str]):
    if not src.exists(): return
    for p in src.rglob('*'):
        rel = p.relative_to(src)
        if should_skip_template_artifact(rel):
            continue
        rel_s = str(rel)
        for k,v in mapping.items(): rel_s = rel_s.replace('{'+k+'}', v)
        target = dst/rel_s
        if p.is_dir():
            target.mkdir(parents=True, exist_ok=True)
        else:
            target.parent.mkdir(parents=True, exist_ok=True)
            try:
                text = p.read_text(encoding='utf-8')
                for k,v in mapping.items(): text = text.replace('{'+k+'}', v)
                target.write_text(text, encoding='utf-8')
            except UnicodeDecodeError:
                shutil.copy2(p, target)


def write_decision(project: Path, qid: str, question: str, answer: str, status: str, severity: str, section: str = 'setup'):
    date = dt.date.today().isoformat()
    fname = f"D-{date.replace('-','')}-setup-{qid}.md"
    content = f"""# Decision: Setup - {qid}\n\nDate: {date}\nStatus: {status}\nSeverity: {severity}\nSection: {section}\n\n## Question\n{question}\n\n## Answer\n{answer or 'Deferred.'}\n\n## Consequence\nAgents must consult this artifact before asking the same question again. If status is Deferred and the issue becomes blocking, create a question in `question_queue/pending/`.\n"""
    (project/'artifacts'/'decisions').mkdir(parents=True, exist_ok=True)
    (project/'artifacts'/'decisions'/fname).write_text(content, encoding='utf-8')


def interactive_answers(questions: list[dict]) -> dict:
    answers={}
    print("ProjectForge setup interview. Use 'undecided' to defer a question.\n")
    current=None
    for q in questions:
        if q.get('section') != current:
            current = q.get('section')
            print(f"\n== {current} ==")
        req = 'required' if q.get('required_for_bootstrap') else 'optional/deferable'
        ans = input(f"[{q.get('severity','L2')} | {req}] {q.get('text')}\n> ").strip()
        answers[q['id']] = ans
    return answers


def ensure_gitkeep_dirs(project: Path):
    for rel in ['artifacts/decisions','artifacts/tasks','artifacts/reports','artifacts/handoffs','logs/raw','logs/derived','logs/agents','question_queue/pending','question_queue/answered','question_queue/archive','context','knowledge','recovery','metrics/reports','metrics/recommendations','hardware','simulation/dry_runs','confidence','memory/archive','memory/deprecated_decisions','tests/invariants','docs']:
        d=project/rel; d.mkdir(parents=True, exist_ok=True); (d/'.gitkeep').touch(exist_ok=True)


def answer(answers: dict, key: str, default: str = 'Deferred.') -> str:
    value = str(answers.get(key, '')).strip()
    return value or default


def write_state_files(project: Path, name: str, template: str, answers: dict, unresolved: list[str]) -> None:
    today = dt.date.today().isoformat()
    (project/'state').mkdir(parents=True, exist_ok=True)
    (project/'state'/'active_goal.md').write_text(f"""# Active Goal\n\nProject: {name}\n\n## Purpose\n{answer(answers, 'purpose')}\n\n## V1 Success\n{answer(answers, 'success')}\n\n## Non-goals\n{answer(answers, 'non_goals', 'Deferred until needed.')}\n\n## Current first milestone\nBootstrap the ProjectForge-generated project, preserve setup decisions, and run generated-project coherence before broad implementation.\n\n## Last updated\n{today}\n""", encoding='utf-8')
    deferred = ', '.join(unresolved) if unresolved else 'Nonblocking unknowns are recorded as Deferred setup decisions.'
    (project/'state'/'project_state.md').write_text(f"""# Project State\n\nProject: {name}\nTemplate: {template}\nCreated by: ProjectForge\n\n## Operating context\n- Project type: {answer(answers, 'project_type')}\n- Primary users: {answer(answers, 'users', 'Deferred.')}\n- Agent autonomy: {answer(answers, 'autonomy')}\n- Command policy: {answer(answers, 'command_policy')}\n- Secrets policy: {answer(answers, 'secrets')}\n- Logging standard: {answer(answers, 'logging')}\n- Testing standard: {answer(answers, 'testing', 'ProjectForge default: run relevant tests before summarizing changes.')}\n- Documentation standard: {answer(answers, 'documentation_standard', 'Normal ProjectForge file-backed documentation.')}\n\n## Deferred or watchlist items\n{deferred}\n\n## Source of truth\nSetup answers are recorded under `artifacts/decisions/`. Future agents must update decision artifacts when durable policy changes.\n""", encoding='utf-8')
    (project/'state'/'architecture.md').write_text(f"""# Architecture\n\nProject: {name}\n\n## Initial architecture posture\n- Project type: {answer(answers, 'project_type')}\n- Language/runtime: {answer(answers, 'language', 'Deferred until implementation requires it.')}\n- Storage: {answer(answers, 'storage', 'Deferred until implementation requires it.')}\n- Deployment: {answer(answers, 'deployment', 'Deferred until implementation requires it.')}\n- External services: {answer(answers, 'external_services', 'Deferred; do not add paid or credentialed services without a decision artifact.')}\n\n## ArchitectureHarvest\nThis project includes lightweight MetaHarvest advisory placeholders under `architecture/architectureharvest/`. Consult them only at architecture decision points, scheduled architecture reviews, repeated failures, and user-requested improvement scans; do not force MetaHarvest into ordinary implementation tasks.\n\n## Guardrails\nUse the local constitution, permissions, dry-run policy, setup decision artifacts, `architecture/architecture_state.md`, and MetaHarvest compatibility relevance map before changing architecture.\n""", encoding='utf-8')


def should_register(base: Path, output_arg: str | None, output_root: Path, explicit_register: bool | None) -> bool:
    canonical = (base/'workspace'/'projects').resolve()
    if explicit_register is not None:
        return explicit_register
    return output_arg is None or output_root.resolve() == canonical


def main() -> int:
    base = Path(__file__).resolve().parents[1]
    canonical_output = base/'workspace'/'projects'
    ap = argparse.ArgumentParser()
    ap.add_argument('--name', required=True)
    ap.add_argument('--template', default='default_project', choices=['default_project','python_data_project','web_project','research_project'])
    ap.add_argument('--output', default=None, help='Project parent directory. Defaults to this ProjectForge root workspace/projects.')
    ap.add_argument('--answers-json')
    ap.add_argument('--noninteractive', action='store_true')
    ap.add_argument('--allow-deferred-required', action='store_true', help='Allow unresolved must-pause sufficiency items and record them as Deferred decisions.')
    group = ap.add_mutually_exclusive_group()
    group.add_argument('--register', dest='register', action='store_true', default=None, help='Force registration in the parent workspace registry.')
    group.add_argument('--no-register', dest='register', action='store_false', help='Do not register the generated project.')
    ns = ap.parse_args()

    template = base/'templates'/ns.template
    shared = base/'templates'/'_shared_project'
    if not template.exists():
        print(f'Template not found: {template}', file=sys.stderr); return 2
    output_root = Path(ns.output).resolve() if ns.output else canonical_output.resolve()
    slug = slugify(ns.name); out = output_root/slug
    if out.exists():
        print(f'Output already exists: {out}', file=sys.stderr); return 3

    questions, undecided_values = load_questions(base)
    if ns.answers_json:
        answers = json.loads(Path(ns.answers_json).read_text(encoding='utf-8'))
    elif ns.noninteractive:
        answers = {}
    else:
        answers = interactive_answers(questions)
    policy = load_sufficiency_policy(base)
    unresolved = validate_answers(answers, questions, undecided_values, policy, ns.allow_deferred_required)
    if unresolved:
        print('ERROR: unresolved must-pause setup answers: ' + ', '.join(unresolved), file=sys.stderr)
        print('Provide answers or pass --allow-deferred-required to intentionally create Deferred decisions.', file=sys.stderr)
        return 4

    mapping={
        'project_name': ns.name, 'project_slug': slug, 'date': dt.date.today().isoformat(),
        'projectforge_root': str(base.resolve()), 'workspace_root': str((base/'workspace').resolve()),
        'projects_root': str(canonical_output.resolve()),
    }
    copy_tree_render(shared, out, mapping)
    copy_tree_render(template, out, mapping)
    factory_tool = out/'tools'/'new_project.py'
    if factory_tool.exists():
        factory_tool.unlink()
    ensure_gitkeep_dirs(out)

    deferred_ids = []
    for q in questions:
        ans = str(answers.get(q['id'], 'undecided')).strip()
        status = 'Deferred' if ans.lower() in undecided_values else 'Accepted'
        if status == 'Deferred': deferred_ids.append(q['id'])
        write_decision(out, q['id'], q.get('text',''), ans, status, q.get('severity','L2'), q.get('section','setup'))
    write_state_files(out, ns.name, ns.template, answers, deferred_ids)
    (out/'state'/'recent_changes.md').write_text(f"# Recent Changes\n\n- {dt.date.today().isoformat()}: Project initialized by ProjectForge using `{ns.template}`.\n", encoding='utf-8')

    updater = base/'tools'/'update_context_summaries.py'
    if updater.exists():
        subprocess.run([sys.executable, str(updater), '--project', str(out), '--core-only'], check=False)

    if should_register(base, ns.output, output_root, ns.register):
        workspace = base/'workspace'
        registrar = base/'tools'/'register_project.py'
        if registrar.exists() and workspace.exists():
            result = subprocess.run([sys.executable, str(registrar), '--workspace', str(workspace), '--project', str(out), '--name', ns.name], check=False, text=True, capture_output=True)
            if result.returncode != 0:
                print(result.stderr, file=sys.stderr, end='')
                return result.returncode
    print(out)
    return 0
if __name__ == '__main__':
    raise SystemExit(main())
