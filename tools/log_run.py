#!/usr/bin/env python3
from __future__ import annotations
import argparse, json, time, uuid
from pathlib import Path


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--project", default=".")
    p.add_argument("--agent", required=True)
    p.add_argument("--goal", required=True)
    p.add_argument("--status", required=True)
    p.add_argument("--files", default="")
    p.add_argument("--notes", default="")
    ns = p.parse_args()
    project = Path(ns.project).resolve()
    out = project / "logs" / "agents"
    out.mkdir(parents=True, exist_ok=True)
    rec = {
        "id": str(uuid.uuid4()),
        "ts": time.time(),
        "agent": ns.agent,
        "goal": ns.goal,
        "status": ns.status,
        "files": [x for x in ns.files.split(",") if x],
        "notes": ns.notes,
    }
    with (out / "runs.jsonl").open("a", encoding="utf-8") as f:
        f.write(json.dumps(rec, ensure_ascii=False) + "\n")
    print(rec["id"])
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
