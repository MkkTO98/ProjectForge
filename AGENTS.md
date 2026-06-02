# ProjectForge Agent Instructions

ProjectForge is a Hermes-native project factory and governance scaffold. It creates and maintains AI-assistable projects with explicit state, decisions, tasks, run evidence, and safety boundaries.

## Required startup context

Before changing files, inspect the smallest sufficient set of authoritative project files:

1. `CONSTITUTION.md` — non-negotiable project rules.
2. `state/active_goal.md` and `state/project_state.md` — current truth and active direction.
3. Relevant `artifacts/decisions/` and `artifacts/tasks/` — durable choices and work contracts.
4. `context/context_policy.yaml` and folder `_SUMMARY.md` files before exploring large directories.
5. `context/latest_handoff.md` when present.

Do not rely on hidden chat memory when a file-backed artifact exists.

## Context and model architecture

ProjectForge is local-execution / cloud-governance. Local tools and local models should do implementation, refactoring, testing, debugging, summarization, indexing, retrieval, documentation updates, and routine development whenever reasonably possible. Cloud models are reserved for high-leverage governance: architecture review, strategic planning, project audits, gap analysis, redesign, consistency review, high ambiguity, repeated local failure, explicit user request, or safety-critical reasoning.

Context is summary-first and expands incrementally. Normal task context may include only project summaries, the active task file, relevant folder summaries, relevant decision records, explicitly retrieved source files, and a short recent handoff. Normal context must not include raw logs, full session JSONL files, entire previous conversations, whole-project file dumps, unrelated folders, large tool outputs, or generated artifacts unless explicitly relevant.

Use `tools/build_context.py` for explicit context bundles. It writes `context/context_audit.json` and `context/context_audit.md` with estimated tokens, included/excluded files and reasons, raw-log exclusion status, summary usage, context mode, review justification, and model selection reason. Cloud/Codex use requires this audit. Project-wide reviews are allowed and expected when justified; use `--context-mode project_wide_review --review-justification ...` instead of forcing every cloud task into the compact governance budget.

Raw logs remain saved for audit/debugging, but agents may read them only for failure investigation, forensic, or incident work when summaries are insufficient.

## Hermes-native operating model

Hermes is the primary operator. Use Hermes tools directly for file inspection, targeted edits, tests, git inspection, subagent delegation, session search, and cron scheduling when that is the safest and clearest path.

ProjectForge tools remain project-local helpers:

- `tools/new_project.py` renders scaffolds from templates and recorded answers.
- `tools/build_context.py` builds explicit context bundles.
- `tools/dry_run.py` and `tools/validate_dry_run.py` document and validate risky changes.
- `tools/check_coherence.py` verifies ProjectForge invariants.
- `tools/update_context_summaries.py` refreshes folder summaries.
- `tools/run.py` is an audit/policy wrapper for manual or non-Hermes command execution; do not force every Hermes file/tool operation through it.

## Project creation rule

When creating a project, do not default to the terminal questionnaire. Use Hermes-led adaptive interrogation:

1. Load the `projectforge` Hermes skill if available.
2. Treat `config/setup_questionnaire.yaml` as a coverage map, not a rigid script.
3. Ask one focused topic at a time and explain why the question matters when useful.
4. Reuse known context before asking; ask only blocking questions.
5. Stop when `config/sufficiency_policy.yaml` says bootstrap is operationally sufficient.
6. Write accepted/deferred answers to a JSON file or decision artifacts.
7. Run `tools/new_project.py` noninteractively with `--answers-json` when rendering is needed.
8. Verify the generated project with tests/coherence and summarize real outputs.

## Safety and governance

- Do not change architecture, permissions, model routing, templates, or scope silently. Create or update a decision artifact when the change is durable.
- Human approval is required for secrets, destructive operations, production data, money/billing risk, and git push.
- Prefer small, reversible changes with verification.
- Run relevant tests before summarizing code changes.

## Completion discipline

Before reporting done:

1. Run the narrowest meaningful tests/checks.
2. Run `python3 tools/check_coherence.py --project . --json` for ProjectForge-level changes when possible.
3. Update state, task, handoff, and summaries when the change affects future agents.
4. Report what changed, why, where, and the exact verification output.
