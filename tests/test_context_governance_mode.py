from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

from test_context_policy_strict import ROOT, make_project


def run(*args, cwd=ROOT):
    return subprocess.run([sys.executable, *map(str, args)], cwd=cwd, capture_output=True, text=True)


def test_project_wide_review_requires_justification(tmp_path):
    project = make_project(tmp_path)
    result = run(
        ROOT / "tools" / "build_context.py",
        "--project", project,
        "--task", "project-wide gap analysis",
        "--task-type", "gap_analysis",
        "--context-mode", "project_wide_review",
        "--model-target", "cloud",
        "--model-selected", "codex_supervisor",
        "--model-reason", "gap_analysis",
    )
    assert result.returncode == 2
    assert "review-justification" in result.stderr


def test_project_wide_review_includes_broader_summaries_without_raw_logs(tmp_path):
    project = make_project(tmp_path)
    result = run(
        ROOT / "tools" / "build_context.py",
        "--project", project,
        "--task", "project-wide gap analysis",
        "--task-type", "gap_analysis",
        "--context-mode", "project_wide_review",
        "--review-justification", "Quarterly architecture/gap review needs a folder-level map across the project.",
        "--model-target", "cloud",
        "--model-selected", "codex_supervisor",
        "--model-reason", "gap_analysis",
    )
    assert result.returncode == 0, result.stderr
    audit = json.loads((project / "context" / "context_audit.json").read_text(encoding="utf-8"))
    included = {item["path"] for item in audit["included_files"]}
    assert audit["context_mode"] == "project_wide_review"
    assert audit["review_justification"]
    assert "src/_SUMMARY.md" in included
    assert "tests/_SUMMARY.md" in included
    assert "docs/_SUMMARY.md" in included
    assert audit["raw_logs_excluded"] is True
    assert all(not item["path"].startswith("logs/raw/") for item in audit["included_files"])


def test_cloud_governance_selection_accepts_project_wide_audit(tmp_path):
    project = make_project(tmp_path)
    build = run(
        ROOT / "tools" / "build_context.py",
        "--project", project,
        "--task", "project-wide strategic planning",
        "--task-type", "strategic_planning",
        "--context-mode", "project_wide_review",
        "--review-justification", "Strategic planning needs cross-project folder summaries and current state.",
        "--model-target", "cloud",
        "--model-selected", "codex_supervisor",
        "--model-reason", "strategic_planning",
    )
    assert build.returncode == 0, build.stderr
    selected = run(
        ROOT / "tools" / "select_model.py",
        "--project", project,
        "--agent", "planner",
        "--task", "strategic_planning",
        "--governance",
        "--context-audit", "context/context_audit.json",
        "--json",
    )
    assert selected.returncode == 0, selected.stdout + selected.stderr
    data = json.loads(selected.stdout)
    assert data["allowed"] is True
    assert data["audit_status"].endswith("mode=project_wide_review)")


def test_routine_implementation_stays_local_even_with_cloud_flag_absent(tmp_path):
    project = make_project(tmp_path)
    result = run(ROOT / "tools" / "select_model.py", "--project", project, "--agent", "coder", "--task", "routine_implementation", "--json")
    assert result.returncode == 0, result.stderr
    data = json.loads(result.stdout)
    assert data["allowed"] is True
    assert data["model"] != "codex_supervisor"
    assert data["audit_status"] == "not_required"
