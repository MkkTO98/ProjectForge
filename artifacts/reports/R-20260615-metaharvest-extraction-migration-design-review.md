# MetaHarvest Extraction-Migration Design Review

Date: 2026-06-15
Status: bounded migration-design and extraction-readiness planning
Permission level: L4 foundational design only
Scope: naming strategy, compatibility strategy, template/tooling/test implications, evidence-reference strategy, historical/transitional artifacts, compatibility shims, verification, rollback, extraction location, and complete migration sequence

## Explicit non-actions

This task did not authorize or perform:

- commits;
- staging;
- directory moves;
- directory renames;
- MetaHarvest extraction;
- MacroForge modification;
- EII modification;
- compatibility-layer implementation;
- aliases;
- template modification;
- tooling modification;
- test modification;
- ecosystem infrastructure implementation;
- repository restructuring.

## Governance visibility

FOUNDATIONAL_GOVERNANCE_WARNING
PERMISSION_LEVEL=L4
CATEGORY=FOUNDATIONAL
PROJECT=ProjectForge / MetaHarvest / EIP ecosystem
DECISION=MetaHarvest extraction migration design only

Impact:
This review designs how a later MetaHarvest extraction should be performed if explicit extraction approval is granted.

Risk:
A premature extraction could break path references, generated-project templates, ProjectForge coherence checks, recommendation/adoption lineage, evidence references, and historical interpretability. A premature rename could also make old ArchitectureHarvest evidence harder to interpret.

Required approval:
STOP. This artifact is a migration design and extraction-readiness plan only. Extraction, rename, directory movement, compatibility aliases, template/tooling/test changes, ecosystem infrastructure, and project creation remain prohibited until separately approved.
END_FOUNDATIONAL_GOVERNANCE_WARNING

## Executive conclusion

Recommended strategy: **Option A — extract first, rename later**.

Rationale:

- extraction and rename are separate sources of risk;
- extraction tests project-boundary autonomy while preserving historical naming stability;
- No project owns the EIP root, and extraction should not adopt an EIP root or create root ownership;
- keeping `ArchitectureHarvest` during first extraction minimizes compatibility churn across roughly 266 references/files and 224 hosted-subtree files;
- rename to `MetaHarvest` should be a later semantic migration after the extracted project proves stable;
- if the two are combined, failures become harder to diagnose because path, ownership, naming, template, and evidence-reference changes all occur at once.

Target later state:

1. MetaHarvest/ArchitectureHarvest becomes an autonomous sibling project in an explicitly approved interim location.
2. Historical artifacts preserve `ArchitectureHarvest` terminology unless they are active guidance surfaces.
3. ProjectForge keeps only framework-owned integration guidance, generated-project placeholders, and compatibility notices.
4. Consumer projects keep their own local adoption/rejection/governance records.
5. Ecosystem-owned registry/interface responsibilities remain unresolved/TBD unless separately approved.
6. Compatibility shims are minimal, documented, and sunsetted after evidence that all active references have migrated.

Current readiness after this review:

- Conceptual readiness: ready.
- Operational readiness: still not ready for execution, but migration uncertainty is now reducible to explicit design tasks.
- Extraction status: extraction should remain blocked until a compatibility/verification/rollback implementation plan is approved.

## 1. Naming-strategy recommendation

### Option A — Extract first, rename later

Benefits:

- isolates project-boundary migration from semantic naming migration;
- preserves old `ArchitectureHarvest` references during the highest-risk physical move;
- reduces changes required in templates, tools, tests, reports, and historical artifacts at extraction time;
- makes rollback simpler because restoring the prior hosted path does not also reverse a terminology migration;
- supports evidence-reference stability because reports/cards/source registry paths can keep their existing name initially;
- lets the extracted project later decide its public name through its own governance.

Risks:

- the extracted sibling may initially carry an outdated name;
- conceptual `MetaHarvest` language and physical `ArchitectureHarvest` naming remain temporarily divergent;
- users/agents may continue using the old name longer than desired;
- later rename requires a second migration.

Compatibility implications:

- minimum compatibility burden at extraction time;
- ProjectForge can point to extracted `ArchitectureHarvest` as the current physical project while documenting that its conceptual purpose is MetaHarvest-like reusable non-domain knowledge;
- generated-project placeholders can remain `architecture/architectureharvest/` during first extraction.

Historical interpretability:

- strongest option. Old reports, recommendation IDs, evidence records, and adoption logs remain naturally interpretable.

Migration complexity:

- lowest first-step complexity;
- total ecosystem complexity is split across two smaller migrations.

### Option B — Rename first, extract later

Benefits:

- aligns terminology with current conceptual doctrine before physical extraction;
- makes future sibling project name cleaner;
- forces agents to stop treating ArchitectureHarvest as architecture-only.

Risks:

- high churn while still hosted inside ProjectForge;
- generated-project templates/tools/tests would need rename compatibility before extraction;
- may make later extraction harder because ProjectForge would carry transitional aliases internally;
- risks creating the false impression that conceptual rename solved operational extraction readiness.

Compatibility implications:

- requires active aliasing inside ProjectForge before project boundary changes;
- increases probability of dual-path references (`ArchitectureHarvest` and `MetaHarvest`) in the same repository.

Historical interpretability:

- weaker than Option A unless historical artifacts are protected from rewrite.

Migration complexity:

- medium/high; creates compatibility work without yet reducing ProjectForge hosting burden.

### Option C — Single migration: `ArchitectureHarvest` -> `MetaHarvest` during extraction

Benefits:

- one visible migration event;
- final state is semantically clean immediately;
- avoids living with an extracted project whose name is conceptually stale.

Risks:

- combines all failure modes: directory movement, project-boundary extraction, naming migration, template migration, test migration, tool migration, evidence-path migration, and historical-reference interpretation;
- rollback becomes more complex;
- hard to determine whether breakage is caused by extraction or rename;
- likely creates broad diffs across historical and active artifacts;
- highest risk of accidental MacroForge/local consumer edits.

Compatibility implications:

- requires the strongest shim layer;
- generated-project placeholders and ProjectForge tooling would need either dual-name support or immediate migration;
- evidence references would need explicit old->new mapping.

Historical interpretability:

- risky unless old names remain preserved in historical artifacts and an explicit alias map is maintained.

Migration complexity:

- highest.

### Naming recommendation

Choose **Option A: Extract first, rename later**.

Recommended phrasing for the extraction approval checkpoint:

```text
Approve extraction of the currently hosted ArchitectureHarvest subsystem as an autonomous sibling project, while preserving the physical/name identity `ArchitectureHarvest` for the first migration. Conceptual doctrine may describe the project as MetaHarvest-like reusable non-domain knowledge, but physical rename to `MetaHarvest` remains a later migration.
```

Confidence: 0.84
Priority: 0.79

## 2. Compatibility-strategy recommendation

Compatibility should be evidence-preserving and minimal. Do not mass-rewrite history.

### What should remain unchanged

- Historical reports, reviews, decisions, simulations, and audit artifacts.
- Old recommendation identifiers containing `architectureharvest` or `AH` when they are part of lineage.
- Adoption outcome IDs and source references that were generated under ArchitectureHarvest naming.
- Evidence reports/cards/synthesis artifacts whose content describes work performed under the old name.
- MacroForge local artifacts unless MacroForge separately approves changes.

### What should be aliased

- The old ProjectForge-local path `ArchitectureHarvest/` should receive a temporary compatibility notice or redirect after extraction, not a silent duplicate.
- Old name `ArchitectureHarvest` should be an accepted alias for the extracted project during transition.
- Generated-project references to `architecture/architectureharvest/` should remain accepted for at least one compatibility cycle.
- Documentation should define: `ArchitectureHarvest` = historical/physical first-extraction name; `MetaHarvest` = broader conceptual purpose / possible later rename.

### What should be migrated

- Active ProjectForge guidance that points agents to the hosted subsystem should be updated to point to the extracted sibling location after extraction approval.
- Active integration docs should move from "hosted subsystem" wording to "external sibling advisory project" wording.
- ProjectForge-owned tooling/tests should be updated to validate either the old placeholder path or the chosen new integration convention, but only in the implementation phase.
- Future generated-project templates should be reviewed after extraction proves stable.

### What should remain historical

- ArchitectureHarvest deep-analysis reports and comparative reports.
- Old ArchitectureHarvest-guided ProjectForge review artifacts.
- Adoption/rejection history as originally recorded.
- Historical references under `artifacts/**` and `simulation/**`.

### Compatibility principle

Compatibility should preserve interpretability, not preserve every path forever. The shim should answer, "Where did this go and how should I interpret old references?" It should not become a second living copy.

## 3. Template-migration recommendation

Scope: `templates/_shared_project/**`, especially `templates/_shared_project/architecture/architectureharvest/`.

Current template implications:

- generated projects inherit `architecture/architectureharvest/` placeholders;
- generated coherence and context policy reference ArchitectureHarvest-style advisory artifacts;
- template names are ProjectForge-owned compatibility surfaces, not MetaHarvest-owned knowledge.

Options:

### Keep `architecture/architectureharvest/`

Benefits:

- preserves existing generated-project compatibility;
- no immediate template churn during extraction;
- aligns with Option A extract-first/rename-later;
- avoids rewriting existing generated projects.

Risks:

- old name persists in future projects;
- conceptual MetaHarvest naming remains hidden from generated-project surfaces.

### Switch to `architecture/metaharvest/`

Benefits:

- clearer future conceptual name;
- better matches non-domain reusable knowledge scope.

Risks:

- breaks old path assumptions unless templates/tools/tests support both;
- high churn if done during extraction;
- may imply rename was approved when it was not.

### Support both paths

Benefits:

- strongest compatibility;
- allows staged migration.

Risks:

- creates permanent clutter if no sunset plan exists;
- doubles places agents may check;
- generated projects may diverge.

### Use something else, e.g. `architecture/advisory/` or `ecosystem/recommendations/`

Benefits:

- avoids naming project-specific dependency into generated projects;
- may better express the interface rather than the provider.

Risks:

- larger conceptual/template redesign;
- could obscure lineage to MetaHarvest;
- not necessary for extraction.

Template recommendation:

- For first extraction: keep `architecture/architectureharvest/` unchanged.
- Add no new generated-project path during extraction.
- After extraction stabilizes, perform a separate template design review to decide whether future projects should use a provider-neutral path such as `architecture/advisory/` with explicit `origin_project: MetaHarvest` metadata.
- Avoid dual-path templates unless a later rename requires them.

Preferred eventual direction:

```text
architecture/advisory/
```

with artifacts carrying explicit origin metadata, e.g. `origin_project: MetaHarvest`, rather than encoding provider identity in the folder path. This should not be part of first extraction.

## 4. Tooling/test recommendation

Relevant ProjectForge-owned surfaces:

- `tools/new_project.py`
- `tools/check_coherence.py`
- `tests/test_architectureharvest_integration.py`
- generated-project local `tools/check_coherence.py` from templates
- possibly docs/instructions referencing ArchitectureHarvest paths

Required changes for eventual extraction:

1. Identify every code/test assumption that `ArchitectureHarvest/` exists inside ProjectForge root.
2. Replace hardcoded hosted-subsystem assumptions with explicit configured/advisory-project location semantics.
3. Keep generated-project placeholder validation separate from extracted MetaHarvest project validation.
4. Update tests so they verify ProjectForge integration expectations, not MetaHarvest internals.
5. Add a path/reference validation check that fails on accidental live dependencies on the old hosted path after the extraction implementation phase.

Optional changes:

- add a config key for advisory source location;
- add a coherence warning when the compatibility shim is still present past its sunset condition;
- add a read-only integration smoke check that confirms the extracted sibling exists and has expected public docs, without taking dependency on its internal structure;
- add a template mode flag later if generated projects move from `architecture/architectureharvest/` to provider-neutral advisory folders.

Compatibility concerns:

- `tests/test_architectureharvest_integration.py` likely encodes current folder expectations and should not be blindly renamed;
- `tools/check_coherence.py` should not start governing MetaHarvest internals after extraction;
- ProjectForge should validate only its own integration promises and generated-project placeholders;
- MetaHarvest should own its own coherence once extracted.

Migration order:

1. Pre-extraction: write implementation dry-run identifying exact code/test references.
2. Pre-extraction: add tests for the intended post-extraction integration contract while old state still exists.
3. Extraction implementation: update tools/tests to use explicit location/shim policy.
4. Post-extraction: run ProjectForge tests/coherence and MetaHarvest's own checks separately.
5. Later rename: update tests only after naming decision is separately approved.

## 5. Evidence-reference recommendation

Evidence must remain traceable across extraction without making ProjectForge or MetaHarvest claim ownership of consumer-local decisions.

Surfaces:

- `ArchitectureHarvest/source_registry.yaml`
- recommendation candidates/proposals
- adoption logs
- evidence references in reports/cards/synthesis artifacts
- relevance maps
- external source references
- generated-project local ArchitectureHarvest placeholders

Strategy:

1. Preserve original evidence IDs and source identifiers.
2. Preserve old `ArchitectureHarvest` names in historical artifacts.
3. Add a future extraction manifest during implementation containing:
   - old path;
   - new path;
   - artifact classification;
   - owner after extraction;
   - historical status;
   - compatibility handling;
   - checksum or file identity where useful.
4. Keep `source_registry.yaml` with MetaHarvest/ArchitectureHarvest-owned evidence unless it contains ProjectForge-only runtime configuration.
5. Keep external source references stable; do not move `external_sources/` unless a separate source-storage decision approves it.
6. Use relative paths within the extracted project where possible after extraction.
7. Use explicit `origin_project`, `target_project`, and `consumer_project` fields in future recommendation/adoption/evolution artifacts instead of relying on folder location.
8. Treat relevance maps carefully:
   - generic and ProjectForge relevance maps may move as MetaHarvest records or be split into project-local mirrors;
   - MacroForge relevance maps must not be treated as permission to modify MacroForge.

Evidence-reference anti-goals:

- no mass rewriting of historical evidence;
- no hidden duplication of evidence records;
- no inference that ProjectForge owns MetaHarvest evidence after extraction;
- no inference that MetaHarvest owns consumer decisions.

## 6. Historical-artifact recommendation

Historical artifacts should remain immutable by default.

Recommendation:

- Preserve `ArchitectureHarvest` terminology in historical artifacts.
- Do not rewrite old reports, reviews, decisions, simulations, adoption IDs, or source evidence just to match current naming.
- If needed, add a narrow historical interpretation notice in active docs or compatibility shim, not inside every old artifact.
- Only update active guidance surfaces whose job is to guide current agents.

Rationale:

- historical names are evidence of what was true at the time;
- rewriting history risks corrupting lineage;
- old terminology helps explain why older artifacts have `AH`, `architectureharvest`, or `ArchitectureHarvest` IDs;
- compatibility notices are cheaper and safer than mass edits.

## 7. Transitional-artifact recommendation

Transitional categories from prior inventory:

- `ArchitectureHarvest/relevance_maps/projectforge/**`
- `ArchitectureHarvest/relevance_maps/macroforge/**`
- generated-project `architecture/architectureharvest/` placeholders
- ProjectForge root guidance referring to hosted ArchitectureHarvest
- ProjectForge tools/tests validating hosted assumptions
- workspace registry references

### Should disappear after migration

- ProjectForge statements that ArchitectureHarvest is physically hosted inside ProjectForge.
- Tests that assert the internal hosted path as a permanent requirement.
- Any temporary compatibility notice after all active references are migrated and sunset criteria are met.

### Should become compatibility shims

- old `ArchitectureHarvest/` path in ProjectForge root, if extraction physically moves it;
- active docs explaining old name/new location;
- generated-project placeholder interpretation if future templates move to provider-neutral naming.

### Should remain permanently

- historical artifacts and historical references;
- recommendation/adoption lineage IDs;
- consumer-local adoption/rejection decisions;
- a short stable glossary mapping ArchitectureHarvest and MetaHarvest terminology.

### Indicate unresolved ownership ambiguity

- relevance maps for named consumer projects living inside MetaHarvest;
- workspace registry semantics if extraction tries to make it ecosystem-level;
- any future active contracts/registries without an ecosystem owner;
- external source storage if both ProjectForge and MetaHarvest expect to read/write it.

Recommendation:

Resolve relevance-map ownership before physical extraction. Either classify each map as MetaHarvest-owned relevance evidence or consumer-owned mirror. Do not let ambiguous relevance maps become cross-project authority.

## 8. Compatibility-shim recommendation

Minimum acceptable shim set for first extraction:

1. A ProjectForge-root compatibility notice at the old `ArchitectureHarvest` location or adjacent active docs, saying the subsystem was extracted and where it lives.
2. A naming glossary:
   - `ArchitectureHarvest`: historical/initial physical name;
   - `MetaHarvest`: conceptual broader purpose / possible future rename.
3. A path mapping manifest for moved artifacts.
4. ProjectForge active docs updated to point to extracted sibling location.
5. Tooling/tests updated to avoid treating old hosted path as authoritative.
6. Historical references left unchanged.

What not to build:

- a permanent duplicated tree;
- an automatic sync layer;
- service-based redirects;
- ecosystem registry infrastructure;
- broad alias support across every historical artifact;
- generated-project dual-folder scaffolds unless later approved.

Sunset criteria:

- ProjectForge coherence/tests pass without depending on the old hosted tree;
- new generated projects do not require the old hosted path to exist;
- active ProjectForge docs point to the extracted sibling location;
- path-reference validation shows no live ProjectForge-owned dependency on old `ArchitectureHarvest/` internals except the shim notice/manifest;
- at least one post-extraction review confirms historical references remain interpretable.

Removal criteria:

- shim has been present for at least one completed post-extraction task cycle;
- no active tooling/templates/docs require it;
- removal dry-run identifies only expected historical references;
- rollback plan no longer depends on it;
- explicit approval is granted for shim removal.

## 9. Verification strategy

Do not execute during this design task. Eventual extraction should have this verification plan ready before approval.

### Coherence validation

- Run ProjectForge root coherence after every extraction implementation stage.
- Run extracted MetaHarvest coherence if it has its own checker, or a minimum file/schema validation if not yet scaffolded.
- Run generated-project sample coherence for a freshly generated project if template/tooling changes are part of the extraction implementation.

### Doctrine consistency validation

Check that active doctrine still states:

- projects are autonomous;
- recommendations are advisory;
- no project owns the EIP root;
- conceptual readiness and physical readiness are separate;
- ProjectForge does not govern extracted MetaHarvest;
- MetaHarvest does not govern ProjectForge, MacroForge, EII, or future projects.

### Architecture-reality audit

- Run `python3 tools/architecture_reality_audit.py --project . --json` before extraction approval if many tasks have occurred since last audit.
- Run it after extraction implementation to detect docs-vs-reality drift.
- If MetaHarvest becomes a ProjectForge-managed project, run its own audit once scaffolded.

### Path validation

- Search for active ProjectForge-owned references to old hosted paths.
- Distinguish historical references from live operational dependencies.
- Validate path mapping manifest old->new entries.
- Confirm no MacroForge files changed unless explicitly approved.

### Template validation

- Generate a temporary sample project if templates are changed.
- Confirm placeholder paths and generated coherence behavior.
- Confirm no duplicate advisory directories unless explicitly intended.

### Tooling validation

- Run ProjectForge tests focused on `new_project`, coherence, and ArchitectureHarvest/MetaHarvest integration expectations.
- Confirm tools validate ProjectForge contracts only, not extracted MetaHarvest internals.

### Reference validation

- Validate Markdown/YAML references in moved artifacts where practical.
- Confirm historical references remain understandable through glossary/manifest.

### Lineage validation

- Sample recommendation candidate -> review -> adoption/rejection/outcome chain.
- Verify IDs remain stable.
- Verify origin/target/consumer project fields or interpretation remain clear.

### Evidence validation

- Validate `source_registry.yaml` parses.
- Confirm external source references still resolve or are intentionally historical.
- Check sample project cards, component cards, reports, synthesis, and contradiction records.

## 10. Rollback strategy

Minimum rollback capability:

- pre-extraction git clean/staged boundary check;
- no unrelated changes in same migration;
- a recorded extraction manifest listing every moved/changed path;
- ability to restore the hosted `ArchitectureHarvest/` tree exactly;
- ability to revert ProjectForge docs/tooling/tests/templates independently;
- compatibility shim must not be the only copy of moved data;
- post-rollback coherence/test commands recorded.

Rollback triggers:

- ProjectForge coherence blocks;
- ProjectForge tests fail due to integration changes;
- extracted MetaHarvest cannot validate its own core artifacts;
- evidence registry or major YAML artifacts fail parsing;
- generated-project template validation fails;
- active references cannot distinguish historical from live dependencies;
- MacroForge or EII are modified accidentally;
- ownership ambiguity causes MetaHarvest to appear to govern consumer projects;
- rollback path is discovered incomplete during dry-run.

Rollback validation:

- old hosted path restored or compatibility state documented;
- ProjectForge coherence passes;
- relevant ProjectForge tests pass;
- no unintended MacroForge/EII diffs;
- path-reference validation returns only pre-existing historical references;
- git status shows only expected rollback artifacts or is clean after revert;
- state/handoff explains rollback reason and next decision point.

## 11. Extraction-location recommendation

Assumption: MetaHarvest may become a sibling project before EIP-root adoption.

Options:

### Sibling repository beside ProjectForge, e.g. `/home/mkkto/srv/metaharvest` or `/home/mkkto/srv/architectureharvest`

Benefits:

- simple mental model;
- ProjectForge and MetaHarvest become peers;
- no need to adopt EIP root;
- aligns with existing `/home/mkkto/srv/projectforge` pattern;
- easy to later relocate under a future approved ecosystem root if needed.

Risks:

- `/home/mkkto/srv/` is not a formal ecosystem root;
- sibling placement may be mistaken for equal ecosystem authority unless docs are explicit;
- later EIP-root adoption may require another move.

### Sibling project inside a temporary projects root

Benefits:

- can group autonomous projects without claiming EIP-root authority;
- may make future relocation more systematic.

Risks:

- creating a temporary root starts to look like ecosystem infrastructure;
- may violate the instruction not to implement ecosystem infrastructure if done prematurely;
- adds one more concept to govern.

### Remain hosted until EIP root exists

Benefits:

- avoids interim path churn;
- keeps current working state stable.

Risks:

- delays de-hosting despite conceptual readiness;
- continues filesystem-location ambiguity;
- ProjectForge keeps hosting a separable purpose longer than necessary.

### Preferred interim location

For first extraction, prefer a simple sibling path beside ProjectForge, preserving the first-extraction physical name:

```text
/home/mkkto/srv/architectureharvest
```

If the rename is separately approved later, rename/migrate to:

```text
/home/mkkto/srv/metaharvest
```

Rationale:

- aligns with Option A extract-first/rename-later;
- avoids adopting an EIP root;
- minimizes simultaneous naming/path changes;
- makes ProjectForge and ArchitectureHarvest peers;
- keeps future EIP-root relocation as an independent decision.

Alternative if Mikkel strongly prefers semantic naming despite extra risk:

```text
/home/mkkto/srv/metaharvest
```

But that effectively combines extraction with rename and should be treated closer to Option C.

## 12. Complete migration sequence

### Phase 0 — Preconditions

- Confirm explicit L4 approval for extraction planning implementation is not yet extraction.
- Confirm no commit/staging boundary ambiguity.
- Confirm MacroForge and EII are excluded unless separately approved.
- Run current coherence and doctrine checks.

### Phase 1 — Naming decision

- Approve Option A: extract current `ArchitectureHarvest` first; rename later.
- Record that `MetaHarvest` remains conceptual broader purpose until later rename decision.
- Record that historical terminology remains valid.

### Phase 2 — Compatibility preparation

- Produce an extraction manifest design with old path, new path, owner, historical status, shim handling, and validation command.
- Design old-path compatibility notice.
- Define glossary and naming alias rules.
- Decide shim sunset/removal criteria.

### Phase 3 — Template preparation

- Keep current generated-project `architecture/architectureharvest/` placeholders for first extraction.
- Identify exact template references but do not rename them during extraction.
- Defer provider-neutral `architecture/advisory/` review until after extraction is stable.

### Phase 4 — Tooling preparation

- Inventory hardcoded `ArchitectureHarvest/` assumptions in tools/tests.
- Design ProjectForge integration contract: ProjectForge validates pointer/shim/template behavior, not MetaHarvest internals.
- Plan tests before code changes.

### Phase 5 — Evidence preparation

- Classify all moved artifacts by ownership.
- Preserve source registry and evidence IDs.
- Plan path mapping for source registry, reports, cards, synthesis, recommendations, adoption logs, and relevance maps.
- Resolve relevance-map ownership before extraction.

### Phase 6 — Verification preparation

- Define exact commands for ProjectForge coherence/tests.
- Define exact commands for extracted MetaHarvest validation.
- Define path/reference validation script behavior.
- Define sample lineage/evidence checks.
- Define generated-project template validation if templates change.

### Phase 7 — Rollback preparation

- Confirm clean/known worktree boundary.
- Record exact pre-extraction tree status.
- Prepare restore plan for moved tree and changed ProjectForge integration files.
- Define rollback triggers and validation commands.

### Phase 8 — Extraction approval checkpoint

Required approval should explicitly state:

- extraction location;
- name retained during first extraction;
- artifact classes to move;
- artifact classes to leave;
- compatibility shim scope;
- no MacroForge/EII modifications;
- no EIP-root adoption;
- rollback acceptance criteria.

### Phase 9 — Extraction execution

Only after approval:

- move the approved MetaHarvest/ArchitectureHarvest-owned subtree;
- add compatibility notice/manifest;
- update ProjectForge active pointers;
- update tooling/tests as planned;
- do not rewrite historical artifacts;
- do not modify consumer projects.

### Phase 10 — Post-extraction validation

- Run ProjectForge coherence/tests.
- Run extracted project validation.
- Run path/reference validation.
- Run lineage/evidence samples.
- Run architecture-reality audit.
- Verify no MacroForge/EII diffs.
- Verify nothing unintended staged.

### Phase 11 — Stabilization

- Complete at least one normal ProjectForge task cycle using extracted advisory project references.
- Record any broken references or agent confusion.
- Decide whether to keep, reduce, or remove shims.

### Phase 12 — Shim-removal review

- Run removal dry-run.
- Confirm active references migrated.
- Confirm historical references remain interpretable.
- Remove only after explicit approval.

### Phase 13 — Rename review, if desired

- Separately review `ArchitectureHarvest` -> `MetaHarvest` rename.
- Reuse the same readiness doctrine: naming migration requires path inventory, compatibility, verification, rollback, and evidence stability.
- Consider provider-neutral generated-project paths only then.

## 13. Risks, conflicts, and open questions

### Risks

- old name persists too long after extraction;
- shims become permanent clutter;
- historical artifacts are over-edited and lose interpretability;
- ProjectForge tools accidentally validate MetaHarvest internals;
- extracted MetaHarvest accidentally claims ownership of consumer adoption decisions;
- generated-project placeholders encode provider identity longer than desired;
- future EIP-root adoption causes a second relocation;
- path aliases mask broken live references instead of forcing cleanup.

### Conflicts

No hard doctrine conflict found.

Soft conflicts:

- conceptual name `MetaHarvest` is broader than physical name `ArchitectureHarvest`;
- generated-project placeholders are provider-named rather than interface-named;
- relevance maps mix reusable fit evidence with target-project locality;
- sibling location under `/home/mkkto/srv/` is practical but not a formal ecosystem root.

### Open questions

1. Should the first extracted sibling be named `/home/mkkto/srv/architectureharvest` or `/home/mkkto/srv/metaharvest` despite the recommended Option A?
2. Which relevance maps are authoritative MetaHarvest fit evidence versus consumer-local mirrors?
3. Should generated projects eventually use provider-neutral `architecture/advisory/` paths?
4. What minimum extracted-project governance scaffold is required: full ProjectForge-generated project or lightweight existing docs first?
5. Should `external_sources/` remain ProjectForge-local, move with MetaHarvest, or be governed by a later evidence-store decision?
6. How long should compatibility shims live: fixed number of task cycles, reference-count based, or manual review only?
7. Should the extracted project have its own git repository immediately or remain in a multi-project local tree until stable?

## Final recommendation

Do not extract yet.

When extraction is later approved, use a two-stage migration:

1. **Extract current `ArchitectureHarvest` as an autonomous sibling while preserving the name.**
2. **After stability, separately review rename to `MetaHarvest` and possible generated-project advisory-path modernization.**

This minimizes first-migration risk, preserves historical interpretability, and keeps extraction independent from EIP-root adoption while avoiding premature ecosystem infrastructure.
