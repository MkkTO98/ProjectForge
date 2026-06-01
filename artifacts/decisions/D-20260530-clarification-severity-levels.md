# Decision: Clarification Severity Levels

Date: 2026-05-30
Status: Accepted

## Decision
ProjectForge uses four clarification severity levels.

## Levels

### L1 — Silent autonomy
Agent may proceed without asking. Used for low-risk implementation details.

### L2 — Batched clarification
Agent may continue if safe but should record a question for later review.

### L3 — Blocking clarification
Agent must pause and ask before proceeding.

### L4 — Emergency stop
Agent must stop execution. Used for destructive actions, secrets, irreversible operations, or unsafe ambiguity.

## Rationale
Not all questions deserve interruption. A severity model preserves momentum while keeping dangerous ambiguity under control.
