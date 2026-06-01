# Decision: Deferred Specification Policy

Date: 2026-05-30
Status: Accepted

## Decision
ProjectForge supports deferred specification by default. If a question cannot be answered at setup time, the initializer records it as a decision artifact with status `Deferred`.

## Rules
- Deferred specifications are not failures.
- Deferred specifications must be explicit.
- Agents must consult existing decisions before asking.
- If a deferred specification becomes blocking, the agent must create a question in `question_queue/pending/`.

## Rationale
Some project details only become clear during implementation. This avoids both over-questioning during setup and silent invention later.
