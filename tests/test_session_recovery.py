from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def run(*args, cwd=ROOT):
    return subprocess.run([sys.executable, *map(str, args)], cwd=cwd, capture_output=True, text=True)


def test_recover_session_reports_required_fields_without_raw_logs():
    result = run(ROOT / "tools" / "recover_session.py", "--project", ROOT, "--json")
    assert result.returncode == 0, result.stderr
    report = json.loads(result.stdout)

    assert report["recovery_contract"]["raw_logs_read"] is False
    assert report["recovery_contract"]["repository_wide_scan"] is False
    assert report["current_project_state"]
    assert report["active_goal"]
    assert "recommended_resume_procedure" in report
    assert "next_recommended_actions" in report
    consulted = {item["rel"] for item in report["files_consulted"]}
    assert "state/active_goal.md" in consulted
    assert "state/project_state.md" in consulted
    assert all(not item.startswith("logs/") for item in consulted)


def test_generated_project_inherits_recovery_framework(tmp_path):
    create = run(
        ROOT / "tools" / "new_project.py",
        "--name",
        "Recovery Inheritance",
        "--template",
        "default_project",
        "--output",
        tmp_path,
        "--noninteractive",
        "--allow-deferred-required",
    )
    assert create.returncode == 0, create.stderr
    project = tmp_path / "recovery_inheritance"

    assert (project / "tools" / "recover_session.py").exists()
    assert (project / "recovery" / "continuity_framework.md").exists()
    assert "recover_session.py" in (project / "AGENTS.md").read_text(encoding="utf-8")
    assert "standard project closeout" in (project / "AGENTS.md").read_text(encoding="utf-8")
    policy_text = (project / "context" / "context_policy.yaml").read_text(encoding="utf-8")
    assert "continuity_recovery" in policy_text
    assert "standard_closeout_order" in policy_text
    framework_text = (project / "recovery" / "continuity_framework.md").read_text(encoding="utf-8")
    assert "Standard project closeout contract" in framework_text
    assert "Recover project state and continue work" in framework_text

    recovery = run(project / "tools" / "recover_session.py", "--project", project, "--json")
    assert recovery.returncode == 0, recovery.stderr
    report = json.loads(recovery.stdout)
    assert report["current_project_state"]
    assert report["recovery_contract"]["repository_wide_scan"] is False

    coherence = run(ROOT / "tools" / "check_coherence.py", "--project", project, "--mode", "generated", "--json")
    assert coherence.returncode == 0, coherence.stdout + coherence.stderr


def test_recover_session_identifies_active_task_and_recent_decision(tmp_path):
    files = {
        "CONSTITUTION.md": "# Constitution\n",
        "state/active_goal.md": "# Active Goal\n\nCurrent objective.\n\nActive task: `artifacts/tasks/TASK-001-demo.md`.\n\n## Current blockers\nNone.\n\n## Next recommended actions\nRun the focused smoke test.\n",
        "state/project_state.md": "# Project State\n\nCompact current truth.\n",
        "state/architecture.md": "# Architecture\n\nBoring file-backed project.\n",
        "context/latest_handoff.md": "# Latest Handoff\n\nContinue TASK-001. Do not treat `artifacts/tasks/_SUMMARY.md` as active.\n",
        "artifacts/tasks/TASK-001-demo.md": "# TASK-001 Demo\n\nStatus: In Progress\n\nImplement the recovery smoke.\n",
        "artifacts/decisions/DEC-001-demo.md": "# Decision\n\nStatus: Accepted\n\nUse file-backed recovery.\n",
        "logs/raw/session.jsonl": "DO NOT READ\n" * 100,
    }
    for rel, text in files.items():
        path = tmp_path / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")

    result = run(ROOT / "tools" / "recover_session.py", "--project", tmp_path, "--json")
    assert result.returncode == 0, result.stderr
    report = json.loads(result.stdout)
    assert report["active_or_recent_tasks"][0]["path"] == "artifacts/tasks/TASK-001-demo.md"
    assert all(item["path"] != "artifacts/tasks/_SUMMARY.md" for item in report["active_or_recent_tasks"])
    assert report["recent_decisions"][0]["path"] == "artifacts/decisions/DEC-001-demo.md"
    assert report["current_blockers"] == ["None."]
    assert "Run the focused smoke test." in report["next_recommended_actions"][0]
    assert all("logs/raw" not in item["rel"] for item in report["files_consulted"])
