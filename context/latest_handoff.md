# Latest Handoff

Updated: 2026-06-18
Agent: Hermes
Status: EIP relocation, cleanup, validation, and retrospective complete

## Current EIP locations

- ProjectForge: `/home/mkkto/srv/EIP/projects/ProjectForge`
- MacroForge: `/home/mkkto/srv/EIP/projects/MacroForge`
- MetaHarvest: `/home/mkkto/srv/EIP/projects/MetaHarvest`

## Current outcome

ProjectForge, MacroForge, and MetaHarvest operate from their EIP locations. Core recovery, coherence, and test workflows no longer require `/home/mkkto/srv/projectforge`.

MetaHarvest source-cache paths were migrated from the legacy root to:

```text
/home/mkkto/srv/EIP/projects/ProjectForge/external_sources
```

MetaHarvest `source_registry.yaml` points analyzed source `local_path` entries at the EIP cache root, and source-cache git HEADs matched recorded analyzed commits during final validation.

## Cleanup completed

- Removed obsolete nested MacroForge copy from ProjectForge after confirming current MacroForge operates at `/home/mkkto/srv/EIP/projects/MacroForge`.
- Relocation evidence remains in:
  - `/home/mkkto/srv/EIP/projects/ProjectForge/artifacts/reports/R-20260618-eip-relocation-retrospective.md`
  - `/home/mkkto/srv/EIP/recovery/backups/20260618_090131`
- Archived stale generated ProjectForge context bundle from:
  - `/home/mkkto/srv/EIP/projects/ProjectForge/context/active_context.md`
- Archive destination:
  - `/home/mkkto/srv/EIP/projects/ProjectForge/context/archive/generated-context-bundles/20260618T075848Z/active_context.md`

## Retrospective

Durable relocation retrospective created:

```text
/home/mkkto/srv/EIP/projects/ProjectForge/artifacts/reports/R-20260618-eip-relocation-retrospective.md
```

Key lesson: future relocations should avoid repeated architecture/governance/extraction-readiness review once blockers are known; update active path surfaces, validate from destination roots, classify residual references, archive obsolete duplicates, and preserve historical evidence unchanged.

## Verification notes

Final cleanup validation passed:

- ProjectForge recovery: no blockers, no pending questions.
- ProjectForge coherence: no blocks.
- ProjectForge tests: passing.
- MacroForge recovery: no blockers, no pending questions.
- MacroForge coherence: no blocks.
- MacroForge tests: passing.
- MetaHarvest registry integrity: required files present, YAML parses, no registry errors, source git HEADs checked with no mismatches.

## Known remaining warnings

- ProjectForge `state/project_state.md` is approaching context-health limit.
- MacroForge `state/active_goal.md` is approaching context-health limit.
- Legacy root `/home/mkkto/srv/projectforge` may still exist outside active EIP operation; delete only with explicit destructive-action approval and exact-path guards.

## Resume instruction

No relocation work remains. Resume normal ProjectForge or MacroForge work only by explicit user request.
