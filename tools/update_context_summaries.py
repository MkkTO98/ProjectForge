#!/usr/bin/env python3
"""Maintain lightweight `_SUMMARY.md` files used by the context system.

Refresh policy: triggered by folder changes, completed tasks, or context build.
This tool is the canonical summary maintainer; do not maintain a second summary tool.
"""
from __future__ import annotations
import argparse, os, datetime as dt
from pathlib import Path

IGNORE = {'.git','__pycache__','.venv','node_modules','.pytest_cache','generated'}

def summarize_dir(d: Path, root: Path):
    entries = [p.name + ('/' if p.is_dir() else '') for p in sorted(d.iterdir()) if p.name not in IGNORE and p.name != '_SUMMARY.md']
    rel = '.' if d == root else str(d.relative_to(root))
    content = f"# Folder Summary: {rel}\n\n"
    content += "Purpose: Auto-maintained context-map summary used by `tools/build_context.py`. Agents may refine Purpose/Active Work/Needs, but must preserve the basic sections.\n\n"
    content += "## Contains\n" + ''.join(f"- `{e}`\n" for e in entries[:120])
    content += "\n## Active Work\n- Not specified.\n\n## Needs Attention\n- Keep this summary current when changing this folder.\n"
    content += f"\nLast refreshed: {dt.datetime.now().isoformat(timespec='seconds')}\n"
    (d/'_SUMMARY.md').write_text(content, encoding='utf-8')

def main() -> int:
    ap=argparse.ArgumentParser(); ap.add_argument('--project', default='.'); ap.add_argument('--max-depth', type=int, default=2); ap.add_argument('--core-only', action='store_true')
    ns=ap.parse_args(); root=Path(ns.project).resolve()
    for d, subdirs, files in os.walk(root):
        p=Path(d); subdirs[:] = [s for s in subdirs if s not in IGNORE]
        depth=len(p.relative_to(root).parts) if p != root else 0
        if depth <= ns.max_depth: summarize_dir(p, root)
    print(root); return 0
if __name__ == '__main__': raise SystemExit(main())
