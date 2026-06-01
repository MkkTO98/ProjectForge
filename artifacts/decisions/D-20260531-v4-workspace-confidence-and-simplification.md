# Decision: v4 Workspace, Confidence, Memory, and Knowledge Simplification

Date: 2026-05-31
Status: Accepted
Severity: L2

## Decision
ProjectForge v4 adds a workspace layer, confidence scoring, memory retention policy, invariant tests, and simplifies the knowledge graph to components and dependencies only.

## Reason
The workspace layer supports future interlinked projects. Confidence scoring makes uncertainty explicit and supports Codex-before-human escalation. Memory retention prevents context rot. Invariant tests protect design rules. The knowledge graph is intentionally simplified to avoid stale over-engineering.

## Consequence
Future generated projects inherit a broader but still file-readable governance structure. More sophisticated graph databases, dashboards, or autonomous schedulers remain deferred.
