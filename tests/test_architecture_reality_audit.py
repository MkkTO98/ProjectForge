import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def run(*args):
    return subprocess.run([sys.executable, *map(str, args)], cwd=ROOT, capture_output=True, text=True)


def test_architecture_reality_audit_passes_root():
    result = run(ROOT / "tools" / "architecture_reality_audit.py", "--project", ROOT, "--json")
    assert result.returncode == 0, result.stdout + result.stderr
    report = json.loads(result.stdout)
    assert report["blocks"] == []
    assert "architecture_vs_implementation" in report["audit_categories"]
    assert "documentation_without_implementation" in report["drift_types"]


def test_architecture_reality_audit_detects_missing_tool(tmp_path):
    project = tmp_path / "drift"
    for rel, text in {
        "CONSTITUTION.md": "# Constitution\n",
        "AGENTS.md": "Architecture-to-Reality Audit every 5-10 completed tasks before major architecture changes before major governance reviews. Context used.\n",
        "context/context_policy.yaml": "context_policy:\n  context_loading_hierarchy: {}\n  architecture_reality_audit:\n    name: Architecture-to-Reality Audit\n",
        "instructions/GENERAL_INSTRUCTIONS.md": "Architecture-to-Reality Audit every 5-10 completed tasks before major architecture changes before major governance reviews.\n",
        "state/active_goal.md": "# Active Goal\n",
        "state/project_state.md": "# Project State\n",
        "state/architecture.md": "# Architecture\n",
    }.items():
        p = project / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(text, encoding="utf-8")
    for d in ["tools", "agents", "logs", "metrics", "artifacts/tasks", "artifacts/reports"]:
        (project / d).mkdir(parents=True, exist_ok=True)
    (project / "agents" / "auditor.md").write_text("Context used. Architecture-to-Reality Audit trigger.\n", encoding="utf-8")
    (project / "logs" / "logging_policy.yaml").write_text("raw operational records\n", encoding="utf-8")
    (project / "metrics" / "metrics_policy.yaml").write_text("derived evidence\n", encoding="utf-8")
    for tool in ["check_coherence.py", "context_health.py", "build_context.py"]:
        (project / "tools" / tool).write_text("# placeholder\n", encoding="utf-8")

    result = run(ROOT / "tools" / "architecture_reality_audit.py", "--project", project, "--json")
    assert result.returncode != 0
    report = json.loads(result.stdout)
    assert any("tools/architecture_reality_audit.py" in item["message"] for item in report["blocks"])


def test_generated_projects_inherit_architecture_reality_audit(tmp_path):
    result = run(
        ROOT / "tools" / "new_project.py",
        "--name",
        "Architecture Audit Generated",
        "--template",
        "default_project",
        "--output",
        tmp_path,
        "--noninteractive",
        "--allow-deferred-required",
    )
    assert result.returncode == 0, result.stderr
    project = tmp_path / "architecture_audit_generated"
    assert (project / "tools" / "architecture_reality_audit.py").exists()
    assert "Architecture-to-Reality Audit" in (project / "AGENTS.md").read_text(encoding="utf-8")
    assert "architecture_reality_audit" in (project / "context" / "context_policy.yaml").read_text(encoding="utf-8")
    assert (project / "automation" / "orchestration_schedule.yaml").exists()

    audit = run(project / "tools" / "architecture_reality_audit.py", "--project", project, "--json")
    assert audit.returncode == 0, audit.stdout + audit.stderr
    report = json.loads(audit.stdout)
    assert report["blocks"] == []

    coherence = run(ROOT / "tools" / "check_coherence.py", "--project", project, "--mode", "generated", "--json")
    assert coherence.returncode == 0, coherence.stdout + coherence.stderr
