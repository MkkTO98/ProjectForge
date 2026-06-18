# ProjectForge v6

ProjectForge is a reusable, Hermes-native project initializer, framework, and governance scaffold for agent-supported projects. It creates projects with explicit state, decisions, tasks, logs, summaries, safety policy, and verification hooks so future Hermes sessions and humans can resume work without reconstructing context from chat. Generated projects become autonomous at creation; ProjectForge improves itself and future inheritance, but does not own or silently mutate existing projects.

ProjectForge is not MacroForge. ProjectForge is the factory/governance system; MacroForge is one generated or managed project.


## Ecosystem autonomy boundary

ProjectForge is not an ecosystem meta-controller. Projects remain autonomous and communicate through recommendations, notifications, documented interfaces, manifests, registries, and explicit contracts. A project may recommend or notify, but it may not govern, directly modify, create tasks inside, or assume authority over another project.

Future ecosystem concepts such as the EIP ecosystem, ResearchMemory, EconGraph, MonitorForge, ReportForge, EII, and future ecosystem infrastructure are architectural context only unless separately approved. EIP means Economic Intelligence Platform, the ecosystem as a whole; EII means Economic Intelligence Initiative, a possible future user-facing intelligence project. They are not implementation targets and must not be used to expand ProjectForge scope by default. No project owns the EIP root by default; if a root is adopted later, it represents ecosystem organization and neutral infrastructure, not project authority.

Project extraction readiness separates conceptual readiness from physical migration readiness. Conceptual readiness depends primarily on purpose, ownership boundaries, authority boundaries, and interface boundaries. Physical extraction additionally requires path inventory, artifact ownership inventory, compatibility planning, verification planning, rollback planning, and stable evidence references. Filesystem structure is a migration constraint, not governance authority.

## Primary operating model

```text
Hermes-led adaptive interview -> sufficiency policy -> captured answers -> scaffold render -> decisions/tasks/state -> verification -> summaries/handoff
```

Hermes should lead project creation as a discovery conversation. The static questionnaire in `config/setup_questionnaire.yaml` is a coverage map, not the user-facing script. Hermes should distinguish FOUNDATIONAL, ARCHITECTURAL, IMPLEMENTATION, and PREFERENCE questions, explain why foundational choices matter, and defer implementation details where possible. `tools/new_project.py` remains the deterministic scaffold renderer and should normally be called with `--answers-json` after Hermes has gathered enough information.

## Important defaults

- Boring reliable infrastructure: Markdown, YAML, JSONL, small Python tools.
- Hermes-native instructions: `AGENTS.md` at the ProjectForge root and in generated projects.
- Hybrid workspace inheritance: shared resources centralized, project governance local.
- Soft-block enforcement: block high-impact violations, warn on lower-risk drift.
- Risk-scaled dry-run: micro preflight for low risk, standard dry-run for medium risk, full dry-run for high risk.
- Manual GitHub push.
- JSONL metrics, no SQLite default.
- Specialized agents require user approval, then ProjectForge may generate them automatically.
- Capability failures escalate current Hermes session -> stronger local model if configured -> Codex/premium after context audit -> human.
- ProjectForge is local-execution / cloud-governance: local models/tools handle implementation, refactoring, tests, debugging, summarization, retrieval, and routine docs; cloud models handle high-leverage governance such as architecture review, strategic planning, project audits, gap analysis, redesign, and consistency review.
- Context is summary-first and expands incrementally. Raw logs and previous full conversations are audit/debug artifacts only and are excluded from normal task context.
- Cloud/Codex context defaults to a compact governance target (`context/context_policy.yaml`, normally 8k-10k tokens), but justified project-wide reviews may use the larger configured project-wide review budget.

## Context and token policy

ProjectForge context follows a strict hierarchy:

1. Priority 1 current-state context: `state/active_goal.md`, `state/project_state.md`, `state/architecture.md`, and `context/latest_handoff.md` when present.
2. Priority 2 task-scoped context: the active task file, relevant decision records, and relevant folder `_SUMMARY.md` files.
3. Priority 3 broader context: documentation, reports, design notes, roadmap files, and historical artifacts only after narrower context is insufficient or a justified project-wide review requires it.
4. Explicit source files only when summaries/current state are insufficient for the task.
5. Raw logs only for `failure_investigation`, `forensic`, or `incident` task types.

Repository-wide exploration is not default startup behavior. Normal task context may include only the current-state files, active task file, relevant folder summaries, relevant decision records, explicitly retrieved source files, and a short handoff. It must not include raw logs, previous full conversations, full session JSONL files, whole-project dumps, unrelated folders, large tool outputs, or generated artifacts unless explicitly relevant.

Build and inspect context with:

```bash
python3 tools/build_context.py --project . --task "describe task" --folders src,tests --files src/example.py --task-file artifacts/tasks/TASK-001-example.md
python3 tools/build_context.py --project . --task "cloud review" --model-target cloud --model-selected codex_supervisor --model-reason "architecture_decision" --folders src --files src/example.py
```

The builder writes generated artifacts for that specific task/model target:

- `context/active_context.md`: generated bundle; do not treat stale copies as mandatory startup context.
- `context/context_manifest.json`: files used and estimated tokens.
- `context/context_audit.json`: machine-readable audit.
- `context/context_audit.md`: human-readable audit with included/excluded files and reasons.

Keep primary state artifacts concise. `state/active_goal.md`, `state/project_state.md`, and `state/architecture.md` should describe current truth and pointers, not become historical ledgers. Move long verification transcripts and old file-change inventories to task artifacts, reports, handoffs, or derived logs. Check drift with:

```bash
python3 tools/context_health.py --project . --json
```

If compact cloud context exceeds the governance budget, first reduce context or summarize locally. If the work is a legitimate project-wide audit, redesign, strategic review, gap analysis, or consistency review, use project-wide review mode with an explicit justification rather than treating the larger context as an error:

```bash
python3 tools/build_context.py --project . --task "quarterly architecture audit" --task-type project_audit --context-mode project_wide_review --review-justification "Need folder-level coverage across the project before a redesign decision" --model-target cloud --model-selected codex_supervisor --model-reason project_audit
```

Project-wide review mode still starts from summaries, excludes raw logs by default, records included/excluded evidence, and enforces the larger configurable project-wide budget.

## Local-execution / cloud-governance routing

Use local tools/models for implementation, refactoring, tests, debugging, summaries, log compression, code search, retrieval/indexing, and routine documentation. Use cloud models for architecture decisions, project audits, strategic planning, gap analysis, redesign, consistency review, two failed local attempts, high ambiguity, explicit user request, or safety-critical destructive operations. `tools/select_model.py` enforces cloud escalation reasons and requires a valid context audit before returning a cloud model:

```bash
python3 tools/select_model.py --project . --agent planner --task architecture_decision --architecture-decision --context-audit context/context_audit.json --json
python3 tools/select_model.py --project . --agent planner --task project_audit --governance --context-audit context/context_audit.json --json
```

## Debugging token overuse

1. Open `context/context_audit.md`.
2. Check `Estimated tokens`, `Included files`, and `Excluded files`.
3. Confirm `Raw logs excluded: True` and `Summaries used: True`.
4. If tokens are high, remove broad `--files`, add or refresh folder summaries, and retrieve only target source files.
5. If summaries are stale, run `python3 tools/update_context_summaries.py --project . --core-only` and record a compact handoff with `tools/log_run.py`.

## Main tools

- `tools/new_project.py`: render a generated project from templates and accepted/deferred setup answers.
- `tools/build_context.py`: build a task context bundle.
- `tools/context_health.py`: check state/handoff/generated context size hygiene.
- `tools/architecture_reality_audit.py`: run the recurring Architecture-to-Reality Audit every 5-10 completed tasks, before major architecture changes, and before major governance reviews; writes results to `artifacts/reports/`.
- `tools/update_context_summaries.py`: refresh `_SUMMARY.md` context maps.
- `tools/dry_run.py`: create validated dry-run reports.
- `tools/validate_dry_run.py`: validate dry-run reports.
- `tools/check_coherence.py`: check scaffold coherence.
- `tools/escalate.py`: create escalation records/questions.
- `tools/review_metrics.py`: turn metrics into improvement proposals.

## Verification

From the ProjectForge root:

```bash
python3 tools/check_coherence.py --project . --json
python3 tools/architecture_reality_audit.py --project . --json
uvx --from pytest --with pyyaml pytest tests -q
```

## MetaHarvest advisory loop

ProjectForge consumes MetaHarvest as an autonomous sibling EIP project at `/home/mkkto/srv/EIP/projects/MetaHarvest`. MetaHarvest is a librarian, reference system, evidence repository, and architectural advisory layer. ProjectForge validates the external provider interface and must not host a full MetaHarvest project tree.

MetaHarvest is consulted for architecture definition, major architecture changes, new subsystems, new agent roles, memory/context systems, orchestration, permissions, workflow redesign, scheduled architecture reviews, repeated implementation failures, and user-requested improvement scans. During new project creation, consult it when architectural uncertainty or relevant pattern evidence exists; simple projects should not be forced into unnecessary ceremony. It is not consulted for ordinary bug fixes, minor documentation edits, small utilities, simple test additions, or implementation work that does not alter architecture.

Every generated project receives lightweight architecture review and MetaHarvest placeholders under `architecture/`, including `architecture/architectureharvest/relevance_map.yaml`, recommendation/rejection trackers, and review history. MetaHarvest recommendations remain advisory: strong recommendations are allowed, but adoption remains project-local and implementation continues through normal project decisions, dry-runs, tests, and coherence checks. MetaHarvest may recommend that a project consider opening a task; it may not create that task automatically.

Adoption outcomes flow back into the external MetaHarvest provider's `adoption_log/` so the EIP ecosystem preserves local evidence about which external patterns actually helped, failed, or became stale.
