# T-20260615-ecosystem-autonomy-doctrine-alignment

Status: completed
Task type: Doctrine and Schema Alignment Only
Project: ProjectForge
Started: 2026-06-15

## Objective

Align ProjectForge and ArchitectureHarvest doctrine with the accepted ecosystem-autonomy doctrine while avoiding restructuring, project creation, ArchitectureHarvest separation, MacroForge modification, automation, cross-project task creation, governance authority, or future-project implementation.

## Scope constraints

- Doctrine and schema/template alignment only.
- No ecosystem restructuring.
- No new projects.
- No ArchitectureHarvest split.
- No MacroForge modification.
- No automation or runtime behavior change.
- No cross-project task creation.
- No project governance authority introduced.
- Future projects remain context only.

## Planned/actual change areas

- Project autonomy, ownership, ecosystem awareness, anti-monolith, extraction, project-creation threshold, interface, recommendation persistence, registry, future ecosystem vision, and infrastructure doctrine.
- ArchitectureHarvest boundary language: hosted advisory subsystem, conceptually separable, not split.
- ArchitectureHarvest recommendation language: candidate task proposals, no automatic task creation.
- Recommendation schema v2 template and backward-compatible candidate template guidance.
- Future-review note for ecosystem-level decision registry and ArchitectureHarvest separation review.

## Validation

Pre-closeout validation:

- YAML/template validation: `uv run --with pyyaml python - <<'PY' ... yaml.safe_load(...) ... PY` parsed touched YAML policy/schema/template files successfully.
- Coherence: `python3 tools/check_coherence.py --project . --json` returned no blocks and one known stale generated `context/active_context.md` warning.
- Architecture reality audit: `python3 tools/architecture_reality_audit.py --project . --json` returned no blocks and no warnings.

Final post-closeout validation:

- YAML/template validation: touched YAML policy/schema/template files parsed/read successfully.
- `python3 tools/check_coherence.py --project . --json` returned no blocks and one known stale generated `context/active_context.md` warning.
- `python3 tools/architecture_reality_audit.py --project . --json` returned no blocks and no warnings; `completed_tasks_since_latest_audit` is 4.
- `git diff --check` passed.

## Outcome

Doctrine/schema alignment completed within scope. No ecosystem restructuring, new projects, ArchitectureHarvest split, MacroForge modification, automation, cross-project task creation, governance authority, or future-project functionality was performed.
