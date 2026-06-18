from pathlib import Path
import subprocess, sys, json

ROOT = Path(__file__).resolve().parents[1]


def read(rel: str) -> str:
    return (ROOT / rel).read_text(encoding='utf-8')


def test_operator_manual_exists_and_mentions_manual_tasks():
    text = read('docs/OPERATOR_MANUAL.md')
    assert 'workspace/projects/' in text
    assert 'python3 tools/check_coherence.py --project .' in text
    assert 'logs/    = raw operational records' in text
    assert 'metrics/ = derived performance evidence' in text


def test_hermes_native_entrypoints_exist():
    root_agents = read('AGENTS.md')
    template_agents = read('templates/_shared_project/AGENTS.md')
    readme = read('README.md')
    assert 'Hermes-led adaptive interrogation' in root_agents
    assert 'Generated Project Agent Instructions' in template_agents
    assert 'Hermes-native' in readme
    assert 'coverage map, not the user-facing script' in readme


def test_orchestration_schedule_exists_and_automates_hygiene():
    text = read('automation/orchestration_schedule.yaml')
    for needle in ['select_model', 'validate_dry_run', 'update_context_summaries', 'check_coherence', 'review_metrics', 'resolve_deferred_specs']:
        assert needle in text


def test_new_project_default_output_is_derived_from_projectforge_root():
    text = read('tools/new_project.py')
    assert "canonical_output = base/'workspace'/'projects'" in text
    assert 'register_project.py' in text


def test_workspace_config_uses_rendered_projectforge_paths():
    text = read('templates/_shared_project/workspace_config.yaml')
    assert '{projectforge_root}' in text
    assert '{workspace_root}' in text
    assert '{projects_root}' in text


def test_orchestrator_hygiene_after_task(tmp_path):
    answers = {
        'purpose': 'Hygiene smoke project',
        'success': 'orchestrator hygiene runs on an isolated generated project',
        'project_type': 'general',
        'autonomy': 'balanced',
        'command_policy': 'layered default',
        'secrets': 'No secrets in v1.',
        'logging': 'ProjectForge default logging.',
        'folder_summaries': 'yes',
    }
    answers_path = tmp_path / 'answers.json'
    answers_path.write_text(json.dumps(answers), encoding='utf-8')
    generated = subprocess.run([
        sys.executable, str(ROOT/'tools'/'new_project.py'), '--name', 'Hygiene Test', '--template', 'default_project',
        '--output', str(tmp_path), '--answers-json', str(answers_path)
    ], capture_output=True, text=True)
    assert generated.returncode == 0, generated.stderr
    project = tmp_path / 'hygiene_test'
    result = subprocess.run([sys.executable, str(ROOT/'tools'/'orchestrator_hygiene.py'), '--project', str(project), '--phase', 'after_task'], capture_output=True, text=True)
    assert result.returncode == 0, result.stderr
    assert (project/'logs'/'derived'/'orchestrator_hygiene.log').exists()


def test_resolve_deferred_specs_creates_L3_question(tmp_path):
    (tmp_path/'metrics').mkdir(parents=True)
    (tmp_path/'metrics'/'events.jsonl').write_text(
        '{"event":"deferred_spec_block","entity":"orm_choice","status":"blocked"}\n'
        '{"event":"deferred_spec_block","entity":"orm_choice","status":"blocked"}\n',
        encoding='utf-8'
    )
    result = subprocess.run([sys.executable, str(ROOT/'tools'/'resolve_deferred_specs.py'), '--project', str(tmp_path)], capture_output=True, text=True)
    assert result.returncode == 0, result.stderr
    pending = list((tmp_path/'question_queue'/'pending').glob('*.json'))
    assert pending
    data = json.loads(pending[0].read_text(encoding='utf-8'))
    assert data['severity'] == 'L3'
