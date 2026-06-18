import json
import subprocess
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]


def run(*args):
    return subprocess.run([str(a) for a in args], cwd=ROOT, capture_output=True, text=True)


def projectforge_config() -> dict:
    return yaml.safe_load((ROOT / "projectforge.yaml").read_text(encoding="utf-8"))["projectforge"]


def context_policy() -> dict:
    return yaml.safe_load((ROOT / "context" / "context_policy.yaml").read_text(encoding="utf-8"))["context_policy"]


def resolve_provider_root() -> Path:
    provider = projectforge_config()["metaharvest_provider"]
    configured = Path(provider["path"])
    if configured.exists():
        return configured
    if provider.get("status") == "copy_pending":
        fallback = Path(provider["transition_fallback_path"])
        return fallback if fallback.is_absolute() else ROOT / fallback
    return configured


def test_metaharvest_provider_interface_configured_for_external_copy_first_cutover():
    provider = projectforge_config()["metaharvest_provider"]
    assert provider["provider"] == "external"
    assert provider["status"] == "active"
    assert provider["path"] == "/home/mkkto/srv/EIP/projects/MetaHarvest"
    assert provider["transition_fallback_path"] == "MetaHarvest"
    assert provider["compatibility"]["generated_project_path"] == "architecture/architectureharvest"
    assert provider["compatibility"]["source_cache_root"] == "/home/mkkto/srv/EIP/projects/ProjectForge/external_sources"
    assert provider["compatibility"]["source_cache_policy"] == "transitional_projectforge_hosted_cache"
    assert provider["authority"]["advisory_only"] is True
    assert provider["authority"]["may_modify_consumer_projects"] is False
    assert provider["authority"]["may_create_consumer_tasks"] is False

    policy = context_policy()["architecture_harvest"]
    assert policy["provider"] == "external"
    assert policy["provider_status"] == "active"
    assert policy["root_location"] == "/home/mkkto/srv/EIP/projects/MetaHarvest"
    assert policy["transition_fallback_location"] == "MetaHarvest"
    assert policy["generated_project_location"] == "architecture/architectureharvest"


def test_metaharvest_provider_interface_files_exist_via_configured_interface():
    provider = projectforge_config()["metaharvest_provider"]
    root = resolve_provider_root()
    assert root.exists(), root

    for rel in provider["required_interface_files"]:
        assert (root / rel).exists(), rel

    integration = (root / "INTEGRATION.md").read_text(encoding="utf-8")
    assert "MetaHarvest Interface Contract" in integration
    assert "MetaHarvest is advisory only" in integration
    assert "ProjectForge-specific consumption behavior is owned by ProjectForge" in integration

    behavior = (ROOT / "docs" / "METAHARVEST_INTEGRATION.md").read_text(encoding="utf-8")
    assert "ProjectForge MetaHarvest Integration Behavior" in behavior
    assert "architecture/architectureharvest/" in behavior
    assert "transitional" in behavior.lower()

    for rel in provider["required_interface_files"]:
        if rel.endswith(".yaml"):
            yaml.safe_load((root / rel).read_text(encoding="utf-8"))


def test_metaharvest_governance_text_and_templates_parse():
    required_text = [
        ROOT / "CONSTITUTION.md",
        ROOT / "AGENTS.md",
        ROOT / "README.md",
        ROOT / "instructions" / "GENERAL_INSTRUCTIONS.md",
        ROOT / "MetaHarvest" / "INTEGRATION.md",
        ROOT / "docs" / "METAHARVEST_INTEGRATION.md",
        ROOT / "templates" / "_shared_project" / "AGENTS.md",
    ]
    for path in required_text:
        text = path.read_text(encoding="utf-8").lower()
        assert "metaharvest" in text or "architectureharvest" in text
        assert "advisory" in text or path.name == "AGENTS.md"

    policy = context_policy()["architecture_harvest"]
    assert "new_project_creation" in policy["consult_required_during"]
    assert "bug_fixes" in policy["consult_not_required_during"]
    assert set(["active", "stale", "superseded", "retired"]).issubset(policy["recommendation_statuses"])


def test_generated_project_receives_metaharvest_compatibility_placeholders(tmp_path):
    result = run(
        sys.executable,
        ROOT / "tools" / "new_project.py",
        "--name",
        "MetaHarvest Generated",
        "--template",
        "default_project",
        "--output",
        tmp_path,
        "--noninteractive",
        "--allow-deferred-required",
    )
    assert result.returncode == 0, result.stderr
    project = tmp_path / "metaharvest_generated"

    expected = [
        "architecture/architecture_state.md",
        "architecture/architecture_decisions/.gitkeep",
        "architecture/architecture_reviews/architecture_review.template.md",
        "architecture/architectureharvest/relevance_map.yaml",
        "architecture/architectureharvest/adoption_candidates.md",
        "architecture/architectureharvest/rejected_candidates.md",
        "architecture/architectureharvest/review_history.md",
        "architecture/architectureharvest/adoption_outcome.template.yaml",
    ]
    for rel in expected:
        assert (project / rel).exists(), rel

    relevance = yaml.safe_load((project / "architecture" / "architectureharvest" / "relevance_map.yaml").read_text(encoding="utf-8"))
    assert relevance["target"]["project_id"] == "metaharvest_generated"
    assert "architecture_definition" in relevance["consult_required_during"]
    assert "bug_fixes" in relevance["consult_not_required_during"]

    coherence = run(sys.executable, project / "tools" / "check_coherence.py", "--project", project, "--json")
    assert coherence.returncode == 0, coherence.stderr
    report = json.loads(coherence.stdout)
    assert report["blocks"] == []
