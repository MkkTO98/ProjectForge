#!/usr/bin/env python3
"""Maintain lightweight `_SUMMARY.md` files used by the context system.

Refresh policy: triggered by folder changes, completed tasks, or context build.
This tool is the canonical summary maintainer; do not maintain a second summary tool.
Tracked summaries are deterministic: volatile refresh timestamps belong in logs, not
in `_SUMMARY.md` files.
"""
from __future__ import annotations
import argparse, os
from pathlib import Path

IGNORE = {'.git','__pycache__','.venv','node_modules','.pytest_cache','generated'}
DYNAMIC_SUFFIXES = ('-dry-run.md',)
CORE_DIRS = {
    Path('.'), Path('state'), Path('artifacts'), Path('artifacts/decisions'), Path('artifacts/tasks'),
    Path('docs'), Path('instructions'), Path('context'), Path('tools'), Path('permissions'),
    Path('logs'), Path('metrics'), Path('simulation'), Path('question_queue'), Path('knowledge'), Path('recovery')
}


def summarize_content(d: Path, root: Path) -> str:
    entries = [p.name + ('/' if p.is_dir() else '') for p in sorted(d.iterdir()) if p.name not in IGNORE and p.name != '_SUMMARY.md' and not any(p.name.endswith(suffix) for suffix in DYNAMIC_SUFFIXES)]
    rel = '.' if d == root else str(d.relative_to(root))
    content = f"# Folder Summary: {rel}\n\n"
    content += "Purpose: Auto-maintained context-map summary used by `tools/build_context.py`. Agents may refine Purpose/Active Work/Needs, but must preserve the basic sections.\n\n"
    content += "## Contains\n" + ''.join(f"- `{e}`\n" for e in entries[:120])
    content += "\n## Active Work\n- Not specified.\n\n## Needs Attention\n- Keep this summary current when changing this folder.\n"
    return content


def should_include(p: Path, root: Path, max_depth: int, core_only: bool) -> bool:
    rel = Path('.') if p == root else p.relative_to(root)
    if core_only:
        return rel in CORE_DIRS
    depth = len(rel.parts) if rel != Path('.') else 0
    return depth <= max_depth


def summarize_dir(d: Path, root: Path) -> bool:
    content = summarize_content(d, root)
    target = d / '_SUMMARY.md'
    if target.exists() and target.read_text(encoding='utf-8') == content:
        return False
    target.write_text(content, encoding='utf-8')
    return True


def main() -> int:
    ap=argparse.ArgumentParser(); ap.add_argument('--project', default='.'); ap.add_argument('--max-depth', type=int, default=2); ap.add_argument('--core-only', action='store_true')
    ns=ap.parse_args(); root=Path(ns.project).resolve(); changed=0
    for d, subdirs, files in os.walk(root):
        p=Path(d); subdirs[:] = [s for s in subdirs if s not in IGNORE]
        if should_include(p, root, ns.max_depth, ns.core_only):
            changed += int(summarize_dir(p, root))
    print(root); return 0
if __name__ == '__main__': raise SystemExit(main())
