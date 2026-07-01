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
    return Path(provider["path"])


def test_metaharvest_provider_interface_configured_for_external_provider():
    provider = projectforge_config()["metaharvest_provider"]
    assert provider["provider"] == "external"
    assert provider["status"] == "active"
    assert provider["path"] == "/home/mkkto/srv/EIP/projects/MetaHarvest"
    assert "transition_fallback_path" not in provider
    assert provider["compatibility"]["generated_project_path"] == "architecture/architectureharvest"
    assert provider["compatibility"]["source_cache_root"] == "/home/mkkto/srv/ProjectForge/external_sources"
    assert provider["compatibility"]["source_cache_policy"] == "optional_replaceable_projectforge_hosted_cache_hint"
    assert provider["authority"]["advisory_only"] is True
    assert provider["authority"]["may_modify_consumer_projects"] is False
    assert provider["authority"]["may_create_consumer_tasks"] is False

    policy = context_policy()["architecture_harvest"]
    assert policy["provider"] == "external"
    assert policy["provider_status"] == "active"
    assert policy["root_location"] == "/home/mkkto/srv/EIP/projects/MetaHarvest"
    assert "transition_fallback_location" not in policy
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
    assert "change-discoverability boundary" in integration.lower()
    assert "change_discovery/index.yaml" in provider["required_interface_files"]

    change_index = yaml.safe_load((root / "change_discovery" / "index.yaml").read_text(encoding="utf-8"))
    assert change_index["kind"] == "metaharvest_change_discovery_index"
    assert change_index["consumer_contract"]["question_answered"] == "What changed in MetaHarvest since I last looked?"

    behavior = (ROOT / "docs" / "METAHARVEST_INTEGRATION.md").read_text(encoding="utf-8")
    assert "ProjectForge MetaHarvest Integration Behavior" in behavior
    assert "architecture/architectureharvest/" in behavior
    assert "replaceable" in behavior.lower()

    for rel in provider["required_interface_files"]:
        if rel.endswith(".yaml"):
            yaml.safe_load((root / rel).read_text(encoding="utf-8"))


def test_metaharvest_governance_text_and_templates_parse():
    required_text = [
        ROOT / "CONSTITUTION.md",
        ROOT / "AGENTS.md",
        ROOT / "README.md",
        ROOT / "instructions" / "GENERAL_INSTRUCTIONS.md",
        resolve_provider_root() / "INTEGRATION.md",
        ROOT / "docs" / "METAHARVEST_INTEGRATION.md",
    ]
    for path in required_text:
        text = path.read_text(encoding="utf-8").lower()
        assert "metaharvest" in text or "architectureharvest" in text
        assert "advisory" in text or path.name == "AGENTS.md"

    policy = context_policy()["architecture_harvest"]
    assert "new_project_creation" in policy["consult_required_during"]
    assert "bug_fixes" in policy["consult_not_required_during"]
    assert set(["active", "stale", "superseded", "retired"]).issubset(policy["recommendation_statuses"])
    assert not (ROOT / "templates" / "_shared_project" / "architecture" / "architectureharvest").exists()


def test_default_generated_project_does_not_receive_metaharvest_placeholders(tmp_path):
    result = run(
        sys.executable,
        ROOT / "tools" / "new_project.py",
        "--name",
        "Neutral Generated",
        "--template",
        "default_project",
        "--output",
        tmp_path,
        "--noninteractive",
        "--allow-deferred-required",
    )
    assert result.returncode == 0, result.stderr
    project = tmp_path / "neutral_generated"

    assert (project / "architecture" / "architecture_state.md").exists()
    assert not (project / "architecture" / "architectureharvest").exists()
    assert not (project / "architecture" / "architecture_reviews" / "architecture_review.template.md").exists()

    generated_text = "\n".join(
        path.read_text(encoding="utf-8", errors="replace")
        for path in project.rglob("*")
        if path.is_file()
    ).lower()
    assert "metaharvest" not in generated_text
    assert "architectureharvest" not in generated_text

    coherence = run(sys.executable, project / "tools" / "check_coherence.py", "--project", project, "--json")
    assert coherence.returncode == 0, coherence.stderr
    report = json.loads(coherence.stdout)
    assert report["blocks"] == []
