# D-20260615 Governance Permission Framework

Date: 2026-06-15
Status: accepted
Decision type: governance doctrine
Scope: ProjectForge governance, permission levels, escalation, warning blocks, recommendation authority, and purpose protection

## Context

Recent governance work established project autonomy, scope extraction doctrine, project creation thresholds, MetaHarvest's advisory-only role, recommendation persistence, and ownership-by-purpose guidance.

The remaining gap was decision visibility: agents need a lightweight way to distinguish routine work from architectural, strategic, and foundational decisions.

## Decision

ProjectForge adopts a four-level permission ladder:

- L1 Operational: routine implementation inside approved scope; no special escalation.
- L2 Architectural: project-local architecture change; explicit approval required before implementation.
- L3 Strategic: scope expansion, ecosystem interaction, cross-project implications, extraction recommendations, or new long-term responsibilities; explicit approval and structured warning block required.
- L4 Foundational: purpose, doctrine, constitutional, ecosystem ownership, project creation/split/merge, or authority-boundary changes; implementation must stop until explicit foundational approval is received and a highest-visibility warning block is shown.

Project purpose is protected. Hermes may identify tensions and recommend expansion or extraction, but may not silently expand, redefine, or substantially reinterpret a project's purpose. Purpose changes require L4 approval.

L3 and L4 proposals must include a structured warning block with permission level, category, project/scope, decision, impact, risk, and required approval.

Confidence and priority do not imply authority. Confidence describes belief; priority describes perceived value or sequencing importance; authority comes only from project-local governance and explicit approval where required.

Rejected recommendations remain discoverable with rationale and context so the ecosystem preserves negative knowledge and avoids repeated rediscovery.

## Non-decisions

This decision does not:

- create projects;
- implement ecosystem infrastructure;
- delegate authority;
- automate approvals;
- modify MetaHarvest, MacroForge, or EIP purpose;
- create mandatory standards outside ProjectForge governance doctrine;
- implement new schemas.

## Rationale

The permission ladder protects project purposes and ecosystem architecture while avoiding friction for routine work. It helps humans allocate attention to high-impact decisions and makes governance risk visible even when proposals are copied across tools or skimmed quickly.

## Consequences

Agents should classify high-impact work before implementation and stop or request approval at the appropriate level.

Routine L1 work remains lightweight.

L2, L3, and L4 work require increasing visibility and approval discipline.

## Related artifacts

- `CONSTITUTION.md`
- `AGENTS.md`
- `state/architecture.md`
- `artifacts/reports/R-20260615-governance-permission-framework-review.md`
- `artifacts/reports/R-20260615-soft-governance-risk-future-review-note.md`
