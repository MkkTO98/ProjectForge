# MetaHarvest Doctrine Finalization and Extraction-Readiness Inventory

Date: 2026-06-15
Status: bounded doctrine-finalization and inventory task
Permission level: L4 doctrine guidance and inventory; no extraction or restructuring
Scope: extraction-readiness doctrine, EIP-root ownership doctrine, path-dependency inventory, artifact-ownership inventory, Evolution Interface, extraction-readiness report

## Explicit non-actions

This task did not authorize or perform:

- commits;
- staging;
- directory moves;
- directory renames;
- MetaHarvest extraction;
- project creation;
- ecosystem infrastructure implementation;
- contract implementation;
- service implementation;
- MacroForge modification;
- EII modification;
- repository restructuring.

## Governance visibility

FOUNDATIONAL_GOVERNANCE_WARNING
PERMISSION_LEVEL=L4
CATEGORY=FOUNDATIONAL
PROJECT=ProjectForge / MetaHarvest / EIP ecosystem
DECISION=Extraction-readiness doctrine and EIP-root ownership doctrine

Impact:
This task finalizes doctrine guidance that separates conceptual project extraction readiness from physical migration readiness and clarifies that no project owns the EIP root.

Risk:
Treating filesystem layout as governance authority, or treating operational migration readiness as conceptual architecture readiness, can either block necessary project autonomy or cause premature extraction.

Required approval:
STOP. This artifact is doctrine guidance and inventory only. Extraction, root adoption, directory movement, new projects, infrastructure, contracts, services, schemas, and restructuring remain prohibited without explicit foundational approval.
END_FOUNDATIONAL_GOVERNANCE_WARNING

## Executive conclusion

The extraction-readiness doctrine is sound and mature enough to become ProjectForge doctrine guidance, but not constitutional doctrine beyond the bounded ProjectForge constitution updates made here. The doctrine distinguishes conceptual readiness from physical migration readiness:

- conceptual extraction readiness depends primarily on purpose, ownership boundaries, authority boundaries, and interface boundaries;
- physical extraction additionally requires path inventory, artifact ownership inventory, compatibility planning, verification planning, rollback planning, and stable evidence references.

The EIP-root ownership doctrine is also sound: no project owns the EIP root. ProjectForge, MetaHarvest, MacroForge, EII, ResearchMemory, and future projects may participate in EIP, but root organization is ecosystem infrastructure, not project authority.

MetaHarvest is now conceptually ready only. It is not operationally ready for physical extraction.

## 1. Doctrine-finalization assessment

Assessment: sound and justified as doctrine guidance.

Refined doctrine wording implemented in bounded active guidance:

```text
Project extraction decisions should be evaluated in two separate layers.

Conceptual extraction readiness depends primarily on purpose, ownership boundaries, authority boundaries, and interface boundaries.

Physical extraction additionally requires path inventory, artifact ownership inventory, compatibility planning, verification planning, rollback planning, and evidence-reference stability.

Filesystem structure is evidence and migration constraint; it is not governance authority by itself.
```

Why this is useful:

- prevents filesystem structure from becoming pseudo-governance;
- prevents architecture readiness from being confused with migration readiness;
- avoids blocking valid autonomy on neutral-root adoption;
- prevents easy directory moves from masquerading as legitimate project extraction;
- forces physical extraction to be backed by inventory, compatibility, verification, rollback, and evidence strategy.

Edge cases:

- A responsibility can be conceptually ready but physically blocked by path/evidence compatibility.
- A responsibility can be physically easy to move but conceptually not a project.
- A hosted subsystem can remain hosted even after conceptual autonomy is accepted if migration risk is not worth paying yet.
- A future ecosystem root can simplify placement without becoming a prerequisite for extraction.

Doctrine update locations:

- `CONSTITUTION.md` — added Extraction-readiness doctrine.
- `README.md` — added concise active guidance.
- `state/architecture.md` — added current architecture guidance.

No constitutional promotion beyond ProjectForge doctrine guidance was performed.

## 2. EIP-root ownership assessment

Assessment: sound and justified as doctrine guidance.

Implemented guidance:

```text
No project owns the EIP root.
```

Implications:

- ProjectForge does not own the EIP root.
- MetaHarvest does not own the EIP root.
- MacroForge does not own the EIP root.
- EII does not own the EIP root.
- ResearchMemory and future projects do not own the EIP root.
- Root-level artifacts, if adopted later, represent ecosystem organization or neutral infrastructure, not project authority.

Interactions:

- Supports project autonomy doctrine by preventing root placement from becoming a controller hierarchy.
- Supports ownership-by-purpose guidance by preventing a project from owning ecosystem-wide responsibilities merely because it hosts or consumes them.
- Supports registry doctrine by keeping current ProjectForge-hosted registry semantics descriptive and transitional.

Edge cases:

- A project may temporarily host ecosystem-facing artifacts as a convenience; that does not transfer ownership.
- A root may contain governance artifacts; those artifacts must remain bounded by explicit foundational approval.
- A future infrastructure owner may be approved, but that approval must be explicit and cannot be inferred from root location.

Doctrine update locations:

- `CONSTITUTION.md` — added EIP-root ownership doctrine.
- `README.md` — added concise active guidance.
- `state/architecture.md` — added current architecture guidance.

## 3. Path-dependency inventory

Total files with a relevant content or filename reference: `266`.

References searched:

- `ArchitectureHarvest`;
- `MetaHarvest`;
- `architectureharvest`;
- `metaharvest`.

### By top-level area

- `AGENTS.md`: 1
- `ArchitectureHarvest`: 162
- `CONSTITUTION.md`: 1
- `README.md`: 1
- `_SUMMARY.md`: 1
- `artifacts`: 34
- `automation`: 1
- `context`: 2
- `external_sources`: 1
- `instructions`: 1
- `projectforge.egg-info`: 1
- `projectforge.yaml`: 1
- `simulation`: 15
- `state`: 5
- `templates`: 13
- `tests`: 2
- `tools`: 2
- `workspace`: 22

### ArchitectureHarvest directory file inventory

- `ArchitectureHarvest/[root]`: 5
- `ArchitectureHarvest/adoption_candidates`: 40
- `ArchitectureHarvest/adoption_log`: 4
- `ArchitectureHarvest/adoption_proposals`: 3
- `ArchitectureHarvest/anti_patterns`: 2
- `ArchitectureHarvest/audits`: 2
- `ArchitectureHarvest/component_cards`: 33
- `ArchitectureHarvest/contradictions`: 16
- `ArchitectureHarvest/decisions`: 2
- `ArchitectureHarvest/experiments`: 3
- `ArchitectureHarvest/indexes`: 10
- `ArchitectureHarvest/outcome_models`: 5
- `ArchitectureHarvest/pattern_library`: 2
- `ArchitectureHarvest/project_cards`: 8
- `ArchitectureHarvest/projects`: 2
- `ArchitectureHarvest/rejected`: 2
- `ArchitectureHarvest/relevance_maps`: 14
- `ArchitectureHarvest/reports`: 11
- `ArchitectureHarvest/retired`: 2
- `ArchitectureHarvest/retrieval`: 6
- `ArchitectureHarvest/reviews`: 9
- `ArchitectureHarvest/synthesis`: 26
- `ArchitectureHarvest/templates`: 15
- `ArchitectureHarvest/tools`: 2

### Generated-project placeholder/template references

- `templates/_shared_project/AGENTS.md`
- `templates/_shared_project/_SUMMARY.md`
- `templates/_shared_project/architecture/_SUMMARY.md`
- `templates/_shared_project/architecture/architecture_state.md`
- `templates/_shared_project/architecture/architecture_reviews/architecture_review.template.md`
- `templates/_shared_project/architecture/architectureharvest/adoption_outcome.template.yaml`
- `templates/_shared_project/architecture/architectureharvest/relevance_map.yaml`
- `templates/_shared_project/architecture/architectureharvest/rejected_candidates.md`
- `templates/_shared_project/architecture/architectureharvest/review_history.md`
- `templates/_shared_project/architecture/architectureharvest/adoption_candidates.md`
- `templates/_shared_project/context/context_policy.yaml`
- `templates/_shared_project/instructions/GENERAL_INSTRUCTIONS.md`
- `templates/_shared_project/tools/check_coherence.py`

### Active dependency categories

- Root guidance: `README.md`, `CONSTITUTION.md`, `AGENTS.md`, `_SUMMARY.md`, `projectforge.yaml`.
- Current state/architecture: `state/active_goal.md`, `state/architecture.md`, `state/project_state.md`, `state/recent_changes.md`, `state/_SUMMARY.md`.
- MetaHarvest hosted subtree: `ArchitectureHarvest/` with 224 files.
- ProjectForge templates: `templates/_shared_project/**` including generated `architecture/architectureharvest/` placeholders.
- ProjectForge tools/tests: `tools/new_project.py`, `tools/check_coherence.py`, `tests/test_architectureharvest_integration.py`.
- Workspace registry/project references: `workspace/_SUMMARY.md`, `workspace/projects_registry.yaml`, and MacroForge local artifacts under `workspace/projects/macroforge/`.
- Historical governance/review artifacts under `artifacts/` and `simulation/`.
- Evidence/source references including `ArchitectureHarvest/source_registry.yaml` and `external_sources/`.

## 4. Artifact-ownership inventory

### Classification summary

- Consumer-owned MacroForge local artifact; do not modify from ProjectForge extraction: 20
- External-source artifact; evidence-reference risk: 1
- Historical-only ProjectForge governance/audit artifact: 31
- Historical/planning artifact: 18
- MetaHarvest-owned analysis/evidence: 19
- MetaHarvest-owned evolution/outcome memory: 3
- MetaHarvest-owned recommendations/candidates: 42
- MetaHarvest-owned reusable non-domain knowledge: 82
- MetaHarvest-owned; compatibility-shim candidate: 4
- MetaHarvest-owned; evidence-reference risk: 1
- Other / manual review: 2
- ProjectForge-owned active guidance/state: 13
- ProjectForge-owned template; compatibility-shim candidate: 13
- ProjectForge-owned tooling/test; compatibility-shim candidate: 4
- ProjectForge-owned workspace/registry; ecosystem-owned/TBD risk: 2
- Transitional; consumer relevance mirror: 4
- Transitional; relevance interface artifact: 7

### Ownership interpretation by category

| Category | Ownership | Extraction implication |
|---|---|---|
| `ArchitectureHarvest/CONSTITUTION.md`, `README.md`, `INTEGRATION.md`, `_SUMMARY.md` | MetaHarvest-owned, currently hosted | Move candidate if extraction approved; update ProjectForge pointers. |
| `ArchitectureHarvest/project_cards`, `component_cards`, `synthesis`, `contradictions`, `pattern_library`, `anti_patterns`, `retrieval`, `indexes`, `outcome_models` | MetaHarvest-owned reusable non-domain knowledge | Core move candidates; preserve relative references. |
| `ArchitectureHarvest/reports`, `reviews`, `experiments`, `audits`, `decisions` | MetaHarvest-owned analysis/evidence, with historical lineage | Move candidate, but preserve historical paths or redirects. |
| `ArchitectureHarvest/adoption_candidates`, `adoption_proposals` | MetaHarvest-owned recommendation/candidate artifacts | Move candidate; verify target-project references and lineage. |
| `ArchitectureHarvest/adoption_log` | MetaHarvest-owned Evolution Interface memory | Move candidate; ensure local project decisions remain consumer-owned. |
| `ArchitectureHarvest/relevance_maps/projectforge` | Transitional relevance interface | Decide whether to move as MetaHarvest record or convert to ProjectForge-local relevance after extraction. |
| `ArchitectureHarvest/relevance_maps/macroforge` | Transitional consumer relevance mirror | Do not treat as MetaHarvest authority over MacroForge; likely compatibility/evidence handling required. |
| `ArchitectureHarvest/source_registry.yaml` | MetaHarvest-owned evidence/source registry | High evidence-reference risk; stable paths or relocation strategy required. |
| `ArchitectureHarvest/templates` | MetaHarvest-owned templates | Move candidate, but may need ProjectForge compatibility references. |
| `templates/_shared_project/architecture/architectureharvest/**` | ProjectForge-owned generated-project template; compatibility-shim candidate | Extraction blocker until naming/location compatibility is decided. |
| `tools/new_project.py`, `tools/check_coherence.py`, `tests/test_architectureharvest_integration.py` | ProjectForge-owned tooling/test dependency | Extraction blocker unless updated, shimmed, or explicitly left referencing hosted compatibility path. |
| `workspace/projects/macroforge/**` | Consumer-owned MacroForge local artifacts | Must not be modified by ProjectForge extraction task unless MacroForge is explicitly approved target. |
| `workspace/projects_registry.yaml`, `workspace/_SUMMARY.md` | ProjectForge-owned descriptive registry; possible future ecosystem-owned/TBD | Do not move into MetaHarvest. |
| `artifacts/**`, `simulation/**` historical references | Historical-only or planning evidence | Preserve; do not mass rewrite unless active guidance. |

### Detailed inventory table

| Path | Classification | Hit count |
|---|---:|---:|
| `AGENTS.md` | ProjectForge-owned active guidance/state | 16 |
| `ArchitectureHarvest/CONSTITUTION.md` | MetaHarvest-owned reusable non-domain knowledge | 34 |
| `ArchitectureHarvest/INTEGRATION.md` | MetaHarvest-owned reusable non-domain knowledge | 18 |
| `ArchitectureHarvest/README.md` | MetaHarvest-owned reusable non-domain knowledge | 21 |
| `ArchitectureHarvest/_SUMMARY.md` | MetaHarvest-owned reusable non-domain knowledge | 5 |
| `ArchitectureHarvest/adoption_candidates/_SUMMARY.md` | MetaHarvest-owned recommendations/candidates | 4 |
| `ArchitectureHarvest/adoption_candidates/ah-future-001-evidence-propagation-layer.yaml` | MetaHarvest-owned recommendations/candidates | 13 |
| `ArchitectureHarvest/adoption_candidates/aider-adoption-candidate.yaml` | MetaHarvest-owned recommendations/candidates | 14 |
| `ArchitectureHarvest/adoption_candidates/aider-deletion-candidate.yaml` | MetaHarvest-owned recommendations/candidates | 14 |
| `ArchitectureHarvest/adoption_candidates/aider-replacement-candidate.yaml` | MetaHarvest-owned recommendations/candidates | 14 |
| `ArchitectureHarvest/adoption_candidates/aider-simplification-candidate.yaml` | MetaHarvest-owned recommendations/candidates | 14 |
| `ArchitectureHarvest/adoption_candidates/dagster-adoption-candidate.yaml` | MetaHarvest-owned recommendations/candidates | 19 |
| `ArchitectureHarvest/adoption_candidates/dagster-deletion-candidate.yaml` | MetaHarvest-owned recommendations/candidates | 19 |
| `ArchitectureHarvest/adoption_candidates/dagster-replacement-candidate.yaml` | MetaHarvest-owned recommendations/candidates | 19 |
| `ArchitectureHarvest/adoption_candidates/dagster-simplification-candidate.yaml` | MetaHarvest-owned recommendations/candidates | 19 |
| `ArchitectureHarvest/adoption_candidates/dbt-adoption-candidate.yaml` | MetaHarvest-owned recommendations/candidates | 19 |
| `ArchitectureHarvest/adoption_candidates/dbt-deletion-candidate.yaml` | MetaHarvest-owned recommendations/candidates | 19 |
| `ArchitectureHarvest/adoption_candidates/dbt-replacement-candidate.yaml` | MetaHarvest-owned recommendations/candidates | 19 |
| `ArchitectureHarvest/adoption_candidates/dbt-simplification-candidate.yaml` | MetaHarvest-owned recommendations/candidates | 19 |
| `ArchitectureHarvest/adoption_candidates/langgraph-adoption-candidate.yaml` | MetaHarvest-owned recommendations/candidates | 11 |
| `ArchitectureHarvest/adoption_candidates/langgraph-deletion-candidate.yaml` | MetaHarvest-owned recommendations/candidates | 11 |
| `ArchitectureHarvest/adoption_candidates/langgraph-replacement-candidate.yaml` | MetaHarvest-owned recommendations/candidates | 11 |
| `ArchitectureHarvest/adoption_candidates/langgraph-simplification-candidate.yaml` | MetaHarvest-owned recommendations/candidates | 11 |
| `ArchitectureHarvest/adoption_candidates/macroforge-mf-ah-rev-001-simplification-create-a-tiny-file-backed-canonical-asset-manifest-registry-for-accept.yaml` | MetaHarvest-owned recommendations/candidates | 30 |
| `ArchitectureHarvest/adoption_candidates/macroforge-mf-ah-rev-002-missing_capability-add-explicit-lineage-edge-artifacts-for-raw-to-staging-to-canonical-to.yaml` | MetaHarvest-owned recommendations/candidates | 29 |
| `ArchitectureHarvest/adoption_candidates/macroforge-mf-ah-rev-003-missing_capability-represent-accepted-canonicalization-checks-as-reusable-contract-check-.yaml` | MetaHarvest-owned recommendations/candidates | 29 |
| `ArchitectureHarvest/adoption_candidates/macroforge-mf-ah-rev-004-replacement-replace-ad-hoc-validation-lineage-report-shapes-with-explicit-manifest.yaml` | MetaHarvest-owned recommendations/candidates | 29 |
| `ArchitectureHarvest/adoption_candidates/macroforge-mf-ah-rev-005-missing_capability-add-schema-mapping-proposal-version-and-deprecation-staleness-fields.yaml` | MetaHarvest-owned recommendations/candidates | 29 |
| `ArchitectureHarvest/adoption_candidates/macroforge-mf-ah-rev-006-simplification-use-typed-definitions-to-reduce-scattered-report-lineage-evidence-whil.yaml` | MetaHarvest-owned recommendations/candidates | 29 |
| `ArchitectureHarvest/adoption_candidates/macroforge-mf-ah-rev-007-deletion-retire-broad-dbt-dagster-runtime-adoption-as-a-near-term-macroforge-ca.yaml` | MetaHarvest-owned recommendations/candidates | 29 |
| `ArchitectureHarvest/adoption_candidates/macroforge-mf-ah-rev-008-deletion-reject-generalized-ingestion-framework-extraction-from-dbt-dagster-evi.yaml` | MetaHarvest-owned recommendations/candidates | 29 |
| `ArchitectureHarvest/adoption_candidates/macroforge-mf-ah-rev-009-more_evidence-measure-repeated-validation-report-boilerplate-across-macroforge-sourc.yaml` | MetaHarvest-owned recommendations/candidates | 29 |
| `ArchitectureHarvest/adoption_candidates/macroforge-mf-ah-rev-010-more_evidence-measure-operational-refresh-scheduling-materialization-pressure-before.yaml` | MetaHarvest-owned recommendations/candidates | 29 |
| `ArchitectureHarvest/adoption_candidates/openhands-adoption-candidate.yaml` | MetaHarvest-owned recommendations/candidates | 11 |
| `ArchitectureHarvest/adoption_candidates/openhands-deletion-candidate.yaml` | MetaHarvest-owned recommendations/candidates | 11 |
| `ArchitectureHarvest/adoption_candidates/openhands-replacement-candidate.yaml` | MetaHarvest-owned recommendations/candidates | 11 |
| `ArchitectureHarvest/adoption_candidates/openhands-simplification-candidate.yaml` | MetaHarvest-owned recommendations/candidates | 11 |
| `ArchitectureHarvest/adoption_candidates/projectforge-doctrine-principles-candidate.yaml` | MetaHarvest-owned recommendations/candidates | 17 |
| `ArchitectureHarvest/adoption_candidates/projectforge-emerging-patterns-candidate.yaml` | MetaHarvest-owned recommendations/candidates | 17 |
| `ArchitectureHarvest/adoption_candidates/projectforge-strong-recommendations-candidate.yaml` | MetaHarvest-owned recommendations/candidates | 12 |
| `ArchitectureHarvest/adoption_candidates/swe-agent-adoption-candidate.yaml` | MetaHarvest-owned recommendations/candidates | 16 |
| `ArchitectureHarvest/adoption_candidates/swe-agent-deletion-candidate.yaml` | MetaHarvest-owned recommendations/candidates | 16 |
| `ArchitectureHarvest/adoption_candidates/swe-agent-replacement-candidate.yaml` | MetaHarvest-owned recommendations/candidates | 16 |
| `ArchitectureHarvest/adoption_candidates/swe-agent-simplification-candidate.yaml` | MetaHarvest-owned recommendations/candidates | 16 |
| `ArchitectureHarvest/adoption_log/O-20260606-lifecycle-checkpoint-vocabulary.yaml` | MetaHarvest-owned evolution/outcome memory | 5 |
| `ArchitectureHarvest/adoption_log/O-20260608-macroforge-canonical-asset-manifest-registry.yaml` | MetaHarvest-owned evolution/outcome memory | 9 |
| `ArchitectureHarvest/adoption_log/_SUMMARY.md` | MetaHarvest-owned evolution/outcome memory | 2 |
| `ArchitectureHarvest/adoption_proposals/P-20260606-architectureharvest-first-adoption-outcome.md` | MetaHarvest-owned recommendations/candidates | 37 |
| `ArchitectureHarvest/adoption_proposals/P-20260606-architectureharvest-first-adoption-outcome.yaml` | MetaHarvest-owned recommendations/candidates | 26 |
| `ArchitectureHarvest/adoption_proposals/_SUMMARY.md` | MetaHarvest-owned recommendations/candidates | 4 |
| `ArchitectureHarvest/anti_patterns/_SUMMARY.md` | MetaHarvest-owned reusable non-domain knowledge | 2 |
| `ArchitectureHarvest/audits/_SUMMARY.md` | MetaHarvest-owned reusable non-domain knowledge | 2 |
| `ArchitectureHarvest/component_cards/_SUMMARY.md` | MetaHarvest-owned reusable non-domain knowledge | 3 |
| `ArchitectureHarvest/component_cards/aider-architect-editor-separation.yaml` | MetaHarvest-owned reusable non-domain knowledge | 3 |
| `ArchitectureHarvest/component_cards/aider-autocommit-undo-lint-test.yaml` | MetaHarvest-owned reusable non-domain knowledge | 4 |
| `ArchitectureHarvest/component_cards/aider-chat-history-summarization.yaml` | MetaHarvest-owned reusable non-domain knowledge | 4 |
| `ArchitectureHarvest/component_cards/aider-git-repo-boundary.yaml` | MetaHarvest-owned reusable non-domain knowledge | 3 |
| `ArchitectureHarvest/component_cards/aider-repo-map-context.yaml` | MetaHarvest-owned reusable non-domain knowledge | 3 |
| `ArchitectureHarvest/component_cards/langgraph-checkpoint-saver.yaml` | MetaHarvest-owned reusable non-domain knowledge | 3 |
| `ArchitectureHarvest/component_cards/langgraph-interrupt-command.yaml` | MetaHarvest-owned reusable non-domain knowledge | 3 |
| `ArchitectureHarvest/component_cards/langgraph-pregel-loop.yaml` | MetaHarvest-owned reusable non-domain knowledge | 3 |
| `ArchitectureHarvest/component_cards/langgraph-stategraph.yaml` | MetaHarvest-owned reusable non-domain knowledge | 3 |
| `ArchitectureHarvest/component_cards/langgraph-streaming-task-events.yaml` | MetaHarvest-owned reusable non-domain knowledge | 3 |
| `ArchitectureHarvest/component_cards/openhands-conversation-lifecycle.yaml` | MetaHarvest-owned reusable non-domain knowledge | 3 |
| `ArchitectureHarvest/component_cards/openhands-event-service.yaml` | MetaHarvest-owned reusable non-domain knowledge | 3 |
| `ArchitectureHarvest/component_cards/openhands-mcp-source-control-tools.yaml` | MetaHarvest-owned reusable non-domain knowledge | 3 |
| `ArchitectureHarvest/component_cards/openhands-pending-message-queue.yaml` | MetaHarvest-owned reusable non-domain knowledge | 3 |
| `ArchitectureHarvest/component_cards/openhands-sandbox-boundary.yaml` | MetaHarvest-owned reusable non-domain knowledge | 3 |
| `ArchitectureHarvest/component_cards/swe-agent-environment-reset.yaml` | MetaHarvest-owned reusable non-domain knowledge | 3 |
| `ArchitectureHarvest/component_cards/swe-agent-history-processors.yaml` | MetaHarvest-owned reusable non-domain knowledge | 3 |
| `ArchitectureHarvest/component_cards/swe-agent-patch-submission-pr-hooks.yaml` | MetaHarvest-owned reusable non-domain knowledge | 3 |
| `ArchitectureHarvest/component_cards/swe-agent-retry-review-loop.yaml` | MetaHarvest-owned reusable non-domain knowledge | 3 |
| `ArchitectureHarvest/component_cards/swe-agent-run-single-lifecycle.yaml` | MetaHarvest-owned reusable non-domain knowledge | 3 |
| `ArchitectureHarvest/component_cards/swe-agent-trajectory-persistence.yaml` | MetaHarvest-owned reusable non-domain knowledge | 3 |
| `ArchitectureHarvest/contradictions/_SUMMARY.md` | MetaHarvest-owned reusable non-domain knowledge | 3 |
| `ArchitectureHarvest/contradictions/asset_manifest_vs_source_specific_simplicity.yaml` | MetaHarvest-owned reusable non-domain knowledge | 7 |
| `ArchitectureHarvest/contradictions/auto_orchestration_vs_governance_boundaries.yaml` | MetaHarvest-owned reusable non-domain knowledge | 7 |
| `ArchitectureHarvest/contradictions/autocommit-vs-dry-run-approval.yaml` | MetaHarvest-owned reusable non-domain knowledge | 3 |
| `ArchitectureHarvest/contradictions/benchmark-agent-loop-vs-human-governance.yaml` | MetaHarvest-owned reusable non-domain knowledge | 3 |
| `ArchitectureHarvest/contradictions/contracts_vs_flexible_exploration.yaml` | MetaHarvest-owned reusable non-domain knowledge | 7 |
| `ArchitectureHarvest/contradictions/definition_execution_boundary_vs_runtime_platform.yaml` | MetaHarvest-owned reusable non-domain knowledge | 7 |
| `ArchitectureHarvest/contradictions/event-log-vs-state-snapshot.yaml` | MetaHarvest-owned reusable non-domain knowledge | 2 |
| `ArchitectureHarvest/contradictions/lineage_completeness_vs_context_bloat.yaml` | MetaHarvest-owned reusable non-domain knowledge | 7 |
| `ArchitectureHarvest/contradictions/repo-map-vs-explicit-context-bundles.yaml` | MetaHarvest-owned reusable non-domain knowledge | 3 |
| `ArchitectureHarvest/contradictions/runtime-orchestration-vs-file-backed-governance.yaml` | MetaHarvest-owned reusable non-domain knowledge | 2 |
| `ArchitectureHarvest/contradictions/sandbox-tool-proxy-vs-hermes-tool-approval.yaml` | MetaHarvest-owned reusable non-domain knowledge | 2 |
| `ArchitectureHarvest/contradictions/trajectory-replay-vs-compact-state.yaml` | MetaHarvest-owned reusable non-domain knowledge | 3 |
| `ArchitectureHarvest/decisions/_SUMMARY.md` | MetaHarvest-owned reusable non-domain knowledge | 2 |
| `ArchitectureHarvest/experiments/PF-AH-REC-010-lifecycle-checkpoint-validation-experiment.md` | MetaHarvest-owned reusable non-domain knowledge | 9 |
| `ArchitectureHarvest/experiments/PF-AH-REC-010-lifecycle-checkpoint-validation-experiment.yaml` | MetaHarvest-owned reusable non-domain knowledge | 11 |
| `ArchitectureHarvest/experiments/_SUMMARY.md` | MetaHarvest-owned reusable non-domain knowledge | 2 |
| `ArchitectureHarvest/indexes/_SUMMARY.md` | MetaHarvest-owned reusable non-domain knowledge | 3 |
| `ArchitectureHarvest/indexes/problem_index.md` | MetaHarvest-owned reusable non-domain knowledge | 1 |
| `ArchitectureHarvest/outcome_models/README.md` | MetaHarvest-owned reusable non-domain knowledge | 1 |
| `ArchitectureHarvest/outcome_models/_SUMMARY.md` | MetaHarvest-owned reusable non-domain knowledge | 2 |
| `ArchitectureHarvest/pattern_library/_SUMMARY.md` | MetaHarvest-owned reusable non-domain knowledge | 2 |
| `ArchitectureHarvest/project_cards/_SUMMARY.md` | MetaHarvest-owned reusable non-domain knowledge | 3 |
| `ArchitectureHarvest/project_cards/aider.yaml` | MetaHarvest-owned reusable non-domain knowledge | 8 |
| `ArchitectureHarvest/project_cards/dagster.yaml` | MetaHarvest-owned reusable non-domain knowledge | 9 |
| `ArchitectureHarvest/project_cards/dbt.yaml` | MetaHarvest-owned reusable non-domain knowledge | 9 |
| `ArchitectureHarvest/project_cards/langgraph.yaml` | MetaHarvest-owned reusable non-domain knowledge | 8 |
| `ArchitectureHarvest/project_cards/openhands.yaml` | MetaHarvest-owned reusable non-domain knowledge | 8 |
| `ArchitectureHarvest/project_cards/swe-agent.yaml` | MetaHarvest-owned reusable non-domain knowledge | 9 |
| `ArchitectureHarvest/projects/_SUMMARY.md` | MetaHarvest-owned reusable non-domain knowledge | 2 |
| `ArchitectureHarvest/rejected/_SUMMARY.md` | MetaHarvest-owned reusable non-domain knowledge | 2 |
| `ArchitectureHarvest/relevance_maps/_SUMMARY.md` | Transitional; relevance interface artifact | 2 |
| `ArchitectureHarvest/relevance_maps/generic/_SUMMARY.md` | Transitional; relevance interface artifact | 2 |
| `ArchitectureHarvest/relevance_maps/macroforge/_SUMMARY.md` | Transitional; consumer relevance mirror | 2 |
| `ArchitectureHarvest/relevance_maps/macroforge/dagster-relevance-map.yaml` | Transitional; consumer relevance mirror | 6 |
| `ArchitectureHarvest/relevance_maps/macroforge/dbt-relevance-map.yaml` | Transitional; consumer relevance mirror | 6 |
| `ArchitectureHarvest/relevance_maps/macroforge/macroforge-relevance-map.yaml` | Transitional; consumer relevance mirror | 2 |
| `ArchitectureHarvest/relevance_maps/projectforge/_SUMMARY.md` | Transitional; relevance interface artifact | 3 |
| `ArchitectureHarvest/relevance_maps/projectforge/aider-relevance-map.yaml` | Transitional; relevance interface artifact | 8 |
| `ArchitectureHarvest/relevance_maps/projectforge/langgraph-relevance-map.yaml` | Transitional; relevance interface artifact | 4 |
| `ArchitectureHarvest/relevance_maps/projectforge/openhands-relevance-map.yaml` | Transitional; relevance interface artifact | 4 |
| `ArchitectureHarvest/relevance_maps/projectforge/swe-agent-relevance-map.yaml` | Transitional; relevance interface artifact | 10 |
| `ArchitectureHarvest/reports/R-20260606-aider-deep-analysis.md` | MetaHarvest-owned analysis/evidence | 1 |
| `ArchitectureHarvest/reports/R-20260606-aider-swe-agent-comparative-final-report.md` | MetaHarvest-owned analysis/evidence | 13 |
| `ArchitectureHarvest/reports/R-20260606-langgraph-deep-analysis.md` | MetaHarvest-owned analysis/evidence | 2 |
| `ArchitectureHarvest/reports/R-20260606-openhands-deep-analysis.md` | MetaHarvest-owned analysis/evidence | 1 |
| `ArchitectureHarvest/reports/R-20260606-openhands-langgraph-first-cycle-final-report.md` | MetaHarvest-owned analysis/evidence | 11 |
| `ArchitectureHarvest/reports/R-20260606-swe-agent-deep-analysis.md` | MetaHarvest-owned analysis/evidence | 1 |
| `ArchitectureHarvest/reports/R-20260608-dagster-deep-analysis.md` | MetaHarvest-owned analysis/evidence | 1 |
| `ArchitectureHarvest/reports/R-20260608-dbt-dagster-macroforge-comparative-final-report.md` | MetaHarvest-owned analysis/evidence | 2 |
| `ArchitectureHarvest/reports/R-20260608-dbt-deep-analysis.md` | MetaHarvest-owned analysis/evidence | 1 |
| `ArchitectureHarvest/reports/_SUMMARY.md` | MetaHarvest-owned analysis/evidence | 3 |
| `ArchitectureHarvest/retired/_SUMMARY.md` | MetaHarvest-owned reusable non-domain knowledge | 2 |
| `ArchitectureHarvest/retrieval/_SUMMARY.md` | MetaHarvest-owned reusable non-domain knowledge | 3 |
| `ArchitectureHarvest/retrieval/problem_catalog.yaml` | MetaHarvest-owned reusable non-domain knowledge | 2 |
| `ArchitectureHarvest/retrieval/recommendation_rules.yaml` | MetaHarvest-owned reusable non-domain knowledge | 3 |
| `ArchitectureHarvest/retrieval/retrieval_index.yaml` | MetaHarvest-owned reusable non-domain knowledge | 1 |
| `ArchitectureHarvest/retrieval/retrieval_policy.md` | MetaHarvest-owned reusable non-domain knowledge | 3 |
| `ArchitectureHarvest/reviews/R-20260606-projectforge-architectureharvest-guided-review.md` | MetaHarvest-owned analysis/evidence | 37 |
| `ArchitectureHarvest/reviews/R-20260606-projectforge-architectureharvest-guided-review.yaml` | MetaHarvest-owned analysis/evidence | 61 |
| `ArchitectureHarvest/reviews/R-20260606-projectforge-validation-objective-rerank.md` | MetaHarvest-owned analysis/evidence | 26 |
| `ArchitectureHarvest/reviews/R-20260606-projectforge-validation-objective-rerank.yaml` | MetaHarvest-owned analysis/evidence | 22 |
| `ArchitectureHarvest/reviews/R-20260608-confidence-consolidation-review.md` | MetaHarvest-owned analysis/evidence | 13 |
| `ArchitectureHarvest/reviews/R-20260608-confidence-consolidation-review.yaml` | MetaHarvest-owned analysis/evidence | 26 |
| `ArchitectureHarvest/reviews/R-20260608-macroforge-first-architectureharvest-review.md` | MetaHarvest-owned analysis/evidence | 4 |
| `ArchitectureHarvest/reviews/R-20260608-macroforge-first-architectureharvest-review.yaml` | MetaHarvest-owned analysis/evidence | 27 |
| `ArchitectureHarvest/reviews/_SUMMARY.md` | MetaHarvest-owned analysis/evidence | 8 |
| `ArchitectureHarvest/source_registry.yaml` | MetaHarvest-owned; evidence-reference risk | 1 |
| `ArchitectureHarvest/synthesis/_SUMMARY.md` | MetaHarvest-owned reusable non-domain knowledge | 3 |
| `ArchitectureHarvest/synthesis/bounded_context_selection.yaml` | MetaHarvest-owned reusable non-domain knowledge | 2 |
| `ArchitectureHarvest/synthesis/credential_scoped_tool_proxy.yaml` | MetaHarvest-owned reusable non-domain knowledge | 2 |
| `ArchitectureHarvest/synthesis/environment_reset_boundary.yaml` | MetaHarvest-owned reusable non-domain knowledge | 2 |
| `ArchitectureHarvest/synthesis/git_anchored_coding_workflow.yaml` | MetaHarvest-owned reusable non-domain knowledge | 2 |
| `ArchitectureHarvest/synthesis/interrupt_as_approval_gate.yaml` | MetaHarvest-owned reusable non-domain knowledge | 2 |
| `ArchitectureHarvest/synthesis/observable_task_stream.yaml` | MetaHarvest-owned reusable non-domain knowledge | 2 |
| `ArchitectureHarvest/synthesis/patch_submission_boundary.yaml` | MetaHarvest-owned reusable non-domain knowledge | 2 |
| `ArchitectureHarvest/synthesis/pending_input_queue.yaml` | MetaHarvest-owned reusable non-domain knowledge | 2 |
| `ArchitectureHarvest/synthesis/plan_execute_split.yaml` | MetaHarvest-owned reusable non-domain knowledge | 2 |
| `ArchitectureHarvest/synthesis/problem-first-decision-support.example.yaml` | MetaHarvest-owned reusable non-domain knowledge | 1 |
| `ArchitectureHarvest/synthesis/reviewer_retry_loop.yaml` | MetaHarvest-owned reusable non-domain knowledge | 2 |
| `ArchitectureHarvest/synthesis/sandboxed_conversation_runtime.yaml` | MetaHarvest-owned reusable non-domain knowledge | 2 |
| `ArchitectureHarvest/synthesis/thread_checkpoint_contract.yaml` | MetaHarvest-owned reusable non-domain knowledge | 2 |
| `ArchitectureHarvest/synthesis/trajectory_artifact_recovery.yaml` | MetaHarvest-owned reusable non-domain knowledge | 2 |
| `ArchitectureHarvest/synthesis/typed_state_graph.yaml` | MetaHarvest-owned reusable non-domain knowledge | 2 |
| `ArchitectureHarvest/templates/_SUMMARY.md` | MetaHarvest-owned; compatibility-shim candidate | 2 |
| `ArchitectureHarvest/templates/adoption_candidate.template.yaml` | MetaHarvest-owned; compatibility-shim candidate | 1 |
| `ArchitectureHarvest/templates/adoption_outcome.template.yaml` | MetaHarvest-owned; compatibility-shim candidate | 1 |
| `ArchitectureHarvest/templates/recommendation.template.yaml` | MetaHarvest-owned; compatibility-shim candidate | 1 |
| `ArchitectureHarvest/tools/_SUMMARY.md` | MetaHarvest-owned reusable non-domain knowledge | 2 |
| `CONSTITUTION.md` | ProjectForge-owned active guidance/state | 17 |
| `README.md` | ProjectForge-owned active guidance/state | 9 |
| `_SUMMARY.md` | ProjectForge-owned active guidance/state | 2 |
| `artifacts/decisions/D-20260606-architectureharvest-advisory-integration.md` | Historical-only ProjectForge governance/audit artifact | 9 |
| `artifacts/decisions/D-20260606-architectureharvest-decision-support-layer.md` | Historical-only ProjectForge governance/audit artifact | 12 |
| `artifacts/decisions/D-20260606-architectureharvest-file-based-subsystem.md` | Historical-only ProjectForge governance/audit artifact | 7 |
| `artifacts/decisions/D-20260615-governance-permission-framework.md` | Historical/planning artifact | 2 |
| `artifacts/decisions/_SUMMARY.md` | Historical-only ProjectForge governance/audit artifact | 3 |
| `artifacts/reports/R-20260606-architectureharvest-decision-support-enhancement.md` | Historical-only ProjectForge governance/audit artifact | 39 |
| `artifacts/reports/R-20260606-architectureharvest-integration.md` | Historical-only ProjectForge governance/audit artifact | 7 |
| `artifacts/reports/R-20260606-lifecycle-checkpoint-validation-results.md` | Historical-only ProjectForge governance/audit artifact | 7 |
| `artifacts/reports/R-20260614-framework-improvement-notice-doctrine.md` | Historical-only ProjectForge governance/audit artifact | 7 |
| `artifacts/reports/R-20260615-commit-boundary-intelligence-future-review.md` | Historical/planning artifact | 12 |
| `artifacts/reports/R-20260615-ecosystem-future-review-note.md` | Historical/planning artifact | 6 |
| `artifacts/reports/R-20260615-ecosystem-infrastructure-future-review-note.md` | Historical/planning artifact | 4 |
| `artifacts/reports/R-20260615-ecosystem-infrastructure-ownership-future-review-note.md` | Historical/planning artifact | 3 |
| `artifacts/reports/R-20260615-ecosystem-structure-migration-planning-review.md` | Historical/planning artifact | 31 |
| `artifacts/reports/R-20260615-governance-permission-framework-review.md` | Historical/planning artifact | 2 |
| `artifacts/reports/R-20260615-metaharvest-architecture-consolidation-review.md` | Historical/planning artifact | 45 |
| `artifacts/reports/R-20260615-metaharvest-commit-boundary-intelligence-future-note.md` | Historical/planning artifact | 7 |
| `artifacts/reports/R-20260615-metaharvest-conceptual-evolution-review.md` | Historical/planning artifact | 27 |
| `artifacts/reports/R-20260615-metaharvest-extraction-independence-review.md` | Historical/planning artifact | 63 |
| `artifacts/reports/R-20260615-metaharvest-interface-boundary-review.md` | Historical/planning artifact | 79 |
| `artifacts/reports/R-20260615-soft-governance-risk-future-review-note.md` | Historical/planning artifact | 2 |
| `artifacts/reports/_SUMMARY.md` | Historical-only ProjectForge governance/audit artifact | 4 |
| `artifacts/tasks/T-20260606-architectureharvest-initial-analysis-batch.md` | Historical-only ProjectForge governance/audit artifact | 13 |
| `artifacts/tasks/T-20260606-lifecycle-checkpoint-validation.checkpoints.yaml` | Historical-only ProjectForge governance/audit artifact | 4 |
| `artifacts/tasks/T-20260606-lifecycle-checkpoint-validation.md` | Historical-only ProjectForge governance/audit artifact | 3 |
| `artifacts/tasks/T-20260614-continuity-recovery-framework.md` | Historical-only ProjectForge governance/audit artifact | 3 |
| `artifacts/tasks/T-20260614-framework-improvement-notice-doctrine.md` | Historical-only ProjectForge governance/audit artifact | 1 |
| `artifacts/tasks/T-20260614-projectforge-doctrine-alignment.md` | Historical-only ProjectForge governance/audit artifact | 9 |
| `artifacts/tasks/T-20260615-ecosystem-autonomy-doctrine-alignment.md` | Historical/planning artifact | 7 |
| `artifacts/tasks/T-20260615-ecosystem-structure-migration-planning.md` | Historical/planning artifact | 3 |
| `artifacts/tasks/T-20260615-governance-permission-framework.md` | Historical/planning artifact | 1 |
| `artifacts/tasks/T-20260615-metaharvest-extraction-independence-review.md` | Historical/planning artifact | 9 |
| `artifacts/tasks/T-20260615-metaharvest-interface-boundary-review.md` | Historical/planning artifact | 8 |
| `artifacts/tasks/_SUMMARY.md` | Historical-only ProjectForge governance/audit artifact | 2 |
| `automation/orchestration_schedule.yaml` | Other / manual review | 6 |
| `context/context_policy.yaml` | ProjectForge-owned active guidance/state | 9 |
| `context/latest_handoff.md` | ProjectForge-owned active guidance/state | 5 |
| `external_sources/dbt-core/.github/actions/setup-postgres-windows/setup_db.sh` | External-source artifact; evidence-reference risk | 1 |
| `instructions/GENERAL_INSTRUCTIONS.md` | ProjectForge-owned active guidance/state | 3 |
| `projectforge.egg-info/SOURCES.txt` | Other / manual review | 1 |
| `projectforge.yaml` | ProjectForge-owned active guidance/state | 1 |
| `simulation/dry_runs/20260606_095300-architectureharvest-openhands-langgraph-analysis.md` | Historical-only ProjectForge governance/audit artifact | 32 |
| `simulation/dry_runs/20260606_110716-dry-run.md` | Historical-only ProjectForge governance/audit artifact | 4 |
| `simulation/dry_runs/20260606_112358-dry-run.md` | Historical-only ProjectForge governance/audit artifact | 6 |
| `simulation/dry_runs/20260606_113938-dry-run.md` | Historical-only ProjectForge governance/audit artifact | 21 |
| `simulation/dry_runs/20260606_121442-dry-run.md` | Historical-only ProjectForge governance/audit artifact | 9 |
| `simulation/dry_runs/20260606_122403-dry-run.md` | Historical-only ProjectForge governance/audit artifact | 11 |
| `simulation/dry_runs/20260606_123202-dry-run.md` | Historical-only ProjectForge governance/audit artifact | 5 |
| `simulation/dry_runs/20260606_135136-dry-run.md` | Historical-only ProjectForge governance/audit artifact | 6 |
| `simulation/dry_runs/20260606_135706-dry-run.md` | Historical-only ProjectForge governance/audit artifact | 2 |
| `simulation/dry_runs/20260606_144152-dry-run.md` | Historical-only ProjectForge governance/audit artifact | 23 |
| `simulation/dry_runs/20260608_153053-dry-run.md` | Historical-only ProjectForge governance/audit artifact | 12 |
| `simulation/dry_runs/20260608_154000-dry-run.md` | Historical-only ProjectForge governance/audit artifact | 21 |
| `simulation/dry_runs/20260608_162742-dry-run.md` | Historical-only ProjectForge governance/audit artifact | 1 |
| `simulation/dry_runs/20260614_072135-dry-run.md` | Historical-only ProjectForge governance/audit artifact | 2 |
| `simulation/dry_runs/_SUMMARY.md` | Historical-only ProjectForge governance/audit artifact | 1 |
| `state/_SUMMARY.md` | ProjectForge-owned active guidance/state | 1 |
| `state/active_goal.md` | ProjectForge-owned active guidance/state | 3 |
| `state/architecture.md` | ProjectForge-owned active guidance/state | 9 |
| `state/project_state.md` | ProjectForge-owned active guidance/state | 15 |
| `state/recent_changes.md` | ProjectForge-owned active guidance/state | 6 |
| `templates/_shared_project/AGENTS.md` | ProjectForge-owned template; compatibility-shim candidate | 6 |
| `templates/_shared_project/_SUMMARY.md` | ProjectForge-owned template; compatibility-shim candidate | 3 |
| `templates/_shared_project/architecture/_SUMMARY.md` | ProjectForge-owned template; compatibility-shim candidate | 1 |
| `templates/_shared_project/architecture/architecture_reviews/architecture_review.template.md` | ProjectForge-owned template; compatibility-shim candidate | 4 |
| `templates/_shared_project/architecture/architecture_state.md` | ProjectForge-owned template; compatibility-shim candidate | 4 |
| `templates/_shared_project/architecture/architectureharvest/adoption_candidates.md` | ProjectForge-owned template; compatibility-shim candidate | 2 |
| `templates/_shared_project/architecture/architectureharvest/adoption_outcome.template.yaml` | ProjectForge-owned template; compatibility-shim candidate | 2 |
| `templates/_shared_project/architecture/architectureharvest/rejected_candidates.md` | ProjectForge-owned template; compatibility-shim candidate | 1 |
| `templates/_shared_project/architecture/architectureharvest/relevance_map.yaml` | ProjectForge-owned template; compatibility-shim candidate | 2 |
| `templates/_shared_project/architecture/architectureharvest/review_history.md` | ProjectForge-owned template; compatibility-shim candidate | 2 |
| `templates/_shared_project/context/context_policy.yaml` | ProjectForge-owned template; compatibility-shim candidate | 9 |
| `templates/_shared_project/instructions/GENERAL_INSTRUCTIONS.md` | ProjectForge-owned template; compatibility-shim candidate | 3 |
| `templates/_shared_project/tools/check_coherence.py` | ProjectForge-owned template; compatibility-shim candidate | 8 |
| `tests/_SUMMARY.md` | ProjectForge-owned tooling/test; compatibility-shim candidate | 1 |
| `tests/test_architectureharvest_integration.py` | ProjectForge-owned tooling/test; compatibility-shim candidate | 29 |
| `tools/check_coherence.py` | ProjectForge-owned tooling/test; compatibility-shim candidate | 8 |
| `tools/new_project.py` | ProjectForge-owned tooling/test; compatibility-shim candidate | 5 |
| `workspace/_SUMMARY.md` | ProjectForge-owned workspace/registry; ecosystem-owned/TBD risk | 1 |
| `workspace/projects/macroforge/architecture/_SUMMARY.md` | Consumer-owned MacroForge local artifact; do not modify from ProjectForge extraction | 3 |
| `workspace/projects/macroforge/architecture/architecture_state.md` | Consumer-owned MacroForge local artifact; do not modify from ProjectForge extraction | 5 |
| `workspace/projects/macroforge/architecture/architectureharvest/_SUMMARY.md` | Consumer-owned MacroForge local artifact; do not modify from ProjectForge extraction | 2 |
| `workspace/projects/macroforge/architecture/architectureharvest/adoption_candidates.md` | Consumer-owned MacroForge local artifact; do not modify from ProjectForge extraction | 2 |
| `workspace/projects/macroforge/architecture/architectureharvest/rejected_candidates.md` | Consumer-owned MacroForge local artifact; do not modify from ProjectForge extraction | 2 |
| `workspace/projects/macroforge/architecture/architectureharvest/relevance_map.yaml` | Consumer-owned MacroForge local artifact; do not modify from ProjectForge extraction | 6 |
| `workspace/projects/macroforge/architecture/architectureharvest/review_history.md` | Consumer-owned MacroForge local artifact; do not modify from ProjectForge extraction | 6 |
| `workspace/projects/macroforge/artifacts/decisions/DEC-020-architectureharvest-canonical-asset-manifest-registry.md` | Consumer-owned MacroForge local artifact; do not modify from ProjectForge extraction | 6 |
| `workspace/projects/macroforge/artifacts/decisions/_SUMMARY.md` | Consumer-owned MacroForge local artifact; do not modify from ProjectForge extraction | 1 |
| `workspace/projects/macroforge/artifacts/reports/R-20260613-largest-canonicalization-uncertainty.md` | Consumer-owned MacroForge local artifact; do not modify from ProjectForge extraction | 8 |
| `workspace/projects/macroforge/artifacts/reports/R-20260613-review-to-accepted-lifecycle-validation-design.md` | Consumer-owned MacroForge local artifact; do not modify from ProjectForge extraction | 2 |
| `workspace/projects/macroforge/artifacts/tasks/TASK-035-implement-narrow-architectureharvest-canonical-asset-manifest.md` | Consumer-owned MacroForge local artifact; do not modify from ProjectForge extraction | 12 |
| `workspace/projects/macroforge/artifacts/tasks/_SUMMARY.md` | Consumer-owned MacroForge local artifact; do not modify from ProjectForge extraction | 2 |
| `workspace/projects/macroforge/docs/roadmap.md` | Consumer-owned MacroForge local artifact; do not modify from ProjectForge extraction | 1 |
| `workspace/projects/macroforge/simulation/dry_runs/20260608_164056-dry-run.md` | Consumer-owned MacroForge local artifact; do not modify from ProjectForge extraction | 2 |
| `workspace/projects/macroforge/state/architecture.md` | Consumer-owned MacroForge local artifact; do not modify from ProjectForge extraction | 1 |
| `workspace/projects/macroforge/state/project_state.md` | Consumer-owned MacroForge local artifact; do not modify from ProjectForge extraction | 5 |
| `workspace/projects/macroforge/tests/_SUMMARY.md` | Consumer-owned MacroForge local artifact; do not modify from ProjectForge extraction | 3 |
| `workspace/projects/macroforge/tests/test_architectureharvest_integration.py` | Consumer-owned MacroForge local artifact; do not modify from ProjectForge extraction | 7 |
| `workspace/projects/macroforge/tools/check_coherence.py` | Consumer-owned MacroForge local artifact; do not modify from ProjectForge extraction | 8 |
| `workspace/projects_registry.yaml` | ProjectForge-owned workspace/registry; ecosystem-owned/TBD risk | 1 |

## 5. Evolution-interface assessment

Assessment: approved as a conceptual interface for MetaHarvest planning.

The Evolution Interface is distinct enough to name because it governs learning over time rather than a single adoption/rejection event. It allows projects to contribute reusable lessons back into MetaHarvest without transferring ownership of local history.

Approved conceptual interface set:

1. Consultation Interface
2. Recommendation Interface
3. Adoption Outcome Interface
4. Rejection Memory Interface
5. Evidence Reference Interface
6. Relevance Interface
7. Staleness Interface
8. Authority Boundary Interface
9. Evolution Interface

Authority risks and controls:

- It must not force consumers to report every outcome.
- It must not transfer project-local history into MetaHarvest ownership.
- It must not create automatic adoption/rejection propagation.
- It must not make repeated success into governance authority.
- It should update reusable lessons, fit conditions, confidence, priority, anti-patterns, and revisit triggers only as advisory knowledge.

Bounded doctrine update location:

- `ArchitectureHarvest/CONSTITUTION.md` — Feedback loop and recommendation staleness now names the Evolution Interface and its authority limits.

## 6. Extraction-readiness report

Status: conceptually ready only.

### Conceptual readiness

Ready:

- durable independent purpose;
- conceptually separable from ProjectForge;
- advisory and non-domain boundary;
- ownership boundaries;
- authority boundaries;
- conceptual interface set, now including Evolution Interface;
- extraction readiness independent from EIP-root adoption;
- EIP-root ownership doctrine clarified.

Conceptual blockers:

- None that block continued extraction planning.

Remaining conceptual refinements:

- Decide whether current `ArchitectureHarvest` physical name and future `MetaHarvest` conceptual name are renamed during extraction or left as compatibility naming.
- Decide whether ProjectForge-local and MacroForge-local relevance mirrors remain mirrored, move, or become purely consumer-local.

### Operational readiness

Not ready.

Operational blockers:

- 266 relevant references found across active guidance, hosted subtree, templates, tools/tests, workspace artifacts, historical artifacts, and external/evidence records.
- `ArchitectureHarvest/` contains 224 files whose move would require path compatibility and historical-reference strategy.
- ProjectForge generated-project templates still create `architecture/architectureharvest/` paths.
- ProjectForge tools/tests still validate or generate ArchitectureHarvest conventions.
- MacroForge local artifacts under `workspace/projects/macroforge/` reference ArchitectureHarvest and must not be modified without MacroForge approval.
- Evidence/source references require stable path policy, especially `ArchitectureHarvest/source_registry.yaml` and external source records.
- Compatibility shim plan does not exist yet.
- Verification and rollback plan does not exist yet.
- Interim sibling location has not been approved.

Migration risks:

- breaking generated-project coherence checks;
- losing historical interpretability of old ArchitectureHarvest references;
- accidentally moving consumer-owned MacroForge local history;
- dragging potential ecosystem-owned registry/interface responsibilities into MetaHarvest;
- creating duplicate names (`ArchitectureHarvest` physical vs `MetaHarvest` conceptual) without clear compatibility;
- breaking source/evidence lineage.

Compatibility risks:

- existing ProjectForge and generated-project code expects `architecture/architectureharvest/`;
- tests and coherence tools have ArchitectureHarvest-specific assumptions;
- old reports and decisions use ArchitectureHarvest names;
- external source references may encode ProjectForge-relative paths.

Evidence-reference risks:

- reports, component cards, synthesis, and source registry may reference source paths that become ambiguous after a move;
- adoption logs may need both MetaHarvest-owned generalized lessons and consumer-local evidence pointers;
- historical artifacts should remain interpretable without mass rewrite.

Readiness classification:

```text
MetaHarvest extraction is conceptually ready only.
It is not operationally ready and not fully ready.
```

## 7. Recommended migration sequence

1. Freeze doctrine boundary: treat current doctrine updates as guidance, not extraction approval.
2. Decide extraction location explicitly if extraction is later approved, without requiring EIP-root adoption.
3. Decide naming strategy: keep `ArchitectureHarvest`, rename to `MetaHarvest`, or use compatibility aliasing.
4. Classify every moved artifact into MetaHarvest-owned, ProjectForge-owned, consumer-owned, ecosystem-owned/TBD, historical-only, transitional, or compatibility-shim candidate.
5. Design compatibility strategy for old paths and generated-project `architecture/architectureharvest/` placeholders.
6. Design evidence-reference strategy for `source_registry.yaml`, reports, reviews, cards, and adoption/evolution records.
7. Update ProjectForge tools/tests/templates in a reviewed migration plan.
8. Define verification plan: coherence, targeted tests, path-reference checks, YAML validation, architecture-reality audit.
9. Define rollback plan.
10. Only then request L4 approval for physical extraction or rename.

## 8. Risks, conflicts, and open questions

### Risks

- Doctrine could be overread as extraction approval. It is not.
- No-project-owns-root could be misread as no one may maintain root artifacts. Maintenance may be approved; ownership authority is the issue.
- Evolution Interface could become bureaucratic if outcome reporting becomes mandatory.
- Compatibility shims could become permanent clutter if not time-bounded.
- Evidence paths could silently rot after extraction.
- MacroForge references may tempt cross-project edits; those are prohibited without explicit MacroForge approval.

### Conflicts found

- No hard doctrine conflict.
- Soft conflict: physical hosting still implies ProjectForge locality while doctrine says filesystem location is not authority. This is acceptable as transitional but should not be left ambiguous forever.
- Soft conflict: `ArchitectureHarvest` path naming diverges from conceptual `MetaHarvest` name. This is an operational naming issue, not a purpose conflict.
- Soft conflict: some relevance maps represent consumer-local fit while living under hosted ArchitectureHarvest. These should be classified before extraction.

### Open questions

- Should physical extraction keep `ArchitectureHarvest` name for compatibility or rename to `MetaHarvest`?
- Should extraction and rename be one migration or two?
- What interim sibling location is acceptable before EIP-root adoption?
- Should generated projects continue using `architecture/architectureharvest/`, migrate to `architecture/metaharvest/`, or support both?
- Which `ArchitectureHarvest/relevance_maps/**` records are MetaHarvest-owned versus consumer-owned mirrors?
- What is the minimum viable compatibility shim and how long should it live?
- How should historical artifacts reference moved files without mass rewrite?
- Who eventually maintains ecosystem-owned contracts/registries if they are created later?

