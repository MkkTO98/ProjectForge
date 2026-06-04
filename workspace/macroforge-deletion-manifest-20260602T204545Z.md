# MacroForge deletion manifest

- Exported UTC: 2026-06-02T20:45:45.183413+00:00
- Deleted project path intended: /home/mkkto/srv/projectforge/workspace/projects/macroforge
- Purpose: compact pre-deletion record before rebuilding MacroForge with updated ProjectForge.

## Git status
```text
M artifacts/decisions/_SUMMARY.md
 M artifacts/reports/_SUMMARY.md
 M artifacts/tasks/_SUMMARY.md
 M data/metadata/_SUMMARY.md
 M db/migrations/_SUMMARY.md
 M db/queries/_SUMMARY.md
 M db/schema/_SUMMARY.md
 M src/_SUMMARY.md
 M src/macroforge/_SUMMARY.md
 M state/active_goal.md
 M state/project_state.md
 M tests/_SUMMARY.md
?? artifacts/decisions/DEC-004-v0-postgresql-schema-foundation.md
?? artifacts/reports/wdi_extract_smoke_20260602_task004.json
?? artifacts/reports/wdi_extract_smoke_20260602_task004_hardened.json
?? artifacts/tasks/TASK-003-v0-postgresql-schema-foundation.md
?? artifacts/tasks/TASK-004-narrow-wdi-extract-raw-evidence.md
?? db/migrations/001_v0_schema.sql
?? db/queries/verify_v0_schema.sql
?? db/schema/v0_schema.md
?? simulation/dry_runs/20260602_120708-dry-run.md
?? simulation/dry_runs/20260602_121839-dry-run.md
?? src/macroforge/wdi.py
?? tests/test_v0_schema_migration.py
?? tests/test_wdi_extract.py
```

## Git HEAD
```text
890d1ee
```

## Durable file inventory
```text
.gitignore	1299 bytes
.gitkeep	0 bytes
AGENTS.md	3141 bytes
CONSTITUTION.md	1639 bytes
README.md	2052 bytes
_SUMMARY.md	845 bytes
agents/.gitkeep	0 bytes
agents/_SUMMARY.md	493 bytes
agents/auditor.md	970 bytes
agents/bootstrapper.md	1044 bytes
agents/coder.md	1394 bytes
agents/context_manager.md	660 bytes
agents/model_router.md	806 bytes
agents/planner.md	1040 bytes
agents/researcher.md	987 bytes
agents/reviewer.md	1395 bytes
agents/summarizer.md	546 bytes
artifacts/_SUMMARY.md	381 bytes
artifacts/decisions/.gitkeep	0 bytes
artifacts/decisions/D-20260602-setup-autonomy.md	763 bytes
artifacts/decisions/D-20260602-setup-available_models.md	601 bytes
artifacts/decisions/D-20260602-setup-branch_strategy.md	574 bytes
artifacts/decisions/D-20260602-setup-clarification_channel.md	596 bytes
artifacts/decisions/D-20260602-setup-command_policy.md	711 bytes
artifacts/decisions/D-20260602-setup-deployment.md	583 bytes
artifacts/decisions/D-20260602-setup-documentation_standard.md	603 bytes
artifacts/decisions/D-20260602-setup-external_services.md	658 bytes
artifacts/decisions/D-20260602-setup-folder_summaries.md	492 bytes
artifacts/decisions/D-20260602-setup-git_remote.md	542 bytes
artifacts/decisions/D-20260602-setup-language.md	564 bytes
artifacts/decisions/D-20260602-setup-logging.md	715 bytes
artifacts/decisions/D-20260602-setup-model_policy.md	658 bytes
artifacts/decisions/D-20260602-setup-non_goals.md	847 bytes
artifacts/decisions/D-20260602-setup-premium_escalation.md	596 bytes
artifacts/decisions/D-20260602-setup-project_type.md	548 bytes
artifacts/decisions/D-20260602-setup-purpose.md	843 bytes
artifacts/decisions/D-20260602-setup-secrets.md	727 bytes
artifacts/decisions/D-20260602-setup-specialized_agents.md	679 bytes
artifacts/decisions/D-20260602-setup-storage.md	670 bytes
artifacts/decisions/D-20260602-setup-success.md	797 bytes
artifacts/decisions/D-20260602-setup-testing.md	610 bytes
artifacts/decisions/D-20260602-setup-unanswered_blocking_policy.md	643 bytes
artifacts/decisions/D-20260602-setup-users.md	598 bytes
artifacts/decisions/D-SETUP-project-initialization.md	238 bytes
artifacts/decisions/DEC-001-project-scope-and-v1-slice.md	1698 bytes
artifacts/decisions/DEC-002-local-agent-operating-model.md	1845 bytes
artifacts/decisions/DEC-003-canonical-projectforge-workspace-location.md	1707 bytes
artifacts/decisions/DEC-004-v0-postgresql-schema-foundation.md	2884 bytes
artifacts/decisions/_SUMMARY.md	1569 bytes
artifacts/handoffs/.gitkeep	0 bytes
artifacts/handoffs/_SUMMARY.md	359 bytes
artifacts/reports/.gitkeep	0 bytes
artifacts/reports/_SUMMARY.md	726 bytes
artifacts/reports/wdi_extract_smoke_20260602_task004.json	5537 bytes
artifacts/reports/wdi_extract_smoke_20260602_task004_hardened.json	5600 bytes
artifacts/tasks/.gitkeep	0 bytes
artifacts/tasks/TASK-001-initial-validation.md	737 bytes
artifacts/tasks/TASK-002-v0-schema-wdi-ingestion.md	1806 bytes
artifacts/tasks/TASK-003-v0-postgresql-schema-foundation.md	3177 bytes
artifacts/tasks/TASK-004-narrow-wdi-extract-raw-evidence.md	3704 bytes
artifacts/tasks/_SUMMARY.md	659 bytes
confidence/.gitkeep	0 bytes
confidence/_SUMMARY.md	397 bytes
confidence/confidence_policy.yaml	568 bytes
confidence/confidence_template.md	226 bytes
config/_SUMMARY.md	379 bytes
config/setup_questionnaire.yaml	5184 bytes
config/sufficiency_policy.yaml	931 bytes
context/.gitkeep	0 bytes
context/PROJECT_CONTEXT.md	3304 bytes
context/_SUMMARY.md	497 bytes
context/active_context.md	25044 bytes
context/compressed_context.md	79 bytes
context/context_manifest.json	1110 bytes
context/context_manifest.yaml	408 bytes
context/context_policy.yaml	655 bytes
context/imports/_SUMMARY.md	369 bytes
context/imports/chatgpt_export_recovery/conversation_index.md	2333 bytes
context/imports/chatgpt_export_recovery/recovery_summary.md	8607 bytes
data/.gitkeep	0 bytes
data/_SUMMARY.md	380 bytes
data/curated/.gitkeep	0 bytes
data/curated/_SUMMARY.md	347 bytes
data/metadata/.gitkeep	0 bytes
data/metadata/_SUMMARY.md	713 bytes
data/metadata/checksums/.gitkeep	0 bytes
data/metadata/checksums/wdi/smoke_20260602_task004/NY.GDP.MKTP.CD__USA-DNK__2020_2021.metadata.json	115 bytes
data/metadata/checksums/wdi/smoke_20260602_task004/NY.GDP.MKTP.CD__USA-DNK__2020_2021.sha256.json	538 bytes
data/metadata/checksums/wdi/smoke_20260602_task004/SP.POP.TOTL__USA-DNK__2020_2021.metadata.json	115 bytes
data/metadata/checksums/wdi/smoke_20260602_task004/SP.POP.TOTL__USA-DNK__2020_2021.sha256.json	529 bytes
data/metadata/checksums/wdi/smoke_20260602_task004_hardened/NY.GDP.MKTP.CD__USA-DNK__2020_2021.metadata.json	115 bytes
data/metadata/checksums/wdi/smoke_20260602_task004_hardened/NY.GDP.MKTP.CD__USA-DNK__2020_2021.sha256.json	547 bytes
data/metadata/checksums/wdi/smoke_20260602_task004_hardened/SP.POP.TOTL__USA-DNK__2020_2021.metadata.json	115 bytes
data/metadata/checksums/wdi/smoke_20260602_task004_hardened/SP.POP.TOTL__USA-DNK__2020_2021.sha256.json	538 bytes
data/metadata/lineage/.gitkeep	0 bytes
data/raw/.gitkeep	0 bytes
data/raw/_SUMMARY.md	587 bytes
data/raw/wdi/smoke_20260602_task004/NY.GDP.MKTP.CD__USA-DNK__2020_2021.json	929 bytes
data/raw/wdi/smoke_20260602_task004/SP.POP.TOTL__USA-DNK__2020_2021.json	889 bytes
data/raw/wdi/smoke_20260602_task004_hardened/NY.GDP.MKTP.CD__USA-DNK__2020_2021.json	929 bytes
data/raw/wdi/smoke_20260602_task004_hardened/SP.POP.TOTL__USA-DNK__2020_2021.json	889 bytes
data/staging/.gitkeep	0 bytes
data/staging/_SUMMARY.md	347 bytes
db/.gitkeep	0 bytes
db/_SUMMARY.md	368 bytes
db/migrations/.gitkeep	0 bytes
db/migrations/001_v0_schema.sql	7607 bytes
db/migrations/_SUMMARY.md	448 bytes
db/queries/.gitkeep	0 bytes
db/queries/_SUMMARY.md	416 bytes
db/queries/verify_v0_schema.sql	880 bytes
db/schema/.gitkeep	0 bytes
db/schema/_SUMMARY.md	430 bytes
db/schema/v0_schema.md	2453 bytes
docs/.gitkeep	0 bytes
docs/AUTONOMY_LEVELS.md	582 bytes
docs/BRANCH_STRATEGY.md	501 bytes
docs/_SUMMARY.md	419 bytes
docs/architecture/.gitkeep	0 bytes
docs/architecture/_SUMMARY.md	357 bytes
docs/data/.gitkeep	0 bytes
docs/data/_SUMMARY.md	341 bytes
docs/runbooks/.gitkeep	0 bytes
docs/runbooks/_SUMMARY.md	387 bytes
docs/runbooks/low-token-local-agent-workflow.md	3117 bytes
hardware/.gitkeep	0 bytes
hardware/_SUMMARY.md	381 bytes
hardware/profile.yaml	479 bytes
hardware/resource_policy.yaml	380 bytes
instructions/CONTEXT_POLICY.md	590 bytes
instructions/FOLDER_SUMMARY_POLICY.md	461 bytes
instructions/GENERAL_INSTRUCTIONS.md	918 bytes
instructions/MODEL_ROUTING_POLICY.md	475 bytes
instructions/PROJECTFORGE_SELF_MANAGEMENT.md	406 bytes
instructions/SMALL_SKILLS_POLICY.md	328 bytes
instructions/SPECIALIZED_AGENT_POLICY.md	465 bytes
instructions/_SUMMARY.md	536 bytes
knowledge/.gitkeep	0 bytes
knowledge/_SUMMARY.md	383 bytes
knowledge/components.yaml	910 bytes
knowledge/dependencies.yaml	552 bytes
logs/_SUMMARY.md	376 bytes
logs/agents/.gitkeep	0 bytes
logs/agents/_SUMMARY.md	345 bytes
logs/derived/.gitkeep	0 bytes
logs/derived/_SUMMARY.md	347 bytes
logs/logging_policy.yaml	640 bytes
logs/raw/.gitkeep	0 bytes
logs/raw/_SUMMARY.md	339 bytes
memory/_SUMMARY.md	387 bytes
memory/archive/.gitkeep	0 bytes
memory/archive/_SUMMARY.md	351 bytes
memory/deprecated_decisions/.gitkeep	0 bytes
memory/deprecated_decisions/_SUMMARY.md	377 bytes
memory/retention_policy.yaml	663 bytes
metrics/_SUMMARY.md	399 bytes
metrics/events.jsonl	0 bytes
metrics/metrics_policy.yaml	681 bytes
metrics/recommendations/.gitkeep	0 bytes
metrics/recommendations/README.md	101 bytes
metrics/recommendations/_SUMMARY.md	383 bytes
metrics/reports/.gitkeep	0 bytes
metrics/reports/README.md	72 bytes
metrics/reports/_SUMMARY.md	367 bytes
models/_SUMMARY.md	383 bytes
models/registry.yaml	1096 bytes
models/routing.yaml	1264 bytes
models/selection_policy.yaml	716 bytes
permissions/.gitkeep	0 bytes
permissions/_SUMMARY.md	408 bytes
permissions/allowlist.yaml	1727 bytes
permissions/denylist.yaml	347 bytes
permissions/escalation_rules.yaml	1157 bytes
pipelines/.gitkeep	0 bytes
pipelines/_SUMMARY.md	341 bytes
policies/_SUMMARY.md	354 bytes
policies/enforcement_policy.yaml	797 bytes
project.yaml	199 bytes
pyproject.toml	189 bytes
question_queue/_SUMMARY.md	378 bytes
question_queue/answered/.gitkeep	0 bytes
question_queue/answered/_SUMMARY.md	369 bytes
question_queue/archive/.gitkeep	0 bytes
question_queue/archive/_SUMMARY.md	367 bytes
question_queue/pending/.gitkeep	0 bytes
question_queue/pending/_SUMMARY.md	367 bytes
recovery/.gitkeep	0 bytes
recovery/_SUMMARY.md	411 bytes
recovery/escalation_policy.yaml	609 bytes
recovery/failure_playbooks.md	1956 bytes
recovery/incident_log.md	114 bytes
reports/.gitkeep	0 bytes
reports/_SUMMARY.md	337 bytes
research/.gitkeep	0 bytes
research/_SUMMARY.md	339 bytes
simulation/_SUMMARY.md	419 bytes
simulation/dry_run_policy.yaml	860 bytes
simulation/dry_run_schema.yaml	434 bytes
simulation/dry_runs/.gitkeep	0 bytes
simulation/dry_runs/20260602_120708-dry-run.md	2230 bytes
simulation/dry_runs/20260602_121839-dry-run.md	2056 bytes
simulation/dry_runs/README.md	69 bytes
simulation/dry_runs/_SUMMARY.md	375 bytes
simulation/risk_classification.md	316 bytes
skills/.gitkeep	0 bytes
skills/_SUMMARY.md	658 bytes
skills/clarification-queue.md	310 bytes
skills/command-permissions.md	448 bytes
skills/context-budgeting.md	301 bytes
skills/deferred-specification.md	340 bytes
skills/dry-run-workflow.md	299 bytes
skills/folder-summaries.md	363 bytes
skills/git-workflow.md	558 bytes
skills/logging-workflow.md	229 bytes
skills/metrics-feedback.md	250 bytes
skills/model-routing.md	482 bytes
skills/project-bootstrap.md	1029 bytes
skills/state-update.md	380 bytes
skills/structured-questionnaire.md	995 bytes
src/_SUMMARY.md	346 bytes
src/macroforge/_SUMMARY.md	484 bytes
src/macroforge/__init__.py	0 bytes
src/macroforge/wdi.py	10232 bytes
state/.gitkeep	0 bytes
state/_SUMMARY.md	450 bytes
state/active_goal.md	2197 bytes
state/architecture.md	2948 bytes
state/known_issues.md	37 bytes
state/lessons.md	32 bytes
state/project_state.md	3417 bytes
state/recent_changes.md	97 bytes
tests/_SUMMARY.md	679 bytes
tests/invariants/.gitkeep	0 bytes
tests/invariants/README.md	338 bytes
tests/invariants/_SUMMARY.md	369 bytes
tests/test_placeholder.py	40 bytes
tests/test_v0_schema_migration.py	4368 bytes
tests/test_wdi_extract.py	6260 bytes
tools/.gitkeep	0 bytes
tools/_SUMMARY.md	731 bytes
tools/analyze_metrics.py	1301 bytes
tools/build_context.py	2552 bytes
tools/check_coherence.py	7155 bytes
tools/create_question.py	1259 bytes
tools/detect_hardware.py	835 bytes
tools/dry_run.py	3928 bytes
tools/escalate.py	1829 bytes
tools/git_autopush.py	1285 bytes
tools/install.sh	495 bytes
tools/log_run.py	1039 bytes
tools/record_metric.py	1067 bytes
tools/register_project.py	3143 bytes
tools/review_metrics.py	2074 bytes
tools/run.py	3361 bytes
tools/select_model.py	1736 bytes
tools/telegram_notifier_stub.py	632 bytes
tools/update_context_summaries.py	4636 bytes
tools/update_state.py	934 bytes
tools/validate_dry_run.py	1824 bytes
workspace_config.yaml	641 bytes
```

## Selected source-of-truth excerpts
### CONSTITUTION.md
```text
# ProjectForge Constitution

ProjectForge exists to create and maintain boring, legible, reusable project environments for agent-assisted work.

## Non-negotiable rules

1. Project state must be explicit on disk, not hidden in chat memory.
2. Setup answers and deferred specifications must be stored as decision artifacts under `artifacts/decisions/`.
3. Agents must not silently invent project-wide policy. If a decision is absent, ambiguous, or conflicting, use deferred specification and clarification severity rules.
4. GitHub pushes require human approval by default. Auto-commit is allowed only after validation passes and policy permits it.
5. Dry-run/preflight is mandatory according to the risk-scaled dry-run policy in `simulation/dry_run_policy.yaml`.
6. Capability failures escalate to stronger models before humans. Permission, safety, credential, destructive, monetary, or strategic decisions escalate to humans.
7. Specialized agents are never created silently. ProjectForge may request one with a short explanation; after approval, it may generate the agent automatically.
8. Skills should be small and composable by default. Large playbooks are allowed only for complex domains.
9. Metrics must be used to improve agents, tools, model routing, templates, and task workflows, but not to justify opaque automation.
10. The system must remain understandable from ordinary files: Markdown, YAML, JSON, and JSONL.

## Default operating posture

The default is AI-first project execution under human-designed constraints. Humans specify constitution, risk boundaries, and project intent; agents execute inside those boundaries.
```

### context/PROJECT_CONTEXT.md
```text
# MacroForge Project Context

## Identity

MacroForge is a long-lived, AI-first macroeconomic and investing research platform. It is both:

1. a macroeconomic data warehouse that ingests, normalizes, validates, versions, and stores public macro datasets in PostgreSQL; and
2. a research operating system that lets constrained local agents perform reproducible, evidence-backed analysis from curated project state instead of raw chat history.

The project may later expand into equities, firm-level data, filings, fundamentals, stock analysis, dashboards, and briefs. Those are downstream of the first reliable macro data loop.

## V1 success

V1 succeeds when one public macro dataset is ingested end-to-end into PostgreSQL with:

- immutable raw input preserved on disk;
- checksum and source/release metadata;
- standardized staging records;
- curated canonical observations;
- idempotent load semantics;
- source/run/lineage/quality tables;
- validation checks for row counts, keys, nulls, duplicate grain, and sanity ranges;
- an inspectable query/report output;
- run evidence under `logs/` or `artifacts/reports/`.

## First-source assumption

Because the user did not provide a blocking override during setup, the scaffold assumes World Bank WDI for the first vertical slice. Rationale: public, keyless, broad, and good for testing indicator/geography/time/unit modeling. Historical UN WPP/UNPD discussions remain useful and can be revived later.

## Non-goals for v1

- Do not make AI-generated research briefs the first deliverable.
- Do not build many pipelines before schema, grain, idempotency, logging, and validation stabilize.
- Do not add Airflow/Dagster/Prefect before several local/manual pipelines exist.
- Do not provide agents raw shell, secrets, production access, deployment authority, or billing authority.
- Do not treat raw ChatGPT exports as project truth.
- Do not overbuild a universal framework before real source variation is observed.

## Source-of-truth hierarchy

1. Current files: `AGENTS.md`, `CONSTITUTION.md`, `state/`, accepted decisions, active tasks.
2. Project docs and runbooks.
3. Compact recovered summaries under `context/imports/`.
4. Raw chat/export material only for forensic lookup.

## ChatGPT export recovery

Useful historical context was recovered from:

`/home/mkkto/Desktop/ChatGPT_chats/ChatGPT_exports.zip`

The compact import lives at:

`context/imports/chatgpt_export_recovery/recovery_summary.md`

That summary helped pre-answer ProjectForge setup questions. It is historical evidence, not live policy unless promoted into current decisions/tasks/docs.

## Local-agent design intent

MacroForge should be operated through bounded task contracts and context bundles:

- Operator/context-manager updates state and chooses the next task.
- Planner decomposes accepted goals into artifacts/tasks.
- Builder implements small code/doc changes.
- Reviewer checks against acceptance criteria and tests.
- Data steward owns schema, lineage, source catalog, validation.
- Researcher/analyst gathers sources and writes evidence-backed notes.
- Auditor checks reproducibility, security, and artifact consistency.

Agents should consume `_SUMMARY.md`, `context/PROJECT_CONTEXT.md`, state files, and task artifacts before opening large logs or raw imports.
```

### state/active_goal.md
```text
# Active Goal

Project: MacroForge

## Purpose

MacroForge is a long-lived AI-first macroeconomic and investing research platform. It starts as a PostgreSQL-backed macroeconomic data warehouse and expands into evidence-backed research workflows for macro, equities, firm-level data, filings, fundamentals, stocks, and investment analysis. It must preserve provenance, lineage, quality checks, run logs, decisions, and agent boundaries so local agents can do most implementation/research work from curated context rather than raw chat history.

## V1 Success

V1 succeeds when MacroForge has one real macro data vertical slice: extract one public dataset, preserve immutable raw evidence and checksum, transform to staging, load idempotently into PostgreSQL canonical tables, record source/release/run/lineage/quality metadata, validate row counts/keys/duplicates/sanity checks, and produce an inspectable query or report output with a reproducible run summary.

## Current first milestone

Implement the World Bank WDI vertical-slice foundation unless the user explicitly switches to UN WPP/UNPD before implementation:

1. Create v0 schema decision. Done in `artifacts/decisions/DEC-004-v0-postgresql-schema-foundation.md`.
2. Add PostgreSQL migration for meta/dim/fact tables. Done in `db/migrations/001_v0_schema.sql`.
3. Add validation queries/tests. Done in `db/queries/verify_v0_schema.sql` and `tests/test_v0_schema_migration.py`.
4. Implement narrow WDI extract/transform/load task. Extraction and raw/checksum evidence are done in `artifacts/tasks/TASK-004-narrow-wdi-extract-raw-evidence.md`; PostgreSQL load remains next.
5. Produce run evidence and update state.

## Non-goals

Do not make AI-generated research briefs the first milestone; prove the data loop first. Do not build many pipelines before grain/schema/idempotency/logging/validation are stable. Do not add Airflow/Dagster/Prefect before several manual/local pipelines exist. Do not give agents raw shell, secrets, production, deployment, or billing authority. Do not treat raw ChatGPT exports as canonical truth. Do not overbuild a universal framework before real source variation is observed.

## Last updated

2026-06-02
```

### state/project_state.md
```text
# Project State

Project: MacroForge
Template: python_data_project
Created by: ProjectForge

Canonical location: `/home/mkkto/srv/projectforge/workspace/projects/macroforge`
Workspace registry: `/home/mkkto/srv/projectforge/workspace/projects_registry.yaml`

## Operating context
- Project type: mixed: python_data_project + research operating system + local agent-assisted project OS. Data platform first, research/analysis second.
- Primary users: Primary user is the owner; secondary users are constrained local agents acting as operator, planner, builder, reviewer, researcher/analyst, data steward, auditor, and teacher/explainer. No public users in v1.
- Agent autonomy: balanced-to-aggressive local autonomy inside strict project boundaries: agents may inspect files, propose plans, edit docs/code for accepted tasks, run local tests, and produce run evidence. Agents must pause/escalate for secrets, destructive operations, schema/architecture policy changes, production data, billing, deployment, git push, or unresolved blocking questions.
- Command policy: Layered default with restrictive denylist and escalation. Hermes may use Hermes-native tools for normal reads/edits/tests. Recurring or manual commands should go through project wrappers/dry-run policy. Mutating infra, secrets, production data, deploys, broad deletes, and git push require human approval.
- Secrets policy: Yes eventually, but v1 starts with no required secrets. Secrets/API keys/credentials must live outside git in environment files, OS secret store, or service-specific config with strict permissions. Agents receive only role-required secrets and never raw secret dumps. No paid/credentialed sources until explicit decision.
- Logging standard: Use ProjectForge default logging plus MacroForge-specific run evidence: raw append-only run logs, derived summaries, actions, command outputs/pointers, checksums, source metadata, validation reports, lineage, decisions, tasks, and handoffs. Raw logs are evidence; summaries/indexes are regeneratable; decisions/tasks/docs are promoted truth.
- Testing standard: Tests must be run before summarizing code changes. Minimum v1 testing: smoke/coherence tests, unit tests for parsers/mappers/loaders, SQL migration/schema verification, validation queries for data quality, and end-to-end test or dry-run evidence for the first ingestion slice.
- Documentation standard: Rigorous but concise. Maintain PROJECT_CONTEXT, state, decisions, tasks, runbooks, architecture, glossary, data model, source catalog, and run summaries. Prefer durable artifacts over chat-only explanations.

## Current implementation status
- V0 PostgreSQL schema foundation is implemented and documented under `db/migrations/001_v0_schema.sql`, `db/schema/v0_schema.md`, and `artifacts/decisions/DEC-004-v0-postgresql-schema-foundation.md`.
- Narrow World Bank WDI extraction and raw/checksum evidence writing is implemented in `src/macroforge/wdi.py`; smoke evidence is summarized in `artifacts/reports/wdi_extract_smoke_20260602_task004.json`.
- Next implementation focus is loading normalized WDI records into PostgreSQL staging/curated tables against the v0 schema.

## Deferred or watchlist items
Nonblocking unknowns are recorded as Deferred setup decisions.

## Source of truth
Setup answers are recorded under `artifacts/decisions/`. Future agents must update decision artifacts when durable policy changes.
```

### state/architecture.md
```text
# Architecture

Project: MacroForge

## Initial architecture posture

- Project type: mixed Python data project + research operating system + local agent-assisted project OS.
- Primary language/runtime: Python 3.12+ for ingestion, validation, CLI/tools, and agent-operable workflows.
- Database: PostgreSQL for authoritative storage, constraints, views, and queryable macro observations.
- File formats: Markdown/YAML/JSON/JSONL for project operating artifacts; raw data files are immutable evidence.
- Deployment: local/home server first. Docker/cloud/public deployment deferred.
- External services: public no-key data first; no paid/credentialed APIs in v1.

## Project-specific directories

- `data/raw/`: immutable source extracts and checksums.
- `data/staging/`: intermediate standardized records for local inspection.
- `data/curated/`: generated analysis-ready exports, if needed outside PostgreSQL.
- `data/metadata/`: checksums, lineage, source metadata snapshots.
- `db/migrations/`: SQL migrations.
- `db/schema/`: current schema documentation or generated schema snapshots.
- `db/queries/`: reusable verification/analysis queries.
- `pipelines/`: source-specific extraction/transform/load modules or task wrappers.
- `reports/`: generated outputs and validation reports.
- `research/`: curated research notes and source notes.

## PostgreSQL schema direction

Core schemas:

- `meta`: sources, dataset releases, runs, lineage, quality checks.
- `raw`: optional raw database mirrors; raw files remain evidence.
- `staging`: source-normalized loading structures.
- `curated`: canonical facts/dimensions/views.
- `mart`: later derived views for reports/dashboards.

Core model:

- `dim_source`
- `dim_dataset_release`
- `dim_indicator`
- `dim_territory`
- `dim_period` with frequency plus period start/end dates
- `dim_unit`
- optional `dim_status`
- optional `dim_attribute_set`
- `fact_observation`

Candidate fact grain:

One row = one observation for source + indicator + territory + period + unit + attribute set + vintage/as-of date.

Candidate uniqueness:

`(source_id, indicator_id, territory_id, period_id, attribute_set_id, unit_id, as_of_date)`

Use latest-vintage views for common analysis instead of overwriting history.

## Pipeline shape

Every source pipeline should follow the same contract:

1. Extract raw source data.
2. Save raw input and checksum.
3. Normalize to staging shape.
4. Load/upsert dimensions.
5. Load/upsert observations idempotently.
6. Record run metadata, lineage, and quality checks.
7. Emit validation report and run summary.

Only source clients/mappers should vary by source. Shared loader, validation, and run logging should stay reusable.

## Guardrails

Use the local constitution, permissions, dry-run policy, and setup decisions before changing architecture.
Create a decision artifact before changing schema grain, secrets policy, deployment policy, agent autonomy, or first-source scope.
```

### artifacts/tasks/TASK-001-initial-validation.md
```text
# TASK-001: Initial validation of ProjectForge-generated MacroForge

Status: done
Created: 2026-06-02

## Goal

Verify that the rebuilt MacroForge scaffold is coherent and testable after generation from the current ProjectForge template.

## Acceptance criteria

- ProjectForge generated-project coherence passes.
- Template tests pass.
- Project-specific context, decisions, and first implementation task exist.
- Legacy repo was backed up before replacement.

## Evidence

Legacy backup:

`/home/mkkto/srv/macroforge_legacy_20260602_101533`

Verification should be repeated after any further structural edits:

```bash
python3 tools/check_coherence.py --project . --mode generated --json
PYTHONPATH=src uvx --from pytest pytest -q
```
```

### artifacts/tasks/TASK-002-v0-schema-wdi-ingestion.md
```text
# TASK-002: Build v0 schema and World Bank WDI ingestion slice

Status: todo
Created: 2026-06-02
Depends on: `artifacts/decisions/DEC-001-project-scope-and-v1-slice.md`

## Goal

Implement MacroForge's first real data-platform vertical slice using World Bank WDI unless the user explicitly changes the first source before implementation starts.

## Scope

Build only the minimum end-to-end loop:

1. v0 PostgreSQL schema decision/details.
2. SQL migration for metadata, dimensions, and canonical observations.
3. WDI extraction for a narrow indicator/country/year scope.
4. Immutable raw data storage with checksum.
5. Transform to staging shape.
6. Idempotent load into PostgreSQL.
7. Validation queries/tests.
8. One inspectable output report/query.
9. Run summary with evidence.

## Suggested initial dataset slice

Use a very small set first, for example:

- indicators: GDP current US$, population total, inflation CPI;
- territories: United States, Denmark, Euro area or World;
- years: 2000-present.

This is enough to validate model shape without pretending the whole source is solved.

## Acceptance criteria

- Real SQL migration exists under `db/migrations/`.
- Tests verify schema assumptions and basic transform/load behavior.
- Pipeline can be run locally with no API key.
- Raw response/data and checksum are written under `data/raw/` / `data/metadata/checksums/`.
- Run metadata and validation output are written under `logs/` or `artifacts/reports/`.
- PostgreSQL contains loaded observations with no duplicate canonical grain.
- A query/report output demonstrates the loaded data.
- State and folder summaries are updated.

## Out of scope

- Full source coverage.
- Multiple sources.
- Airflow/Dagster/Prefect.
- Research brief generation.
- Public deployment.
- Paid/credentialed APIs.
```

### artifacts/tasks/TASK-003-v0-postgresql-schema-foundation.md
```text
# TASK-003: Define and verify v0 PostgreSQL schema foundation

Status: done
Created: 2026-06-02
Depends on:
- `artifacts/tasks/TASK-002-v0-schema-wdi-ingestion.md`
- `artifacts/decisions/DEC-001-project-scope-and-v1-slice.md`

## Goal

Create the minimum PostgreSQL schema foundation required before implementing the World Bank WDI ingestion slice.

## Scope

This task covers only the schema foundation for TASK-002:

1. Record the v0 schema choices as a decision artifact.
2. Add the initial SQL migration under `db/migrations/`.
3. Add schema documentation under `db/schema/`.
4. Add validation/inspection SQL under `db/queries/`.
5. Add tests that verify migration structure and transactional application against local PostgreSQL when available.

## Out of scope

- WDI network extraction.
- WDI transform/load implementation.
- Raw response/checksum writing.
- Multi-source abstractions.
- Airflow/Dagster/Prefect or other orchestrators.
- Research briefs, dashboards, or public deployment.

## Acceptance criteria

- `artifacts/decisions/DEC-004-v0-postgresql-schema-foundation.md` records the v0 grain, schemas, tables, idempotency posture, and deferred choices.
- `db/migrations/001_v0_schema.sql` creates the minimum metadata, staging, and curated schemas/tables.
- Canonical observation uniqueness enforces one row per source + indicator + territory + period + unit + attribute set + as-of date.
- `db/schema/v0_schema.md` summarizes the v0 schema for future agents.
- `db/queries/verify_v0_schema.sql` provides an inspectable verification query set.
- Tests verify required SQL objects/constraints and apply the migration transactionally to PostgreSQL when `psql` can connect to `postgres`.
- Project coherence and the full test suite pass.

## TDD notes

Write schema verification tests first and confirm they fail before adding the migration/schema files.

## Evidence

Dry-run/preflight:

`simulation/dry_runs/20260602_120708-dry-run.md`

TDD RED result before migration/schema files were added:

```text
PYTHONPATH=src uvx --from pytest pytest tests/test_v0_schema_migration.py -q
FFF [100%]
3 failed ... missing db/migrations/001_v0_schema.sql
```

Targeted schema test after implementation and reviewer-driven staging idempotency fix:

```text
PYTHONPATH=src uvx --from pytest pytest tests/test_v0_schema_migration.py -q
... [100%]
3 passed in 0.23s
```

Final verification commands run before handoff:

```text
PYTHONPATH=src uvx --from pytest pytest -q
.... [100%]
4 passed in 0.23s

python3 tools/check_coherence.py --project . --mode generated --json
{
  "mode": "generated",
  "blocks": [],
  "warnings": []
}

git status --short
M artifacts/decisions/_SUMMARY.md
M artifacts/tasks/_SUMMARY.md
M db/migrations/_SUMMARY.md
M db/queries/_SUMMARY.md
M db/schema/_SUMMARY.md
M state/active_goal.md
M state/project_state.md
M tests/_SUMMARY.md
?? artifacts/decisions/DEC-004-v0-postgresql-schema-foundation.md
?? artifacts/tasks/TASK-003-v0-postgresql-schema-foundation.md
?? db/migrations/001_v0_schema.sql
?? db/queries/verify_v0_schema.sql
?? db/schema/v0_schema.md
?? simulation/dry_runs/20260602_120708-dry-run.md
?? tests/test_v0_schema_migration.py
```
```

### artifacts/tasks/TASK-004-narrow-wdi-extract-raw-evidence.md
```text
# TASK-004: Narrow WDI extract and raw evidence writer

Status: done
Created: 2026-06-02
Depends on:
- `artifacts/tasks/TASK-002-v0-schema-wdi-ingestion.md`
- `artifacts/tasks/TASK-003-v0-postgresql-schema-foundation.md`
- `artifacts/decisions/DEC-004-v0-postgresql-schema-foundation.md`

## Goal

Implement the first narrow World Bank WDI extraction step and immutable raw evidence writer for the v1 vertical slice.

## Scope

This task covers only extraction and raw evidence preservation:

1. Add a small stdlib-only WDI client for the keyless World Bank API.
2. Support a narrow indicator/country/year slice.
3. Preserve raw API payloads under ignored `data/raw/` runtime paths.
4. Write checksum/source metadata under ignored `data/metadata/checksums/` runtime paths.
5. Normalize fetched rows to the v0 staging shape in memory for the next loader task.
6. Produce a small run report under `artifacts/reports/`.

## Initial smoke slice

Use this no-key API slice for verification:

- countries: `USA`, `DNK`
- indicators: `NY.GDP.MKTP.CD`, `SP.POP.TOTL`
- years: `2020:2021`

## Out of scope

- PostgreSQL loading.
- Transform/load upserts into dimensions or facts.
- Full WDI source coverage.
- Multiple sources.
- Scheduler/orchestrator setup.
- Research briefs or dashboards.

## Acceptance criteria

- Tests cover WDI URL construction, API response parsing, staging-shape normalization, raw artifact writing, and checksum metadata.
- Targeted WDI tests fail before implementation and pass after implementation.
- A live no-key smoke extraction writes raw payload/checksum/report evidence.
- Full tests and ProjectForge generated coherence pass.
- State and folder summaries are updated.

## Evidence

Dry-run/preflight:

`simulation/dry_runs/20260602_121839-dry-run.md`

TDD RED result before `src/macroforge/wdi.py` existed:

```text
PYTHONPATH=src uvx --from pytest pytest tests/test_wdi_extract.py -q
ImportError: cannot import name 'wdi' from 'macroforge'
```

Targeted WDI tests after implementation:

```text
PYTHONPATH=src uvx --from pytest pytest tests/test_wdi_extract.py -q
.... [100%]
4 passed in 0.02s
```

Live no-key smoke extraction:

```text
PYTHONPATH=src python3 -m macroforge.wdi extract --countries USA,DNK --indicators NY.GDP.MKTP.CD,SP.POP.TOTL --start-year 2020 --end-year 2021 --run-id smoke_20260602_task004
```

Smoke extraction wrote:

- `data/raw/wdi/smoke_20260602_task004/NY.GDP.MKTP.CD__USA-DNK__2020_2021.json` with checksum `ddd87d06ce3e488c263d8515cfc88d9a069befbe316c33c9fc2b3f82ee706b1a`
- `data/raw/wdi/smoke_20260602_task004/SP.POP.TOTL__USA-DNK__2020_2021.json` with checksum `1efe73e21ac470625a5faf95781671cf7524901b5075f3a678b83820a9ea69af`
- `artifacts/reports/wdi_extract_smoke_20260602_task004.json`

Smoke result: 2 indicators x 2 countries x 2 years = 8 staging-shaped records.

Reviewer hardening fixes:

- Rejected unsafe `run_id` values that could escape artifact roots.
- Prevented overwrites of existing raw payload/checksum/metadata/report files.
- Added tests for both behaviors.

Final hardened smoke extraction:

```text
PYTHONPATH=src python3 -m macroforge.wdi extract --countries USA,DNK --indicators NY.GDP.MKTP.CD,SP.POP.TOTL --start-year 2020 --end-year 2021 --run-id smoke_20260602_task004_hardened
```

Final report:

`artifacts/reports/wdi_extract_smoke_20260602_task004_hardened.json`

Final verification:

```text
PYTHONPATH=src uvx --from pytest pytest tests/test_wdi_extract.py -q
...... [100%]
6 passed in 0.02s

PYTHONPATH=src uvx --from pytest pytest -q
.......... [100%]
10 passed in 0.24s

python3 tools/check_coherence.py --project . --mode generated --json
{
  "mode": "generated",
  "blocks": [],
  "warnings": []
}
```
```

### artifacts/decisions/DEC-004-v0-postgresql-schema-foundation.md
```text
# DEC-004: v0 PostgreSQL schema foundation

Status: accepted
Date: 2026-06-02
Depends on:
- `artifacts/decisions/DEC-001-project-scope-and-v1-slice.md`

## Context

MacroForge v1 is a PostgreSQL-backed World Bank WDI vertical slice. The project architecture already points to metadata, staging, and curated schemas with canonical observations keyed by source, indicator, territory, period, unit, attribute set, and as-of/vintage date.

This decision narrows that existing direction into an implementable v0 schema. It does not broaden v1 beyond schema plus one WDI ingestion slice.

## Decision

Use raw SQL for the v0 migration rather than introducing Alembic or another migration framework immediately.

Create these PostgreSQL schemas in v0:

- `meta`: source catalog, dataset releases, pipeline runs, lineage events, and quality checks.
- `staging`: source-normalized WDI observations for inspection before canonical load.
- `curated`: canonical dimensions and fact observations.

Create these core v0 tables:

- `meta.source`
- `meta.dataset_release`
- `meta.pipeline_run`
- `meta.lineage_event`
- `meta.quality_check`
- `staging.wdi_observation`
- `curated.dim_indicator`
- `curated.dim_territory`
- `curated.dim_period`
- `curated.dim_unit`
- `curated.dim_attribute_set`
- `curated.fact_observation`

Use this canonical v0 fact grain:

`source_id + indicator_id + territory_id + period_id + unit_id + attribute_set_id + as_of_date`

Use a default empty attribute-set row for simple WDI observations so the fact grain remains stable without forcing source-specific optional attributes into early tables.

Use `as_of_date` as the v0 vintage marker. For WDI, this can initially be the extraction/run date or release metadata date when available. Do not overwrite historical vintages; later latest-vintage views can hide this complexity for normal analysis.

Use idempotent natural-key constraints on source codes, releases, dimension codes, staging run/source rows, and canonical fact grain. Loader implementation should use `INSERT ... ON CONFLICT` against these constraints in the later WDI task.

## Consequences

- The first migration can be applied and tested without a migration framework dependency.
- The schema supports v1 provenance, lineage, quality checks, staging, and canonical duplicate prevention.
- The WDI loader task has a clear destination contract and should not invent a different grain.
- Later sources may require additional dimensions or attributes, but those should be driven by observed source variation and recorded in future decisions.

## Deferred choices

- Formal migration framework such as Alembic.
- `raw` database mirror schema; raw files remain immutable evidence for v1.
- `mart` views and latest-vintage convenience views.
- Full currency/unit normalization beyond a v0 unit dimension.
- Rich geography hierarchy beyond WDI territory codes.
```
