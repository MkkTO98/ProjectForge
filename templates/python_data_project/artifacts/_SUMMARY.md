# Folder Summary: artifacts

Artifact role: durable governance history root.

## Purpose
This folder stores project-owned durable governance history for task, decision, report, and handoff accountability records. It is not current-state startup context and not a project-management database. Historical artifacts should not be rewritten merely to make history look clean; amend or supersede them instead.

## Governance artifact responsibilities
- `tasks/` — durable records of substantive work, status, outcome, and links to decisions/reports/handoffs.
- `decisions/` — accepted, rejected, deferred, or superseded choices with rationale, alternatives, consequences, and status.
- `reports/` — review, audit, architecture-to-reality, investigation, or implementation findings.
- `handoffs/` — durable handoff snapshots when more history is needed than `context/latest_handoff.md` should carry.

## Rules
- Current state belongs in `state/` and `context/latest_handoff.md`; long history belongs here.
- Historical artifacts should not be rewritten merely to make history look clean. Amend or supersede them instead.
- Advisory recommendations, ideas, and review notes do not automatically become tasks.
