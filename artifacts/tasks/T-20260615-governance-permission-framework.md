# T-20260615 Governance Permission Framework

Date: 2026-06-15
Status: completed
Scope: bounded governance architecture review and implementation

## Goal

Create a lightweight permission and escalation framework that protects project purposes, ecosystem architecture, decision visibility, and recommendation authority boundaries without adding friction to routine work.

## Explicit non-actions

This task did not authorize or perform:

- commits;
- staging;
- project creation;
- MetaHarvest purpose changes;
- MacroForge purpose changes;
- EIP purpose changes;
- ecosystem infrastructure implementation;
- automation implementation;
- authority delegation;
- mandatory standards outside approved ProjectForge governance doctrine.

## Implemented

- Added four-level permission ladder doctrine to `CONSTITUTION.md`.
- Added project purpose protection doctrine to `CONSTITUTION.md`.
- Added L3/L4 structured governance warning block doctrine to `CONSTITUTION.md`.
- Added recommendation confidence/priority/authority separation doctrine to `CONSTITUTION.md`.
- Added decimal guidance for confidence/priority/likelihood/uncertainty to `CONSTITUTION.md`.
- Expanded recommendation persistence doctrine with rejection-memory requirements.
- Updated `AGENTS.md` with operational instructions for permission classification and warning blocks.
- Updated `state/architecture.md` and `state/project_state.md` with concise current-state pointers.
- Created decision artifact `artifacts/decisions/D-20260615-governance-permission-framework.md`.
- Created review artifact `artifacts/reports/R-20260615-governance-permission-framework-review.md`.

## Review-only conclusions

- Normalized task-size scales may be useful later but should not be standardized now.
- A foundational-decision registry may be useful later but overlaps existing decision artifacts and should not be implemented now.

## Verification

Final verification should include:

- `git diff --check`
- `python3 tools/check_coherence.py --project . --json`
- `python3 tools/architecture_reality_audit.py --project . --json`
- YAML/schema checks only if YAML templates or schemas were modified.
