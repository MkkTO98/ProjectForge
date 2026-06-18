# ProjectForge Operator Manual

This manual lists the manual actions you may still want to perform, how to do them, why they matter, and examples. Routine hygiene should be automated by the brain/orchestrator according to `automation/orchestration_schedule.yaml`; these commands remain useful for setup, audit, debugging, and recovery.

## Canonical installation layout

Assumed location:

```txt
/home/mkkto/srv/EIP/projects/ProjectForge/
```

Generated projects should be created under:

```txt
/home/mkkto/srv/EIP/projects/ProjectForge/workspace/projects/
```

Example:

```txt
/home/mkkto/srv/EIP/projects/MacroForge/
```

Why: this keeps ProjectForge, its workspace, shared resources, and generated projects under one predictable hierarchy.

## 1. Create a new project

Preferred path: ask Hermes to use ProjectForge. Hermes should load the `projectforge` skill, interview you adaptively, capture answers, then render the scaffold noninteractively.

The questionnaire in `config/setup_questionnaire.yaml` is a coverage map. It is not meant to be dumped mechanically on the user. Hermes should ask one focused topic at a time, explain tradeoffs when useful, reuse known context, and stop once `config/sufficiency_policy.yaml` says bootstrap is operationally sufficient.

Manual fallback:

```bash
cd /home/mkkto/srv/EIP/projects/ProjectForge
python3 tools/new_project.py --name "My New Project" --template python_data_project
```

Hermes/noninteractive rendering path:

```bash
cd /home/mkkto/srv/EIP/projects/ProjectForge
python3 tools/new_project.py --name "My New Project" --template python_data_project --answers-json context/project_creation_answers_my_new_project.json
```

By default, this creates:

```txt
/home/mkkto/srv/EIP/projects/ProjectForge/workspace/projects/my_new_project/
```

It also registers the project in:

```txt
workspace/projects_registry.yaml
```

Why: project creation should be standardized without making the user operate a rigid terminal questionnaire. Hermes owns interrogation and sufficiency judgment; `tools/new_project.py` owns deterministic scaffold rendering, state initialization, decision artifacts, permissions, logs, metrics, context policies, and workspace linkage.

## 2. Fill or update the hardware profile

Edit:

```txt
hardware/profile.yaml
hardware/resource_policy.yaml
```

Include approximate values for:

```txt
RAM
GPU/VRAM if available
CPU threads
model runtime, such as Ollama or Hermes
parallel model limits
```

Example:

```yaml
machine_name: mikkel-desktop
ram_gb: 32
gpu:
  vendor: nvidia
  vram_gb: 12
local_model_runtime:
  - ollama
limits:
  max_parallel_large_models: 1
  max_parallel_small_models: 3
```

Why: model routing and parallel agents need real hardware constraints. Otherwise agents may choose models your machine cannot run efficiently.

## 3. Register available models

Edit:

```txt
models/registry.yaml
models/routing.yaml
models/selection_policy.yaml
```

Manual check:

```bash
python3 tools/select_model.py --project . --agent coder --task implementation
```

Why: different work requires different models. A small summarizer should not handle architecture. A large coder should not waste resources on folder summaries.

Example routing principle:

```txt
summarizer -> small local model
coder -> code-specialized local model
planner/reviewer -> stronger reasoning model
capability failure -> stronger local -> Codex/premium -> human
```

## 4. Run routine hygiene manually

Normally the orchestrator should run this. Manual use is for debugging or audit.

After a task:

```bash
python3 tools/orchestrator_hygiene.py --project . --phase after_task
```

Before commit:

```bash
python3 tools/orchestrator_hygiene.py --project . --phase before_commit
```

Periodic review:

```bash
python3 tools/orchestrator_hygiene.py --project . --phase periodic
```

Why: this bundles context-summary refresh, coherence checking, metrics review, and deferred-specification review.

## 5. Check coherence

Use:

```bash
python3 tools/check_coherence.py --project .
```

Why: verifies required files, policy separation, dry-run validity, workspace linkage, manual push rules, and agent context-reporting discipline.

Example output:

```txt
coherence: 0 block(s), 0 warning(s)
```

If blocks appear, fix them before continuing. Warnings can be reviewed but do not always block work.

## 5a. Run Architecture-to-Reality Audit

Use:

```bash
python3 tools/architecture_reality_audit.py --project . --write-report
```

When to run it:

- every 5-10 completed tasks;
- before major architecture changes;
- before major governance reviews;
- when documentation and implementation appear to disagree.

Why: normal coherence checks catch required files and known invariants, but long-running projects also drift in softer ways: architecture documents describe systems that no longer exist, implementation grows without matching decisions, state files become historical ledgers, templates diverge from generated projects, or governance rules stop matching actual agent behavior.

Audit categories:

- architecture vs implementation;
- state files vs reality;
- agent instructions vs behavior;
- logging systems;
- context-management systems;
- governance processes;
- automation workflows;
- templates vs generated projects.

The audit should identify drift, obsolete documentation, duplicated systems, unused systems, missing implementations, implementation without documentation, and documentation without implementation.

Record results under:

```txt
artifacts/reports/R-YYYYMMDD-architecture-reality-audit.md
```

Remediation workflow:

1. Fix blocks before major architecture/governance work continues.
2. For durable policy, architecture, template, permission, model-routing, or scope changes, create or update a decision artifact.
3. Update docs, state, templates, tools, tests, and operating procedures together rather than patching only one surface.
4. Refresh affected `_SUMMARY.md` files and `context/latest_handoff.md`.
5. Rerun `architecture_reality_audit.py`, `check_coherence.py`, and relevant tests.

## 6. Validate a dry-run report

Use:

```bash
python3 tools/validate_dry_run.py simulation/dry_runs/<report>.md
```

Why: prevents vague dry-runs from becoming execution permission.

A valid dry-run must include:

```txt
proposal
risk
files
commands
validation_plan
rollback_plan
context_used
decision_artifacts_checked
approval_required
```

## 7. Refresh context summaries

Use:

```bash
python3 tools/update_context_summaries.py --project .
```

Why: `_SUMMARY.md` files are folder-local navigation aids used by the context system. They should be refreshed after folder changes or before important context builds.

Do not store durable decisions in summaries. Decisions belong in:

```txt
artifacts/decisions/
```

## 8. Build task context

Use:

```bash
python3 tools/build_context.py --project . --task "implement ingestion pipeline"
```

Why: agents should not read the whole repo blindly. Context budgeting starts with Priority 1 current-state files, then adds Priority 2 active-task/decision/folder-summary context only when relevant, and uses Priority 3 broader docs/reports/history only after justified expansion.

Important: `context/active_context.md` is a generated output for the task/model target that produced it. Do not make stale `active_context.md` mandatory startup context. For normal work, start from `state/active_goal.md`, `state/project_state.md`, `state/architecture.md`, and `context/latest_handoff.md`; then add active task/decisions/folder summaries and explicit files as needed. Rebuild a fresh bundle when a context bundle or cloud governance call is needed.

Keep state files concise:

```txt
state/active_goal.md      = current objective and boundaries
state/project_state.md    = current truth and compact pointers, not history
state/architecture.md     = current architecture posture and active decisions
context/latest_handoff.md = short recent handoff/pointers
```

Move long verification logs, old file-change inventories, and session history to task artifacts, reports, handoffs, or derived logs. Check context drift with:

```bash
python3 tools/context_health.py --project . --json
```

## 9. Review metrics

Use:

```bash
python3 tools/review_metrics.py --project .
```

Why: metrics convert repeated failures into improvement proposals, such as model-routing changes, skill refinements, or specialized-agent requests.

Metrics are derived evidence. Raw command output belongs in `logs/`, not `metrics/`.

## 10. Resolve deferred specifications

Use:

```bash
python3 tools/resolve_deferred_specs.py --project .
```

Why: deferred specifications are allowed, but not forever. If the same deferred issue blocks work twice, it should become an L3 blocking question.

Severity levels:

```txt
L1 = silent autonomy
L2 = nonblocking/batched question
L3 = blocking clarification; task pauses
L4 = emergency stop; human approval required
```

## 11. Handle questions

Pending questions live in:

```txt
question_queue/pending/
```

After answering, store durable answers as decision artifacts:

```txt
artifacts/decisions/D-YYYYMMDD-short-description.md
```

Why: agents must not ask the same question repeatedly or rely on chat memory.

## 12. Adjust permissions

Edit:

```txt
permissions/allowlist.yaml
permissions/denylist.yaml
permissions/escalation_rules.yaml
```

Why: ProjectForge should be strict by default. Useful blocked commands should become explicit decisions, not casual permission creep.

Example:

```txt
A project needs `npm test`.
→ create decision artifact explaining why.
→ add command to allowlist.
```

## 13. Git workflow

Default:

```txt
auto-commit allowed after validation
manual push required
force push forbidden by default
```

Before committing, run:

```bash
python3 tools/orchestrator_hygiene.py --project . --phase before_commit
```

Why: local commits are useful checkpoints. Remote pushes expose changes outside the local environment and should remain deliberate.

## 14. Workspace registry

Projects are registered in:

```txt
workspace/projects_registry.yaml
```

Manual registration:

```bash
python3 tools/register_project.py \
  --workspace /home/mkkto/srv/EIP/projects/ProjectForge/workspace \
  --project /home/mkkto/srv/EIP/projects/ProjectForge/workspace/projects/my_project \
  --name "My Project"
```

Why: workspace-level coordination lets ProjectForge know which projects exist and which shared resources they inherit.

## 15. Logs vs metrics

Use this rule:

```txt
logs/    = raw operational records
metrics/ = derived performance evidence
```

Examples:

```txt
command output -> logs/raw/
failure-rate analysis -> metrics/reports/
agent improvement recommendation -> metrics/recommendations/
```

Why: mixing raw records and derived conclusions creates two conflicting truth systems.

## 16. State vs summaries

Use this rule:

```txt
state/       = current project truth
_SUMMARY.md  = folder-local navigation
```

Examples:

```txt
Current architecture -> state/architecture.md
What a folder contains -> folder/_SUMMARY.md
Why a choice was made -> artifacts/decisions/
```

Why: summaries should help agents navigate. They should not become hidden architecture documents.

## 17. Knowledge vs architecture

Use this rule:

```txt
state/architecture.md = prose explanation
knowledge/*.yaml      = machine-readable dependency hints
```

Before structural changes, coder/reviewer agents must inspect:

```txt
knowledge/components.yaml
knowledge/dependencies.yaml
```

Why: agents need dependency awareness before refactoring.

## 18. Agent/skill separation

Use this rule:

```txt
agent = role and responsibility
skill = reusable procedure
model = LLM chosen for the task
```

Example:

```txt
coder agent decides what implementation work is needed
skills/dry-run-workflow.md defines dry-run procedure
models/routing.yaml chooses which local or premium model powers the work
```

Skills should be loaded on demand, not injected universally. A session should read a skill when the task matches the skill trigger, an artifact explicitly references it, or an attempt fails in a way covered by that skill. Keep startup context focused on state/task/decision/summary artifacts; use skills as procedural expansion points.

Why: without this separation, agent files become bloated, skills become redundant, and every run pays token cost for procedures it does not need.

## 19. Updating this manual

The orchestrator should propose an update to this manual when ProjectForge changes behavior, paths, tools, or policies. It may auto-fix minor stale references when safe, but substantive policy changes require a decision artifact.
