import json
import os
import time
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def run(*args):
    return subprocess.run([sys.executable, *map(str, args)], cwd=ROOT, capture_output=True, text=True)


def minimal_project(tmp_path: Path) -> Path:
    project = tmp_path / "ctx"
    for d in ["state", "context", "permissions", "confidence", "metrics", "logs", "tools"]:
        (project / d).mkdir(parents=True, exist_ok=True)
    (project / "state" / "active_goal.md").write_text("# Active Goal\n\nCurrent objective.\n", encoding="utf-8")
    (project / "state" / "project_state.md").write_text("# Project State\n\nCurrent truth.\n", encoding="utf-8")
    (project / "state" / "architecture.md").write_text("# Architecture\n\nCurrent architecture.\n", encoding="utf-8")
    (project / "context" / "context_policy.yaml").write_text((ROOT / "context" / "context_policy.yaml").read_text(encoding="utf-8"), encoding="utf-8")
    return project


def test_context_health_blocks_oversized_primary_state(tmp_path):
    project = minimal_project(tmp_path)
    long_history = "# Project State\n\n" + ("historical verification completed\n" * 1000)
    project.joinpath("state", "project_state.md").write_text(long_history, encoding="utf-8")

    result = run(ROOT / "tools" / "context_health.py", "--project", project, "--json")
    assert result.returncode != 0
    report = json.loads(result.stdout)
    assert any("state/project_state.md" in item for item in report["blocks"])


def test_context_health_warns_on_large_non_project_wide_generated_context(tmp_path):
    project = minimal_project(tmp_path)
    project.joinpath("context", "active_context.md").write_text("x" * 45000, encoding="utf-8")
    project.joinpath("context", "context_audit.json").write_text(json.dumps({"context_mode": "normal"}), encoding="utf-8")

    result = run(ROOT / "tools" / "context_health.py", "--project", project, "--json")
    assert result.returncode == 0
    report = json.loads(result.stdout)
    assert any("generated bundle" in item or "generated" in item for item in report["warnings"])


def test_coherence_runs_context_health_for_generated_projects(tmp_path):
    result = run(
        ROOT / "tools" / "new_project.py",
        "--name",
        "Context Health Generated",
        "--template",
        "default_project",
        "--output",
        tmp_path,
        "--noninteractive",
        "--allow-deferred-required",
    )
    assert result.returncode == 0, result.stderr
    project = tmp_path / "context_health_generated"
    assert (project / "tools" / "context_health.py").exists()
    project.joinpath("state", "project_state.md").write_text("# Project State\n\n" + ("old verification log\n" * 1000), encoding="utf-8")

    coherence = run(ROOT / "tools" / "check_coherence.py", "--project", project, "--mode", "generated", "--json")
    assert coherence.returncode != 0
    report = json.loads(coherence.stdout)
    assert any("context health" in item and "state/project_state.md" in item for item in report["blocks"])


def test_generated_templates_mark_active_context_as_generated_and_skills_on_demand():
    agents = (ROOT / "templates" / "_shared_project" / "AGENTS.md").read_text(encoding="utf-8")
    general = (ROOT / "templates" / "_shared_project" / "instructions" / "GENERAL_INSTRUCTIONS.md").read_text(encoding="utf-8")
    skills_policy = (ROOT / "templates" / "_shared_project" / "instructions" / "SMALL_SKILLS_POLICY.md").read_text(encoding="utf-8")
    active_context = (ROOT / "templates" / "_shared_project" / "context" / "active_context.md").read_text(encoding="utf-8")
    context_budgeting = (ROOT / "templates" / "_shared_project" / "skills" / "context-budgeting.md").read_text(encoding="utf-8")

    assert "not mandatory startup context" in agents
    assert "not mandatory startup context" in general
    assert "not mandatory startup context" in active_context
    assert "load or read a skill only when" in skills_policy
    assert "Regenerate task-specific bundles" in context_budgeting

def test_context_health_warns_on_stale_generated_context_bundle(tmp_path):
    project = minimal_project(tmp_path)
    active = project / "context" / "active_context.md"
    active.write_text("# Old Context\n", encoding="utf-8")
    project.joinpath("context", "context_audit.json").write_text(json.dumps({"context_mode": "normal"}), encoding="utf-8")
    old = time.time() - (8 * 24 * 3600)
    os.utime(active, (old, old))

    result = run(ROOT / "tools" / "context_health.py", "--project", project, "--json")
    assert result.returncode == 0
    report = json.loads(result.stdout)
    assert any("hours old" in item and "regenerated" in item for item in report["warnings"])


def test_context_health_blocks_unjustified_project_wide_review_audit(tmp_path):
    project = minimal_project(tmp_path)
    project.joinpath("context", "active_context.md").write_text("# Project-wide Context\n", encoding="utf-8")
    project.joinpath("context", "context_audit.json").write_text(json.dumps({"context_mode": "project_wide_review", "raw_logs_excluded": True}), encoding="utf-8")

    result = run(ROOT / "tools" / "context_health.py", "--project", project, "--json")
    assert result.returncode != 0
    report = json.loads(result.stdout)
    assert any("project_wide_review" in item and "review_justification" in item for item in report["blocks"])
