from pathlib import Path
import subprocess, sys, json

ROOT = Path(__file__).resolve().parents[1]

def test_required_files_exist():
    for rel in [
        'README.md', 'projectforge.yaml', 'CONSTITUTION.md', 'AGENTS.md', 'tools/new_project.py',
        'permissions/allowlist.yaml', 'permissions/denylist.yaml', 'permissions/escalation_rules.yaml',
        'state/active_goal.md', 'config/setup_questionnaire.yaml', 'config/sufficiency_policy.yaml',
        'models/registry.yaml', 'models/routing.yaml', 'models/selection_policy.yaml',
        'instructions/GENERAL_INSTRUCTIONS.md', 'instructions/CONTEXT_POLICY.md',
        'instructions/SMALL_SKILLS_POLICY.md', 'instructions/SPECIALIZED_AGENT_POLICY.md',
        'context/context_policy.yaml', 'knowledge/components.yaml', 'recovery/failure_playbooks.md',
        'metrics/metrics_policy.yaml', 'hardware/profile.yaml', 'simulation/dry_run_policy.yaml',
        'tools/select_model.py', 'tools/build_context.py', 'tools/update_context_summaries.py',
        'tools/dry_run.py', 'tools/validate_dry_run.py', 'tools/check_coherence.py', 'tools/escalate.py', 'tools/review_metrics.py',
        'tools/record_metric.py', 'tools/analyze_metrics.py'
    ]:
        assert (ROOT/rel).exists(), rel

def test_noninteractive_project_generation(tmp_path):
    script = ROOT/'tools'/'new_project.py'
    result = subprocess.run([sys.executable, str(script), '--name', 'Example Project', '--template', 'default_project', '--output', str(tmp_path), '--noninteractive', '--allow-deferred-required'], capture_output=True, text=True)
    assert result.returncode == 0, result.stderr
    project = tmp_path/'example_project'
    assert (project/'state'/'active_goal.md').exists()
    assert (project/'instructions'/'GENERAL_INSTRUCTIONS.md').exists()
    assert (project/'AGENTS.md').exists()
    assert 'Hermes operating model' in (project/'AGENTS.md').read_text(encoding='utf-8')
    assert (project/'models'/'registry.yaml').exists()
    assert (project/'context'/'context_policy.yaml').exists()
    assert (project/'simulation'/'dry_run_policy.yaml').exists()
    assert (project/'workspace_config.yaml').exists()
    assert not (project/'workspace').exists()
    assert (project/'metrics'/'metrics_policy.yaml').exists()
    assert (project/'state'/'_SUMMARY.md').exists()
    assert not (project/'logs'/'index').exists()
    assert any((project/'artifacts'/'decisions').glob('D-*-setup-purpose.md'))

def test_model_selection_tool():
    script = ROOT/'tools'/'select_model.py'
    result = subprocess.run([sys.executable, str(script), '--project', str(ROOT), '--agent', 'summarizer', '--task', 'folder_summary_update'], capture_output=True, text=True)
    assert result.returncode == 0, result.stderr
    assert result.stdout.strip() in {'small_summarizer','hermes_default'}

def test_dry_run_tool(tmp_path):
    (tmp_path/'simulation'/'dry_runs').mkdir(parents=True)
    script = ROOT/'tools'/'dry_run.py'
    result = subprocess.run([sys.executable, str(script), '--project', str(tmp_path), '--proposal', 'install dependency for schema migration', '--context-used', 'CONSTITUTION.md', '--decisions-checked', 'artifacts/decisions/D-20260530-projectforge-default-philosophy.md'], capture_output=True, text=True)
    assert result.returncode == 0, result.stderr
    out = Path(result.stdout.strip())
    assert out.exists()
    text = out.read_text(encoding='utf-8')
    assert 'full_dry_run' in text
    assert 'high' in text

def test_metrics_tools(tmp_path):
    rec = ROOT/'tools'/'record_metric.py'
    ana = ROOT/'tools'/'analyze_metrics.py'
    r1 = subprocess.run([sys.executable, str(rec), '--project', str(tmp_path), '--entity-type', 'agent', '--entity', 'coder', '--event', 'task_attempt', '--status', 'failed'], capture_output=True, text=True)
    assert r1.returncode == 0, r1.stderr
    r2 = subprocess.run([sys.executable, str(ana), '--project', str(tmp_path)], capture_output=True, text=True)
    assert r2.returncode == 0, r2.stderr
    assert (tmp_path/'metrics'/'reports'/'metrics_rollup.md').exists()

def test_context_builder(tmp_path):
    for rel, txt in {
        'CONSTITUTION.md': '# Constitution',
        'instructions/GENERAL_INSTRUCTIONS.md': '# General',
        'state/active_goal.md': '# Goal',
        'state/project_state.md': '# State',
        'state/architecture.md': '# Architecture',
    }.items():
        p=tmp_path/rel; p.parent.mkdir(parents=True, exist_ok=True); p.write_text(txt, encoding='utf-8')
    script = ROOT/'tools'/'build_context.py'
    result = subprocess.run([sys.executable, str(script), '--project', str(tmp_path), '--task', 'test'], capture_output=True, text=True)
    assert result.returncode == 0, result.stderr
    assert (tmp_path/'context'/'active_context.md').exists()
