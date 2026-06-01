from __future__ import annotations

import json
import shutil
import subprocess
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]


def run(*args: str, cwd: Path | None = None) -> subprocess.CompletedProcess[str]:
    return subprocess.run([sys.executable, *map(str, args)], cwd=cwd, capture_output=True, text=True)


def test_safe_runner_allows_python3_coherence_and_handles_missing_executable(tmp_path):
    project = tmp_path / "projectforge_copy"
    ignore = shutil.ignore_patterns(".git", ".pytest_cache", "__pycache__", "workspace/projects/*")
    shutil.copytree(ROOT, project, ignore=ignore)
    ok = run(project / "tools" / "run.py", "--project", project, "--level", "safe", "--", "python3", "tools/check_coherence.py", "--project", ".")
    assert ok.returncode == 0, ok.stderr + ok.stdout

    missing = run(project / "tools" / "run.py", "--project", project, "--level", "safe", "--", "definitely-not-a-real-projectforge-command")
    assert missing.returncode in {12, 13}
    assert "Traceback" not in missing.stderr


def test_workspace_registry_schema_is_clean_and_has_no_pytest_paths():
    data = yaml.safe_load((ROOT / "workspace" / "projects_registry.yaml").read_text(encoding="utf-8"))
    assert isinstance(data, dict)
    assert "raw" not in data
    assert isinstance(data.get("projects"), list)
    serialized = yaml.safe_dump(data)
    assert "/tmp/pytest" not in serialized


def test_new_project_temp_output_does_not_register_and_populates_state(tmp_path):
    registry_before = (ROOT / "workspace" / "projects_registry.yaml").read_text(encoding="utf-8")
    answers = {
        "purpose": "Validate hardened generation.",
        "success": "Generated project passes generated coherence.",
        "project_type": "research",
        "autonomy": "balanced",
        "command_policy": "layered default",
        "secrets": "No secrets in v1.",
        "logging": "ProjectForge default logging.",
        "folder_summaries": "yes",
    }
    answers_path = tmp_path / "answers.json"
    answers_path.write_text(json.dumps(answers), encoding="utf-8")

    result = run(ROOT / "tools" / "new_project.py", "--name", "Hardening Smoke", "--template", "default_project", "--output", tmp_path, "--answers-json", answers_path)
    assert result.returncode == 0, result.stderr
    project = tmp_path / "hardening_smoke"
    assert project.exists()
    assert (ROOT / "workspace" / "projects_registry.yaml").read_text(encoding="utf-8") == registry_before
    assert "Validate hardened generation." in (project / "state" / "active_goal.md").read_text(encoding="utf-8")
    assert "layered default" in (project / "state" / "project_state.md").read_text(encoding="utf-8")
    assert "No secrets in v1." in (project / "state" / "project_state.md").read_text(encoding="utf-8")
    assert "projectforge_root:" in (project / "workspace_config.yaml").read_text(encoding="utf-8")
    assert not (project / "tools" / "new_project.py").exists()

    coherence = run(ROOT / "tools" / "check_coherence.py", "--project", project, "--mode", "generated", "--json")
    assert coherence.returncode == 0, coherence.stdout + coherence.stderr
    report = json.loads(coherence.stdout)
    assert report["blocks"] == []


def test_new_project_blocks_unresolved_must_pause_answers_without_override(tmp_path):
    answers_path = tmp_path / "answers.json"
    answers_path.write_text(json.dumps({"purpose": "x", "success": "x"}), encoding="utf-8")
    result = run(ROOT / "tools" / "new_project.py", "--name", "Unsafe Deferred", "--output", tmp_path, "--answers-json", answers_path)
    assert result.returncode != 0
    assert "unresolved must-pause" in result.stderr.lower()
    assert not (tmp_path / "unsafe_deferred").exists()


def test_update_context_summaries_is_stable_and_core_only(tmp_path):
    for rel in ["state/active_goal.md", "artifacts/decisions/D.md", "deep/nested/file.txt"]:
        p = tmp_path / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text("x", encoding="utf-8")
    first = run(ROOT / "tools" / "update_context_summaries.py", "--project", tmp_path, "--core-only")
    assert first.returncode == 0, first.stderr
    summaries = {p.relative_to(tmp_path): p.read_text(encoding="utf-8") for p in tmp_path.rglob("_SUMMARY.md")}
    second = run(ROOT / "tools" / "update_context_summaries.py", "--project", tmp_path, "--core-only")
    assert second.returncode == 0, second.stderr
    assert summaries == {p.relative_to(tmp_path): p.read_text(encoding="utf-8") for p in tmp_path.rglob("_SUMMARY.md")}
    assert (tmp_path / "state" / "_SUMMARY.md").exists()
    assert not (tmp_path / "deep" / "_SUMMARY.md").exists()


def test_projectforge_verification_commands_do_not_mutate_real_registry(tmp_path):
    registry_before = (ROOT / "workspace" / "projects_registry.yaml").read_text(encoding="utf-8")
    result = run(ROOT / "tools" / "new_project.py", "--name", "No Registry Side Effect", "--template", "default_project", "--output", tmp_path, "--noninteractive", "--allow-deferred-required")
    assert result.returncode == 0, result.stderr
    assert (ROOT / "workspace" / "projects_registry.yaml").read_text(encoding="utf-8") == registry_before


def test_no_stale_rigid_questionnaire_language_remains():
    stale_phrases = [
        "Conduct the extensive questionnaire",
        "baseline interview source",
        "must not replace or silently ignore the structured questionnaire",
    ]
    for rel in [
        "skills/project-bootstrap.md",
        "skills/structured-questionnaire.md",
        "templates/_shared_project/skills/project-bootstrap.md",
        "templates/_shared_project/skills/structured-questionnaire.md",
    ]:
        text = (ROOT / rel).read_text(encoding="utf-8")
        for phrase in stale_phrases:
            assert phrase not in text
