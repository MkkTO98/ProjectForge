from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def read(rel: str) -> str:
    return (ROOT / rel).read_text(encoding='utf-8')


def test_no_sqlite_index_default():
    text = read('projectforge.yaml')
    assert 'sqlite_index_default: false' in text


def test_manual_push_default():
    assert 'manual' in read('projectforge.yaml').lower()
    assert 'push_requires_human_approval' in read('permissions/escalation_rules.yaml')


def test_specialized_agents_require_request():
    text = read('instructions/SPECIALIZED_AGENT_POLICY.md').lower()
    assert 'request' in text
    assert 'approval' in text


def test_knowledge_graph_is_simple():
    assert (ROOT / 'knowledge/components.yaml').exists()
    assert (ROOT / 'knowledge/dependencies.yaml').exists()
    assert not (ROOT / 'knowledge/validation_map.yaml').exists()


def test_workspace_layer_exists():
    for rel in ['workspace/projects_registry.yaml', 'workspace/cross_project_dependencies.yaml']:
        assert (ROOT / rel).exists(), rel


def test_confidence_policy_exists():
    text = read('confidence/confidence_policy.yaml')
    assert 'codex_or_premium_model' in text
    assert 'human_if_still_blocked' in text
