# Decision: Recurring Architecture-to-Reality Audit

Date: 2026-06-05
Status: Accepted

## Context

ProjectForge already had invariant-oriented coherence checks and context-health checks, but long-running projects can still drift when documented architecture, governance rules, operating procedures, state artifacts, templates, and implementation evolve at different speeds.

## Decision

ProjectForge projects will use a formal Architecture-to-Reality Audit process.

Cadence and triggers:

- every 5-10 completed tasks;
- before major architecture changes;
- before major governance reviews.

The audit is run with:

```bash
python3 tools/architecture_reality_audit.py --project . --write-report
```

Results are recorded under:

```txt
artifacts/reports/R-YYYYMMDD-architecture-reality-audit.md
```

## Scope

The audit covers:

- architecture vs implementation;
- state files vs reality;
- agent instructions vs behavior;
- logging systems;
- context-management systems;
- governance processes;
- automation workflows;
- templates vs generated projects.

It should identify:

- drift;
- obsolete documentation;
- duplicated systems;
- unused systems;
- missing implementations;
- implementation without documentation;
- documentation without implementation.

## Consequences

- `tools/architecture_reality_audit.py` becomes part of root and generated-project tooling.
- Periodic orchestrator hygiene runs the audit.
- Major architecture/governance work should not proceed past audit blocks.
- Durable remediation that changes policy, architecture, scope, permissions, model routing, templates, or operating procedure requires a decision artifact.
- Future generated projects inherit the audit process through shared templates.
