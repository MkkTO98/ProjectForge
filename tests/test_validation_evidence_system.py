import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def run(*args):
    return subprocess.run([sys.executable, *map(str, args)], cwd=ROOT, capture_output=True, text=True)


def generate_project(tmp_path: Path, name: str = "Validation Evidence Generated") -> Path:
    result = run(
        ROOT / "tools" / "new_project.py",
        "--name",
        name,
        "--template",
        "default_project",
        "--output",
        tmp_path,
        "--noninteractive",
        "--allow-deferred-required",
    )
    assert result.returncode == 0, result.stderr
    return tmp_path / name.lower().replace(" ", "_")


def coherence(project: Path):
    result = run(ROOT / "tools" / "check_coherence.py", "--project", project, "--mode", "generated", "--json")
    return result, json.loads(result.stdout)


def test_generated_project_coherence_emits_validation_evidence(tmp_path):
    project = generate_project(tmp_path)
    result, report = coherence(project)

    assert result.returncode == 0, result.stdout + result.stderr
    assert report["blocks"] == []
    checks = {item["check"] for item in report["evidence"]}
    assert "identity structural contract" in checks
    assert "context and recovery structural contract" in checks
    assert "governance structural contract" in checks
    assert "work execution methodology structural contract" in checks
    assert "generated-project independence scan" in checks


def test_coherence_detects_forbidden_generated_project_reference(tmp_path):
    project = generate_project(tmp_path, "Forbidden Reference Generated")
    constitution = project / "CONSTITUTION.md"
    constitution.write_text(constitution.read_text(encoding="utf-8") + "\nThis project is governed by ProjectForge.\n", encoding="utf-8")

    result, report = coherence(project)

    assert result.returncode != 0
    assert any("forbidden external-authority references" in item for item in report["blocks"])


def test_coherence_detects_missing_methodology_contract(tmp_path):
    project = generate_project(tmp_path, "Methodology Missing Generated")
    (project / "instructions" / "WORK_EXECUTION_METHODOLOGY.md").unlink()

    result, report = coherence(project)

    assert result.returncode != 0
    assert any("missing methodology file" in item for item in report["blocks"])


def test_coherence_detects_governance_template_drift(tmp_path):
    project = generate_project(tmp_path, "Governance Template Drift")
    task_template = project / "artifacts" / "tasks" / "TEMPLATE.md"
    task_template.write_text("# Task\n\nStatus: Proposed\n", encoding="utf-8")

    result, report = coherence(project)

    assert result.returncode != 0
    assert any("artifacts/tasks/TEMPLATE.md missing required text" in item for item in report["blocks"])


def test_context_health_warns_on_incomplete_substantive_handoff(tmp_path):
    project = generate_project(tmp_path, "Handoff Evidence Generated")
    handoff = project / "context" / "latest_handoff.md"
    handoff.write_text("# Latest Handoff\n\n" + ("A substantive but unstructured note. " * 40), encoding="utf-8")

    result = run(project / "tools" / "context_health.py", "--project", project, "--json")
    assert result.returncode == 0, result.stdout + result.stderr
    report = json.loads(result.stdout)
    assert "files_checked" in report
    assert "checks_performed" in report
    assert any("incomplete for recovery evidence" in item for item in report["warnings"])


def test_architecture_reality_audit_reports_evidence_and_detects_validation_policy_creep(tmp_path):
    project = generate_project(tmp_path, "Architecture Drift Generated")
    policy = project / "instructions" / "VALIDATION_AND_EVIDENCE.md"
    policy.write_text("# Validation and Evidence\n\nStandalone validation doctrine.\n", encoding="utf-8")

    result = run(project / "tools" / "architecture_reality_audit.py", "--project", project, "--json")
    assert result.returncode == 0, result.stdout + result.stderr
    report = json.loads(result.stdout)
    assert "files_checked" in report
    assert "checks_performed" in report
    assert any("VALIDATION_AND_EVIDENCE.md" in item["message"] for item in report["warnings"])
