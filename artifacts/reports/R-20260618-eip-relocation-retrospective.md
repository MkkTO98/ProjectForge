# EIP Relocation Retrospective

Date: 2026-06-18T08:03:08Z
Scope: ProjectForge, MacroForge, MetaHarvest relocation into `/home/mkkto/srv/EIP/projects/`
Status: relocation and cleanup complete

## Purpose

Capture relocation lessons learned with emphasis on reducing future token consumption while preserving safety, traceability, and operational confidence.

## 1. What went well

- Copy-first relocation was the right safety posture. It allowed validation from the destination before treating the old tree as disposable.
- Keeping ProjectForge, MacroForge, and MetaHarvest as explicit roots made validation concrete and prevented abstract ecosystem redesign from creeping into the task.
- The most useful state surfaces were the small current-state files, latest handoffs, project registries, and source registries.
- Recovery and coherence tools provided a fast, bounded signal that active workflows still resolved after path updates.
- Running tests from the relocated roots gave high confidence that runtime assumptions were not still bound to the legacy location.
- MetaHarvest source-cache migration was safer after separating canonical source identity from replaceable local clone paths.
- Cleanup improved the final state without deleting historical evidence: obsolete duplicate project copies and stale generated context were archived, not destroyed.

## 2. What caused unnecessary token expenditure

- Repeated architecture/governance/extraction-readiness reviews after the blockers were already known consumed the most avoidable reasoning budget.
- Broad repository scans produced many historical path references that were not operational defects.
- Treating every legacy path reference as potentially active created noise; reports, decisions, handoffs, reconstruction artifacts, and evidence manifests should be classified historical early.
- Generated context bundles and nested obsolete project copies created false positives until they were explicitly classified as stale or obsolete.
- Re-validating already-settled design questions blurred implementation work with review work.
- Large tool outputs from full path-reference scans were less useful than targeted active-surface checks.

## 3. Checks that were actually valuable

- Exact root existence checks for all active destination projects.
- Registry/config path checks:
  - `projectforge.yaml`
  - `workspace/projects_registry.yaml`
  - `workspace/workspace_policy.yaml`
  - `workspace_config.yaml`
  - `source_registry.yaml`
- Recovery checks from relocated roots:
  - ProjectForge recovery
  - MacroForge recovery
- Coherence checks from relocated roots:
  - ProjectForge coherence
  - MacroForge coherence
- Full project tests from relocated roots:
  - ProjectForge tests
  - MacroForge tests
- MetaHarvest registry integrity:
  - YAML parse
  - required interface file presence
  - no active legacy source-cache paths
  - local cache paths exist
  - git HEADs match recorded analyzed/cloned commits
- Active-surface path-reference checks, limited to startup, recovery, validation, registry/configuration, docs, tests, and tools.
- Duplicate project marker search, followed by classification as active, compatibility, obsolete, template, or historical.

## 4. Reviews that were redundant

- Re-running architecture review after relocation blockers were already identified.
- Re-running governance review when the task was path/config relocation and validation.
- Re-running extraction-readiness review after MetaHarvest had already been extracted and validated.
- Re-assessing destination design after the target paths were fixed.
- Re-analyzing historical evidence artifacts solely because they contained old absolute paths.

## 5. Validation steps that should become standard for future relocations

1. Establish immutable relocation scope:
   - source root
   - destination root
   - project roots
   - explicit non-goals

2. Perform copy-first relocation:
   - preserve source until destination passes validation
   - do not delete or archive during the first copy/validation pass

3. Update only active path surfaces:
   - startup files
   - recovery files
   - registry/configuration files
   - validation/test surfaces
   - active operator documentation

4. Classify path references before editing:
   - active
   - compatibility
   - obsolete
   - historical/evidence
   - template/example

5. Validate from destination roots:
   - recovery
   - coherence
   - tests
   - registry integrity
   - provider/integration paths

6. Confirm legacy-root independence:
   - active configs do not point to source root
   - runtime/test/recovery passes without source-root dependency
   - source caches, if needed, are copied or intentionally externalized

7. Cleanup only after active validation:
   - archive obsolete project copies
   - archive stale generated context bundles
   - preserve decisions, reports, evidence, handoffs, and historical records

8. Only then classify the old source root for deletion:
   - exact-path guard
   - destination roots exist
   - no active dependencies remain
   - deletion requires explicit destructive-action approval

## 6. Minimal relocation playbook

### Phase 0 — Freeze scope

- Record source and destination paths.
- State non-goals: no architecture review, no governance review, no redesign, no feature work.
- Load only current handoff/state/config files needed to execute relocation.

### Phase 1 — Copy first

- Copy project directories to destination.
- Preserve file contents and permissions as far as practical.
- Do not delete source.

### Phase 2 — Active path update

Update only active surfaces:

- project root config
- workspace registry/policy
- generated project config
- provider/source registry
- startup/handoff/current-state files if they contain active paths
- tests or tools with hardcoded active paths
- operator docs that instruct current workflow

Do not rewrite historical reports, decisions, evidence, or reconstruction artifacts just because they contain old paths.

### Phase 3 — Destination validation

Run from destination roots:

- Project recovery
- Project coherence
- Project tests
- Provider/source registry validation
- Retrieval/index YAML validation if the project has retrieval metadata

### Phase 4 — Reference classification

Search for old paths, but classify before editing:

- Active references: update.
- Compatibility references: keep or align with canonical copy.
- Obsolete duplicate project copies: archive.
- Historical/evidence references: keep.
- Template/example references: keep unless misleading.

### Phase 5 — Cleanup

- Archive obsolete duplicate project copies.
- Archive stale generated context bundles.
- Do not delete historical/evidence artifacts.
- Re-run destination validation.

### Phase 6 — Legacy-root disposition

- If destination validation passes and no active dependencies remain, classify source root as safe to delete.
- Delete only with explicit approval and exact-path guards.

## Bottom line

Future relocations should be implementation-first and classification-driven. The safest low-token approach is not to prove the whole architecture again, but to update active path surfaces, validate from destination roots, classify residual references, archive obsolete duplicates, and preserve historical evidence unchanged.
