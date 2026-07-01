# Architecture

ProjectForge is a reusable project initialization and governance framework. Generated projects are outputs of the framework, not subordinate runtime components owned by ProjectForge.

ProjectForge v1 now consists of five architectural systems. These systems are stable infrastructure and should remain the permanent foundation unless repeated implementation evidence from multiple independent generated projects proves that an existing subsystem cannot reasonably own a missing responsibility.

## 1. Project Identity

Project Identity defines project purpose, scope, non-scope, ownership boundaries, instruction hierarchy, and generated-project independence.

Primary artifacts:

- `CONSTITUTION.md`
- `AGENTS.md`
- generated-project constitution and agent instructions

Boundary:
Project Identity owns doctrine and authority. It does not own context management, governance records, implementation methodology, or validation mechanics.

## 2. Context and Continuity

Context and Continuity define bounded startup context, state pointers, handoffs, context bundles, summary-first retrieval, recovery behavior, and closeout discipline.

Primary artifacts/tools:

- `state/active_goal.md`
- `state/project_state.md`
- `state/architecture.md`
- `context/latest_handoff.md`
- `context/context_policy.yaml`
- `tools/build_context.py`
- `tools/recover_session.py`

Boundary:
Context files are current-state pointers and recovery aids, not historical ledgers or hidden governance records.

## 3. Governance and Decision

Governance and Decision define durable task, decision, report, handoff, approval, and architecture-audit records.

Primary artifacts:

- `artifacts/tasks/`
- `artifacts/decisions/`
- `artifacts/reports/`
- `artifacts/handoffs/`
- governance templates and folder summaries

Boundary:
Governance records preserve decisions and evidence. They do not create automatic authority over generated or external projects.

## 4. Work Execution Methodology

Work Execution Methodology defines bounded implementation slices, explicit non-goals, implementation boundaries, readiness, verification expectations, expected evidence, and evidence-gated architecture evolution.

Primary artifacts:

- `templates/_shared_project/instructions/WORK_EXECUTION_METHODOLOGY.md`
- generated task/report methodology sections
- methodology references from agent/general instructions

Boundary:
Methodology guides implementation work. It does not own project identity, context management, governance lifecycle, validation policy, or test strategy.

## 5. Validation and Evidence

Validation and Evidence strengthens existing project-owned tools rather than introducing a new validation platform.

Primary tools:

- `tools/check_coherence.py` for deterministic structural validation.
- `tools/context_health.py` for context boundedness and current-state hygiene.
- `tools/architecture_reality_audit.py` for advisory drift detection.
- `tools/recover_session.py` for bounded recovery contract evidence.
- `tools/validate_dry_run.py` for narrow dry-run report validation.

Boundary:
Validation checks mechanically verifiable claims and emits concise evidence. It does not become CI/CD, a workflow engine, an issue tracker, a quality management system, or a generic static analysis framework.

## MetaHarvest provider boundary

ProjectForge uses `/home/mkkto/srv/EIP/projects/MetaHarvest` as an active external advisory provider. ProjectForge must not host a full MetaHarvest project tree. Generated projects remain independent and project-owned.

MetaHarvest may recommend and preserve reusable non-domain knowledge, but it may not decide adoption, modify projects, create tasks inside target projects, enforce standards, force migration, or act as a controller.

## Framework-change doctrine

A framework change affects inheritance, templates, governance, questioning, artifact standards, handoff standards, delegation infrastructure, worker infrastructure, framework doctrine, or MetaHarvest doctrine. Such changes must be explicitly named.

ProjectForge improvements affect future inheritance by default. Existing projects receive recommendations or improvement notices, review them locally, and decide adoption through their own governance.

ProjectForge canonizes proven patterns, not examples, projects, or domains. Reusable capabilities should remain project-local until repeated implementation evidence demonstrates broader reuse.

## Automation doctrine

Automation is not a goal. Automation is justified only when it is reliable, understandable, maintainable, testable, coherent, observable, and reversible. Correctness takes precedence over automation.
