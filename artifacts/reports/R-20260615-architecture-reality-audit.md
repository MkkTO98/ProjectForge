# Architecture-to-Reality Audit

Date: 2026-06-15T21:19:34+00:00
Project: /home/mkkto/srv/projectforge
Mode: root
Latest previous audit: artifacts/reports/R-20260605-architecture-reality-audit.md
Completed tasks since latest audit: 10

## Scope

This audit checks documented architecture, governance rules, operating procedures, state artifacts, templates, automation, logging/context systems, and available implementation for drift.

## Categories

- architecture_vs_implementation
- state_files_vs_reality
- agent_instructions_vs_behavior
- logging_systems
- context_management_systems
- governance_processes
- automation_workflows
- templates_vs_generated_projects

## Drift types

- drift
- obsolete_documentation
- duplicated_systems
- unused_systems
- missing_implementation
- implementation_without_documentation
- documentation_without_implementation

## Blocks

- Category: governance_processes
  Drift type: drift
  Finding: 10 completed task(s) since last Architecture-to-Reality Audit
  Remediation: Run and record an Architecture-to-Reality Audit before continuing major work.

## Warnings

None.

## Remediation workflow

1. Fix blocks before major architecture/governance work continues.
2. Convert durable policy or architecture changes into decision artifacts.
3. Update implementation, templates, docs, and state together so future projects inherit the correction.
4. Refresh affected folder summaries and latest handoff.
5. Rerun `tools/architecture_reality_audit.py`, `tools/check_coherence.py`, and relevant tests.
