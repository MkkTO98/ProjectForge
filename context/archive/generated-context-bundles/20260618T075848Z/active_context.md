# Active Context Bundle

Task: ProjectForge local-execution cloud-governance architecture audit
Task type: project_audit
Context mode: project_wide_review

Review justification:
Verify that ProjectForge supports legitimate project-wide cloud governance reviews while keeping implementation local-first.

## context/project_summary.md

Reason included: project summary/current state

# Project Summary

## Latest recorded run
- Time: 2026-06-02T19:47:56.018331+00:00
- Agent: hermes
- Status: completed
- Goal: Implement strict ProjectForge context/token architecture
- Run ID: 4ebf51ed-cdd3-4d61-9eab-73c85d0c48d1


## state/project_state.md

Reason included: project summary/current state

# Project State

ProjectForge is a reusable, Hermes-native project initializer for agent-assisted projects. It is a file-first project operating system: Markdown for human-readable policy, YAML for machine-readable configuration, JSONL for events/metrics, and explicit artifacts for decisions, tasks, reports, and handoffs.

## Stable defaults
- AI-first but human-designed through initial questioning.
- Hermes is the primary operator and adaptive interviewer.
- `config/setup_questionnaire.yaml` is a coverage map, not a rigid user-facing terminal script.
- `tools/new_project.py` is the deterministic scaffold renderer and manual fallback.
- Balanced-to-aggressive local autonomy with permission and dry-run constraints.
- Standard logging by default; no SQLite index by default.
- Auto-commit after tests may be allowed; remote push requires human approval.
- Specialized agents require a request and explanation before generation.
- Context budgeting uses auto-maintained folder summaries as inputs.
- Capability failures escalate current Hermes session -> stronger local model if configured -> Codex/premium model -> human.

## Current local-execution/cloud-governance hardening
- `tools/build_context.py` builds summary-first bundles, estimates tokens, excludes raw logs/session transcripts from normal context, writes `context/context_audit.json` and `context/context_audit.md`, and supports three modes: normal, compact governance, and justified `project_wide_review`.
- `tools/select_model.py` routes implementation/refactoring/testing/debugging/summarization/retrieval toward local tools/models and requires an allowed governance/escalation reason plus a passing context audit before returning a cloud/Codex model.
- Project-wide architecture audits, redesigns, strategic planning, gap analysis, and consistency review remain possible under a larger configurable review budget when a review justification is recorded.
- `tools/log_run.py` preserves raw JSONL audit records while also maintaining compact derived session summaries, `context/latest_handoff.md`, and `context/project_summary.md`.
- `context/context_policy.yaml`, model routing/selection policies, logging policy, AGENTS/CONSTITUTION/README/instructions, and generated-project templates state the local-execution/cloud-governance split and raw-log exclusion requirements.

## Current v6 additions
- Root ProjectForge `AGENTS.md` for Hermes/local agent startup instructions.
- Generated-project `AGENTS.md` in `templates/_shared_project/`.
- Local Hermes skill `projectforge` installed under `~/.hermes/skills/software-development/projectforge/`.
- Hermes-led project creation flow documented in README and operator manual.
- Model registry/routing YAML repaired and reframed as advisory to Hermes.
- Test coverage now verifies Hermes-native entrypoints and generated-project `AGENTS.md`.

## Current hardening additions
- Root and generated-project coherence contracts are split with `tools/check_coherence.py --mode root|generated|auto`.
- Project scaffolding validates must-pause sufficiency items, derives paths from the active ProjectForge root, and avoids registering noncanonical temp outputs by default.
- Generated projects receive setup-answer-derived state files and no longer receive the factory-only `tools/new_project.py`.
- Workspace registry schema is clean YAML with no `raw` fallback or pytest temp entries.
- Context summary refreshes are deterministic, preserve curated Purpose/Active Work/Needs Attention sections, and avoid volatile timestamps/ignored dry-run report listings.
- Tests now exercise registry side effects, generated coherence, generated wrapper behavior across all templates, runtime-cache filtering, stale questionnaire language, uv-first install guidance, and non-mutating verification behavior.
- Generated templates use uv/venv-first setup guidance on this PEP 668/no-pip host.
- Generated agent prompts now tell Hermes sessions to use Hermes tools directly and reserve `tools/run.py` f

[TRUNCATED BY CONTEXT POLICY]


## state/active_goal.md

Reason included: project summary/current state

# Active Goal

Current objective:
- Maintain ProjectForge v1 as the reusable bootstrap scaffold for future AI-assisted projects.

Definition of done for ProjectForge v1:
- Can initialize a new project from templates.
- Stores setup decisions in `artifacts/decisions/`.
- Supports deferred specifications.
- Provides layered command permissions.
- Provides always-on logging.
- Provides MacroForge-like state files.
- Provides agent and skill instructions usable by Hermes or other agent frameworks.

Current constraints:
- Framework-adjacent by default.
- Do not rely on hidden chat memory.
- All durable assumptions must be file-backed.


## state/architecture.md

Reason included: project summary/current state

# Architecture

ProjectForge has four layers.

## 1. Global Foundation
Reusable skills, agent role documents, permissions, logging utilities, and project templates.

## 2. Bootstrap Layer
`tools/new_project.py` conducts an extensive setup interview or consumes a config file, then generates a new project instance.

## 3. Project Instance Layer
Generated projects include state files, decision/task artifacts, logging, permissions, and optional specialized agents.

## 4. Task Layer
Temporary task context is stored in `state/active_goal.md`, `artifacts/tasks/`, and run logs.

## Deferred specification
If a decision cannot be made during setup, it must be written as a deferred decision artifact. Agents should later ask for specification when that decision becomes relevant.

## Clarification severity
Questions are classified as:

- L1: Silent autonomy. The agent may proceed.
- L2: Batched clarification. Ask later; continue if safe.
- L3: Blocking clarification. Pause and ask immediately.
- L4: Emergency stop. Stop execution and require explicit human action.


## context/latest_handoff.md

Reason included: short recent handoff summary

# Latest Handoff

Updated: 2026-06-02T19:47:56.018331+00:00
Agent: hermes
Status: completed
Run ID: 4ebf51ed-cdd3-4d61-9eab-73c85d0c48d1

## Goal
Implement strict ProjectForge context/token architecture

## Files changed or touched
- `tools/build_context.py`
- `tools/select_model.py`
- `tools/log_run.py`
- `context/context_policy.yaml`
- `models/routing.yaml`
- `models/selection_policy.yaml`
- `logs/logging_policy.yaml`
- `AGENTS.md`
- `CONSTITUTION.md`
- `README.md`
- `instructions/CONTEXT_POLICY.md`
- `templates/_shared_project`
- `tests/test_context_policy_strict.py`
- `state/project_state.md`

## Compact notes
Strict summary-first context policy implemented. Raw logs remain stored but are excluded from normal context. Cloud/Codex routing now requires allowed escalation reason and context audit under budget. Tests and coherence passed.

## Context rule
Future agents should read this handoff, project/folder summaries, active task files, and relevant decisions first. Raw logs remain available for audit/debugging but must not be loaded into normal task context.


## state/recent_changes.md

Reason included: short recent handoff summary

# Recent Changes

- 2026-06-01: Made ProjectForge Hermes-native: added root/template `AGENTS.md`, created a local Hermes `projectforge` skill, reframed project creation as Hermes-led adaptive interrogation followed by noninteractive scaffold rendering, fixed model registry/routing YAML, updated tests, and recorded the decision in `artifacts/decisions/D-20260601-hermes-native-project-creation.md`.
- 2026-05-31: v4 added workspace layer, confidence scoring, memory retention, invariant tests, and simplified knowledge graph scope.
- v4 preserved manual GitHub push default, JSONL-first metrics, risk-scaled dry-run, and request-before-generation for specialized agents.


## _SUMMARY.md

Reason included: project-wide governance review folder map

# Folder Summary: .

## Purpose
This folder is part of the ProjectForge file-backed operating system for `.`.

## Contains
<!-- PROJECTFORGE:BEGIN-CONTAINS -->
- `.gitignore`
- `AGENTS.md`
- `CONSTITUTION.md`
- `README.md`
- `agents/`
- `artifacts/`
- `automation/`
- `confidence/`
- `config/`
- `context/`
- `docs/`
- `examples/`
- `hardware/`
- `instructions/`
- `knowledge/`
- `logs/`
- `memory/`
- `metrics/`
- `models/`
- `permissions/`
- `policies/`
- `projectforge.yaml`
- `pyproject.toml`
- `question_queue/`
- `recovery/`
- `simulation/`
- `skills/`
- `state/`
- `templates/`
- `tests/`
- `tools/`
- `workspace/`
<!-- PROJECTFORGE:END-CONTAINS -->

## Active Work
- No folder-specific active work recorded.

## Needs Attention
- No folder-specific issues recorded.


## agents/_SUMMARY.md

Reason included: project-wide governance review folder map

# Folder Summary: agents

## Purpose
This folder is part of the ProjectForge file-backed operating system for `agents`.

## Contains
<!-- PROJECTFORGE:BEGIN-CONTAINS -->
- `.gitkeep`
- `auditor.md`
- `bootstrapper.md`
- `coder.md`
- `context_manager.md`
- `model_router.md`
- `planner.md`
- `researcher.md`
- `reviewer.md`
- `summarizer.md`
<!-- PROJECTFORGE:END-CONTAINS -->

## Active Work
- No folder-specific active work recorded.

## Needs Attention
- No folder-specific issues recorded.


## artifacts/_SUMMARY.md

Reason included: project-wide governance review folder map

# Folder Summary: artifacts

## Purpose
This folder is part of the ProjectForge file-backed operating system for `artifacts`.

## Contains
<!-- PROJECTFORGE:BEGIN-CONTAINS -->
- `decisions/`
- `handoffs/`
- `reports/`
- `tasks/`
<!-- PROJECTFORGE:END-CONTAINS -->

## Active Work
- No folder-specific active work recorded.

## Needs Attention
- No folder-specific issues recorded.


## artifacts/decisions/_SUMMARY.md

Reason included: project-wide governance review folder map

# Folder Summary: artifacts/decisions

## Purpose
This folder is part of the ProjectForge file-backed operating system for `artifacts/decisions`.

## Contains
<!-- PROJECTFORGE:BEGIN-CONTAINS -->
- `.gitkeep`
- `D-20260530-clarification-severity-levels.md`
- `D-20260530-deferred-specification-policy.md`
- `D-20260530-folder-summary-policy.md`
- `D-20260530-git-workflow-default.md`
- `D-20260530-model-registry-and-routing.md`
- `D-20260530-projectforge-default-philosophy.md`
- `D-20260530-structured-questionnaire-and-sufficiency.md`
- `D-20260531-v4-workspace-confidence-and-simplification.md`
- `D-20260601-hermes-native-project-creation.md`
- `D-20260601-projectforge-batch2-generated-ux.md`
- `D-20260601-projectforge-hardening.md`
<!-- PROJECTFORGE:END-CONTAINS -->

## Active Work
- No folder-specific active work recorded.

## Needs Attention
- No folder-specific issues recorded.


## artifacts/handoffs/_SUMMARY.md

Reason included: project-wide governance review folder map

# Folder Summary: artifacts/handoffs

## Purpose
This folder is part of the ProjectForge file-backed operating system for `artifacts/handoffs`.

## Contains
<!-- PROJECTFORGE:BEGIN-CONTAINS -->
- `.gitkeep`
<!-- PROJECTFORGE:END-CONTAINS -->

## Active Work
- No folder-specific active work recorded.

## Needs Attention
- No folder-specific issues recorded.


## artifacts/reports/_SUMMARY.md

Reason included: project-wide governance review folder map

# Folder Summary: artifacts/reports

## Purpose
This folder is part of the ProjectForge file-backed operating system for `artifacts/reports`.

## Contains
<!-- PROJECTFORGE:BEGIN-CONTAINS -->
- `.gitkeep`
- `R-20260530-v2-gap-audit.md`
- `R-20260531-v5-coherence-report.md`
<!-- PROJECTFORGE:END-CONTAINS -->

## Active Work
- No folder-specific active work recorded.

## Needs Attention
- No folder-specific issues recorded.


## artifacts/tasks/_SUMMARY.md

Reason included: project-wide governance review folder map

# Folder Summary: artifacts/tasks

## Purpose
This folder is part of the ProjectForge file-backed operating system for `artifacts/tasks`.

## Contains
<!-- PROJECTFORGE:BEGIN-CONTAINS -->
- `.gitkeep`
- `T-001-verify-hermes-local-integration.md`
<!-- PROJECTFORGE:END-CONTAINS -->

## Active Work
- No folder-specific active work recorded.

## Needs Attention
- No folder-specific issues recorded.


## automation/_SUMMARY.md

Reason included: project-wide governance review folder map

# Folder Summary: automation

## Purpose
This folder is part of the ProjectForge file-backed operating system for `automation`.

## Contains
<!-- PROJECTFORGE:BEGIN-CONTAINS -->
- `orchestration_schedule.yaml`
<!-- PROJECTFORGE:END-CONTAINS -->

## Active Work
- No folder-specific active work recorded.

## Needs Attention
- No folder-specific issues recorded.


## confidence/_SUMMARY.md

Reason included: project-wide governance review folder map

# Folder Summary: confidence

## Purpose
This folder is part of the ProjectForge file-backed operating system for `confidence`.

## Contains
<!-- PROJECTFORGE:BEGIN-CONTAINS -->
- `confidence_policy.yaml`
- `confidence_template.md`
<!-- PROJECTFORGE:END-CONTAINS -->

## Active Work
- No folder-specific active work recorded.

## Needs Attention
- No folder-specific issues recorded.


## config/_SUMMARY.md

Reason included: project-wide governance review folder map

# Folder Summary: config

## Purpose
This folder is part of the ProjectForge file-backed operating system for `config`.

## Contains
<!-- PROJECTFORGE:BEGIN-CONTAINS -->
- `setup_questionnaire.yaml`
- `sufficiency_policy.yaml`
<!-- PROJECTFORGE:END-CONTAINS -->

## Active Work
- No folder-specific active work recorded.

## Needs Attention
- No folder-specific issues recorded.


## context/_SUMMARY.md

Reason included: summary for explicitly retrieved source file parent

# Folder Summary: context

## Purpose
This folder stores compact context policy, generated task-context reports, setup answer imports, and current handoff/project summaries. Generated bundles and audit files are for inspection and are not normal upstream context sources.

## Contains
<!-- PROJECTFORGE:BEGIN-CONTAINS -->
- `active_context.md`
- `compressed_context.md`
- `context_audit.json`
- `context_audit.md`
- `context_manifest.json`
- `context_manifest.yaml`
- `context_policy.yaml`
- `latest_handoff.md`
- `project_creation_answers_macroforge.json`
- `project_summary.md`
<!-- PROJECTFORGE:END-CONTAINS -->

## Active Work
- No folder-specific active work recorded.

## Needs Attention
- No folder-specific issues recorded.


## docs/_SUMMARY.md

Reason included: project-wide governance review folder map

# Folder Summary: docs

## Purpose
This folder is part of the ProjectForge file-backed operating system for `docs`.

## Contains
<!-- PROJECTFORGE:BEGIN-CONTAINS -->
- `AUTONOMY_LEVELS.md`
- `BRANCH_STRATEGY.md`
- `OPERATOR_MANUAL.md`
<!-- PROJECTFORGE:END-CONTAINS -->

## Active Work
- No folder-specific active work recorded.

## Needs Attention
- No folder-specific issues recorded.


## examples/_SUMMARY.md

Reason included: project-wide governance review folder map

# Folder Summary: examples

## Purpose
This folder is part of the ProjectForge file-backed operating system for `examples`.

## Contains
<!-- PROJECTFORGE:BEGIN-CONTAINS -->
- `answers.example.json`
<!-- PROJECTFORGE:END-CONTAINS -->

## Active Work
- No folder-specific active work recorded.

## Needs Attention
- No folder-specific issues recorded.


## hardware/_SUMMARY.md

Reason included: project-wide governance review folder map

# Folder Summary: hardware

## Purpose
This folder is part of the ProjectForge file-backed operating system for `hardware`.

## Contains
<!-- PROJECTFORGE:BEGIN-CONTAINS -->
- `profile.yaml`
- `resource_policy.yaml`
<!-- PROJECTFORGE:END-CONTAINS -->

## Active Work
- No folder-specific active work recorded.

## Needs Attention
- No folder-specific issues recorded.


## instructions/_SUMMARY.md

Reason included: project-wide governance review folder map

# Folder Summary: instructions

## Purpose
This folder is part of the ProjectForge file-backed operating system for `instructions`.

## Contains
<!-- PROJECTFORGE:BEGIN-CONTAINS -->
- `CONTEXT_POLICY.md`
- `FOLDER_SUMMARY_POLICY.md`
- `GENERAL_INSTRUCTIONS.md`
- `MODEL_ROUTING_POLICY.md`
- `PROJECTFORGE_SELF_MANAGEMENT.md`
- `SMALL_SKILLS_POLICY.md`
- `SPECIALIZED_AGENT_POLICY.md`
<!-- PROJECTFORGE:END-CONTAINS -->

## Active Work
- No folder-specific active work recorded.

## Needs Attention
- No folder-specific issues recorded.


## knowledge/_SUMMARY.md

Reason included: project-wide governance review folder map

# Folder Summary: knowledge

## Purpose
This folder is part of the ProjectForge file-backed operating system for `knowledge`.

## Contains
<!-- PROJECTFORGE:BEGIN-CONTAINS -->
- `components.yaml`
- `dependencies.yaml`
<!-- PROJECTFORGE:END-CONTAINS -->

## Active Work
- No folder-specific active work recorded.

## Needs Attention
- No folder-specific issues recorded.


## logs/_SUMMARY.md

Reason included: explicitly requested relevant folder summary

# Folder Summary: logs

## Purpose
This folder is part of the ProjectForge file-backed operating system for `logs`.

## Contains
<!-- PROJECTFORGE:BEGIN-CONTAINS -->
- `agents/`
- `derived/`
- `logging_policy.yaml`
- `raw/`
<!-- PROJECTFORGE:END-CONTAINS -->

## Active Work
- No folder-specific active work recorded.

## Needs Attention
- No folder-specific issues recorded.


## logs/derived/_SUMMARY.md

Reason included: project-wide governance review folder map

# Folder Summary: logs/derived

## Purpose
This folder is part of the ProjectForge file-backed operating system for `logs/derived`.

## Contains
<!-- PROJECTFORGE:BEGIN-CONTAINS -->
- `.gitkeep`
- `orchestrator_hygiene.log`
<!-- PROJECTFORGE:END-CONTAINS -->

## Active Work
- No folder-specific active work recorded.

## Needs Attention
- No folder-specific issues recorded.


## memory/_SUMMARY.md

Reason included: project-wide governance review folder map

# Folder Summary: memory

## Purpose
This folder is part of the ProjectForge file-backed operating system for `memory`.

## Contains
<!-- PROJECTFORGE:BEGIN-CONTAINS -->
- `archive/`
- `deprecated_decisions/`
- `retention_policy.yaml`
<!-- PROJECTFORGE:END-CONTAINS -->

## Active Work
- No folder-specific active work recorded.

## Needs Attention
- No folder-specific issues recorded.


## memory/archive/_SUMMARY.md

Reason included: project-wide governance review folder map

# Folder Summary: memory/archive

## Purpose
This folder is part of the ProjectForge file-backed operating system for `memory/archive`.

## Contains
<!-- PROJECTFORGE:BEGIN-CONTAINS -->
- Empty or placeholder-only folder.
<!-- PROJECTFORGE:END-CONTAINS -->

## Active Work
- No folder-specific active work recorded.

## Needs Attention
- No folder-specific issues recorded.


## memory/deprecated_decisions/_SUMMARY.md

Reason included: project-wide governance review folder map

# Folder Summary: memory/deprecated_decisions

## Purpose
This folder is part of the ProjectForge file-backed operating system for `memory/deprecated_decisions`.

## Contains
<!-- PROJECTFORGE:BEGIN-CONTAINS -->
- Empty or placeholder-only folder.
<!-- PROJECTFORGE:END-CONTAINS -->

## Active Work
- No folder-specific active work recorded.

## Needs Attention
- No folder-specific issues recorded.


## metrics/_SUMMARY.md

Reason included: project-wide governance review folder map

# Folder Summary: metrics

## Purpose
This folder is part of the ProjectForge file-backed operating system for `metrics`.

## Contains
<!-- PROJECTFORGE:BEGIN-CONTAINS -->
- `events.jsonl`
- `metrics_policy.yaml`
- `recommendations/`
- `reports/`
<!-- PROJECTFORGE:END-CONTAINS -->

## Active Work
- No folder-specific active work recorded.

## Needs Attention
- No folder-specific issues recorded.


## metrics/recommendations/_SUMMARY.md

Reason included: project-wide governance review folder map

# Folder Summary: metrics/recommendations

## Purpose
This folder is part of the ProjectForge file-backed operating system for `metrics/recommendations`.

## Contains
<!-- PROJECTFORGE:BEGIN-CONTAINS -->
- `README.md`
<!-- PROJECTFORGE:END-CONTAINS -->

## Active Work
- No folder-specific active work recorded.

## Needs Attention
- No folder-specific issues recorded.


## metrics/reports/_SUMMARY.md

Reason included: project-wide governance review folder map

# Folder Summary: metrics/reports

## Purpose
This folder is part of the ProjectForge file-backed operating system for `metrics/reports`.

## Contains
<!-- PROJECTFORGE:BEGIN-CONTAINS -->
- `README.md`
<!-- PROJECTFORGE:END-CONTAINS -->

## Active Work
- No folder-specific active work recorded.

## Needs Attention
- No folder-specific issues recorded.


## models/_SUMMARY.md

Reason included: summary for explicitly retrieved source file parent

# Folder Summary: models

## Purpose
This folder is part of the ProjectForge file-backed operating system for `models`.

## Contains
<!-- PROJECTFORGE:BEGIN-CONTAINS -->
- `registry.yaml`
- `routing.yaml`
- `selection_policy.yaml`
<!-- PROJECTFORGE:END-CONTAINS -->

## Active Work
- No folder-specific active work recorded.

## Needs Attention
- No folder-specific issues recorded.


## permissions/_SUMMARY.md

Reason included: project-wide governance review folder map

# Folder Summary: permissions

## Purpose
This folder is part of the ProjectForge file-backed operating system for `permissions`.

## Contains
<!-- PROJECTFORGE:BEGIN-CONTAINS -->
- `.gitkeep`
- `allowlist.yaml`
- `denylist.yaml`
- `escalation_rules.yaml`
<!-- PROJECTFORGE:END-CONTAINS -->

## Active Work
- No folder-specific active work recorded.

## Needs Attention
- No folder-specific issues recorded.


## policies/_SUMMARY.md

Reason included: project-wide governance review folder map

# Folder Summary: policies

## Purpose
This folder is part of the ProjectForge file-backed operating system for `policies`.

## Contains
<!-- PROJECTFORGE:BEGIN-CONTAINS -->
- `enforcement_policy.yaml`
<!-- PROJECTFORGE:END-CONTAINS -->

## Active Work
- No folder-specific active work recorded.

## Needs Attention
- No folder-specific issues recorded.


## question_queue/_SUMMARY.md

Reason included: project-wide governance review folder map

# Folder Summary: question_queue

## Purpose
This folder is part of the ProjectForge file-backed operating system for `question_queue`.

## Contains
<!-- PROJECTFORGE:BEGIN-CONTAINS -->
- `answered/`
- `archive/`
- `pending/`
<!-- PROJECTFORGE:END-CONTAINS -->

## Active Work
- No folder-specific active work recorded.

## Needs Attention
- No folder-specific issues recorded.


## question_queue/answered/_SUMMARY.md

Reason included: project-wide governance review folder map

# Folder Summary: question_queue/answered

## Purpose
This folder is part of the ProjectForge file-backed operating system for `question_queue/answered`.

## Contains
<!-- PROJECTFORGE:BEGIN-CONTAINS -->
- `.gitkeep`
<!-- PROJECTFORGE:END-CONTAINS -->

## Active Work
- No folder-specific active work recorded.

## Needs Attention
- No folder-specific issues recorded.


## question_queue/archive/_SUMMARY.md

Reason included: project-wide governance review folder map

# Folder Summary: question_queue/archive

## Purpose
This folder is part of the ProjectForge file-backed operating system for `question_queue/archive`.

## Contains
<!-- PROJECTFORGE:BEGIN-CONTAINS -->
- `.gitkeep`
<!-- PROJECTFORGE:END-CONTAINS -->

## Active Work
- No folder-specific active work recorded.

## Needs Attention
- No folder-specific issues recorded.


## question_queue/pending/_SUMMARY.md

Reason included: project-wide governance review folder map

# Folder Summary: question_queue/pending

## Purpose
This folder is part of the ProjectForge file-backed operating system for `question_queue/pending`.

## Contains
<!-- PROJECTFORGE:BEGIN-CONTAINS -->
- `.gitkeep`
<!-- PROJECTFORGE:END-CONTAINS -->

## Active Work
- No folder-specific active work recorded.

## Needs Attention
- No folder-specific issues recorded.


## recovery/_SUMMARY.md

Reason included: project-wide governance review folder map

# Folder Summary: recovery

## Purpose
This folder is part of the ProjectForge file-backed operating system for `recovery`.

## Contains
<!-- PROJECTFORGE:BEGIN-CONTAINS -->
- `escalation_policy.yaml`
- `failure_playbooks.md`
- `incident_log.md`
<!-- PROJECTFORGE:END-CONTAINS -->

## Active Work
- No folder-specific active work recorded.

## Needs Attention
- No folder-specific issues recorded.


## simulation/_SUMMARY.md

Reason included: project-wide governance review folder map

# Folder Summary: simulation

## Purpose
This folder is part of the ProjectForge file-backed operating system for `simulation`.

## Contains
<!-- PROJECTFORGE:BEGIN-CONTAINS -->
- `dry_run_policy.yaml`
- `dry_run_schema.yaml`
- `dry_runs/`
- `risk_classification.md`
<!-- PROJECTFORGE:END-CONTAINS -->

## Active Work
- No folder-specific active work recorded.

## Needs Attention
- No folder-specific issues recorded.


## simulation/dry_runs/_SUMMARY.md

Reason included: project-wide governance review folder map

# Folder Summary: simulation/dry_runs

## Purpose
This folder is part of the ProjectForge file-backed operating system for `simulation/dry_runs`.

## Contains
<!-- PROJECTFORGE:BEGIN-CONTAINS -->
- `README.md`
<!-- PROJECTFORGE:END-CONTAINS -->

## Active Work
- No folder-specific active work recorded.

## Needs Attention
- No folder-specific issues recorded.


## skills/_SUMMARY.md

Reason included: project-wide governance review folder map

# Folder Summary: skills

## Purpose
This folder is part of the ProjectForge file-backed operating system for `skills`.

## Contains
<!-- PROJECTFORGE:BEGIN-CONTAINS -->
- `.gitkeep`
- `clarification-queue.md`
- `command-permissions.md`
- `context-budgeting.md`
- `deferred-specification.md`
- `dry-run-workflow.md`
- `folder-summaries.md`
- `git-workflow.md`
- `logging-workflow.md`
- `metrics-feedback.md`
- `model-routing.md`
- `project-bootstrap.md`
- `state-update.md`
- `structured-questionnaire.md`
<!-- PROJECTFORGE:END-CONTAINS -->

## Active Work
- No folder-specific active work recorded.

## Needs Attention
- No folder-specific issues recorded.


## state/_SUMMARY.md

Reason included: project-wide governance review folder map

# Folder Summary: state

## Purpose
This folder is part of the ProjectForge file-backed operating system for `state`.

## Contains
<!-- PROJECTFORGE:BEGIN-CONTAINS -->
- `.gitkeep`
- `active_goal.md`
- `architecture.md`
- `known_issues.md`
- `lessons.md`
- `project_state.md`
- `recent_changes.md`
<!-- PROJECTFORGE:END-CONTAINS -->

## Active Work
- No folder-specific active work recorded.

## Needs Attention
- No folder-specific issues recorded.


## templates/_SUMMARY.md

Reason included: explicitly requested relevant folder summary

# Folder Summary: templates

## Purpose
This folder is part of the ProjectForge file-backed operating system for `templates`.

## Contains
<!-- PROJECTFORGE:BEGIN-CONTAINS -->
- `_shared_project/`
- `default_project/`
- `python_data_project/`
- `research_project/`
- `web_project/`
<!-- PROJECTFORGE:END-CONTAINS -->

## Active Work
- No folder-specific active work recorded.

## Needs Attention
- No folder-specific issues recorded.


## templates/_shared_project/_SUMMARY.md

Reason included: project-wide governance review folder map

# Folder Summary: templates/_shared_project

## Purpose
This folder is part of the ProjectForge file-backed operating system for `templates/_shared_project`.

## Contains
<!-- PROJECTFORGE:BEGIN-CONTAINS -->
- `AGENTS.md`
- `CONSTITUTION.md`
- `agents/`
- `artifacts/`
- `confidence/`
- `config/`
- `context/`
- `docs/`
- `hardware/`
- `instructions/`
- `knowledge/`
- `logs/`
- `memory/`
- `metrics/`
- `models/`
- `permissions/`
- `policies/`
- `question_queue/`
- `recovery/`
- `simulation/`
- `skills/`
- `state/`
- `tests/`
- `tools/`
- `workspace_config.yaml`
<!-- PROJECTFORGE:END-CONTAINS -->

## Active Work
- No folder-specific active work recorded.

## Needs Attention
- No folder-specific issues recorded.


## templates/_shared_project/agents/_SUMMARY.md

Reason included: project-wide governance review folder map

# Folder Summary: agents

## Contains
- `.gitkeep`
- `auditor.md`
- `bootstrapper.md`
- `coder.md`
- `context_manager.md`
- `model_router.md`
- `planner.md`
- `researcher.md`
- `reviewer.md`
- `summarizer.md`

## Purpose
Auto-maintained context-map summary. Agents should refine this when folder responsibilities become clearer.

## Active Work
- Not specified.

## Needs Attention
- Keep this summary current when changing this folder.


## templates/_shared_project/artifacts/_SUMMARY.md

Reason included: project-wide governance review folder map

# Folder Summary: artifacts

Updated: 2026-05-30

## Purpose
TODO: Maintain a concise description of what this folder contains and why it exists.

## Contents
- `decisions/`
- `handoffs/`
- `reports/`
- `tasks/`

## Current Status
- Auto-generated or refreshed summary. Replace TODOs with project-specific detail when material work occurs.

## Open Work
- Keep this summary updated when important files are added, removed, or repurposed.

## Agent Notes
- Read this file before scanning the whole folder.
- Update this file before handoff if you materially change this folder.


## templates/_shared_project/artifacts/decisions/_SUMMARY.md

Reason included: project-wide governance review folder map

# Folder Summary: artifacts/decisions

Updated: 2026-05-30

## Purpose
TODO: Maintain a concise description of what this folder contains and why it exists.

## Contents
- `.gitkeep`

## Current Status
- Auto-generated or refreshed summary. Replace TODOs with project-specific detail when material work occurs.

## Open Work
- Keep this summary updated when important files are added, removed, or repurposed.

## Agent Notes
- Read this file before scanning the whole folder.
- Update this file before handoff if you materially change this folder.


## templates/_shared_project/artifacts/tasks/_SUMMARY.md

Reason included: project-wide governance review folder map

# Folder Summary: artifacts/tasks

Updated: 2026-05-30

## Purpose
TODO: Maintain a concise description of what this folder contains and why it exists.

## Contents
- `.gitkeep`

## Current Status
- Auto-generated or refreshed summary. Replace TODOs with project-specific detail when material work occurs.

## Open Work
- Keep this summary updated when important files are added, removed, or repurposed.

## Agent Notes
- Read this file before scanning the whole folder.
- Update this file before handoff if you materially change this folder.


## templates/_shared_project/config/_SUMMARY.md

Reason included: project-wide governance review folder map

# Folder Summary: config

Updated: 2026-05-30

## Purpose
TODO: Maintain a concise description of what this folder contains and why it exists.

## Contents
- `setup_questionnaire.yaml`
- `sufficiency_policy.yaml`

## Current Status
- Auto-generated or refreshed summary. Replace TODOs with project-specific detail when material work occurs.

## Open Work
- Keep this summary updated when important files are added, removed, or repurposed.

## Agent Notes
- Read this file before scanning the whole folder.
- Update this file before handoff if you materially change this folder.


## templates/_shared_project/docs/_SUMMARY.md

Reason included: project-wide governance review folder map

# Folder Summary: docs

Updated: 2026-05-30

## Purpose
TODO: Maintain a concise description of what this folder contains and why it exists.

## Contents
- `AUTONOMY_LEVELS.md`
- `BRANCH_STRATEGY.md`

## Current Status
- Auto-generated or refreshed summary. Replace TODOs with project-specific detail when material work occurs.

## Open Work
- Keep this summary updated when important files are added, removed, or repurposed.

## Agent Notes
- Read this file before scanning the whole folder.
- Update this file before handoff if you materially change this folder.


## templates/_shared_project/instructions/_SUMMARY.md

Reason included: project-wide governance review folder map

# Folder Summary: instructions

Updated: 2026-05-30

## Purpose
TODO: Maintain a concise description of what this folder contains and why it exists.

## Contents
- `FOLDER_SUMMARY_POLICY.md`
- `GENERAL_INSTRUCTIONS.md`
- `MODEL_ROUTING_POLICY.md`
- `PROJECTFORGE_SELF_MANAGEMENT.md`

## Current Status
- Auto-generated or refreshed summary. Replace TODOs with project-specific detail when material work occurs.

## Open Work
- Keep this summary updated when important files are added, removed, or repurposed.

## Agent Notes
- Read this file before scanning the whole folder.
- Update this file before handoff if you materially change this folder.


## templates/_shared_project/logs/_SUMMARY.md

Reason included: project-wide governance review folder map

# Folder Summary: logs

Updated: 2026-05-30

## Purpose
TODO: Maintain a concise description of what this folder contains and why it exists.

## Contents
- `agents/`
- `derived/`
- `index/`
- `raw/`

## Current Status
- Auto-generated or refreshed summary. Replace TODOs with project-specific detail when material work occurs.

## Open Work
- Keep this summary updated when important files are added, removed, or repurposed.

## Agent Notes
- Read this file before scanning the whole folder.
- Update this file before handoff if you materially change this folder.


## templates/_shared_project/models/_SUMMARY.md

Reason included: project-wide governance review folder map

# Folder Summary: models

Updated: 2026-05-30

## Purpose
TODO: Maintain a concise description of what this folder contains and why it exists.

## Contents
- `hardware_profile.yaml`
- `registry.yaml`
- `routing.yaml`
- `selection_policy.yaml`

## Current Status
- Auto-generated or refreshed summary. Replace TODOs with project-specific detail when material work occurs.

## Open Work
- Keep this summary updated when important files are added, removed, or repurposed.

## Agent Notes
- Read this file before scanning the whole folder.
- Update this file before handoff if you materially change this folder.


## templates/_shared_project/permissions/_SUMMARY.md

Reason included: project-wide governance review folder map

# Folder Summary: permissions

Updated: 2026-05-30

## Purpose
TODO: Maintain a concise description of what this folder contains and why it exists.

## Contents
- `.gitkeep`
- `allowlist.yaml`
- `denylist.yaml`
- `escalation_rules.yaml`

## Current Status
- Auto-generated or refreshed summary. Replace TODOs with project-specific detail when material work occurs.

## Open Work
- Keep this summary updated when important files are added, removed, or repurposed.

## Agent Notes
- Read this file before scanning the whole folder.
- Update this file before handoff if you materially change this folder.


## templates/_shared_project/question_queue/_SUMMARY.md

Reason included: project-wide governance review folder map

# Folder Summary: question_queue

Updated: 2026-05-30

## Purpose
TODO: Maintain a concise description of what this folder contains and why it exists.

## Contents
- `answered/`
- `archive/`
- `pending/`

## Current Status
- Auto-generated or refreshed summary. Replace TODOs with project-specific detail when material work occurs.

## Open Work
- Keep this summary updated when important files are added, removed, or repurposed.

## Agent Notes
- Read this file before scanning the whole folder.
- Update this file before handoff if you materially change this folder.


## templates/_shared_project/skills/_SUMMARY.md

Reason included: project-wide governance review folder map

# Folder Summary: skills

Updated: 2026-05-30

## Purpose
TODO: Maintain a concise description of what this folder contains and why it exists.

## Contents
- `.gitkeep`
- `clarification-queue.md`
- `command-permissions.md`
- `deferred-specification.md`
- `folder-summaries.md`
- `git-workflow.md`
- `logging-workflow.md`
- `model-routing.md`
- `project-bootstrap.md`
- `state-update.md`
- `structured-questionnaire.md`

## Current Status
- Auto-generated or refreshed summary. Replace TODOs with project-specific detail when material work occurs.

## Open Work
- Keep this summary updated when important files are added, removed, or repurposed.

## Agent Notes
- Read this file before scanning the whole folder.
- Update this file before handoff if you materially change this folder.


## templates/_shared_project/state/_SUMMARY.md

Reason included: project-wide governance review folder map

# Folder Summary: state

Updated: 2026-05-30

## Purpose
TODO: Maintain a concise description of what this folder contains and why it exists.

## Contents
- `.gitkeep`

## Current Status
- Auto-generated or refreshed summary. Replace TODOs with project-specific detail when material work occurs.

## Open Work
- Keep this summary updated when important files are added, removed, or repurposed.

## Agent Notes
- Read this file before scanning the whole folder.
- Update this file before handoff if you materially change this folder.


## templates/_shared_project/tools/_SUMMARY.md

Reason included: project-wide governance review folder map

# Folder Summary: tools

Updated: 2026-05-30

## Purpose
TODO: Maintain a concise description of what this folder contains and why it exists.

## Contents
- `.gitkeep`
- `create_question.py`
- `detect_hardware.py`
- `git_autopush.py`
- `install.sh`
- `log_run.py`
- `new_project.py`
- `run.py`
- `select_model.py`
- `telegram_notifier_stub.py`
- `update_folder_summaries.py`
- `update_state.py`

## Current Status
- Auto-generated or refreshed summary. Replace TODOs with project-specific detail when material work occurs.

## Open Work
- Keep this summary updated when important files are added, removed, or repurposed.

## Agent Notes
- Read this file before scanning the whole folder.
- Update this file before handoff if you materially change this folder.


## templates/default_project/_SUMMARY.md

Reason included: project-wide governance review folder map

# Folder Summary: templates/default_project

## Purpose
This folder is part of the ProjectForge file-backed operating system for `templates/default_project`.

## Contains
<!-- PROJECTFORGE:BEGIN-CONTAINS -->
- `.gitignore`
- `.gitkeep`
- `README.md`
- `artifacts/`
- `logs/`
- `permissions/`
- `project.yaml`
- `question_queue/`
- `state/`
<!-- PROJECTFORGE:END-CONTAINS -->

## Active Work
- No folder-specific active work recorded.

## Needs Attention
- No folder-specific issues recorded.


## templates/default_project/artifacts/_SUMMARY.md

Reason included: project-wide governance review folder map

# Folder Summary: artifacts

Updated: 2026-05-30

## Purpose
TODO: Maintain a concise description of what this folder contains and why it exists.

## Contents
- `decisions/`
- `handoffs/`
- `reports/`
- `tasks/`

## Current Status
- Auto-generated or refreshed summary. Replace TODOs with project-specific detail when material work occurs.

## Open Work
- Keep this summary updated when important files are added, removed, or repurposed.

## Agent Notes
- Read this file before scanning the whole folder.
- Update this file before handoff if you materially change this folder.


## templates/default_project/artifacts/decisions/_SUMMARY.md

Reason included: project-wide governance review folder map

# Folder Summary: artifacts/decisions

Updated: 2026-05-30

## Purpose
TODO: Maintain a concise description of what this folder contains and why it exists.

## Contents
- `D-SETUP-project-initialization.md`

## Current Status
- Auto-generated or refreshed summary. Replace TODOs with project-specific detail when material work occurs.

## Open Work
- Keep this summary updated when important files are added, removed, or repurposed.

## Agent Notes
- Read this file before scanning the whole folder.
- Update this file before handoff if you materially change this folder.


## templates/default_project/artifacts/tasks/_SUMMARY.md

Reason included: project-wide governance review folder map

# Folder Summary: artifacts/tasks

Updated: 2026-05-30

## Purpose
TODO: Maintain a concise description of what this folder contains and why it exists.

## Contents
- `T-001-initial-validation.md`

## Current Status
- Auto-generated or refreshed summary. Replace TODOs with project-specific detail when material work occurs.

## Open Work
- Keep this summary updated when important files are added, removed, or repurposed.

## Agent Notes
- Read this file before scanning the whole folder.
- Update this file before handoff if you materially change this folder.


## templates/default_project/logs/_SUMMARY.md

Reason included: project-wide governance review folder map

# Folder Summary: logs

Updated: 2026-05-30

## Purpose
TODO: Maintain a concise description of what this folder contains and why it exists.

## Contents
- `agents/`
- `derived/`
- `index/`
- `raw/`

## Current Status
- Auto-generated or refreshed summary. Replace TODOs with project-specific detail when material work occurs.

## Open Work
- Keep this summary updated when important files are added, removed, or repurposed.

## Agent Notes
- Read this file before scanning the whole folder.
- Update this file before handoff if you materially change this folder.


## templates/default_project/permissions/_SUMMARY.md

Reason included: project-wide governance review folder map

# Folder Summary: permissions

Updated: 2026-05-30

## Purpose
TODO: Maintain a concise description of what this folder contains and why it exists.

## Contents
- `allowlist.yaml`
- `denylist.yaml`
- `escalation_rules.yaml`

## Current Status
- Auto-generated or refreshed summary. Replace TODOs with project-specific detail when material work occurs.

## Open Work
- Keep this summary updated when important files are added, removed, or repurposed.

## Agent Notes
- Read this file before scanning the whole folder.
- Update this file before handoff if you materially change this folder.


## templates/default_project/question_queue/_SUMMARY.md

Reason included: project-wide governance review folder map

# Folder Summary: question_queue

Updated: 2026-05-30

## Purpose
TODO: Maintain a concise description of what this folder contains and why it exists.

## Contents
- `answered/`
- `archive/`
- `pending/`

## Current Status
- Auto-generated or refreshed summary. Replace TODOs with project-specific detail when material work occurs.

## Open Work
- Keep this summary updated when important files are added, removed, or repurposed.

## Agent Notes
- Read this file before scanning the whole folder.
- Update this file before handoff if you materially change this folder.


## templates/default_project/state/_SUMMARY.md

Reason included: project-wide governance review folder map

# Folder Summary: state

Updated: 2026-05-30

## Purpose
TODO: Maintain a concise description of what this folder contains and why it exists.

## Contents
- `active_goal.md`
- `architecture.md`
- `known_issues.md`
- `lessons.md`
- `project_state.md`
- `recent_changes.md`

## Current Status
- Auto-generated or refreshed summary. Replace TODOs with project-specific detail when material work occurs.

## Open Work
- Keep this summary updated when important files are added, removed, or repurposed.

## Agent Notes
- Read this file before scanning the whole folder.
- Update this file before handoff if you materially change this folder.


## templates/python_data_project/_SUMMARY.md

Reason included: project-wide governance review folder map

# Folder Summary: templates/python_data_project

## Purpose
This folder is part of the ProjectForge file-backed operating system for `templates/python_data_project`.

## Contains
<!-- PROJECTFORGE:BEGIN-CONTAINS -->
- `.gitignore`
- `.gitkeep`
- `README.md`
- `artifacts/`
- `logs/`
- `permissions/`
- `project.yaml`
- `pyproject.toml`
- `question_queue/`
- `src/`
- `state/`
- `tests/`
<!-- PROJECTFORGE:END-CONTAINS -->

## Active Work
- No folder-specific active work recorded.

## Needs Attention
- No folder-specific issues recorded.


## templates/python_data_project/artifacts/_SUMMARY.md

Reason included: project-wide governance review folder map

# Folder Summary: artifacts

Updated: 2026-05-30

## Purpose
TODO: Maintain a concise description of what this folder contains and why it exists.

## Contents
- `decisions/`
- `handoffs/`
- `reports/`
- `tasks/`

## Current Status
- Auto-generated or refreshed summary. Replace TODOs with project-specific detail when material work occurs.

## Open Work
- Keep this summary updated when important files are added, removed, or repurposed.

## Agent Notes
- Read this file before scanning the whole folder.
- Update this file before handoff if you materially change this folder.


## templates/python_data_project/artifacts/decisions/_SUMMARY.md

Reason included: project-wide governance review folder map

# Folder Summary: artifacts/decisions

Updated: 2026-05-30

## Purpose
TODO: Maintain a concise description of what this folder contains and why it exists.

## Contents
- `D-SETUP-project-initialization.md`

## Current Status
- Auto-generated or refreshed summary. Replace TODOs with project-specific detail when material work occurs.

## Open Work
- Keep this summary updated when important files are added, removed, or repurposed.

## Agent Notes
- Read this file before scanning the whole folder.
- Update this file before handoff if you materially change this folder.


## templates/python_data_project/artifacts/tasks/_SUMMARY.md

Reason included: project-wide governance review folder map

# Folder Summary: artifacts/tasks

Updated: 2026-05-30

## Purpose
TODO: Maintain a concise description of what this folder contains and why it exists.

## Contents
- `T-001-initial-validation.md`

## Current Status
- Auto-generated or refreshed summary. Replace TODOs with project-specific detail when material work occurs.

## Open Work
- Keep this summary updated when important files are added, removed, or repurposed.

## Agent Notes
- Read this file before scanning the whole folder.
- Update this file before handoff if you materially change this folder.


## templates/python_data_project/logs/_SUMMARY.md

Reason included: project-wide governance review folder map

# Folder Summary: logs

Updated: 2026-05-30

## Purpose
TODO: Maintain a concise description of what this folder contains and why it exists.

## Contents
- `agents/`
- `derived/`
- `index/`
- `raw/`

## Current Status
- Auto-generated or refreshed summary. Replace TODOs with project-specific detail when material work occurs.

## Open Work
- Keep this summary updated when important files are added, removed, or repurposed.

## Agent Notes
- Read this file before scanning the whole folder.
- Update this file before handoff if you materially change this folder.


## templates/python_data_project/permissions/_SUMMARY.md

Reason included: project-wide governance review folder map

# Folder Summary: permissions

Updated: 2026-05-30

## Purpose
TODO: Maintain a concise description of what this folder contains and why it exists.

## Contents
- `allowlist.yaml`
- `denylist.yaml`
- `escalation_rules.yaml`

## Current Status
- Auto-generated or refreshed summary. Replace TODOs with project-specific detail when material work occurs.

## Open Work
- Keep this summary updated when important files are added, removed, or repurposed.

## Agent Notes
- Read this file before scanning the whole folder.
- Update this file before handoff if you materially change this folder.


## templates/python_data_project/question_queue/_SUMMARY.md

Reason included: project-wide governance review folder map

# Folder Summary: question_queue

Updated: 2026-05-30

## Purpose
TODO: Maintain a concise description of what this folder contains and why it exists.

## Contents
- `answered/`
- `archive/`
- `pending/`

## Current Status
- Auto-generated or refreshed summary. Replace TODOs with project-specific detail when material work occurs.

## Open Work
- Keep this summary updated when important files are added, removed, or repurposed.

## Agent Notes
- Read this file before scanning the whole folder.
- Update this file before handoff if you materially change this folder.


## templates/python_data_project/state/_SUMMARY.md

Reason included: project-wide governance review folder map

# Folder Summary: state

Updated: 2026-05-30

## Purpose
TODO: Maintain a concise description of what this folder contains and why it exists.

## Contents
- `active_goal.md`
- `architecture.md`
- `known_issues.md`
- `lessons.md`
- `project_state.md`
- `recent_changes.md`

## Current Status
- Auto-generated or refreshed summary. Replace TODOs with project-specific detail when material work occurs.

## Open Work
- Keep this summary updated when important files are added, removed, or repurposed.

## Agent Notes
- Read this file before scanning the whole folder.
- Update this file before handoff if you materially change this folder.


## templates/research_project/_SUMMARY.md

Reason included: project-wide governance review folder map

# Folder Summary: templates/research_project

## Purpose
This folder is part of the ProjectForge file-backed operating system for `templates/research_project`.

## Contains
<!-- PROJECTFORGE:BEGIN-CONTAINS -->
- `.gitignore`
- `.gitkeep`
- `README.md`
- `artifacts/`
- `logs/`
- `notes/`
- `permissions/`
- `project.yaml`
- `question_queue/`
- `state/`
<!-- PROJECTFORGE:END-CONTAINS -->

## Active Work
- No folder-specific active work recorded.

## Needs Attention
- No folder-specific issues recorded.


## templates/research_project/artifacts/_SUMMARY.md

Reason included: project-wide governance review folder map

# Folder Summary: artifacts

Updated: 2026-05-30

## Purpose
TODO: Maintain a concise description of what this folder contains and why it exists.

## Contents
- `decisions/`
- `handoffs/`
- `reports/`
- `tasks/`

## Current Status
- Auto-generated or refreshed summary. Replace TODOs with project-specific detail when material work occurs.

## Open Work
- Keep this summary updated when important files are added, removed, or repurposed.

## Agent Notes
- Read this file before scanning the whole folder.
- Update this file before handoff if you materially change this folder.


## templates/research_project/artifacts/decisions/_SUMMARY.md

Reason included: project-wide governance review folder map

# Folder Summary: artifacts/decisions

Updated: 2026-05-30

## Purpose
TODO: Maintain a concise description of what this folder contains and why it exists.

## Contents
- `D-SETUP-project-initialization.md`

## Current Status
- Auto-generated or refreshed summary. Replace TODOs with project-specific detail when material work occurs.

## Open Work
- Keep this summary updated when important files are added, removed, or repurposed.

## Agent Notes
- Read this file before scanning the whole folder.
- Update this file before handoff if you materially change this folder.


## templates/research_project/artifacts/tasks/_SUMMARY.md

Reason included: project-wide governance review folder map

# Folder Summary: artifacts/tasks

Updated: 2026-05-30

## Purpose
TODO: Maintain a concise description of what this folder contains and why it exists.

## Contents
- `T-001-initial-validation.md`

## Current Status
- Auto-generated or refreshed summary. Replace TODOs with project-specific detail when material work occurs.

## Open Work
- Keep this summary updated when important files are added, removed, or repurposed.

## Agent Notes
- Read this file before scanning the whole folder.
- Update this file before handoff if you materially change this folder.


## templates/research_project/logs/_SUMMARY.md

Reason included: project-wide governance review folder map

# Folder Summary: logs

Updated: 2026-05-30

## Purpose
TODO: Maintain a concise description of what this folder contains and why it exists.

## Contents
- `agents/`
- `derived/`
- `index/`
- `raw/`

## Current Status
- Auto-generated or refreshed summary. Replace TODOs with project-specific detail when material work occurs.

## Open Work
- Keep this summary updated when important files are added, removed, or repurposed.

## Agent Notes
- Read this file before scanning the whole folder.
- Update this file before handoff if you materially change this folder.


## templates/research_project/permissions/_SUMMARY.md

Reason included: project-wide governance review folder map

# Folder Summary: permissions

Updated: 2026-05-30

## Purpose
TODO: Maintain a concise description of what this folder contains and why it exists.

## Contents
- `allowlist.yaml`
- `denylist.yaml`
- `escalation_rules.yaml`

## Current Status
- Auto-generated or refreshed summary. Replace TODOs with project-specific detail when material work occurs.

## Open Work
- Keep this summary updated when important files are added, removed, or repurposed.

## Agent Notes
- Read this file before scanning the whole folder.
- Update this file before handoff if you materially change this folder.


## templates/research_project/question_queue/_SUMMARY.md

Reason included: project-wide governance review folder map

# Folder Summary: question_queue

Updated: 2026-05-30

## Purpose
TODO: Maintain a concise description of what this folder contains and why it exists.

## Contents
- `answered/`
- `archive/`
- `pending/`

## Current Status
- Auto-generated or refreshed summary. Replace TODOs with project-specific detail when material work occurs.

## Open Work
- Keep this summary updated when important files are added, removed, or repurposed.

## Agent Notes
- Read this file before scanning the whole folder.
- Update this file before handoff if you materially change this folder.


## templates/research_project/state/_SUMMARY.md

Reason included: project-wide governance review folder map

# Folder Summary: state

Updated: 2026-05-30

## Purpose
TODO: Maintain a concise description of what this folder contains and why it exists.

## Contents
- `active_goal.md`
- `architecture.md`
- `known_issues.md`
- `lessons.md`
- `project_state.md`
- `recent_changes.md`

## Current Status
- Auto-generated or refreshed summary. Replace TODOs with project-specific detail when material work occurs.

## Open Work
- Keep this summary updated when important files are added, removed, or repurposed.

## Agent Notes
- Read this file before scanning the whole folder.
- Update this file before handoff if you materially change this folder.


## templates/web_project/_SUMMARY.md

Reason included: project-wide governance review folder map

# Folder Summary: templates/web_project

## Purpose
This folder is part of the ProjectForge file-backed operating system for `templates/web_project`.

## Contains
<!-- PROJECTFORGE:BEGIN-CONTAINS -->
- `.gitignore`
- `.gitkeep`
- `README.md`
- `artifacts/`
- `logs/`
- `package.json`
- `permissions/`
- `project.yaml`
- `question_queue/`
- `state/`
<!-- PROJECTFORGE:END-CONTAINS -->

## Active Work
- No folder-specific active work recorded.

## Needs Attention
- No folder-specific issues recorded.


## templates/web_project/artifacts/_SUMMARY.md

Reason included: project-wide governance review folder map

# Folder Summary: artifacts

Updated: 2026-05-30

## Purpose
TODO: Maintain a concise description of what this folder contains and why it exists.

## Contents
- `decisions/`
- `handoffs/`
- `reports/`
- `tasks/`

## Current Status
- Auto-generated or refreshed summary. Replace TODOs with project-specific detail when material work occurs.

## Open Work
- Keep this summary updated when important files are added, removed, or repurposed.

## Agent Notes
- Read this file before scanning the whole folder.
- Update this file before handoff if you materially change this folder.


## templates/web_project/artifacts/decisions/_SUMMARY.md

Reason included: project-wide governance review folder map

# Folder Summary: artifacts/decisions

Updated: 2026-05-30

## Purpose
TODO: Maintain a concise description of what this folder contains and why it exists.

## Contents
- `D-SETUP-project-initialization.md`

## Current Status
- Auto-generated or refreshed summary. Replace TODOs with project-specific detail when material work occurs.

## Open Work
- Keep this summary updated when important files are added, removed, or repurposed.

## Agent Notes
- Read this file before scanning the whole folder.
- Update this file before handoff if you materially change this folder.


## templates/web_project/artifacts/tasks/_SUMMARY.md

Reason included: project-wide governance review folder map

# Folder Summary: artifacts/tasks

Updated: 2026-05-30

## Purpose
TODO: Maintain a concise description of what this folder contains and why it exists.

## Contents
- `T-001-initial-validation.md`

## Current Status
- Auto-generated or refreshed summary. Replace TODOs with project-specific detail when material work occurs.

## Open Work
- Keep this summary updated when important files are added, removed, or repurposed.

## Agent Notes
- Read this file before scanning the whole folder.
- Update this file before handoff if you materially change this folder.


## templates/web_project/logs/_SUMMARY.md

Reason included: project-wide governance review folder map

# Folder Summary: logs

Updated: 2026-05-30

## Purpose
TODO: Maintain a concise description of what this folder contains and why it exists.

## Contents
- `agents/`
- `derived/`
- `index/`
- `raw/`

## Current Status
- Auto-generated or refreshed summary. Replace TODOs with project-specific detail when material work occurs.

## Open Work
- Keep this summary updated when important files are added, removed, or repurposed.

## Agent Notes
- Read this file before scanning the whole folder.
- Update this file before handoff if you materially change this folder.


## templates/web_project/permissions/_SUMMARY.md

Reason included: project-wide governance review folder map

# Folder Summary: permissions

Updated: 2026-05-30

## Purpose
TODO: Maintain a concise description of what this folder contains and why it exists.

## Contents
- `allowlist.yaml`
- `denylist.yaml`
- `escalation_rules.yaml`

## Current Status
- Auto-generated or refreshed summary. Replace TODOs with project-specific detail when material work occurs.

## Open Work
- Keep this summary updated when important files are added, removed, or repurposed.

## Agent Notes
- Read this file before scanning the whole folder.
- Update this file before handoff if you materially change this folder.


## templates/web_project/question_queue/_SUMMARY.md

Reason included: project-wide governance review folder map

# Folder Summary: question_queue

Updated: 2026-05-30

## Purpose
TODO: Maintain a concise description of what this folder contains and why it exists.

## Contents
- `answered/`
- `archive/`
- `pending/`

## Current Status
- Auto-generated or refreshed summary. Replace TODOs with project-specific detail when material work occurs.

## Open Work
- Keep this summary updated when important files are added, removed, or repurposed.

## Agent Notes
- Read this file before scanning the whole folder.
- Update this file before handoff if you materially change this folder.


## templates/web_project/state/_SUMMARY.md

Reason included: project-wide governance review folder map

# Folder Summary: state

Updated: 2026-05-30

## Purpose
TODO: Maintain a concise description of what this folder contains and why it exists.

## Contents
- `active_goal.md`
- `architecture.md`
- `known_issues.md`
- `lessons.md`
- `project_state.md`
- `recent_changes.md`

## Current Status
- Auto-generated or refreshed summary. Replace TODOs with project-specific detail when material work occurs.

## Open Work
- Keep this summary updated when important files are added, removed, or repurposed.

## Agent Notes
- Read this file before scanning the whole folder.
- Update this file before handoff if you materially change this folder.


## tests/_SUMMARY.md

Reason included: summary for explicitly retrieved source file parent

# Folder Summary: tests

## Purpose
This folder is part of the ProjectForge file-backed operating system for `tests`.

## Contains
<!-- PROJECTFORGE:BEGIN-CONTAINS -->
- `.gitkeep`
- `invariants/`
- `test_batch2_generated_ux.py`
- `test_hardening.py`
- `test_invariants.py`
- `test_scaffold.py`
- `test_v5_enforcement.py`
- `test_v6_orchestration.py`
<!-- PROJECTFORGE:END-CONTAINS -->

## Active Work
- No folder-specific active work recorded.

## Needs Attention
- No folder-specific issues recorded.


## tests/invariants/_SUMMARY.md

Reason included: project-wide governance review folder map

# Folder Summary: tests/invariants

## Purpose
This folder is part of the ProjectForge file-backed operating system for `tests/invariants`.

## Contains
<!-- PROJECTFORGE:BEGIN-CONTAINS -->
- `README.md`
<!-- PROJECTFORGE:END-CONTAINS -->

## Active Work
- No folder-specific active work recorded.

## Needs Attention
- No folder-specific issues recorded.


## tools/_SUMMARY.md

Reason included: summary for explicitly retrieved source file parent

# Folder Summary: tools

## Purpose
This folder is part of the ProjectForge file-backed operating system for `tools`.

## Contains
<!-- PROJECTFORGE:BEGIN-CONTAINS -->
- `.gitkeep`
- `analyze_metrics.py`
- `build_context.py`
- `check_coherence.py`
- `confidence_report.py`
- `create_question.py`
- `detect_hardware.py`
- `dry_run.py`
- `escalate.py`
- `git_autopush.py`
- `install.sh`
- `log_run.py`
- `new_project.py`
- `orchestrator_hygiene.py`
- `record_metric.py`
- `register_project.py`
- `resolve_deferred_specs.py`
- `review_metrics.py`
- `run.py`
- `select_model.py`
- `telegram_notifier_stub.py`
- `update_context_summaries.py`
- `update_state.py`
- `validate_dry_run.py`
<!-- PROJECTFORGE:END-CONTAINS -->

## Active Work
- No folder-specific active work recorded.

## Needs Attention
- No folder-specific issues recorded.


## workspace/_SUMMARY.md

Reason included: project-wide governance review folder map

# Folder Summary: workspace

## Purpose
This folder is part of the ProjectForge file-backed operating system for `workspace`.

## Contains
<!-- PROJECTFORGE:BEGIN-CONTAINS -->
- `cross_project_dependencies.yaml`
- `projects/`
- `projects_registry.yaml`
- `shared_assets/`
- `shared_context/`
- `shared_logging/`
- `shared_models/`
- `shared_notifications/`
- `shared_skills/`
- `workspace_policy.yaml`
<!-- PROJECTFORGE:END-CONTAINS -->

## Active Work
- No folder-specific active work recorded.

## Needs Attention
- No folder-specific issues recorded.


## workspace/projects/_SUMMARY.md

Reason included: project-wide governance review folder map

# Folder Summary: workspace/projects

## Purpose
This folder is part of the ProjectForge file-backed operating system for `workspace/projects`.

## Contains
<!-- PROJECTFORGE:BEGIN-CONTAINS -->
- `macroforge/`
<!-- PROJECTFORGE:END-CONTAINS -->

## Active Work
- No folder-specific active work recorded.

## Needs Attention
- No folder-specific issues recorded.


## workspace/projects/macroforge/_SUMMARY.md

Reason included: project-wide governance review folder map

# Folder Summary: .

## Purpose
This folder is part of the ProjectForge file-backed operating system for `templates/python_data_project`.

## Contains
<!-- PROJECTFORGE:BEGIN-CONTAINS -->
- `.gitignore`
- `.gitkeep`
- `AGENTS.md`
- `CONSTITUTION.md`
- `README.md`
- `agents/`
- `artifacts/`
- `confidence/`
- `config/`
- `context/`
- `data/`
- `db/`
- `docs/`
- `hardware/`
- `instructions/`
- `knowledge/`
- `logs/`
- `memory/`
- `metrics/`
- `models/`
- `permissions/`
- `pipelines/`
- `policies/`
- `project.yaml`
- `pyproject.toml`
- `question_queue/`
- `recovery/`
- `reports/`
- `research/`
- `simulation/`
- `skills/`
- `src/`
- `state/`
- `tests/`
- `tools/`
- `workspace_config.yaml`
<!-- PROJECTFORGE:END-CONTAINS -->

## Active Work
- No folder-specific active work recorded.

## Needs Attention
- No folder-specific issues recorded.


## workspace/projects/macroforge/agents/_SUMMARY.md

Reason included: project-wide governance review folder map

# Folder Summary: agents

## Purpose
This folder is part of the ProjectForge file-backed operating system for `agents`.

## Contains
<!-- PROJECTFORGE:BEGIN-CONTAINS -->
- `.gitkeep`
- `auditor.md`
- `bootstrapper.md`
- `coder.md`
- `context_manager.md`
- `model_router.md`
- `planner.md`
- `researcher.md`
- `reviewer.md`
- `summarizer.md`
<!-- PROJECTFORGE:END-CONTAINS -->

## Active Work
- No folder-specific active work recorded.

## Needs Attention
- No folder-specific issues recorded.


## workspace/projects/macroforge/artifacts/_SUMMARY.md

Reason included: project-wide governance review folder map

# Folder Summary: artifacts

## Purpose
This folder is part of the ProjectForge file-backed operating system for `artifacts`.

## Contains
<!-- PROJECTFORGE:BEGIN-CONTAINS -->
- `decisions/`
- `handoffs/`
- `reports/`
- `tasks/`
<!-- PROJECTFORGE:END-CONTAINS -->

## Active Work
- No folder-specific active work recorded.

## Needs Attention
- No folder-specific issues recorded.


## workspace/projects/macroforge/artifacts/decisions/_SUMMARY.md

Reason included: project-wide governance review folder map

# Folder Summary: artifacts/decisions

## Purpose
This folder is part of the ProjectForge file-backed operating system for `artifacts/decisions`.

## Contains
<!-- PROJECTFORGE:BEGIN-CONTAINS -->
- `.gitkeep`
- `D-20260602-setup-autonomy.md`
- `D-20260602-setup-available_models.md`
- `D-20260602-setup-branch_strategy.md`
- `D-20260602-setup-clarification_channel.md`
- `D-20260602-setup-command_policy.md`
- `D-20260602-setup-deployment.md`
- `D-20260602-setup-documentation_standard.md`
- `D-20260602-setup-external_services.md`
- `D-20260602-setup-folder_summaries.md`
- `D-20260602-setup-git_remote.md`
- `D-20260602-setup-language.md`
- `D-20260602-setup-logging.md`
- `D-20260602-setup-model_policy.md`
- `D-20260602-setup-non_goals.md`
- `D-20260602-setup-premium_escalation.md`
- `D-20260602-setup-project_type.md`
- `D-20260602-setup-purpose.md`
- `D-20260602-setup-secrets.md`
- `D-20260602-setup-specialized_agents.md`
- `D-20260602-setup-storage.md`
- `D-20260602-setup-success.md`
- `D-20260602-setup-testing.md`
- `D-20260602-setup-unanswered_blocking_policy.md`
- `D-20260602-setup-users.md`
- `D-SETUP-project-initialization.md`
- `DEC-001-project-scope-and-v1-slice.md`
- `DEC-002-local-agent-operating-model.md`
- `DEC-003-canonical-projectforge-workspace-location.md`
- `DEC-004-v0-postgresql-schema-foundation.md`
<!-- PROJECTFORGE:END-CONTAINS -->

## Active Work
- `DEC-004-v0-postgresql-schema-foundation.md`: accepted v0 PostgreSQL schema choices for the WDI vertical-slice foundation.

## Needs Attention
- No folder-specific issues recorded.


## workspace/projects/macroforge/artifacts/handoffs/_SUMMARY.md

Reason included: project-wide governance review folder map

# Folder Summary: artifacts/handoffs

## Purpose
This folder is part of the ProjectForge file-backed operating system for `artifacts/handoffs`.

## Contains
<!-- PROJECTFORGE:BEGIN-CONTAINS -->
- `.gitkeep`
<!-- PROJECTFORGE:END-CONTAINS -->

## Active Work
- No folder-specific active work recorded.

## Needs Attention
- No folder-specific issues recorded.


## workspace/projects/macroforge/artifacts/reports/_SUMMARY.md

Reason included: project-wide governance review folder map

# Folder Summary: artifacts/reports

## Purpose
This folder stores durable run reports, validation reports, and inspectable task evidence promoted from runtime logs.

## Contains
<!-- PROJECTFORGE:BEGIN-CONTAINS -->
- `.gitkeep`
- `wdi_extract_smoke_20260602_task004.json`
- `wdi_extract_smoke_20260602_task004_hardened.json`
<!-- PROJECTFORGE:END-CONTAINS -->

## Active Work
- `wdi_extract_smoke_20260602_task004_hardened.json`: final TASK-004 live no-key WDI smoke extraction report after immutability/run-id hardening.
- `wdi_extract_smoke_20260602_task004.json`: earlier TASK-004 smoke report retained as evidence from the first live extraction before hardening.

## Needs Attention
- No folder-specific issues recorded.


## workspace/projects/macroforge/artifacts/tasks/_SUMMARY.md

Reason included: project-wide governance review folder map

# Folder Summary: artifacts/tasks

## Purpose
This folder is part of the ProjectForge file-backed operating system for `artifacts/tasks`.

## Contains
<!-- PROJECTFORGE:BEGIN-CONTAINS -->
- `.gitkeep`
- `TASK-001-initial-validation.md`
- `TASK-002-v0-schema-wdi-ingestion.md`
- `TASK-003-v0-postgresql-schema-foundation.md`
- `TASK-004-narrow-wdi-extract-raw-evidence.md`
<!-- PROJECTFORGE:END-CONTAINS -->

## Active Work
- `TASK-002-v0-schema-wdi-ingestion.md`: todo; next remaining implementation work is loading normalized WDI records into PostgreSQL staging/curated tables against the v0 schema.

## Needs Attention
- No folder-specific issues recorded.


## workspace/projects/macroforge/confidence/_SUMMARY.md

Reason included: project-wide governance review folder map

# Folder Summary: confidence

## Purpose
This folder is part of the ProjectForge file-backed operating system for `confidence`.

## Contains
<!-- PROJECTFORGE:BEGIN-CONTAINS -->
- `.gitkeep`
- `confidence_policy.yaml`
- `confidence_template.md`
<!-- PROJECTFORGE:END-CONTAINS -->

## Active Work
- No folder-specific active work recorded.

## Needs Attention
- No folder-specific issues recorded.


## workspace/projects/macroforge/config/_SUMMARY.md

Reason included: project-wide governance review folder map

# Folder Summary: config

## Purpose
This folder is part of the ProjectForge file-backed operating system for `config`.

## Contains
<!-- PROJECTFORGE:BEGIN-CONTAINS -->
- `setup_questionnaire.yaml`
- `sufficiency_policy.yaml`
<!-- PROJECTFORGE:END-CONTAINS -->

## Active Work
- No folder-specific active work recorded.

## Needs Attention
- No folder-specific issues recorded.


## workspace/projects/macroforge/context/_SUMMARY.md

Reason included: project-wide governance review folder map

# Folder Summary: context

## Purpose
This folder is part of the ProjectForge file-backed operating system for `context`.

## Contains
<!-- PROJECTFORGE:BEGIN-CONTAINS -->
- `.gitkeep`
- `PROJECT_CONTEXT.md`
- `active_context.md`
- `compressed_context.md`
- `context_manifest.json`
- `context_manifest.yaml`
- `context_policy.yaml`
- `imports/`
<!-- PROJECTFORGE:END-CONTAINS -->

## Active Work
- No folder-specific active work recorded.

## Needs Attention
- No folder-specific issues recorded.


## workspace/projects/macroforge/context/imports/_SUMMARY.md

Reason included: project-wide governance review folder map

# Folder Summary: context/imports

## Purpose
This folder is part of the ProjectForge file-backed operating system for `context/imports`.

## Contains
<!-- PROJECTFORGE:BEGIN-CONTAINS -->
- `chatgpt_export_recovery/`
<!-- PROJECTFORGE:END-CONTAINS -->

## Active Work
- No folder-specific active work recorded.

## Needs Attention
- No folder-specific issues recorded.


## workspace/projects/macroforge/data/_SUMMARY.md

Reason included: project-wide governance review folder map

# Folder Summary: data

## Purpose
This folder is part of the ProjectForge file-backed operating system for `data`.

## Contains
<!-- PROJECTFORGE:BEGIN-CONTAINS -->
- `.gitkeep`
- `curated/`
- `metadata/`
- `raw/`
- `staging/`
<!-- PROJECTFORGE:END-CONTAINS -->

## Active Work
- No folder-specific active work recorded.

## Needs Attention
- No folder-specific issues recorded.


## workspace/projects/macroforge/data/curated/_SUMMARY.md

Reason included: project-wide governance review folder map

# Folder Summary: data/curated

## Purpose
This folder is part of the ProjectForge file-backed operating system for `data/curated`.

## Contains
<!-- PROJECTFORGE:BEGIN-CONTAINS -->
- `.gitkeep`
<!-- PROJECTFORGE:END-CONTAINS -->

## Active Work
- No folder-specific active work recorded.

## Needs Attention
- No folder-specific issues recorded.


## workspace/projects/macroforge/data/metadata/_SUMMARY.md

Reason included: project-wide governance review folder map

# Folder Summary: data/metadata

## Purpose
This folder stores source metadata, checksums, and lineage evidence for raw and loaded data. Runtime checksum/lineage contents are ignored by git except `.gitkeep`.

## Contains
<!-- PROJECTFORGE:BEGIN-CONTAINS -->
- `.gitkeep`
- `checksums/`
- `lineage/`
<!-- PROJECTFORGE:END-CONTAINS -->

## Active Work
- Runtime smoke checksum/source metadata exists under ignored paths `data/metadata/checksums/wdi/smoke_20260602_task004/` and `data/metadata/checksums/wdi/smoke_20260602_task004_hardened/` for TASK-004 WDI extraction smoke runs.

## Needs Attention
- Preserve checksum metadata with raw evidence; do not commit large runtime metadata unless explicitly reviewed.


## workspace/projects/macroforge/data/raw/_SUMMARY.md

Reason included: project-wide governance review folder map

# Folder Summary: data/raw

## Purpose
This folder stores immutable raw source extracts as runtime evidence. Contents are ignored by git except `.gitkeep`.

## Contains
<!-- PROJECTFORGE:BEGIN-CONTAINS -->
- `.gitkeep`
<!-- PROJECTFORGE:END-CONTAINS -->

## Active Work
- Runtime smoke evidence exists under ignored paths `data/raw/wdi/smoke_20260602_task004/` and `data/raw/wdi/smoke_20260602_task004_hardened/` for TASK-004 WDI extraction smoke runs.

## Needs Attention
- Preserve raw files as immutable evidence; do not commit large raw runtime artifacts unless explicitly reviewed.


## workspace/projects/macroforge/data/staging/_SUMMARY.md

Reason included: project-wide governance review folder map

# Folder Summary: data/staging

## Purpose
This folder is part of the ProjectForge file-backed operating system for `data/staging`.

## Contains
<!-- PROJECTFORGE:BEGIN-CONTAINS -->
- `.gitkeep`
<!-- PROJECTFORGE:END-CONTAINS -->

## Active Work
- No folder-specific active work recorded.

## Needs Attention
- No folder-specific issues recorded.


## workspace/projects/macroforge/db/_SUMMARY.md

Reason included: project-wide governance review folder map

# Folder Summary: db

## Purpose
This folder is part of the ProjectForge file-backed operating system for `db`.

## Contains
<!-- PROJECTFORGE:BEGIN-CONTAINS -->
- `.gitkeep`
- `migrations/`
- `queries/`
- `schema/`
<!-- PROJECTFORGE:END-CONTAINS -->

## Active Work
- No folder-specific active work recorded.

## Needs Attention
- No folder-specific issues recorded.


## workspace/projects/macroforge/db/migrations/_SUMMARY.md

Reason included: project-wide governance review folder map

# Folder Summary: db/migrations

## Purpose
This folder stores SQL migrations for MacroForge's PostgreSQL-backed macro data warehouse.

## Contains
<!-- PROJECTFORGE:BEGIN-CONTAINS -->
- `.gitkeep`
- `001_v0_schema.sql`
<!-- PROJECTFORGE:END-CONTAINS -->

## Active Work
- `001_v0_schema.sql`: v0 metadata, staging, curated dimensions, and canonical fact schema for the WDI vertical slice.

## Needs Attention
- No folder-specific issues recorded.


## workspace/projects/macroforge/db/queries/_SUMMARY.md

Reason included: project-wide governance review folder map

# Folder Summary: db/queries

## Purpose
This folder stores reusable SQL verification and analysis queries.

## Contains
<!-- PROJECTFORGE:BEGIN-CONTAINS -->
- `.gitkeep`
- `verify_v0_schema.sql`
<!-- PROJECTFORGE:END-CONTAINS -->

## Active Work
- `verify_v0_schema.sql`: inspectable checks for v0 schema tables, constraints, and the default attribute set.

## Needs Attention
- No folder-specific issues recorded.


## workspace/projects/macroforge/db/schema/_SUMMARY.md

Reason included: project-wide governance review folder map

# Folder Summary: db/schema

## Purpose
This folder stores human-readable schema documentation and snapshots for MacroForge's PostgreSQL model.

## Contains
<!-- PROJECTFORGE:BEGIN-CONTAINS -->
- `.gitkeep`
- `v0_schema.md`
<!-- PROJECTFORGE:END-CONTAINS -->

## Active Work
- `v0_schema.md`: documents the v0 PostgreSQL schema foundation and canonical observation grain.

## Needs Attention
- No folder-specific issues recorded.


## workspace/projects/macroforge/docs/_SUMMARY.md

Reason included: project-wide governance review folder map

# Folder Summary: docs

## Purpose
This folder is part of the ProjectForge file-backed operating system for `docs`.

## Contains
<!-- PROJECTFORGE:BEGIN-CONTAINS -->
- `.gitkeep`
- `AUTONOMY_LEVELS.md`
- `BRANCH_STRATEGY.md`
- `architecture/`
- `data/`
- `runbooks/`
<!-- PROJECTFORGE:END-CONTAINS -->

## Active Work
- No folder-specific active work recorded.

## Needs Attention
- No folder-specific issues recorded.


## workspace/projects/macroforge/docs/architecture/_SUMMARY.md

Reason included: project-wide governance review folder map

# Folder Summary: docs/architecture

## Purpose
This folder is part of the ProjectForge file-backed operating system for `docs/architecture`.

## Contains
<!-- PROJECTFORGE:BEGIN-CONTAINS -->
- `.gitkeep`
<!-- PROJECTFORGE:END-CONTAINS -->

## Active Work
- No folder-specific active work recorded.

## Needs Attention
- No folder-specific issues recorded.


## workspace/projects/macroforge/docs/data/_SUMMARY.md

Reason included: project-wide governance review folder map

# Folder Summary: docs/data

## Purpose
This folder is part of the ProjectForge file-backed operating system for `docs/data`.

## Contains
<!-- PROJECTFORGE:BEGIN-CONTAINS -->
- `.gitkeep`
<!-- PROJECTFORGE:END-CONTAINS -->

## Active Work
- No folder-specific active work recorded.

## Needs Attention
- No folder-specific issues recorded.


## workspace/projects/macroforge/docs/runbooks/_SUMMARY.md

Reason included: project-wide governance review folder map

# Folder Summary: docs/runbooks

## Purpose
This folder is part of the ProjectForge file-backed operating system for `docs/runbooks`.

## Contains
<!-- PROJECTFORGE:BEGIN-CONTAINS -->
- `.gitkeep`
- `low-token-local-agent-workflow.md`
<!-- PROJECTFORGE:END-CONTAINS -->

## Active Work
- No folder-specific active work recorded.

## Needs Attention
- No folder-specific issues recorded.


## workspace/projects/macroforge/hardware/_SUMMARY.md

Reason included: project-wide governance review folder map

# Folder Summary: hardware

## Purpose
This folder is part of the ProjectForge file-backed operating system for `hardware`.

## Contains
<!-- PROJECTFORGE:BEGIN-CONTAINS -->
- `.gitkeep`
- `profile.yaml`
- `resource_policy.yaml`
<!-- PROJECTFORGE:END-CONTAINS -->

## Active Work
- No folder-specific active work recorded.

## Needs Attention
- No folder-specific issues recorded.


## workspace/projects/macroforge/instructions/_SUMMARY.md

Reason included: project-wide governance review folder map

# Folder Summary: instructions

## Purpose
This folder is part of the ProjectForge file-backed operating system for `instructions`.

## Contains
<!-- PROJECTFORGE:BEGIN-CONTAINS -->
- `CONTEXT_POLICY.md`
- `FOLDER_SUMMARY_POLICY.md`
- `GENERAL_INSTRUCTIONS.md`
- `MODEL_ROUTING_POLICY.md`
- `PROJECTFORGE_SELF_MANAGEMENT.md`
- `SMALL_SKILLS_POLICY.md`
- `SPECIALIZED_AGENT_POLICY.md`
<!-- PROJECTFORGE:END-CONTAINS -->

## Active Work
- No folder-specific active work recorded.

## Needs Attention
- No folder-specific issues recorded.


## workspace/projects/macroforge/knowledge/_SUMMARY.md

Reason included: project-wide governance review folder map

# Folder Summary: knowledge

## Purpose
This folder is part of the ProjectForge file-backed operating system for `knowledge`.

## Contains
<!-- PROJECTFORGE:BEGIN-CONTAINS -->
- `.gitkeep`
- `components.yaml`
- `dependencies.yaml`
<!-- PROJECTFORGE:END-CONTAINS -->

## Active Work
- No folder-specific active work recorded.

## Needs Attention
- No folder-specific issues recorded.


## workspace/projects/macroforge/logs/_SUMMARY.md

Reason included: project-wide governance review folder map

# Folder Summary: logs

## Purpose
This folder is part of the ProjectForge file-backed operating system for `logs`.

## Contains
<!-- PROJECTFORGE:BEGIN-CONTAINS -->
- `agents/`
- `derived/`
- `logging_policy.yaml`
- `raw/`
<!-- PROJECTFORGE:END-CONTAINS -->

## Active Work
- No folder-specific active work recorded.

## Needs Attention
- No folder-specific issues recorded.


## workspace/projects/macroforge/logs/derived/_SUMMARY.md

Reason included: project-wide governance review folder map

# Folder Summary: logs/derived

## Purpose
This folder is part of the ProjectForge file-backed operating system for `logs/derived`.

## Contains
<!-- PROJECTFORGE:BEGIN-CONTAINS -->
- `.gitkeep`
<!-- PROJECTFORGE:END-CONTAINS -->

## Active Work
- No folder-specific active work recorded.

## Needs Attention
- No folder-specific issues recorded.


## workspace/projects/macroforge/memory/_SUMMARY.md

Reason included: project-wide governance review folder map

# Folder Summary: memory

## Purpose
This folder is part of the ProjectForge file-backed operating system for `memory`.

## Contains
<!-- PROJECTFORGE:BEGIN-CONTAINS -->
- `archive/`
- `deprecated_decisions/`
- `retention_policy.yaml`
<!-- PROJECTFORGE:END-CONTAINS -->

## Active Work
- No folder-specific active work recorded.

## Needs Attention
- No folder-specific issues recorded.


## workspace/projects/macroforge/memory/archive/_SUMMARY.md

Reason included: project-wide governance review folder map

# Folder Summary: memory/archive

## Purpose
This folder is part of the ProjectForge file-backed operating system for `memory/archive`.

## Contains
<!-- PROJECTFORGE:BEGIN-CONTAINS -->
- `.gitkeep`
<!-- PROJECTFORGE:END-CONTAINS -->

## Active Work
- No folder-specific active work recorded.

## Needs Attention
- No folder-specific issues recorded.


## workspace/projects/macroforge/memory/deprecated_decisions/_SUMMARY.md

Reason included: project-wide governance review folder map

# Folder Summary: memory/deprecated_decisions

## Purpose
This folder is part of the ProjectForge file-backed operating system for `memory/deprecated_decisions`.

## Contains
<!-- PROJECTFORGE:BEGIN-CONTAINS -->
- `.gitkeep`
<!-- PROJECTFORGE:END-CONTAINS -->

## Active Work
- No folder-specific active work recorded.

## Needs Attention
- No folder-specific issues recorded.


## workspace/projects/macroforge/metrics/_SUMMARY.md

Reason included: project-wide governance review folder map

# Folder Summary: metrics

## Purpose
This folder is part of the ProjectForge file-backed operating system for `metrics`.

## Contains
<!-- PROJECTFORGE:BEGIN-CONTAINS -->
- `events.jsonl`
- `metrics_policy.yaml`
- `recommendations/`
- `reports/`
<!-- PROJECTFORGE:END-CONTAINS -->

## Active Work
- No folder-specific active work recorded.

## Needs Attention
- No folder-specific issues recorded.


## workspace/projects/macroforge/metrics/recommendations/_SUMMARY.md

Reason included: project-wide governance review folder map

# Folder Summary: metrics/recommendations

## Purpose
This folder is part of the ProjectForge file-backed operating system for `metrics/recommendations`.

## Contains
<!-- PROJECTFORGE:BEGIN-CONTAINS -->
- `.gitkeep`
- `README.md`
<!-- PROJECTFORGE:END-CONTAINS -->

## Active Work
- No folder-specific active work recorded.

## Needs Attention
- No folder-specific issues recorded.


## workspace/projects/macroforge/metrics/reports/_SUMMARY.md

Reason included: project-wide governance review folder map

# Folder Summary: metrics/reports

## Purpose
This folder is part of the ProjectForge file-backed operating system for `metrics/reports`.

## Contains
<!-- PROJECTFORGE:BEGIN-CONTAINS -->
- `.gitkeep`
- `README.md`
<!-- PROJECTFORGE:END-CONTAINS -->

## Active Work
- No folder-specific active work recorded.

## Needs Attention
- No folder-specific issues recorded.


## workspace/projects/macroforge/models/_SUMMARY.md

Reason included: project-wide governance review folder map

# Folder Summary: models

## Purpose
This folder is part of the ProjectForge file-backed operating system for `models`.

## Contains
<!-- PROJECTFORGE:BEGIN-CONTAINS -->
- `registry.yaml`
- `routing.yaml`
- `selection_policy.yaml`
<!-- PROJECTFORGE:END-CONTAINS -->

## Active Work
- No folder-specific active work recorded.

## Needs Attention
- No folder-specific issues recorded.


## workspace/projects/macroforge/permissions/_SUMMARY.md

Reason included: project-wide governance review folder map

# Folder Summary: permissions

## Purpose
This folder is part of the ProjectForge file-backed operating system for `permissions`.

## Contains
<!-- PROJECTFORGE:BEGIN-CONTAINS -->
- `.gitkeep`
- `allowlist.yaml`
- `denylist.yaml`
- `escalation_rules.yaml`
<!-- PROJECTFORGE:END-CONTAINS -->

## Active Work
- No folder-specific active work recorded.

## Needs Attention
- No folder-specific issues recorded.


## workspace/projects/macroforge/pipelines/_SUMMARY.md

Reason included: project-wide governance review folder map

# Folder Summary: pipelines

## Purpose
This folder is part of the ProjectForge file-backed operating system for `pipelines`.

## Contains
<!-- PROJECTFORGE:BEGIN-CONTAINS -->
- `.gitkeep`
<!-- PROJECTFORGE:END-CONTAINS -->

## Active Work
- No folder-specific active work recorded.

## Needs Attention
- No folder-specific issues recorded.


## workspace/projects/macroforge/policies/_SUMMARY.md

Reason included: project-wide governance review folder map

# Folder Summary: policies

## Purpose
This folder is part of the ProjectForge file-backed operating system for `policies`.

## Contains
<!-- PROJECTFORGE:BEGIN-CONTAINS -->
- `enforcement_policy.yaml`
<!-- PROJECTFORGE:END-CONTAINS -->

## Active Work
- No folder-specific active work recorded.

## Needs Attention
- No folder-specific issues recorded.


## workspace/projects/macroforge/question_queue/_SUMMARY.md

Reason included: project-wide governance review folder map

# Folder Summary: question_queue

## Purpose
This folder is part of the ProjectForge file-backed operating system for `question_queue`.

## Contains
<!-- PROJECTFORGE:BEGIN-CONTAINS -->
- `answered/`
- `archive/`
- `pending/`
<!-- PROJECTFORGE:END-CONTAINS -->

## Active Work
- No folder-specific active work recorded.

## Needs Attention
- No folder-specific issues recorded.


## workspace/projects/macroforge/question_queue/answered/_SUMMARY.md

Reason included: project-wide governance review folder map

# Folder Summary: question_queue/answered

## Purpose
This folder is part of the ProjectForge file-backed operating system for `question_queue/answered`.

## Contains
<!-- PROJECTFORGE:BEGIN-CONTAINS -->
- `.gitkeep`
<!-- PROJECTFORGE:END-CONTAINS -->

## Active Work
- No folder-specific active work recorded.

## Needs Attention
- No folder-specific issues recorded.


## workspace/projects/macroforge/question_queue/archive/_SUMMARY.md

Reason included: project-wide governance review folder map

# Folder Summary: question_queue/archive

## Purpose
This folder is part of the ProjectForge file-backed operating system for `question_queue/archive`.

## Contains
<!-- PROJECTFORGE:BEGIN-CONTAINS -->
- `.gitkeep`
<!-- PROJECTFORGE:END-CONTAINS -->

## Active Work
- No folder-specific active work recorded.

## Needs Attention
- No folder-specific issues recorded.


## workspace/projects/macroforge/question_queue/pending/_SUMMARY.md

Reason included: project-wide governance review folder map

# Folder Summary: question_queue/pending

## Purpose
This folder is part of the ProjectForge file-backed operating system for `question_queue/pending`.

## Contains
<!-- PROJECTFORGE:BEGIN-CONTAINS -->
- `.gitkeep`
<!-- PROJECTFORGE:END-CONTAINS -->

## Active Work
- No folder-specific active work recorded.

## Needs Attention
- No folder-specific issues recorded.


## workspace/projects/macroforge/recovery/_SUMMARY.md

Reason included: project-wide governance review folder map

# Folder Summary: recovery

## Purpose
This folder is part of the ProjectForge file-backed operating system for `recovery`.

## Contains
<!-- PROJECTFORGE:BEGIN-CONTAINS -->
- `.gitkeep`
- `escalation_policy.yaml`
- `failure_playbooks.md`
- `incident_log.md`
<!-- PROJECTFORGE:END-CONTAINS -->

## Active Work
- No folder-specific active work recorded.

## Needs Attention
- No folder-specific issues recorded.


## workspace/projects/macroforge/reports/_SUMMARY.md

Reason included: project-wide governance review folder map

# Folder Summary: reports

## Purpose
This folder is part of the ProjectForge file-backed operating system for `reports`.

## Contains
<!-- PROJECTFORGE:BEGIN-CONTAINS -->
- `.gitkeep`
<!-- PROJECTFORGE:END-CONTAINS -->

## Active Work
- No folder-specific active work recorded.

## Needs Attention
- No folder-specific issues recorded.


## workspace/projects/macroforge/research/_SUMMARY.md

Reason included: project-wide governance review folder map

# Folder Summary: research

## Purpose
This folder is part of the ProjectForge file-backed operating system for `research`.

## Contains
<!-- PROJECTFORGE:BEGIN-CONTAINS -->
- `.gitkeep`
<!-- PROJECTFORGE:END-CONTAINS -->

## Active Work
- No folder-specific active work recorded.

## Needs Attention
- No folder-specific issues recorded.


## workspace/projects/macroforge/simulation/_SUMMARY.md

Reason included: project-wide governance review folder map

# Folder Summary: simulation

## Purpose
This folder is part of the ProjectForge file-backed operating system for `simulation`.

## Contains
<!-- PROJECTFORGE:BEGIN-CONTAINS -->
- `dry_run_policy.yaml`
- `dry_run_schema.yaml`
- `dry_runs/`
- `risk_classification.md`
<!-- PROJECTFORGE:END-CONTAINS -->

## Active Work
- No folder-specific active work recorded.

## Needs Attention
- No folder-specific issues recorded.


## workspace/projects/macroforge/simulation/dry_runs/_SUMMARY.md

Reason included: project-wide governance review folder map

# Folder Summary: simulation/dry_runs

## Purpose
This folder is part of the ProjectForge file-backed operating system for `simulation/dry_runs`.

## Contains
<!-- PROJECTFORGE:BEGIN-CONTAINS -->
- `.gitkeep`
- `README.md`
<!-- PROJECTFORGE:END-CONTAINS -->

## Active Work
- No folder-specific active work recorded.

## Needs Attention
- No folder-specific issues recorded.


## workspace/projects/macroforge/skills/_SUMMARY.md

Reason included: project-wide governance review folder map

# Folder Summary: skills

## Purpose
This folder is part of the ProjectForge file-backed operating system for `skills`.

## Contains
<!-- PROJECTFORGE:BEGIN-CONTAINS -->
- `.gitkeep`
- `clarification-queue.md`
- `command-permissions.md`
- `context-budgeting.md`
- `deferred-specification.md`
- `dry-run-workflow.md`
- `folder-summaries.md`
- `git-workflow.md`
- `logging-workflow.md`
- `metrics-feedback.md`
- `model-routing.md`
- `project-bootstrap.md`
- `state-update.md`
- `structured-questionnaire.md`
<!-- PROJECTFORGE:END-CONTAINS -->

## Active Work
- No folder-specific active work recorded.

## Needs Attention
- No folder-specific issues recorded.


## workspace/projects/macroforge/src/_SUMMARY.md

Reason included: project-wide governance review folder map

# Folder Summary: src

## Purpose
This folder contains Python package source for MacroForge.

## Contains
<!-- PROJECTFORGE:BEGIN-CONTAINS -->
- `macroforge/`
<!-- PROJECTFORGE:END-CONTAINS -->

## Active Work
- `macroforge/wdi.py` implements the first WDI extraction/raw-evidence slice.

## Needs Attention
- No folder-specific issues recorded.


## workspace/projects/macroforge/src/macroforge/_SUMMARY.md

Reason included: project-wide governance review folder map

# Folder Summary: src/macroforge

## Purpose
This folder contains the MacroForge Python package for ingestion, validation, and agent-operable data workflows.

## Contains
<!-- PROJECTFORGE:BEGIN-CONTAINS -->
- `__init__.py`
- `wdi.py`
<!-- PROJECTFORGE:END-CONTAINS -->

## Active Work
- `wdi.py`: stdlib-only World Bank WDI extractor, raw evidence/checksum writer, staging-shape normalizer, and CLI smoke extraction command.

## Needs Attention
- No folder-specific issues recorded.


## workspace/projects/macroforge/state/_SUMMARY.md

Reason included: project-wide governance review folder map

# Folder Summary: state

## Purpose
This folder is part of the ProjectForge file-backed operating system for `state`.

## Contains
<!-- PROJECTFORGE:BEGIN-CONTAINS -->
- `.gitkeep`
- `active_goal.md`
- `architecture.md`
- `known_issues.md`
- `lessons.md`
- `project_state.md`
- `recent_changes.md`
<!-- PROJECTFORGE:END-CONTAINS -->

## Active Work
- No folder-specific active work recorded.

## Needs Attention
- No folder-specific issues recorded.


## workspace/projects/macroforge/tests/_SUMMARY.md

Reason included: project-wide governance review folder map

# Folder Summary: tests

## Purpose
This folder is part of the ProjectForge file-backed operating system for `tests`.

## Contains
<!-- PROJECTFORGE:BEGIN-CONTAINS -->
- `invariants/`
- `test_placeholder.py`
- `test_v0_schema_migration.py`
- `test_wdi_extract.py`
<!-- PROJECTFORGE:END-CONTAINS -->

## Active Work
- `test_v0_schema_migration.py`: verifies v0 schema files, required migration objects, canonical grain constraint, and isolated local PostgreSQL migration application.
- `test_wdi_extract.py`: verifies WDI URL construction, response parsing, staging-shape normalization, and raw/checksum evidence writing.

## Needs Attention
- No folder-specific issues recorded.


## workspace/projects/macroforge/tests/invariants/_SUMMARY.md

Reason included: project-wide governance review folder map

# Folder Summary: tests/invariants

## Purpose
This folder is part of the ProjectForge file-backed operating system for `tests/invariants`.

## Contains
<!-- PROJECTFORGE:BEGIN-CONTAINS -->
- `.gitkeep`
- `README.md`
<!-- PROJECTFORGE:END-CONTAINS -->

## Active Work
- No folder-specific active work recorded.

## Needs Attention
- No folder-specific issues recorded.


## workspace/projects/macroforge/tools/_SUMMARY.md

Reason included: project-wide governance review folder map

# Folder Summary: tools

## Purpose
This folder is part of the ProjectForge file-backed operating system for `tools`.

## Contains
<!-- PROJECTFORGE:BEGIN-CONTAINS -->
- `.gitkeep`
- `analyze_metrics.py`
- `build_context.py`
- `check_coherence.py`
- `create_question.py`
- `detect_hardware.py`
- `dry_run.py`
- `escalate.py`
- `git_autopush.py`
- `install.sh`
- `log_run.py`
- `record_metric.py`
- `register_project.py`
- `review_metrics.py`
- `run.py`
- `select_model.py`
- `telegram_notifier_stub.py`
- `update_context_summaries.py`
- `update_state.py`
- `validate_dry_run.py`
<!-- PROJECTFORGE:END-CONTAINS -->

## Active Work
- No folder-specific active work recorded.

## Needs Attention
- No folder-specific issues recorded.


## workspace/shared_assets/_SUMMARY.md

Reason included: project-wide governance review folder map

# Folder Summary: workspace/shared_assets

## Purpose
This folder is part of the ProjectForge file-backed operating system for `workspace/shared_assets`.

## Contains
<!-- PROJECTFORGE:BEGIN-CONTAINS -->
- Empty or placeholder-only folder.
<!-- PROJECTFORGE:END-CONTAINS -->

## Active Work
- No folder-specific active work recorded.

## Needs Attention
- No folder-specific issues recorded.


## workspace/shared_context/_SUMMARY.md

Reason included: project-wide governance review folder map

# Folder Summary: workspace/shared_context

## Purpose
This folder is part of the ProjectForge file-backed operating system for `workspace/shared_context`.

## Contains
<!-- PROJECTFORGE:BEGIN-CONTAINS -->
- `.gitkeep`
<!-- PROJECTFORGE:END-CONTAINS -->

## Active Work
- No folder-specific active work recorded.

## Needs Attention
- No folder-specific issues recorded.


## workspace/shared_logging/_SUMMARY.md

Reason included: project-wide governance review folder map

# Folder Summary: workspace/shared_logging

## Purpose
This folder is part of the ProjectForge file-backed operating system for `workspace/shared_logging`.

## Contains
<!-- PROJECTFORGE:BEGIN-CONTAINS -->
- `.gitkeep`
<!-- PROJECTFORGE:END-CONTAINS -->

## Active Work
- No folder-specific active work recorded.

## Needs Attention
- No folder-specific issues recorded.


## workspace/shared_models/_SUMMARY.md

Reason included: project-wide governance review folder map

# Folder Summary: workspace/shared_models

## Purpose
This folder is part of the ProjectForge file-backed operating system for `workspace/shared_models`.

## Contains
<!-- PROJECTFORGE:BEGIN-CONTAINS -->
- `.gitkeep`
<!-- PROJECTFORGE:END-CONTAINS -->

## Active Work
- No folder-specific active work recorded.

## Needs Attention
- No folder-specific issues recorded.


## workspace/shared_notifications/_SUMMARY.md

Reason included: project-wide governance review folder map

# Folder Summary: workspace/shared_notifications

## Purpose
This folder is part of the ProjectForge file-backed operating system for `workspace/shared_notifications`.

## Contains
<!-- PROJECTFORGE:BEGIN-CONTAINS -->
- `.gitkeep`
<!-- PROJECTFORGE:END-CONTAINS -->

## Active Work
- No folder-specific active work recorded.

## Needs Attention
- No folder-specific issues recorded.


## workspace/shared_skills/_SUMMARY.md

Reason included: project-wide governance review folder map

# Folder Summary: workspace/shared_skills

## Purpose
This folder is part of the ProjectForge file-backed operating system for `workspace/shared_skills`.

## Contains
<!-- PROJECTFORGE:BEGIN-CONTAINS -->
- `.gitkeep`
<!-- PROJECTFORGE:END-CONTAINS -->

## Active Work
- No folder-specific active work recorded.

## Needs Attention
- No folder-specific issues recorded.


## artifacts/decisions/D-20260530-projectforge-default-philosophy.md

Reason included: decision record matched task keywords

# Decision: ProjectForge Default Philosophy

Date: 2026-05-30
Status: Accepted

## Decision
ProjectForge defaults to an AI-first engineering environment where the human designs the architecture through extensive initial questions, and agents execute inside explicit state, logging, git, and permission boundaries.

## Rationale
This matches the intended use: reusable project initialization for future AI-assisted projects while avoiding uncontrolled autonomous drift.

## Consequences
- All generated projects include state, artifacts, logs, permissions, agents, skills, and templates.
- Durable architectural choices must be recorded in `artifacts/decisions/`.
- Agents may ask clarifying questions later when deferred specifications become relevant.


## artifacts/decisions/D-20260601-projectforge-batch2-generated-ux.md

Reason included: decision record matched task keywords

# Decision: ProjectForge Batch 2 generated-project UX hardening

Date: 2026-06-01
Status: Accepted
Severity: L3

## Context
After the first Hermes-native hardening pass, root ProjectForge and direct generated-project coherence were clean, but a second audit found remaining generated-project UX and dependency pitfalls:

- generated projects' `tools/run.py` wrapper could not run their own coherence check through the safe allowlist;
- template runtime artifacts such as `__pycache__` and `*.pyc` could be copied into generated projects;
- `tools/install.sh` still used `python3 -m pip install --user`, which fails on this PEP 668/no-pip host;
- `_SUMMARY.md` refreshes overwrote curated folder context;
- generated agent prompts over-required `tools/run.py` even when Hermes native tools are available.

## Decision
ProjectForge now treats generated-project UX as part of the factory contract and tests it directly.

Accepted changes:

1. Generated project safe wrapper checks must allow read-only ProjectForge validation, especially `python3 tools/check_coherence.py`.
2. Mutating ProjectForge tools belong in the review allowlist level, not safe.
3. Template rendering must skip runtime/cache artifacts such as `__pycache__`, `*.pyc`, `.pytest_cache`, `.mypy_cache`, `.ruff_cache`, `htmlcov`, `dist`, and `build`.
4. ProjectForge installation guidance is uv/venv-first on this host. Do not recommend system/user pip as the default setup path.
5. Summary refreshes must preserve curated Purpose, Active Work, and Needs Attention sections; only the Contains inventory is generated.
6. Generated agent prompts should say Hermes sessions use Hermes tools directly and reserve `tools/run.py` for manual or explicitly audited wrapper use.

## Consequences
- `tools/run.py` remains a policy/audit wrapper, not a full sandbox.
- Safe allowlist entries must stay semantically low-risk/read-only. Prefix matching remains a known future hardening target.
- Generated project tests should cover all templates, not just the default template.
- Summary curation is now durable across routine context refreshes.

## Verification
The accepted implementation was verified with:

```bash
uvx --from pytest --with pyyaml pytest tests -q
python3 tools/check_coherence.py --project . --json
bash tools/install.sh && .venv/bin/python tools/check_coherence.py --project . --json
python3 -m py_compile tools/*.py templates/_shared_project/tools/*.py
git diff --check
```

An all-template smoke test generated `default_project`, `python_data_project`, `web_project`, and `research_project`, then verified each generated project passed generated coherence and its own safe wrapper coherence command without changing the canonical registry.


## artifacts/decisions/D-20260601-projectforge-hardening.md

Reason included: decision record matched task keywords

# Decision: ProjectForge hardening pass

Date: 2026-06-01
Status: Accepted
Severity: L3

## Context
A full audit found that ProjectForge's root checks passed while generated projects, registry behavior, non-Hermes command wrapping, and verification hygiene still had operational gaps.

## Decision
ProjectForge should enforce a Hermes-native factory contract with separate root and generated-project coherence modes, deterministic/non-mutating verification behavior, clean workspace registry semantics, and explicit sufficiency validation before scaffolding.

## Accepted changes
- `python3` is the supported local interpreter command for ProjectForge operational docs, schedules, and allowlists on this host.
- `tools/new_project.py` derives workspace paths from the active ProjectForge root instead of hardcoding `/home/mkkto/srv/projectforge`.
- Temp or explicit noncanonical outputs do not register in the canonical workspace unless `--register` is passed.
- Must-pause sufficiency items such as `secrets` and `command_policy` block generation unless answered or explicitly overridden with `--allow-deferred-required`.
- Generated projects receive populated state files from setup answers and no longer receive the factory-only `tools/new_project.py`.
- `tools/check_coherence.py` supports root-vs-generated contracts through `--mode root|generated|auto`.
- `tools/update_context_summaries.py` is deterministic and avoids volatile timestamps and ignored dry-run reports.
- `tools/register_project.py` treats PyYAML/schema validity as required and rejects invalid `raw` registry fallback data.
- Project-local bootstrap/questionnaire skills define `setup_questionnaire.yaml` as a coverage map, not a rigid script.

## Consequences
Future Hermes sessions should create projects through adaptive questioning plus noninteractive rendering, verify generated projects with generated coherence mode, and avoid treating root ProjectForge invariants as the generated-project contract.

## Verification
- `uvx --from pytest --with pyyaml pytest tests -q`
- `python3 tools/check_coherence.py --project . --json`
- temp generated-project smoke check with root and project-local coherence


## tools/build_context.py

Reason included: explicitly retrieved source file

#!/usr/bin/env python3
"""Build a strict, summary-first task context bundle.

Normal context is intentionally compact. Raw logs, full conversations, generated
artifacts, unrelated folders, and whole-project dumps are excluded unless the
caller explicitly requests a forensic/failure-investigation context.
"""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any

try:
    import yaml  # type: ignore
except Exception:  # pragma: no cover - optional dependency
    yaml = None

RAW_LOG_PATTERNS = (
    "logs/raw/",
    "logs/agents/",
    "logs/sessions/",
    "logs/runs/",
    "session.jsonl",
    "sessions.jsonl",
    "conversation",
    "transcript",
)
GENERATED_OR_BULK_DIRS = {
    ".git",
    ".pytest_cache",
    ".mypy_cache",
    ".ruff_cache",
    "__pycache__",
    ".venv",
    "node_modules",
    "dist",
    "build",
    "htmlcov",
    "generated",
}
DEFAULT_SUMMARY_CANDIDATES = [
    "context/PROJECT_CONTEXT.md",
    "context/project_summary.md",
    "state/project_state.md",
    "state/active_goal.md",
    "state/architecture.md",
]
DEFAULT_HANDOFF_CANDIDATES = [
    "context/latest_handoff.md",
    "context/handoff.md",
    "state/recent_changes.md",
]
DECISION_DIRS = ["artifacts/decisions"]
TASK_DIRS = ["artifacts/tasks"]


@dataclass
class ContextItem:
    rel: str
    path: Path
    reason: str
    category: str
    max_chars: int


def load_yaml(path: Path) -> dict[str, Any]:
    if not path.exists() or yaml is None:
        return {}
    return yaml.safe_load(path.read_text(encoding="utf-8")) or {}


def policy_for(project: Path) -> dict[str, Any]:
    data = load_yaml(project / "context" / "context_policy.yaml").get("context_policy", {})
    budgets = data.get("budgets", {})
    # Backward compatibility with older flat policy.
    if "default_budget_tokens" in data and not budgets:
        budgets = {
            "local_model_tokens": int(data.get("default_budget_tokens", 24000)),
            "cloud_governance_tokens": min(int(data.get("default_budget_tokens", 24000)), 10000),
        }
    return {
        "local_budget": int(budgets.get("local_model_tokens", 24000)),
        "cloud_budget": int(budgets.get("cloud_governance_tokens", budgets.get("cloud_model_tokens", 10000))),
        "cloud_target": int(budgets.get("cloud_governance_target_tokens", budgets.get("cloud_target_tokens", 8000))),
        "project_wide_budget": int(budgets.get("project_wide_review_tokens", 64000)),
        "project_wide_target": int(budgets.get("project_wide_review_target_tokens", 32000)),
        "per_file_chars": int(data.get("limits", {}).get("explicit_source_file_chars", 20000)),
        "project_wide_per_file_chars": int(data.get("limits", {}).get("project_wide_source_file_chars", data.get("limits", {}).get("explicit_source_file_chars", 20000))),
        "summary_chars": int(data.get("limits", {}).get("summary_file_chars", 4000)),
        "handoff_chars": int(data.get("limits", {}).get("handoff_chars", 3000)),
        "decision_chars": int(data.get("limits", {}).get("decision_record_chars", 6000)),
        "task_chars": int(data.get("limits", {}).get("active_task_chars", 8000)),
        "project_wide_summary_limit": int(data.get("limits", {}).get("project_wide_folder_summary_count", 200)),
    }


def estimate_tokens(text: str) -> int:
    # Conservative enough for budget gates without tokenizer dependencies.
    return max(1, (len(text) + 3) // 4)


def rel_for(project: Path, path: Path) -> str:
    return str(path.resolve().relative_to(project.resolve())).replace("\\", "/")


def is_under(path: Path, project: Path) -> bool:
    try:
        path.resolve().relative_to(project.resolve())
        return True
    except ValueError:
        return False


def is_raw_log_rel(rel: str) -> bool:
    rel_l = rel.lower()
    return any(pattern in rel_l for pattern in RAW_LOG_PATTERNS) or rel_l.startswith("logs/raw")


def excluded_reason(project: Path, path: Path, allow_raw_logs: bool, task_type: str) -> str | None:
    if not is_under(path, project):
        return "outside project root"
    rel = rel_for(project, path)
    parts = set(Path(rel).parts)
    if parts & GENERATED_OR_BULK_DIRS:
        return "generated/cache/bulk directory excluded"
    if path.name.endswith((".pyc", ".pyo", ".pyd")):
        return "compiled artifact excluded"
    raw_allowed = allow_raw_logs or task_type in {"failure_investigation", "forensic", "incident"}
    if is_raw_log_rel(rel) and not raw_allowed:
        return "raw logs/session transcripts excluded from normal context"
    if rel.startswith("logs/") and path.name != "_SUMMARY.md" and not raw_allowed:
        return "log files excluded from normal context; use summaries or failure_investigation"
    if rel.startswith("data/raw/") and not raw_allowed:
        return "raw data excluded unless explicitly relevant"
    return None


def read_limited(path: Path, max_chars: int) -> tuple[str, bool]:
    txt = path.read_text(encoding="utf-8", errors="replace")
    truncated = len(txt) > max_chars
    if truncated:
        txt = txt[:max_chars] + "\n\n[TRUNCATED BY CONTEXT POLICY]\n"
    return txt, truncated


def add_if_exists(items: list[ContextItem], project: Path, rel: str, reason: str, category: str, max_chars: int) -> None:
    path = project / rel
    if path.exists() and path.is_file():
        items.append(ContextItem(rel.replace("\\", "/"), path, reason, category, max_chars))


def split_csv(value: str) -> list[str]:
    return [x.strip() for x in value.split(",") if x.strip()]


def relevant_folder_summaries(project: Path, folders: list[str], files: list[str], task: str, context_mode: str = "normal", max_project_wide: int = 200) -> list[tuple[str, str]]:
    candidates: dict[str, str] = {}
    if context_mode == "project_wide_review":
        for summary in sorted(project.glob("**/_SUMMARY.md"))[:max_project_wide]:
            candidates[rel_for(project, summary)] = "project-wide governance review folder map"
    for folder in folders:
        rel = folder.strip("/")
        if rel:
            candidates[f"{rel}/_SUMMARY.md"] = "explicitly requested relevant folder summary"
    for file_rel in files:
        parent = str(Path(file_rel).parent).replace("\\", "/")
        while parent and parent != ".":
            candidates[f"{parent}/_SUMMARY.md"] = "summary for explicitly retrieved source file parent"
            parent = str(Path(parent).parent).replace("\\", "/")
            if parent == ".":
                break
    lowered = task.lower()
    for d in sorted(project.glob("*/_SUMMARY.md")):
        folder = d.parent.name.lower()
        if folder in lowered:
            candidates[rel_for(project, d)] = "folder summary matched task keywords"
    return sorted(candidates.items())


def relevant_decisions(project: Path, decisions: list[str], task: str, max_auto: int = 6) -> list[tuple[str, str]]:
    found: dict[str, str] = {}
    for rel in decisions:
        found[rel] = "explicitly requested decision record"
    terms = {t.strip(".,:;()[]{}!?`").lower() for t in task.split() if len(t.strip(".,:;()[]{}!?`")) >= 5}
    for ddir in DECISION_DIRS:
        base = project / ddir
        if not base.exists():
            continue
        scored: list[tuple[int, Path]] = []
        for path in base.glob("*.md"):
            name = path.name.lower()
            score = sum(1 for term in terms if term in name)
            if score:
                scored.append((score, path))
        for _, path in sorted(scored, reverse=True)[:max_auto]:
            found[rel_for(project, path)] = "decision record matched task keywords"
    return sorted(found.items())


def write_markdown_audit(audit_path: Path, audit: dict[str, Any]) -> None:
    lines = [
        "# Context Audit Report",
        "",
        f"Task: {audit['task']}",
        f"Task type: {audit['task_type']}",
        f"Context mode: {audit['context_mode']}",
        f"Review justification: {audit['review_justification'] or 'not required'}",
        f"Model target: {audit['model_target']}",
        f"Model selected: {audit['model_selected']}",
        f"Model reason: {audit['model_reason']}",
        f"Estimated tokens: {audit['estimated_tokens']}",
        f"Budget tokens: {audit['budget_tokens']}",
        f"Within budget: {audit['within_budget']}",
        f"Raw logs excluded: {audit['raw_logs_excluded']}",
        f"Summaries used: {audit['summaries_used']}",
        "",
        "## Included files",
    ]
    for item in audit["included_files"]:
        lines.append(f"- `{item['path']}` ({item['tokens']} tokens): {item['reason']}")
    lines.extend(["", "## Excluded files"])
    for item in audit["excluded_files"]:
        lines.append(f"- `{item['path']}`: {item['reason']}")
    audit_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    ap = argparse.ArgumentParser(description="Build ProjectForge strict summary-first context")
    ap.add_argument("--project", default=".")
    ap.add_argument("--task", default="general")
    ap.add_argument("--task-type", default="normal", choices=["normal", "implementation", "architecture_decision", "project_audit", "strategic_planning", "gap_analysis", "redesign", "failure_investigation", "forensic", "incident"])
    ap.add_argument("--context-mode", default="normal", choices=["normal", "governance", "project_wide_review"], help="normal is compact; governance is cloud reasoning over selected context; project_wide_review allows larger justified audit context")
    ap.add_argument("--review-justification", default="", help="Required for project_wide_review; explains why broader cloud context is worth the tokens")
    ap.add_argument("--task-file", default="", help="Active task artifact to include")
    ap.add_argument("--files", default="", help="Comma-separated explicit source files to include")
    ap.add_argument("--folders", default="", help="Comma-separated relevant folders whose _SUMMARY.md files should be included")
    ap.add_argument("--decisions", default="", help="Comma-separated decision records to include")
    ap.add_argument("--model-target", choices=["local", "cloud"], default="local")
    ap.add_argument("--model-selected", default="local_first")
    ap.add_argument("--model-reason", default="summary-first local context build")
    ap.add_argument("--allow-raw-logs", action="store_true", help="Only for failure/forensic investigations")
    ap.add_argument("--refresh-summaries", action="store_true")
    ap.add_argument("--dry-run", action="store_true")
    ns = ap.parse_args()

    project = Path(ns.project).resolve()
    if ns.refresh_summaries:
        updater = Path(__file__).with_name("update_context_summaries.py")
        if updater.exists():
            subprocess.run([sys.executable, str(updater), "--project", str(project), "--core-only"], check=False)

    policy = policy_for(project)
    if ns.context_mode == "project_wide_review":
        budget = policy["project_wide_budget"]
    else:
        budget = policy["cloud_budget"] if ns.model_target == "cloud" else policy["local_budget"]
    explicit_files = split_csv(ns.files)
    folders = split_csv(ns.folders)
    explicit_decisions = split_csv(ns.decisions)

    items: list[ContextItem] = []
    excluded: list[dict[str, str]] = []

    for rel in DEFAULT_SUMMARY_CANDIDATES:
        add_if_exists(items, project, rel, "project summary/current state", "project_summary", policy["summary_chars"])
    for rel in DEFAULT_HANDOFF_CANDIDATES:
        add_if_exists(items, project, rel, "short recent handoff summary", "handoff", policy["handoff_chars"])
    if ns.task_file:
        add_if_exists(items, project, ns.task_file, "active task file", "active_task", policy["task_chars"])
    for rel, reason in relevant_folder_summaries(project, folders, explicit_files, ns.task, ns.context_mode, policy["project_wide_summary_limit"]):
       

[TRUNCATED BY CONTEXT POLICY]


## tools/select_model.py

Reason included: explicitly retrieved source file

#!/usr/bin/env python3
"""Select a model from ProjectForge local-first routing policy.

The selector is advisory for Hermes/external agents. It enforces ProjectForge's
rule that cloud/Codex choices need an explicit escalation reason and a recent
context audit that fits the configured cloud budget.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

try:
    import yaml  # type: ignore
except Exception:
    yaml = None

LOCAL_PROVIDERS = {"local", "ollama", "hermes"}
CLOUD_PROVIDERS = {"openai", "anthropic", "google", "openrouter", "external"}
ROUTINE_LOCAL_TASKS = {
    "summarization",
    "folder_summary_update",
    "log_compression",
    "code_search",
    "simple_code_edit",
    "routine_implementation",
    "scaffold_rendering",
    "tests",
}
CLOUD_ESCALATION_REASONS = {
    "architecture_decision",
    "project_audit",
    "strategic_planning",
    "gap_analysis",
    "redesign",
    "consistency_review",
    "local_failed_twice",
    "high_ambiguity",
    "explicit_user_request",
    "safety_critical_destructive_operation",
    "repeated_failure_debugging",
    "security_or_secret_handling",
}


def load_yaml(path: Path) -> dict[str, Any]:
    if yaml is None:
        raise RuntimeError("PyYAML required. Use `uvx --with pyyaml python tools/select_model.py ...` for one-shot execution, or run `uv venv && uv pip install pyyaml`.")
    return yaml.safe_load(path.read_text(encoding="utf-8")) or {}


def model_dirs(project: Path) -> Path:
    if (project / "models").exists():
        return project / "models"
    return Path(__file__).resolve().parents[1] / "models"


def provider_of(registry: dict[str, Any], model: str) -> str:
    return str(registry.get(model, {}).get("provider", "")).lower()


def is_cloud(registry: dict[str, Any], model: str) -> bool:
    provider = provider_of(registry, model)
    return provider in CLOUD_PROVIDERS or model.startswith(("codex", "gpt", "claude"))


def is_local(registry: dict[str, Any], model: str) -> bool:
    return not is_cloud(registry, model) and (provider_of(registry, model) in LOCAL_PROVIDERS or bool(registry.get(model)))


def context_policy(project: Path) -> dict[str, int]:
    data = load_yaml(project / "context" / "context_policy.yaml").get("context_policy", {}) if (project / "context" / "context_policy.yaml").exists() else {}
    budgets = data.get("budgets", {})
    return {
        "cloud_budget": int(budgets.get("cloud_governance_tokens", budgets.get("cloud_model_tokens", min(int(data.get("default_budget_tokens", 24000)), 10000)))),
        "project_wide_budget": int(budgets.get("project_wide_review_tokens", 64000)),
        "local_budget": int(budgets.get("local_model_tokens", int(data.get("default_budget_tokens", 24000)))),
    }


def validate_cloud_audit(project: Path, audit_arg: str, cloud_budget: int, project_wide_budget: int) -> tuple[bool, str]:
    if not audit_arg:
        return False, "cloud model requires context audit report via --context-audit pointing to context/context_audit.json"
    path = Path(audit_arg)
    if not path.is_absolute():
        path = project / audit_arg
    if not path.exists():
        return False, f"context audit not found: {path}"
    audit = json.loads(path.read_text(encoding="utf-8"))
    if not audit.get("raw_logs_excluded", False):
        return False, "context audit does not confirm raw logs were excluded"
    if not audit.get("summaries_used", False):
        return False, "context audit does not confirm summaries were used"
    tokens = int(audit.get("estimated_tokens", 0))
    budget = int(audit.get("budget_tokens", cloud_budget))
    context_mode = str(audit.get("context_mode", "normal"))
    review_justification = str(audit.get("review_justification", "")).strip()
    if context_mode == "project_wide_review":
        if not review_justification:
            return False, "project-wide cloud review requires an audit review_justification"
        effective_budget = min(budget, project_wide_budget)
    else:
        effective_budget = min(budget, cloud_budget)
    if tokens > effective_budget:
        return False, f"audited context has {tokens} tokens, above {context_mode} budget {effective_budget}"
    return True, f"context audit passed ({tokens}/{effective_budget} tokens, mode={context_mode})"


def main() -> int:
    p = argparse.ArgumentParser(description="Select a model from ProjectForge local-first routing policy.")
    p.add_argument("--project", default=".")
    p.add_argument("--agent", required=True)
    p.add_argument("--task", default="")
    p.add_argument("--failure-count", type=int, default=0)
    p.add_argument("--ambiguity", choices=["low", "medium", "high"], default="low")
    p.add_argument("--escalation-reason", default="", help="Required for cloud/Codex selection")
    p.add_argument("--explicit-cloud", action="store_true")
    p.add_argument("--architecture-decision", action="store_true")
    p.add_argument("--governance", action="store_true", help="Cloud governance task: audit, strategy, gap analysis, consistency review, redesign")
    p.add_argument("--destructive-safety", action="store_true")
    p.add_argument("--context-audit", default="")
    p.add_argument("--json", action="store_true")
    ns = p.parse_args()

    project = Path(ns.project).resolve()
    models_dir = model_dirs(project)
    registry = load_yaml(models_dir / "registry.yaml").get("models", {})
    routing = load_yaml(models_dir / "routing.yaml").get("routing", {})
    budgets = context_policy(project)

    task_route = routing.get("by_task", {}).get(ns.task, {}) if ns.task else {}
    agent_route = routing.get("by_agent", {}).get(ns.agent, {})
    candidates = list(task_route.get("preferred") or agent_route.get("preferred") or registry.keys())

    reasons: list[str] = []
    if ns.architecture_decision or ns.task == "architecture_decision":
        reasons.append("architecture_decision")
    if ns.governance or ns.task in {"project_audit", "strategic_planning", "gap_analysis", "redesign", "consistency_review"}:
        reasons.append(ns.task if ns.task else "project_audit")
    if ns.failure_count >= 2:
        reasons.append("local_failed_twice")
    if ns.ambiguity == "high":
        reasons.append("high_ambiguity")
    if ns.explicit_cloud:
        reasons.append("explicit_user_request")
    if ns.destructive_safety:
        reasons.append("safety_critical_destructive_operation")
    if ns.escalation_reason:
        reasons.append(ns.escalation_reason)
    if ns.task in {"repeated_failure_debugging", "security_or_secret_handling"}:
        reasons.append(ns.task)

    cloud_allowed = any(reason in CLOUD_ESCALATION_REASONS for reason in reasons)

    if ns.task in ROUTINE_LOCAL_TASKS:
        local_candidates = [c for c in candidates if c in registry and is_local(registry, c)]
        choice = local_candidates[0] if local_candidates else next((c for c in candidates if c in registry), candidates[0] if candidates else "unknown")
        why = f"routine task `{ns.task}` uses local-first policy"
    elif cloud_allowed:
        threshold = agent_route.get("escalation_after_failures")
        if threshold is not None and ns.failure_count < int(threshold) and not (ns.explicit_cloud or ns.architecture_decision or ns.governance or ns.ambiguity == "high" or ns.destructive_safety):
            local_candidates = [c for c in candidates if c in registry and is_local(registry, c)]
            choice = local_candidates[0] if local_candidates else next((c for c in candidates if c in registry), candidates[0] if candidates else "unknown")
            why = f"below failure threshold {threshold}; stayed local"
        else:
            cloud_candidates = [c for c in candidates if c in registry and is_cloud(registry, c)]
            choice = cloud_candidates[0] if cloud_candidates else ("codex_supervisor" if "codex_supervisor" in registry else next((c for c in candidates if c in registry), candidates[0] if candidates else "unknown"))
            why = "cloud escalation permitted: " + ", ".join(sorted(set(reasons)))
    else:
        local_candidates = [c for c in candidates if c in registry and is_local(registry, c)]
        choice = local_candidates[0] if local_candidates else next((c for c in candidates if c in registry), candidates[0] if candidates else "unknown")
        why = "no cloud escalation condition met; selected local/smallest sufficient candidate"

    audit_status = "not_required"
    audit_ok = True
    if choice in registry and is_cloud(registry, choice):
        audit_ok, audit_status = validate_cloud_audit(project, ns.context_audit, budgets["cloud_budget"], budgets["project_wide_budget"])
        if not audit_ok:
            result = {"model": choice, "allowed": False, "reason": why, "audit_status": audit_status, "cloud_budget_tokens": budgets["cloud_budget"], "project_wide_budget_tokens": budgets["project_wide_budget"]}
            if ns.json:
                print(json.dumps(result, indent=2))
            else:
                print(f"ERROR: {audit_status}")
            return 2

    result = {"model": choice, "allowed": True, "reason": why, "audit_status": audit_status, "cloud_budget_tokens": budgets["cloud_budget"], "project_wide_budget_tokens": budgets["project_wide_budget"]}
    if ns.json:
        print(json.dumps(result, indent=2))
    else:
        print(choice)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())


## context/context_policy.yaml

Reason included: explicitly retrieved source file

context_policy:
  mode: local_execution_cloud_governance

  budgets:
    local_model_tokens: 24000
    cloud_governance_tokens: 10000
    cloud_governance_target_tokens: 8000
    project_wide_review_tokens: 64000
    project_wide_review_target_tokens: 32000

  budget_intent:
    local_model_tokens: routine local execution and implementation context
    cloud_governance_tokens: default compact cloud reasoning bundle for high-leverage decisions
    project_wide_review_tokens: justified cloud governance mode for audits, redesigns, strategic reviews, and gap analysis

  context_modes:
    normal:
      purpose: local execution or narrow task work
      default_model_target: local
      includes: [project_summary, active_task_file, relevant_folder_summaries, relevant_decision_records, explicitly_retrieved_source_files, short_recent_handoff_summary]
    governance:
      purpose: compact cloud architecture/strategy reasoning over selected evidence
      default_model_target: cloud
      requires_context_audit: true
      budget: cloud_governance_tokens
    project_wide_review:
      purpose: larger cloud governance review for architecture audit, redesign, strategic planning, gap analysis, and consistency review
      default_model_target: cloud
      requires_context_audit: true
      requires_review_justification: true
      budget: project_wide_review_tokens
      starts_with_all_folder_summaries: true
      still_excludes_raw_logs_by_default: true

  normal_context_may_include:
    - project_summary
    - active_task_file
    - relevant_folder_summaries
    - relevant_decision_records
    - explicitly_retrieved_source_files
    - short_recent_handoff_summary

  normal_context_must_not_include:
    - raw_logs
    - entire_previous_conversations
    - full_session_jsonl_files
    - whole_project_file_dumps
    - unrelated_folders
    - large_tool_outputs
    - generated_artifacts_unless_explicitly_relevant

  retrieval_order:
    - read_project_summary
    - identify_relevant_folders
    - read_relevant_folder_summaries
    - read_relevant_decision_records
    - retrieve_only_relevant_files
    - expand_context_incrementally_if_audit_or_reasoning_need_justifies_it
    - read_raw_logs_only_for_failure_investigation_or_summary_gap

  folder_summaries:
    enabled: true
    filename: _SUMMARY.md
    maintained_by: context_manager
    use_before_deep_file_reads: true

  limits:
    summary_file_chars: 4000
    handoff_chars: 3000
    active_task_chars: 8000
    decision_record_chars: 6000
    explicit_source_file_chars: 20000
    project_wide_source_file_chars: 12000
    project_wide_folder_summary_count: 200

  raw_logs:
    stored_for: audit_debugging_only
    include_in_normal_context: false
    allowed_contexts:
      - failure_investigation
      - forensic
      - incident
    rule: Raw logs are never included in normal context bundles. Governance reviews use summaries and decision history first.

  cloud_audit:
    required_before_cloud_model: true
    report_paths:
      json: context/context_audit.json
      markdown: context/context_audit.md
    required_fields:
      - total_estimated_tokens
      - context_mode
      - review_justification_when_project_wide
      - included_files_with_reasons
      - excluded_files_with_reasons
      - raw_logs_excluded
      - summaries_used
      - model_selected_and_reason

  compression:
    summarize_large_files: true
    large_file_line_threshold: 250
    prefer_summaries_for_non_target_folders: true
    summaries_and_log_compression_use_local_model: true


## models/routing.yaml

Reason included: explicitly retrieved source file

routing:
  default_policy: local_execution_cloud_governance

  context_requirements:
    cloud_governance_budget_tokens: 10000
    cloud_governance_target_tokens: 8000
    project_wide_review_budget_tokens: 64000
    project_wide_review_target_tokens: 32000
    cloud_requires_context_audit: true
    project_wide_review_requires_justification: true
    raw_logs_forbidden_in_normal_context: true
    summary_first_retrieval: true

  by_agent:
    brain_orchestrator:
      preferred: [hermes_default, deepseek_r1_14b, qwen3_14b]
      escalation_after_failures: 2
    planner:
      preferred: [hermes_default, deepseek_r1_14b, qwen3_14b, codex_supervisor]
      escalation_after_failures: 2
    coder:
      preferred: [qwen_coder, deepseek_coder_v2, hermes_default]
      escalation_after_failures: 2
    reviewer:
      preferred: [hermes_default, deepseek_r1_14b, qwen3_14b, codex_supervisor]
      escalation_after_failures: 2
    auditor:
      preferred: [hermes_default, qwen3_14b, deepseek_r1_14b, codex_supervisor]
      escalation_after_failures: 2
    summarizer:
      preferred: [small_summarizer, qwen3_4b, llama32_3b, hermes_default]
      escalation_after_failures: 4
    context_manager:
      preferred: [small_summarizer, qwen3_4b, llama32_3b, hermes_default]
      escalation_after_failures: 4
    bootstrapper:
      preferred: [hermes_default, deepseek_r1_14b, codex_supervisor]
      escalation_after_failures: 2
    metrics_reviewer:
      preferred: [qwen3_14b, deepseek_r1_14b, hermes_default]
      escalation_after_failures: 3
    dry_run_validator:
      preferred: [hermes_default, qwen3_14b]
      escalation_after_failures: 3

  by_task:
    project_creation_interview:
      preferred: [hermes_default, deepseek_r1_14b, codex_supervisor]
    scaffold_rendering:
      preferred: [hermes_default]
    summarization:
      preferred: [small_summarizer, qwen3_4b, llama32_3b, hermes_default]
    log_compression:
      preferred: [small_summarizer, qwen3_4b, llama32_3b, hermes_default]
    folder_summary_update:
      preferred: [small_summarizer, qwen3_4b, llama32_3b, hermes_default]
    documentation_update:
      preferred: [small_summarizer, qwen3_4b, hermes_default]
    code_search:
      preferred: [hermes_default, qwen3_4b]
    simple_code_edit:
      preferred: [qwen_coder, deepseek_coder_v2, hermes_default]
    routine_implementation:
      preferred: [qwen_coder, deepseek_coder_v2, hermes_default]
    refactoring:
      preferred: [qwen_coder, deepseek_coder_v2, hermes_default]
    debugging:
      preferred: [qwen_coder, deepseek_coder_v2, hermes_default, deepseek_r1_14b]
    tests:
      preferred: [hermes_default]
    architecture_decision:
      preferred: [hermes_default, deepseek_r1_14b, qwen3_14b, codex_supervisor]
    project_audit:
      preferred: [hermes_default, qwen3_14b, deepseek_r1_14b, codex_supervisor]
    strategic_planning:
      preferred: [hermes_default, deepseek_r1_14b, qwen3_14b, codex_supervisor]
    gap_analysis:
      preferred: [hermes_default, qwen3_14b, deepseek_r1_14b, codex_supervisor]
    redesign:
      preferred: [hermes_default, deepseek_r1_14b, qwen3_14b, codex_supervisor]
    consistency_review:
      preferred: [hermes_default, qwen3_14b, deepseek_r1_14b, codex_supervisor]
    repeated_failure_debugging:
      preferred: [hermes_default, deepseek_r1_14b, qwen3_14b, codex_supervisor]
    security_or_secret_handling:
      preferred: [hermes_default, codex_supervisor]

  local_execution_tasks:
    - summarization
    - log_compression
    - folder_summary_update
    - documentation_update
    - code_search
    - simple_code_edit
    - routine_implementation
    - refactoring
    - debugging
    - tests

  cloud_governance_tasks:
    - architecture_decision
    - project_audit
    - strategic_planning
    - gap_analysis
    - redesign
    - consistency_review

  cloud_escalation_only_if:
    - architecture_decision
    - project_audit
    - strategic_planning
    - gap_analysis
    - redesign
    - consistency_review
    - local_failed_twice
    - high_ambiguity
    - explicit_user_request
    - safety_critical_destructive_operation

  escalation:
    capability_failure_chain:
      - current_hermes_session
      - stronger_local_model_if_configured
      - codex_or_premium_model_after_context_audit
      - human_if_still_blocked
    human_first_for:
      - permission_required
      - credential_handling
      - destructive_command
      - git_push
      - money_or_billing_risk
      - production_data_change
      - unresolved_specification


## models/selection_policy.yaml

Reason included: explicitly retrieved source file

selection_policy:
  principle: local_execution_cloud_governance
  prefer_local_for_execution: true
  prefer_cloud_for_high_value_governance: true
  avoid_largest_by_default: true

  context_budgets:
    local_model_tokens: 24000
    cloud_governance_tokens: 10000
    cloud_governance_target_tokens: 8000
    project_wide_review_tokens: 64000
    project_wide_review_target_tokens: 32000
    cloud_requires_context_audit: true
    project_wide_review_requires_justification: true

  local_execution_tasks:
    summaries: small_summarizer
    log_compression: small_summarizer
    code_search: local_tools_or_local_model
    routine_implementation: local_coding_model_if_available
    refactoring: local_coding_model_if_available
    debugging: local_coding_or_reasoning_model_first
    tests: local_tools
    documentation_update: local_model_first

  cloud_governance_tasks:
    architecture_review: compact_or_project_wide_cloud_audit
    strategic_planning: compact_or_project_wide_cloud_audit
    project_audit: compact_or_project_wide_cloud_audit
    gap_analysis: compact_or_project_wide_cloud_audit
    redesign: compact_or_project_wide_cloud_audit
    consistency_review: compact_or_project_wide_cloud_audit

  cloud_escalation_only_if:
    - architecture_decision_needed
    - project_audit_or_gap_analysis_needed
    - strategic_planning_or_redesign_needed
    - consistency_review_needed
    - local_model_fails_twice
    - ambiguity_level_high
    - user_explicitly_requests_cloud_model
    - safety_critical_destructive_operation_requires_higher_reasoning

  escalation:
    capability_failure_chain:
      - current_model
      - stronger_local_model
      - openai_codex_or_premium_model_after_audit
      - human
    human_first_for:
      - permission_required
      - credential_handling
      - destructive_command
      - git_push
      - money_or_billing_risk
      - production_data_change
      - unresolved_specification

  task_size_policy:
    summarization: small_summarizer
    folder_summary_update: small_summarizer
    log_compression: small_summarizer
    routine_coding: coder_default
    debugging: coder_or_reviewer
    architecture_review: planner_or_premium_after_audit
    project_wide_review: premium_after_justified_context_audit
    repeated_failure: escalate_after_local_failures_and_context_audit


## tests/test_context_governance_mode.py

Reason included: explicitly retrieved source file

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

from test_context_policy_strict import ROOT, make_project


def run(*args, cwd=ROOT):
    return subprocess.run([sys.executable, *map(str, args)], cwd=cwd, capture_output=True, text=True)


def test_project_wide_review_requires_justification(tmp_path):
    project = make_project(tmp_path)
    result = run(
        ROOT / "tools" / "build_context.py",
        "--project", project,
        "--task", "project-wide gap analysis",
        "--task-type", "gap_analysis",
        "--context-mode", "project_wide_review",
        "--model-target", "cloud",
        "--model-selected", "codex_supervisor",
        "--model-reason", "gap_analysis",
    )
    assert result.returncode == 2
    assert "review-justification" in result.stderr


def test_project_wide_review_includes_broader_summaries_without_raw_logs(tmp_path):
    project = make_project(tmp_path)
    result = run(
        ROOT / "tools" / "build_context.py",
        "--project", project,
        "--task", "project-wide gap analysis",
        "--task-type", "gap_analysis",
        "--context-mode", "project_wide_review",
        "--review-justification", "Quarterly architecture/gap review needs a folder-level map across the project.",
        "--model-target", "cloud",
        "--model-selected", "codex_supervisor",
        "--model-reason", "gap_analysis",
    )
    assert result.returncode == 0, result.stderr
    audit = json.loads((project / "context" / "context_audit.json").read_text(encoding="utf-8"))
    included = {item["path"] for item in audit["included_files"]}
    assert audit["context_mode"] == "project_wide_review"
    assert audit["review_justification"]
    assert "src/_SUMMARY.md" in included
    assert "tests/_SUMMARY.md" in included
    assert "docs/_SUMMARY.md" in included
    assert audit["raw_logs_excluded"] is True
    assert all(not item["path"].startswith("logs/raw/") for item in audit["included_files"])


def test_cloud_governance_selection_accepts_project_wide_audit(tmp_path):
    project = make_project(tmp_path)
    build = run(
        ROOT / "tools" / "build_context.py",
        "--project", project,
        "--task", "project-wide strategic planning",
        "--task-type", "strategic_planning",
        "--context-mode", "project_wide_review",
        "--review-justification", "Strategic planning needs cross-project folder summaries and current state.",
        "--model-target", "cloud",
        "--model-selected", "codex_supervisor",
        "--model-reason", "strategic_planning",
    )
    assert build.returncode == 0, build.stderr
    selected = run(
        ROOT / "tools" / "select_model.py",
        "--project", project,
        "--agent", "planner",
        "--task", "strategic_planning",
        "--governance",
        "--context-audit", "context/context_audit.json",
        "--json",
    )
    assert selected.returncode == 0, selected.stdout + selected.stderr
    data = json.loads(selected.stdout)
    assert data["allowed"] is True
    assert data["audit_status"].endswith("mode=project_wide_review)")


def test_routine_implementation_stays_local_even_with_cloud_flag_absent(tmp_path):
    project = make_project(tmp_path)
    result = run(ROOT / "tools" / "select_model.py", "--project", project, "--agent", "coder", "--task", "routine_implementation", "--json")
    assert result.returncode == 0, result.stderr
    data = json.loads(result.stdout)
    assert data["allowed"] is True
    assert data["model"] != "codex_supervisor"
    assert data["audit_status"] == "not_required"

