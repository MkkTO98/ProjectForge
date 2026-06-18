# Architecture-to-Reality Audit Process Implementation Report

Date: 2026-06-05
Status: Completed

## Request

Review ProjectForge governance, operating procedures, templates, validation systems, and agent instructions. Add a recurring Architecture-to-Reality Audit process that prevents long-term divergence between documented architecture, governance rules, operating procedures, state artifacts, and actual implementation.

## Startup context used

- `CONSTITUTION.md`
- `state/active_goal.md`
- `state/project_state.md`
- `state/architecture.md`
- `context/latest_handoff.md`
- `context/context_policy.yaml`
- Existing coherence, context-health, orchestration, template, README, operator manual, agent, and test files.

## Existing mechanisms found

ProjectForge already had several related mechanisms:

- `tools/check_coherence.py` validates required files, known duplicate/legacy systems, dry-run validity, workspace linkage, push rules, role prompt reporting discipline, logging/metrics separation, and invokes context health.
- `tools/context_health.py` checks primary-state/handoff/generated-context size and generated-bundle misuse.
- `automation/orchestration_schedule.yaml` already runs coherence after tasks and before commits and runs metrics/deferred-spec review periodically.
- `tools/orchestrator_hygiene.py` already bundles after-task, before-commit, and periodic hygiene steps.
- `context/context_policy.yaml`, `AGENTS.md`, and docs already define summary-first context, state/current-truth hygiene, raw-log separation, and project-wide review governance.
- Generated projects already inherit shared tools and AGENTS/context policy from `templates/_shared_project/`.

## Gaps found before implementation

- No formal named Architecture-to-Reality Audit process existed.
- No periodic audit cadence of every 5-10 completed tasks was encoded.
- No explicit triggers existed for running an audit before major architecture changes or major governance reviews.
- Existing coherence checks were invariant-focused but did not explicitly report the requested audit categories or drift types.
- No durable report template/workflow existed for architecture-vs-reality findings and remediation.
- Generated-project templates did not inherit a dedicated architecture-reality audit tool or policy.
- Orchestrator periodic hygiene did not run an architecture-reality audit.
- Docs and agent instructions did not tell agents when to run the audit, where to record results, or how to remediate findings.

## Implementation plan applied

1. Add a lightweight automated audit tool that checks mechanical drift and produces a markdown/json report.
2. Wire the tool into periodic governance and coherence expectations without replacing existing coherence/context-health checks.
3. Document cadence, triggers, categories, drift types, report location, and remediation workflow.
4. Patch root and shared templates so future generated projects inherit the process.
5. Add tests for root policy/tooling and generated-project inheritance.
6. Validate root and generated-project behavior with tests, coherence, context health, and a generated-project smoke run.

## Implemented changes

- Added `tools/architecture_reality_audit.py`.
- Added `templates/_shared_project/tools/architecture_reality_audit.py`.
- Updated `tools/check_coherence.py` and template copy to require the audit tool and root automation wiring.
- Updated `tools/orchestrator_hygiene.py` so `--phase periodic` and `--phase all` run the audit with `--write-report`.
- Updated `automation/orchestration_schedule.yaml` with:
  - periodic architecture audit cadence;
  - before-major-architecture-change trigger;
  - before-major-governance-review trigger.
- Added `templates/_shared_project/automation/orchestration_schedule.yaml` so generated projects inherit the schedule guidance.
- Updated `projectforge.yaml` orchestration metadata.
- Updated root/template `context/context_policy.yaml` with `architecture_reality_audit` governance settings.
- Updated root/template `AGENTS.md` and `instructions/GENERAL_INSTRUCTIONS.md`.
- Updated planner/reviewer/auditor role prompts in root and templates.
- Updated `docs/OPERATOR_MANUAL.md` with full process guidance.
- Updated `README.md` main tools and verification guidance.
- Updated permission allowlists in root, shared template, and project templates.
- Added regression tests in `tests/test_architecture_reality_audit.py`.
- Recorded generated audit output at `artifacts/reports/R-20260605-architecture-reality-audit.md`.

## Audit categories now covered

- architecture vs implementation
- state files vs reality
- agent instructions vs behavior
- logging systems
- context-management systems
- governance processes
- automation workflows
- templates vs generated projects

## Drift types now reported

- drift
- obsolete documentation
- duplicated systems
- unused systems
- missing implementations
- implementation without documentation
- documentation without implementation

## Migration plan for existing generated projects

Copy or regenerate these files from current ProjectForge templates:

- `tools/architecture_reality_audit.py`
- `tools/check_coherence.py`
- `context/context_policy.yaml`
- `AGENTS.md`
- `instructions/GENERAL_INSTRUCTIONS.md`
- relevant `agents/*.md`
- `automation/orchestration_schedule.yaml` if the project wants local schedule guidance
- `permissions/allowlist.yaml` or equivalent safe-command policy

Then run:

```bash
python3 tools/architecture_reality_audit.py --project . --write-report --json
python3 tools/check_coherence.py --project . --json
```

Resolve blocks before major architecture/governance work continues. Record durable policy/architecture changes as decision artifacts, refresh summaries/handoff, and rerun verification.

## Validation evidence

See final handoff for the latest post-summary verification. Initial architecture-reality audit after implementation reported:

```text
python3 tools/architecture_reality_audit.py --project . --write-report --json
blocks: []
warnings: []
report_path: /home/mkkto/srv/projectforge/artifacts/reports/R-20260605-architecture-reality-audit.md
```
