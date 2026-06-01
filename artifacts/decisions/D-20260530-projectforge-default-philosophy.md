# Decision: ProjectForge Default Philosophy

Date: 2026-05-30
Status: Accepted

## Decision
ProjectForge defaults to an AI-first engineering environment where the human designs the architecture through extensive initial questions, and agents execute inside explicit state, logging, git, and permission boundaries.

## Rationale
This matches the intended use: reusable project initialization for future AI-assisted projects while avoiding uncontrolled autonomous drift.

## Consequences
- All generated projects include state, artifacts, logs, permissions, agents, skills, and templates.
- Durable architectural choices must be recorded in `artifacts/decisions/`.
- Agents may ask clarifying questions later when deferred specifications become relevant.
