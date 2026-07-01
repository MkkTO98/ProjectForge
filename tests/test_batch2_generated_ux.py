from __future__ import annotations

import json
import shutil
import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
TEMPLATES = ["default_project", "python_data_project", "web_project", "research_project"]


def run(*args: object, cwd: Path | None = None) -> subprocess.CompletedProcess[str]:
    return subprocess.run([sys.executable, *map(str, args)], cwd=cwd, capture_output=True, text=True)


def answers_file(tmp_path: Path) -> Path:
    answers = {
        "purpose": "Exercise generated project UX.",
        "success": "Generated project wrapper and hygiene paths work.",
        "project_type": "general",
        "autonomy": "balanced",
        "command_policy": "layered default",
        "secrets": "No secrets in v1.",
        "logging": "project-local default logging.",
        "folder_summaries": "yes",
        "testing": "Run relevant tests before summarizing changes.",
        "documentation_standard": "Maintain project-local state and decisions.",
    }
    path = tmp_path / "answers.json"
    path.write_text(json.dumps(answers), encoding="utf-8")
    return path


@pytest.mark.parametrize("template", TEMPLATES)
def test_generated_project_safe_runner_can_run_own_coherence_for_all_templates(tmp_path, template):
    result = run(
        ROOT / "tools" / "new_project.py",
        "--name",
        f"UX {template}",
        "--template",
        template,
        "--output",
        tmp_path,
        "--answers-json",
        answers_file(tmp_path),
    )
    assert result.returncode == 0, result.stderr
    project = tmp_path / f"ux_{template}"

    direct = run(ROOT / "tools" / "check_coherence.py", "--project", project, "--mode", "generated", "--json")
    assert direct.returncode == 0, direct.stdout + direct.stderr

    wrapped = run(
        project / "tools" / "run.py",
        "--project",
        project,
        "--level",
        "safe",
        "--",
        "python3",
        "tools/check_coherence.py",
        "--project",
        ".",
    )
    assert wrapped.returncode == 0, wrapped.stdout + wrapped.stderr


@pytest.mark.parametrize("template", TEMPLATES)
def test_generated_projects_do_not_copy_template_runtime_caches(tmp_path, template):
    projectforge = tmp_path / "projectforge_copy"
    shutil.copytree(ROOT, projectforge, ignore=shutil.ignore_patterns(".git", ".pytest_cache", ".venv", "external_sources", "workspace/projects/*"))
    cache_dir = projectforge / "templates" / "_shared_project" / "tools" / "__pycache__"
    cache_dir.mkdir(parents=True, exist_ok=True)
    (cache_dir / "stale.cpython-312.pyc").write_bytes(b"stale bytecode")
    (projectforge / "templates" / template / ".pytest_cache").mkdir(exist_ok=True)
    (projectforge / "templates" / template / ".pytest_cache" / "artifact").write_text("cache", encoding="utf-8")

    result = run(
        projectforge / "tools" / "new_project.py",
        "--name",
        f"Cache {template}",
        "--template",
        template,
        "--output",
        tmp_path,
        "--answers-json",
        answers_file(tmp_path),
    )
    assert result.returncode == 0, result.stderr
    project = tmp_path / f"cache_{template}"
    assert not any(project.rglob("__pycache__"))
    assert not any(project.rglob("*.pyc"))
    assert not (project / ".pytest_cache").exists()


def test_update_context_summaries_preserves_curated_sections(tmp_path):
    target = tmp_path / "state"
    target.mkdir(parents=True)
    (target / "active_goal.md").write_text("goal", encoding="utf-8")
    (target / "_SUMMARY.md").write_text(
        """# Folder Summary: state

## Purpose
Curated purpose that future agents need.

## Contains
- stale.md

## Active Work
Curated active work survives refresh.

## Needs Attention
Curated warning survives refresh.
""",
        encoding="utf-8",
    )

    result = run(ROOT / "tools" / "update_context_summaries.py", "--project", tmp_path, "--core-only")
    assert result.returncode == 0, result.stderr
    text = (target / "_SUMMARY.md").read_text(encoding="utf-8")
    assert "Curated purpose that future agents need." in text
    assert "Curated active work survives refresh." in text
    assert "Curated warning survives refresh." in text
    assert "active_goal.md" in text
    assert "stale.md" not in text


def test_install_guidance_is_uv_first_and_not_system_pip():
    install = (ROOT / "tools" / "install.sh").read_text(encoding="utf-8")
    assert "uv venv" in install
    assert "uv pip install" in install
    assert "python3 -m pip install" not in install
    for rel in [
        "tools/run.py",
        "tools/select_model.py",
        "templates/_shared_project/tools/run.py",
        "templates/_shared_project/tools/select_model.py",
    ]:
        text = (ROOT / rel).read_text(encoding="utf-8")
        assert "python3 -m pip install" not in text
        assert "uvx --with pyyaml" in text or "uv pip install" in text


def test_generated_agent_prompts_do_not_force_tools_run_for_hermes_commands():
    for rel in [
        "templates/_shared_project/agents/coder.md",
        "templates/_shared_project/agents/reviewer.md",
    ]:
        text = (ROOT / rel).read_text(encoding="utf-8")
        assert "Use `tools/run.py` for commands." not in text
        assert "Hermes tools directly" in text
