#!/usr/bin/env python3
"""Register a ProjectForge-managed project in a parent workspace registry."""
from __future__ import annotations
import argparse, json
from pathlib import Path
try: import yaml
except Exception: yaml=None

def load(path: Path):
    if path.exists() and yaml: return yaml.safe_load(path.read_text(encoding='utf-8')) or {}
    if path.exists(): return {'raw': path.read_text(encoding='utf-8')}
    return {'workspace': {'name':'default_projectforge_workspace'}, 'projects': []}

def dump(path: Path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    if yaml: path.write_text(yaml.safe_dump(data, sort_keys=False), encoding='utf-8')
    else: path.write_text(json.dumps(data, indent=2), encoding='utf-8')

def main() -> int:
    ap=argparse.ArgumentParser(); ap.add_argument('--workspace', required=True); ap.add_argument('--project', required=True); ap.add_argument('--name', required=True)
    ns=ap.parse_args(); reg=Path(ns.workspace)/'projects_registry.yaml'; data=load(reg)
    data.setdefault('projects', [])
    entry={'name':ns.name,'path':str(Path(ns.project).resolve()),'mode':'hybrid_inheritance'}
    data['projects']=[p for p in data['projects'] if p.get('name')!=ns.name]+[entry]
    dump(reg,data); print(reg); return 0
if __name__=='__main__': raise SystemExit(main())
