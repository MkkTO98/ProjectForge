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
- Capability failures escalate current Hermes session -> stronger local model if configured -> Codex/premium -> human.

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
