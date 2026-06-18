#!/usr/bin/env python3
"""Run routine ProjectForge orchestrator hygiene steps.

This tool is intentionally conservative. It automates the checks the brain/orchestrator
should run often, while keeping policy changes as proposals rather than silent edits.
"""
from __future__ import annotations
import argparse, datetime as dt, json, subprocess, sys
from pathlib import Path


def run(cmd: list[str], cwd: Path) -> dict:
    proc = subprocess.run(cmd, cwd=str(cwd), capture_output=True, text=True)
    return {
        "command": " ".join(cmd),
        "returncode": proc.returncode,
        "stdout": proc.stdout.strip(),
        "stderr": proc.stderr.strip(),
    }


def main() -> int:
    ap = argparse.ArgumentParser(description="Run ProjectForge orchestrator hygiene checks.")
    ap.add_argument("--project", default=".")
    ap.add_argument("--phase", choices=["after_task", "before_commit", "periodic", "all"], default="after_task")
    ap.add_argument("--dry-run-report", help="Optional dry-run report to validate before execution.")
    ns = ap.parse_args()
    root = Path(ns.project).resolve()
    tools = root / "tools"
    if not tools.exists():
        # Allow running from ProjectForge root against generated projects that inherited tools.
        tools = Path(__file__).resolve().parent

    commands: list[list[str]] = []
    if ns.dry_run_report:
        commands.append([sys.executable, str(tools / "validate_dry_run.py"), ns.dry_run_report])
    if ns.phase in {"after_task", "all"}:
        commands.append([sys.executable, str(tools / "update_context_summaries.py"), "--project", str(root)])
        commands.append([sys.executable, str(tools / "check_coherence.py"), "--project", str(root)])
    if ns.phase in {"before_commit", "all"}:
        commands.append([sys.executable, str(tools / "check_coherence.py"), "--project", str(root)])
    if ns.phase in {"periodic", "all"}:
        commands.append([sys.executable, str(tools / "architecture_reality_audit.py"), "--project", str(root), "--write-report"])
        commands.append([sys.executable, str(tools / "review_metrics.py"), "--project", str(root)])
        commands.append([sys.executable, str(tools / "resolve_deferred_specs.py"), "--project", str(root)])

    results = [run(c, root) for c in commands]
    logdir = root / "logs" / "derived"
    logdir.mkdir(parents=True, exist_ok=True)
    record = {
        "timestamp": dt.datetime.now().isoformat(timespec="seconds"),
        "phase": ns.phase,
        "project": str(root),
        "results": results,
    }
    with (logdir / "orchestrator_hygiene.log").open("a", encoding="utf-8") as f:
        f.write(json.dumps(record) + "\n")

    blocks = [r for r in results if r["returncode"] != 0]
    for r in results:
        print(f"[{r['returncode']}] {r['command']}")
        if r["stdout"]:
            print(r["stdout"])
        if r["stderr"]:
            print(r["stderr"], file=sys.stderr)
    return 2 if blocks else 0


if __name__ == "__main__":
    raise SystemExit(main())
