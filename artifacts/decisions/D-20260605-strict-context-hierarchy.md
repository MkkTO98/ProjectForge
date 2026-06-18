# Decision: Strict context hierarchy and generated-bundle health enforcement

Date: 2026-06-05
Status: Accepted
Severity: L2

## Context

A MacroForge context-efficiency audit asked ProjectForge to distinguish already-implemented context controls from missing controls, then implement only gaps. Existing ProjectForge mechanisms already supported summary-first context, raw-log exclusion, generated context audits, project-wide review justification during bundle creation, and generated-project template inheritance.

The remaining weakness was that the exact Priority 1/2/3 loading hierarchy and after-the-fact generated-bundle health checks were not explicit enough in policy, templates, and tests.

## Decision

ProjectForge will enforce this hierarchy for root and generated projects:

1. Priority 1: `state/active_goal.md`, `state/project_state.md`, `state/architecture.md`, and `context/latest_handoff.md`.
2. Priority 2: active task files, relevant decision records, and relevant folder summaries.
3. Priority 3: broader documentation, reports, design notes, roadmap files, and historical artifacts only after justified expansion.

Generated context bundles remain task/model-target outputs, not startup context. `context_health.py` will warn on stale generated bundles and block already-generated project-wide-review audits that lack review justification or include raw logs outside forensic/incident intent.

## Consequences

- Normal context bundles start smaller and more predictably.
- `context/project_summary.md` remains supported, but as broader Priority 3 context by default rather than mandatory normal context.
- Project-wide reviews remain available but are exceptional and auditable.
- Existing projects remain compatible; missing new policy fields fall back to tool defaults.

## Verification

See `artifacts/reports/R-20260605-context-management-audit.md` and final session verification output.
