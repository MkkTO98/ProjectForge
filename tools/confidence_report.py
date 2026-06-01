#!/usr/bin/env python3
"""Create a standard ProjectForge confidence report."""
from __future__ import annotations
import argparse, datetime as dt
from pathlib import Path


def band(score: float) -> str:
    if score < 0.50:
        return "low"
    if score < 0.80:
        return "medium"
    return "high"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--project", default=".")
    ap.add_argument("--task", required=True)
    ap.add_argument("--score", type=float, required=True)
    ap.add_argument("--reason", default="")
    ap.add_argument("--uncertainty", action="append", default=[])
    ap.add_argument("--validation", action="append", default=[])
    ns = ap.parse_args()
    project = Path(ns.project).resolve()
    outdir = project / "confidence"
    outdir.mkdir(parents=True, exist_ok=True)
    score = max(0.0, min(1.0, ns.score))
    b = band(score)
    path = outdir / f"confidence-{dt.datetime.now().strftime('%Y%m%d-%H%M%S')}.md"
    escalation = "none"
    if b == "low":
        escalation = "local reviewer -> stronger local model -> Codex/premium model -> human if still blocked"
    elif b == "medium":
        escalation = "dry-run + validation required"
    lines = [
        "# Confidence Report",
        "",
        f"Task: {ns.task}",
        f"Score: {score:.2f}",
        f"Band: {b}",
        "",
        "## Reason",
        ns.reason or "not specified",
        "",
        "## Uncertainty sources",
    ]
    lines.extend(f"- {x}" for x in (ns.uncertainty or ["not specified"]))
    lines.extend(["", "## Validation plan"])
    lines.extend(f"- {x}" for x in (ns.validation or ["not specified"]))
    lines.extend(["", f"Escalation: {escalation}"])
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
