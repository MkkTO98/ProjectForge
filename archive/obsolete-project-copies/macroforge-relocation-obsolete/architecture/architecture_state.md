# Architecture State

Status: active

This lightweight generated-project architecture state file connects MacroForge to ProjectForge's current ArchitectureHarvest integration contract.

Authoritative current architecture remains summarized in `state/architecture.md`.

## Current ArchitectureHarvest integration

- First MacroForge ArchitectureHarvest review: `/home/mkkto/srv/projectforge/ArchitectureHarvest/reviews/R-20260608-macroforge-first-architectureharvest-review.md`
- Implemented narrow recommendation: `MF-AH-REV-001`
- Local manifest registry: `artifacts/manifests/canonical_assets.json`

## Boundary

MacroForge keeps the implementation file-backed and minimal. This does not adopt dbt, Dagster, an orchestration runtime, a generalized ingestion framework, or new database migrations.
