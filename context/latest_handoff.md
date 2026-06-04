# Latest Handoff

Updated: 2026-06-03T22:51:32Z
Agent: Hermes
Status: completed

## Goal

Add a central task-completion summary policy to ProjectForge and MacroForge so future agents update summaries efficiently when finishing tasks.

## What changed

ProjectForge now records task-completion summary behavior centrally instead of duplicating long instructions in every task.

Updated ProjectForge root:

- `AGENTS.md`
- `context/context_policy.yaml`

Updated generated-project template:

- `templates/_shared_project/AGENTS.md`
- `templates/_shared_project/context/context_policy.yaml`

Updated current MacroForge project:

- `workspace/projects/macroforge/AGENTS.md`
- `workspace/projects/macroforge/context/context_policy.yaml`

Updated Hermes procedural memory:

- local `projectforge` skill was patched to remember this convention.

## Policy now in force

Generated projects should carry a central `context/context_policy.yaml` section:

```yaml
task_completion:
  update_summaries: true
  summary_mode: affected_only
  require_summary_inspection: true
  require_final_verification_after_summary_updates: true
```

Agents completing tasks should update task/state/handoff, refresh affected `_SUMMARY.md` files where relevant, inspect refreshed summaries for stale curated sections such as `Active Work` / `Needs Attention`, and run final verification after governance/summary edits.

## Verification output

ProjectForge root:

```text
python3 tools/check_coherence.py --project . --json && uvx --from pytest --with pyyaml pytest tests -q

{
  "mode": "root",
  "blocks": [],
  "warnings": []
}
.....................................................                    [100%]
53 passed in 3.57s
```

MacroForge generated project:

```text
python3 tools/check_coherence.py --project . --json && PYTHONPATH=src uvx --from pytest --with pyyaml pytest tests -q

{
  "mode": "generated",
  "blocks": [],
  "warnings": []
}
......................                                                   [100%]
22 passed in 1.19s
```

## Remaining risks / notes

- This change is policy/config only; no deterministic `complete_task.py` helper was added yet.
- Existing ProjectForge git status includes older modified state/handoff files and untracked MacroForge reconstruction/deletion manifest files from prior work; no commit or push was performed.
- For MacroForge specifically, the current active implementation direction remains TASK-017 unless a newer session updates it.

## Next recommended task

If further hardening is desired, add a deterministic ProjectForge helper or checker for task completion, for example affected-summary refresh detection plus a coherence warning when completed tasks lack state/handoff/summary updates.
