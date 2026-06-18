# ProjectForge Agent Instructions

ProjectForge is a Hermes-native project factory, reusable framework, and governance scaffold. It creates AI-assistable projects with explicit state, decisions, tasks, run evidence, and safety boundaries.

ProjectForge improves itself and future inheritance; it does not own, manage, or silently mutate instantiated projects after creation. Existing projects decide whether to adopt ProjectForge improvements through their own governance.


ProjectForge participates in an autonomy-first ecosystem. Projects may recommend, notify, expose interfaces, and provide context to each other, but they must not govern, directly modify, create tasks inside, or assume authority over other projects. Future projects are context only until explicitly approved.

## Required startup context

Before changing files, inspect the smallest sufficient set of authoritative project files:

1. `CONSTITUTION.md` — non-negotiable project rules.
2. Priority 1 current-state context: `state/active_goal.md`, `state/project_state.md`, `state/architecture.md`, and `context/latest_handoff.md` when present.
3. For fast recovery or uncertain state, run `python3 tools/recover_session.py --project . --json`; use its bounded output to identify the active task, recent decisions, blockers, next actions, and resume procedure before expanding context.
4. Priority 2 task-scoped context only when relevant: active task files, relevant decision records, and relevant folder `_SUMMARY.md` files.
5. Priority 3 broader docs/reports/design notes/roadmaps/historical artifacts only after narrower context is insufficient or a justified project-wide review requires it.
6. `context/context_policy.yaml` when work is nontrivial or context/model routing is in scope.

Repository-wide exploration is not default startup behavior. Expand context incrementally and state why broader context is needed.

Do not rely on hidden chat memory when a file-backed artifact exists.

## Context and model architecture

ProjectForge is local-execution / cloud-governance. Local tools and local models should do implementation, refactoring, testing, debugging, summarization, indexing, retrieval, documentation updates, and routine development whenever reasonably possible. Cloud models are reserved for high-leverage governance: architecture review, strategic planning, project audits, gap analysis, redesign, consistency review, high ambiguity, repeated local failure, explicit user request, or safety-critical reasoning.

Context is summary-first and expands incrementally. Primary state files are current-state pointers, not append-only ledgers; keep `state/active_goal.md`, `state/project_state.md`, and `state/architecture.md` concise, and move long history to task artifacts, handoffs, reports, or derived logs. Normal task context may include only project summaries, the active task file, relevant folder summaries, relevant decision records, explicitly retrieved source files, and a short recent handoff. Normal context must not include raw logs, full session JSONL files, entire previous conversations, whole-project file dumps, unrelated folders, large tool outputs, or generated artifacts unless explicitly relevant.

Use `tools/build_context.py` for explicit context bundles. It writes generated outputs (`context/active_context.md`, `context/context_manifest.json`, `context/context_audit.json`, and `context/context_audit.md`) for the current task/model target. Do not treat stale `context/active_context.md` as mandatory startup context; rebuild a task-specific bundle when needed. Cloud/Codex use requires a context audit. Project-wide reviews are allowed and expected when justified; use `--context-mode project_wide_review --review-justification ...` instead of forcing every cloud task into the compact governance budget.

Run `tools/context_health.py --project . --json` or coherence to catch oversized state, handoff, and generated context artifacts before they become token sinks.

Raw logs remain saved for audit/debugging, but agents may read them only for failure investigation, forensic, or incident work when summaries are insufficient.

## Architecture-to-Reality Audit

Run a formal Architecture-to-Reality Audit every 5-10 completed tasks, before major architecture changes, and before major governance reviews:

```bash
python3 tools/architecture_reality_audit.py --project . --write-report
```

The audit compares architecture vs implementation, state files vs reality, agent instructions vs behavior, logging systems, context-management systems, governance processes, automation workflows, and templates vs generated projects. It should identify drift, obsolete documentation, duplicated or unused systems, missing implementations, implementation without documentation, and documentation without implementation. Record results under `artifacts/reports/`, convert durable corrections into decision artifacts when policy/architecture/scope/templates change, remediate blocks before continuing major governance work, refresh affected summaries, and rerun audit/coherence/tests.

## Hermes-native operating model

Hermes is the primary operator. Use Hermes tools directly for file inspection, targeted edits, tests, git inspection, subagent delegation, session search, and cron scheduling when that is the safest and clearest path.

ProjectForge tools remain project-local helpers:

- `tools/new_project.py` renders scaffolds from templates and recorded answers.
- `tools/build_context.py` builds explicit context bundles.
- `tools/architecture_reality_audit.py` checks architecture/governance/state/template drift.
- `tools/dry_run.py` and `tools/validate_dry_run.py` document and validate risky changes.
- `tools/check_coherence.py` verifies ProjectForge invariants.
- `tools/update_context_summaries.py` refreshes folder summaries.
- `tools/run.py` is an audit/policy wrapper for manual or non-Hermes command execution; do not force every Hermes file/tool operation through it.

## Project creation rule

When creating a project, do not default to the terminal questionnaire. Use Hermes-led adaptive discovery (the historical "Hermes-led adaptive interrogation" entrypoint), with the questionnaire as a coverage map rather than a script. The goal is clarity of purpose, not maximum questioning. Classify questions as FOUNDATIONAL, ARCHITECTURAL, IMPLEMENTATION, or PREFERENCE. Foundational questions should explain why they matter, what depends on them, and why they should be resolved now; implementation details should be deferred when possible.

1. Load the `projectforge` Hermes skill if available.
2. Treat `config/setup_questionnaire.yaml` as a coverage map, not a rigid script.
3. Ask one focused topic at a time and explain why the question matters when useful.
4. Reuse known context before asking; ask only blocking questions.
5. Stop when `config/sufficiency_policy.yaml` says bootstrap is operationally sufficient.
6. Write accepted/deferred answers to a JSON file or decision artifacts.
7. Run `tools/new_project.py` noninteractively with `--answers-json` when rendering is needed.
8. Verify the generated project with tests/coherence and summarize real outputs.

## Safety and governance

- Classify governance-sensitive work with the ProjectForge permission ladder before implementation when scope, architecture, purpose, doctrine, or ecosystem boundaries may be affected:
  - L1 Operational: routine work inside approved scope; proceed with normal verification.
  - L2 Architectural: project-local architecture change; explicit approval required before implementation.
  - L3 Strategic: scope expansion, ecosystem interaction, extraction recommendations, major governance additions, or new long-term responsibilities; explicit approval and a structured `GOVERNANCE_WARNING` block required before implementation.
  - L4 Foundational: purpose, doctrine, constitution, project creation/split/merge, ecosystem ownership, or authority-boundary change; stop implementation and show a `FOUNDATIONAL_GOVERNANCE_WARNING` block until explicit foundational approval is received.
- A project's approved purpose is protected. Hermes may identify tensions and recommend expansion or extraction, but must not silently expand, redefine, substantially reinterpret, or absorb responsibilities that materially alter project identity.
- Do not change architecture, permissions, model routing, templates, scope, or framework-level doctrine silently. Explicitly name framework changes when they affect inheritance, templates, governance, questioning, artifact standards, handoff standards, delegation/worker infrastructure, or MetaHarvest / MetaHarvest doctrine. Create or update a decision artifact when the change is durable.
- For L3 and L4 proposals, include a concise explanation, explicit impact statement, explicit risk statement, and explicit approval request so the decision remains visible when copied into another tool.
- Confidence and priority never imply authority. Confidence describes belief; priority describes perceived value or sequencing importance; authority comes only from project-local governance and required approval.
- Human approval is required for secrets, destructive operations, production data, money/billing risk, git push, and all L2/L3/L4 implementation gates.
- Prefer small, reversible changes with verification.
- Run relevant tests before summarizing code changes.

## Completion discipline

The command `Perform standard ProjectForge closeout. Follow the continuity framework. Then stop.` is sufficient for a normal safe closeout. Follow `recovery/continuity_framework.md`; do not require the user to restate task/state/handoff/summary/verification steps.

Before reporting done:

1. Run the narrowest meaningful tests/checks.
2. Run `python3 tools/check_coherence.py --project . --json` for ProjectForge-level changes when possible.
3. Update state, task, handoff, and affected folder summaries when the change affects future agents.
4. Prefer affected-only summary refresh. After refreshing, inspect affected `_SUMMARY.md` files for stale curated sections such as `Active Work`, `Needs Attention`, or task status notes; patch them manually when the summary tool only updated generated inventory blocks.
5. Near token, tool, time, or quota exhaustion, continuity comes first: update the active task status, blockers/open questions, next actions, and `context/latest_handoff.md` with an exact resume command before optional cleanup or narrative polish.
6. Run final verification after governance/summary edits, not only before them.
7. Report what changed, why, where, and the exact verification output.

## MetaHarvest / MetaHarvest advisory service

MetaHarvest is an autonomous sibling EIP project at `/home/mkkto/srv/EIP/projects/MetaHarvest`. ProjectForge consumes it through the configured external provider interface; ProjectForge must not host a full MetaHarvest project tree. The historical in-tree copy has been removed, and the `architecture/architectureharvest/` generated-project path remains only a compatibility path.

MetaHarvest is ProjectForge's external advisory knowledge provider: a librarian, reference system, evidence repository, and advisory knowledge system. It discovers, preserves, organizes, analyzes, and recommends reusable non-domain knowledge including architecture patterns, interface patterns, shared concepts, shared vocabulary, shared methodologies, decision patterns, governance patterns, heuristics, anti-patterns, and failure patterns.

Consult MetaHarvest during: architecture definition, major architecture modifications, new subsystem introduction, new agent-role creation, memory/context system design, orchestration design, permission system design, workflow redesign, scheduled architecture reviews, repeated implementation failures, user-requested improvement scans, and reviews of reusable non-domain concepts, vocabulary, methodologies, decision patterns, governance patterns, or heuristics. During new project creation, consult it when architectural uncertainty or relevant pattern evidence exists; do not force simple projects into unnecessary ceremony.

Do not consult MetaHarvest for: bug fixes, minor documentation edits, test additions, small utilities, domain analysis, or implementation work that does not alter architecture or reusable methodology.

MetaHarvest remains non-domain. It may preserve reusable methods or patterns discovered while working on domain projects, but domain conclusions such as GDP analysis, inflation analysis, energy-market knowledge, macroeconomic conclusions, investment theses, and company research belong to domain projects.

MetaHarvest produces recommendations, candidate task proposals, decision inputs, rejection records, and adoption outcome records. Strong recommendations are allowed, but adoption remains project-local. It may recommend that a project consider opening a task, but it must not create tasks inside another project, decide adoption, enforce standards, implement changes directly, modify target projects, force migration, or bypass normal ProjectForge approval, dry-run, testing, and coherence gates. When consulting it, start with the external provider's `retrieval/problem_catalog.yaml`, then `retrieval_index.yaml`, synthesized patterns, contradictions, adoption outcomes, and target relevance maps before reading deep project/component reports. Recommendations must distinguish generic evidence from ProjectForge ecosystem outcomes. When a project adopts/rejects/modifies/removes a MetaHarvest pattern, record the outcome in that project's `architecture/architectureharvest/` files and, when broadly useful, mirror the lesson into the external MetaHarvest provider's `adoption_log/`.
