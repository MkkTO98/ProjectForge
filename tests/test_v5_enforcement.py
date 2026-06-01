from pathlib import Path
import subprocess, sys, json

ROOT = Path(__file__).resolve().parents[1]


def test_no_redundant_hardware_profile_or_legacy_summary_tool():
    assert not (ROOT/'models'/'hardware_profile.yaml').exists()
    assert not (ROOT/'templates/_shared_project/models/hardware_profile.yaml').exists()
    assert not (ROOT/'tools'/'update_folder_summaries.py').exists()
    assert not (ROOT/'templates/_shared_project/tools/update_folder_summaries.py').exists()


def test_dry_run_requires_context_fields(tmp_path):
    script = ROOT/'tools'/'dry_run.py'
    result = subprocess.run([
        sys.executable, str(script), '--project', str(tmp_path), '--proposal', 'small documentation change',
        '--files', 'README.md', '--context-used', 'CONSTITUTION.md,state/project_state.md',
        '--decisions-checked', 'artifacts/decisions/D-20260530-projectforge-default-philosophy.md'
    ], capture_output=True, text=True)
    assert result.returncode == 0, result.stderr
    p = Path(result.stdout.strip())
    assert p.exists()
    text = p.read_text(encoding='utf-8')
    assert 'context_used' in text


def test_validate_dry_run_blocks_missing_fields(tmp_path):
    bad = tmp_path/'bad.md'
    bad.write_text('```json\n{"proposal":"x","risk":"low"}\n```\n', encoding='utf-8')
    result = subprocess.run([sys.executable, str(ROOT/'tools'/'validate_dry_run.py'), str(bad)], capture_output=True, text=True)
    assert result.returncode != 0
    assert 'missing required field' in result.stderr


def test_coherence_checker_passes_projectforge():
    result = subprocess.run([sys.executable, str(ROOT/'tools'/'check_coherence.py'), '--project', str(ROOT)], capture_output=True, text=True)
    assert result.returncode == 0, result.stderr
    assert 'coherence:' in result.stdout


def test_generated_project_uses_workspace_config_not_workspace_tree(tmp_path):
    script = ROOT/'tools'/'new_project.py'
    result = subprocess.run([sys.executable, str(script), '--name', 'Workspace Test', '--template', 'default_project', '--output', str(tmp_path), '--noninteractive', '--allow-deferred-required'], capture_output=True, text=True)
    assert result.returncode == 0, result.stderr
    project = tmp_path/'workspace_test'
    assert (project/'workspace_config.yaml').exists()
    assert not (project/'workspace').exists()


def test_escalation_tool_creates_question_for_specification(tmp_path):
    script = ROOT/'tools'/'escalate.py'
    result = subprocess.run([sys.executable, str(script), '--project', str(tmp_path), '--kind', 'specification', '--reason', 'ORM choice missing', '--task', 'database layer'], capture_output=True, text=True)
    assert result.returncode == 0, result.stderr
    assert any((tmp_path/'question_queue'/'pending').glob('*.md'))


def test_metrics_review_generates_report(tmp_path):
    (tmp_path/'metrics').mkdir(parents=True)
    (tmp_path/'metrics'/'events.jsonl').write_text('{"entity_type":"agent","entity":"coder","event":"task_attempt","status":"failed"}\n'*3, encoding='utf-8')
    result = subprocess.run([sys.executable, str(ROOT/'tools'/'review_metrics.py'), '--project', str(tmp_path)], capture_output=True, text=True)
    assert result.returncode == 0, result.stderr
    report = Path(result.stdout.strip())
    assert report.exists()
    assert 'Consider a specialized agent' in report.read_text(encoding='utf-8')
