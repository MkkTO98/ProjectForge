from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def run(*args, cwd=ROOT):
    return subprocess.run([sys.executable, *map(str, args)], cwd=cwd, capture_output=True, text=True)


def make_project(tmp_path: Path) -> Path:
    files = {
        "CONSTITUTION.md": "# Constitution\n",
        "state/project_state.md": "# Project State\nCompact project summary.\n",
        "state/active_goal.md": "# Active Goal\nDo focused work.\n",
        "context/context_policy.yaml": (ROOT / "context" / "context_policy.yaml").read_text(encoding="utf-8"),
        "context/latest_handoff.md": "# Latest Handoff\nShort handoff only.\n",
        "src/_SUMMARY.md": "# Folder Summary: src\n\n## Purpose\nSource code.\n",
        "tests/_SUMMARY.md": "# Folder Summary: tests\n\n## Purpose\nTests.\n",
        "docs/_SUMMARY.md": "# Folder Summary: docs\n\n## Purpose\nDocumentation.\n",
        "src/app.py": "def main():\n    return 'ok'\n",
        "artifacts/tasks/TASK-001-demo.md": "# TASK-001 Demo\nAcceptance criteria.\n",
        "artifacts/decisions/DEC-001-demo.md": "# Decision\nUse compact context.\n",
        "logs/raw/session.jsonl": "{\"role\": \"user\", \"content\": \"VERY LARGE RAW CONVERSATION\"}\n" * 50,
        "unrelated/huge.txt": "UNRELATED LARGE FILE\n" * 20000,
    }
    for rel, text in files.items():
        path = tmp_path / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")
    (tmp_path / "models").mkdir(exist_ok=True)
    (tmp_path / "models" / "registry.yaml").write_text((ROOT / "models" / "registry.yaml").read_text(encoding="utf-8"), encoding="utf-8")
    (tmp_path / "models" / "routing.yaml").write_text((ROOT / "models" / "routing.yaml").read_text(encoding="utf-8"), encoding="utf-8")
    return tmp_path


def test_normal_context_excludes_raw_logs(tmp_path):
    project = make_project(tmp_path)
    result = run(ROOT / "tools" / "build_context.py", "--project", project, "--task", "demo", "--files", "logs/raw/session.jsonl,src/app.py", "--folders", "src")
    assert result.returncode == 0, result.stderr
    context = (project / "context" / "active_context.md").read_text(encoding="utf-8")
    audit = json.loads((project / "context" / "context_audit.json").read_text(encoding="utf-8"))
    assert "VERY LARGE RAW CONVERSATION" not in context
    assert audit["raw_logs_excluded"] is True
    assert any(item["path"] == "logs/raw/session.jsonl" for item in audit["excluded_files"])


def test_context_size_stays_under_cloud_budget_for_summary_first_bundle(tmp_path):
    project = make_project(tmp_path)
    result = run(ROOT / "tools" / "build_context.py", "--project", project, "--task", "cloud architecture review", "--model-target", "cloud", "--model-selected", "codex_supervisor", "--model-reason", "architecture_decision", "--files", "src/app.py", "--folders", "src")
    assert result.returncode == 0, result.stderr
    audit = json.loads((project / "context" / "context_audit.json").read_text(encoding="utf-8"))
    assert audit["estimated_tokens"] <= audit["budget_tokens"]


def test_cloud_model_selection_requires_audit_report(tmp_path):
    project = make_project(tmp_path)
    result = run(ROOT / "tools" / "select_model.py", "--project", project, "--agent", "planner", "--task", "architecture_decision", "--architecture-decision", "--json")
    assert result.returncode == 2
    assert "context audit" in result.stdout.lower() or "context audit" in result.stderr.lower()


def test_relevant_folder_summaries_are_included(tmp_path):
    project = make_project(tmp_path)
    result = run(ROOT / "tools" / "build_context.py", "--project", project, "--task", "change app", "--files", "src/app.py", "--folders", "src")
    assert result.returncode == 0, result.stderr
    audit = json.loads((project / "context" / "context_audit.json").read_text(encoding="utf-8"))
    assert audit["summaries_used"] is True
    assert any(item["path"] == "src/_SUMMARY.md" for item in audit["included_files"])


def test_unrelated_large_files_are_excluded_from_normal_context(tmp_path):
    project = make_project(tmp_path)
    result = run(ROOT / "tools" / "build_context.py", "--project", project, "--task", "small source edit", "--files", "src/app.py", "--folders", "src")
    assert result.returncode == 0, result.stderr
    context = (project / "context" / "active_context.md").read_text(encoding="utf-8")
    audit = json.loads((project / "context" / "context_audit.json").read_text(encoding="utf-8"))
    assert "UNRELATED LARGE FILE" not in context
    assert all(item["path"] != "unrelated/huge.txt" for item in audit["included_files"])
