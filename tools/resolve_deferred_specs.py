#!/usr/bin/env python3
"""Escalate deferred specifications that repeatedly block work.

The tool scans metrics/events.jsonl for deferred_spec_block events. If the same
specification key blocks work at least twice, it creates an L3 question for the
user and records the escalation. It does not answer the specification itself.
"""
from __future__ import annotations
import argparse, collections, datetime as dt, json, subprocess, sys
from pathlib import Path


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--project", default=".")
    ap.add_argument("--threshold", type=int, default=2)
    ns = ap.parse_args()
    root = Path(ns.project).resolve()
    events = root / "metrics" / "events.jsonl"
    counts: collections.Counter[str] = collections.Counter()
    examples: dict[str, str] = {}
    if events.exists():
        for line in events.read_text(encoding="utf-8").splitlines():
            if not line.strip():
                continue
            try:
                rec = json.loads(line)
            except Exception:
                continue
            if rec.get("event") == "deferred_spec_block":
                key = str(rec.get("entity") or rec.get("specification") or "unspecified")
                counts[key] += 1
                examples.setdefault(key, rec.get("details", ""))
    created = []
    qtool = Path(__file__).with_name("create_question.py")
    for key, count in counts.items():
        if count < ns.threshold:
            continue
        # Avoid duplicate pending questions for the same key.
        pending = root / "question_queue" / "pending"
        exists = False
        if pending.exists():
            for p in pending.glob("*"):
                if key.lower() in p.read_text(encoding="utf-8", errors="replace").lower():
                    exists = True
                    break
        if exists:
            continue
        question = f"Deferred specification `{key}` has blocked work {count} times. Please decide it so the project can continue coherently."
        cmd = [sys.executable, str(qtool), "--project", str(root), "--severity", "L3", "--question", question, "--consequence", "Current task remains blocked until answered. Store final answer as artifacts/decisions/."]
        res = subprocess.run(cmd, capture_output=True, text=True)
        if res.returncode == 0:
            created.append(res.stdout.strip())
    report_dir = root / "metrics" / "reports"
    report_dir.mkdir(parents=True, exist_ok=True)
    report = report_dir / f"deferred_spec_review_{dt.date.today().strftime('%Y%m%d')}.md"
    lines = ["# Deferred Specification Review", f"Date: {dt.date.today().isoformat()}", ""]
    if not counts:
        lines.append("No deferred specification block events found.")
    else:
        for key, count in counts.most_common():
            lines.append(f"- `{key}` blocked work {count} time(s).")
    if created:
        lines.append("\n## L3 questions created")
        for c in created:
            lines.append(f"- {c}")
    report.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(report)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
