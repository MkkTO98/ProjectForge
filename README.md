# ProjectForge v6

ProjectForge is a reusable, Hermes-native project initializer and governance scaffold for agent-supported projects. It creates projects with explicit state, decisions, tasks, logs, summaries, safety policy, and verification hooks so future Hermes sessions and humans can resume work without reconstructing context from chat.

ProjectForge is not MacroForge. ProjectForge is the factory/governance system; MacroForge is one generated or managed project.

## Primary operating model

```text
Hermes-led adaptive interview -> sufficiency policy -> captured answers -> scaffold render -> decisions/tasks/state -> verification -> summaries/handoff
```

Hermes should lead project creation. The static questionnaire in `config/setup_questionnaire.yaml` is a coverage map, not the user-facing script. `tools/new_project.py` remains the deterministic scaffold renderer and should normally be called with `--answers-json` after Hermes has gathered enough information.

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

ProjectForge context is built in this order:

1. Read project summary/current state.
2. Read `context/latest_handoff.md` if present.
3. Identify relevant folders from the task and explicitly requested files.
4. Read only those folders' `_SUMMARY.md` files.
5. Read relevant decision records and the active task file.
6. Retrieve explicit source files only when summaries are insufficient.
7. Read raw logs only for `failure_investigation`, `forensic`, or `incident` task types.

Normal task context may include project summary, active task file, relevant folder summaries, relevant decision records, explicitly retrieved source files, and a short handoff. It must not include raw logs, previous full conversations, full session JSONL files, whole-project dumps, unrelated folders, large tool outputs, or generated artifacts unless explicitly relevant.

Build and inspect context with:

```bash
python3 tools/build_context.py --project . --task "describe task" --folders src,tests --files src/example.py --task-file artifacts/tasks/TASK-001-example.md
python3 tools/build_context.py --project . --task "cloud review" --model-target cloud --model-selected codex_supervisor --model-reason "architecture_decision" --folders src --files src/example.py
```

The builder writes:

- `context/active_context.md`: compact bundle.
- `context/context_manifest.json`: files used and estimated tokens.
- `context/context_audit.json`: machine-readable audit.
- `context/context_audit.md`: human-readable audit with included/excluded files and reasons.

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
uvx --from pytest --with pyyaml pytest tests -q
```
