#!/usr/bin/env python3
"""Build a task-specific context bundle.

This implements ProjectForge context budgeting: load only relevant high-priority
state, instructions, summaries, decisions, and requested target files.
"""
from __future__ import annotations
import argparse, json, subprocess, sys
from pathlib import Path

DEFAULT_FILES = [
    'CONSTITUTION.md','instructions/GENERAL_INSTRUCTIONS.md','instructions/CONTEXT_POLICY.md',
    'state/active_goal.md','state/project_state.md','state/architecture.md',
    'knowledge/components.yaml','knowledge/dependencies.yaml'
]

def read_if_exists(p: Path, max_chars: int = 12000) -> str:
    if not p.exists() or not p.is_file(): return ''
    txt = p.read_text(encoding='utf-8', errors='replace')
    if len(txt) > max_chars: txt = txt[:max_chars] + '\n\n[TRUNCATED]\n'
    return txt

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument('--project', default='.')
    ap.add_argument('--task', default='general')
    ap.add_argument('--files', default='', help='Comma-separated target files to include')
    ap.add_argument('--refresh-summaries', action='store_true')
    ns = ap.parse_args(); project = Path(ns.project).resolve()
    if ns.refresh_summaries:
        updater=Path(__file__).with_name('update_context_summaries.py')
        if updater.exists(): subprocess.run([sys.executable, str(updater), '--project', str(project)], check=False)
    sections = [f'# Active Context Bundle\n\nTask: {ns.task}\n']
    used=[]
    for rel in DEFAULT_FILES:
        txt = read_if_exists(project/rel)
        if txt:
            sections.append(f'\n## {rel}\n\n{txt}\n'); used.append(rel)
    # Include top-level and one-level folder summaries.
    for summary in sorted(project.glob('*/_SUMMARY.md'))[:40]:
        txt = read_if_exists(summary, 4000)
        if txt:
            rel=str(summary.relative_to(project)); sections.append(f'\n## {rel}\n\n{txt}\n'); used.append(rel)
    for rel in [x.strip() for x in ns.files.split(',') if x.strip()]:
        txt = read_if_exists(project/rel, 20000)
        if txt:
            sections.append(f'\n## TARGET {rel}\n\n{txt}\n'); used.append(rel)
    out = project/'context'/'active_context.md'; out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text('\n'.join(sections), encoding='utf-8')
    manifest={'task':ns.task,'context_used':used}
    (project/'context'/'context_manifest.json').write_text(json.dumps(manifest, indent=2), encoding='utf-8')
    print(out)
    return 0
if __name__ == '__main__': raise SystemExit(main())
