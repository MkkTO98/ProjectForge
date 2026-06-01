#!/usr/bin/env python3
from __future__ import annotations
import argparse
from pathlib import Path
try:
    import yaml
except Exception:
    yaml = None

def load_yaml(path: Path):
    if yaml is None:
        raise RuntimeError("PyYAML required: python3 -m pip install pyyaml")
    return yaml.safe_load(path.read_text(encoding='utf-8')) or {}

def main() -> int:
    p = argparse.ArgumentParser(description='Select a model from ProjectForge routing policy.')
    p.add_argument('--project', default='.')
    p.add_argument('--agent', required=True)
    p.add_argument('--task', default='')
    p.add_argument('--failure-count', type=int, default=0)
    ns = p.parse_args()
    project = Path(ns.project).resolve()
    models_dir = project/'models'
    if not models_dir.exists():
        models_dir = Path(__file__).resolve().parents[1]/'models'
    registry = load_yaml(models_dir/'registry.yaml').get('models', {})
    routing = load_yaml(models_dir/'routing.yaml').get('routing', {})
    task_route = routing.get('by_task', {}).get(ns.task, {}) if ns.task else {}
    agent_route = routing.get('by_agent', {}).get(ns.agent, {})
    candidates = task_route.get('preferred') or agent_route.get('preferred') or list(registry.keys())
    threshold = agent_route.get('escalation_after_failures')
    if threshold is not None and ns.failure_count >= int(threshold) and 'codex_supervisor' in registry:
        choice = 'codex_supervisor'
    else:
        choice = next((c for c in candidates if c in registry), candidates[0] if candidates else 'unknown')
    print(choice)
    return 0
if __name__ == '__main__':
    raise SystemExit(main())
