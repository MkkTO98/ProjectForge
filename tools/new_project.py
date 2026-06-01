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
import argparse, datetime as dt, json, re, shutil, sys
from pathlib import Path
try:
    import yaml
except Exception:
    yaml = None

UNDECIDED_DEFAULT = {"", "?", "unsure", "undecided", "ask later", "project specific", "project-specific", "later"}

FALLBACK_QUESTIONS = [
    {"id":"purpose", "text":"What is the project's primary purpose?", "severity":"L3", "required_for_bootstrap": True},
    {"id":"success", "text":"What counts as success for v1?", "severity":"L3", "required_for_bootstrap": True},
    {"id":"autonomy", "text":"Agent autonomy?", "severity":"L3", "required_for_bootstrap": True},
]

def slugify(name: str) -> str:
    s = re.sub(r"[^a-zA-Z0-9]+", "_", name.strip().lower()).strip("_")
    return s or "project"

def load_yaml(path: Path):
    if yaml is None:
        raise RuntimeError("PyYAML required. Run: python3 -m pip install pyyaml")
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

def copy_tree_render(src: Path, dst: Path, mapping: dict[str,str]):
    if not src.exists(): return
    for p in src.rglob('*'):
        rel = p.relative_to(src)
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
    for rel in ['artifacts/decisions','artifacts/tasks','artifacts/reports','artifacts/handoffs','logs/raw','logs/derived','logs/agents','question_queue/pending','question_queue/answered','question_queue/archive','context','knowledge','recovery','metrics/reports','metrics/recommendations','hardware','simulation/dry_runs','confidence','memory/archive','memory/deprecated_decisions','tests/invariants']:
        d=project/rel; d.mkdir(parents=True, exist_ok=True); (d/'.gitkeep').touch(exist_ok=True)

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument('--name', required=True)
    ap.add_argument('--template', default='default_project', choices=['default_project','python_data_project','web_project','research_project'])
    ap.add_argument('--output', default='/home/mkkto/srv/projectforge/workspace/projects')
    ap.add_argument('--answers-json')
    ap.add_argument('--noninteractive', action='store_true')
    ns = ap.parse_args()

    base = Path(__file__).resolve().parents[1]
    template = base/'templates'/ns.template
    shared = base/'templates'/'_shared_project'
    if not template.exists():
        print(f'Template not found: {template}', file=sys.stderr); return 2
    slug = slugify(ns.name); out = Path(ns.output).resolve()/slug
    if out.exists():
        print(f'Output already exists: {out}', file=sys.stderr); return 3
    mapping={'project_name': ns.name, 'project_slug': slug, 'date': dt.date.today().isoformat()}
    copy_tree_render(shared, out, mapping)
    copy_tree_render(template, out, mapping)
    ensure_gitkeep_dirs(out)
    # Generated projects inherit workspace through workspace_config.yaml, not a nested global workspace tree.

    questions, undecided_values = load_questions(base)
    if ns.answers_json:
        answers = json.loads(Path(ns.answers_json).read_text(encoding='utf-8'))
    elif ns.noninteractive:
        answers = {}
    else:
        answers = interactive_answers(questions)
    for q in questions:
        ans = str(answers.get(q['id'], 'undecided')).strip()
        status = 'Deferred' if ans.lower() in undecided_values else 'Accepted'
        write_decision(out, q['id'], q.get('text',''), ans, status, q.get('severity','L2'), q.get('section','setup'))

    (out/'state'/'recent_changes.md').write_text(f"# Recent Changes\n\n- {dt.date.today().isoformat()}: Project initialized by ProjectForge using `{ns.template}`.\n", encoding='utf-8')
    # Best-effort folder summaries and workspace registration.
    import subprocess
    updater = base/'tools'/'update_context_summaries.py'
    if updater.exists():
        subprocess.run([sys.executable, str(updater), '--project', str(out), '--core-only'], check=False)
    # If ProjectForge is installed at /home/mkkto/srv/projectforge, default workspace registration is automatic.
    workspace = base/'workspace'
    registrar = base/'tools'/'register_project.py'
    if registrar.exists() and workspace.exists():
        subprocess.run([sys.executable, str(registrar), '--workspace', str(workspace), '--project', str(out), '--name', ns.name], check=False)
    print(out)
    return 0
if __name__ == '__main__':
    raise SystemExit(main())
