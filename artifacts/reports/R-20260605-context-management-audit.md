# Audit Report: Context-Management Architecture Hardening

Date: 2026-06-05T10:24:41Z
Status: implemented after audit
Scope: ProjectForge root, generated-project templates, context builders, context health, agent instructions, documentation, and tests.

## Executive conclusion

ProjectForge already had most of the MacroForge audit recommendations in place from the prior hardening pass: summary-first context building, raw-log exclusion, generated `active_context.md` handling, project-wide review mode with justification, generated-project template inheritance, folder summaries, and coherence wiring.

The remaining gaps were not wholesale architecture gaps. They were enforcement/clarity gaps:

1. The context-loading hierarchy existed in prose but was not encoded as an explicit Priority 1/2/3 hierarchy in policy, manifests, generated AGENTS instructions, and the context-builder audit output.
2. `tools/build_context.py` still treated broader project summaries as default normal context instead of Priority 3 expansion.
3. `tools/context_health.py` did not detect stale generated context bundles or existing project-wide-review audit misuse after a bundle had already been generated.
4. Tests covered context health and governance mode, but not the strict Priority 1/2/3 ordering or stale/unjustified generated-bundle health failures.

## Objective-by-objective audit

### A. Context Loading Hierarchy

Already implemented:
- Summary-first retrieval existed in `context/context_policy.yaml`, `tools/build_context.py`, `AGENTS.md`, template `AGENTS.md`, and docs.
- Folder summaries were used before broad tree reads.
- Raw logs and whole-project dumps were excluded from normal context.

Partially implemented:
- The exact requested hierarchy was not represented as an explicit Priority 1/2/3 policy object.
- `tools/build_context.py` included compact project summaries by default, which is useful but not strict Priority 1 behavior.

Implemented in this pass:
- Added explicit `context_loading_hierarchy` to root and template context policies.
- Reordered builder defaults so normal context starts with `state/active_goal.md`, `state/project_state.md`, `state/architecture.md`, and `context/latest_handoff.md`.
- Moved broader project summaries to Priority 3, included by default only for governance/review mode.
- Updated root/template AGENTS, role files, instructions, context manifests, skills, README, and operator manual.

### B. State Artifact Hygiene

Already implemented:
- Primary state/current-state wording existed in policy, AGENTS, handoff, and context-health checks.
- `tools/context_health.py` checked state-file size and historical-ledger markers.

Weaknesses:
- `state/project_state.md` is still under the limit but contains multiple current-hardening sections and is trending toward dense status inventory. It remains acceptable, but future closeout should keep it as compact pointers.

Implemented in this pass:
- Reinforced hierarchy/policy language in instructions and manifests.
- No historical material was added to primary state beyond compact current-policy pointers.

### C. Active Context Handling

Already implemented:
- `context/active_context.md` was marked as generated output, not startup context.
- `tools/build_context.py` writes `active_context.md`, `context_manifest.json`, `context_audit.json`, and `context_audit.md`.

Partially implemented:
- Health checks warned on oversized non-project-wide generated bundles but did not warn on stale generated bundles.

Implemented in this pass:
- `context_health.py` now warns on stale generated `context/active_context.md` based on configured `generated_context_stale_hours`.
- Root and template policies set `generated_context_stale_hours: 168`.

### D. Skill Loading Optimization

Already implemented:
- `SMALL_SKILLS_POLICY.md`, AGENTS/instructions, and the ProjectForge skill already say skills are on-demand procedural references, not universal startup context.

Gap status:
- No ProjectForge-local mechanism injects all skills into every session; Hermes global skill discovery is external to ProjectForge. Therefore no additional eager-loading subsystem needed replacement.

Implemented in this pass:
- Preserved on-demand skill language and strengthened adjacent hierarchy instructions.

Estimated overhead:
- ProjectForge project-local skills are not automatically loaded by `tools/build_context.py` or generated AGENTS. Overhead is effectively 0 tokens until an agent explicitly reads a relevant skill file. The global Hermes skill catalog is outside ProjectForge's repository-local initialization logic.

### E. Context Health Monitoring

Already implemented:
- Root and generated `tools/context_health.py` existed.
- Root/generated `tools/check_coherence.py` invoked context health.
- Tests checked oversized primary state and large non-project-wide active context.

Missing:
- Stale generated bundles were not detected.
- Existing `context_audit.json` files with `project_wide_review` but no justification were not detected by health checks.
- Existing project-wide review bundles with raw logs allowed were not blocked by health checks.

Implemented in this pass:
- Added stale generated-bundle warning.
- Added blocks for unjustified existing `project_wide_review` audit records.
- Added blocks for project-wide review audits with `raw_logs_excluded=false`.

### F. Project-Wide Review Governance

Already implemented:
- `tools/build_context.py --context-mode project_wide_review` requires `--review-justification`.
- Project-wide review uses summaries and excludes raw logs by default.
- `tools/select_model.py` accepts project-wide context audits when justified.

Partially implemented:
- Health checks did not catch misuse in already-generated audit files.

Implemented in this pass:
- Context health now detects generated project-wide-review audit misuse after the fact.

### G. Template and Framework Inheritance

Already implemented:
- Shared templates included AGENTS, context policy, context tools, and health/coherence wiring.

Implemented in this pass:
- Updated root and `templates/_shared_project/` copies of policies, manifests, instructions, agents, skills, build-context tool, and context-health tool.
- Future generated projects inherit the stricter hierarchy and health checks.

### H. Backward Compatibility

Preserved:
- Existing project structures remain valid.
- Old context policies without new fields fall back to defaults in `tools/context_health.py` and `tools/build_context.py`.
- `project_summary.md` remains supported as Priority 3 governance/review context rather than being removed.
- Existing generated projects can copy or receive the updated `context_policy.yaml`, `tools/context_health.py`, `tools/build_context.py`, and AGENTS/instructions without schema-breaking changes.

## Migration plan

For existing ProjectForge-generated projects:

1. Copy or regenerate these files from the updated shared template when safe:
   - `AGENTS.md`
   - `context/context_policy.yaml`
   - `context/context_manifest.yaml`
   - `instructions/GENERAL_INSTRUCTIONS.md`
   - `instructions/SMALL_SKILLS_POLICY.md`
   - `skills/context-budgeting.md`
   - `tools/build_context.py`
   - `tools/context_health.py`
   - `tools/check_coherence.py` if not already wired to context health
2. Run:
   - `python3 tools/context_health.py --project . --json`
   - `python3 tools/check_coherence.py --project . --json`
3. If blocked/warned:
   - Compress primary state into concise current-state pointers.
   - Move long verification/session history into `artifacts/reports/`, `artifacts/handoffs/`, or `logs/derived/`.
   - Regenerate stale `context/active_context.md` with `tools/build_context.py` for the current task.
   - For any project-wide review bundle, add a real `review_justification` or regenerate in normal/governance mode.
4. Refresh affected `_SUMMARY.md` files and rerun coherence.

## Implementation plan used

1. Audit authoritative state, policy, handoff, decisions, summaries, and existing context/coherence tools.
2. Preserve already-functioning mechanisms.
3. Patch the missing strict hierarchy in policy, builder, manifests, instructions, agents, skills, README, and operator manual.
4. Extend context health for stale generated bundles and project-wide review misuse.
5. Add regression tests for hierarchy ordering, stale bundle detection, and unjustified project-wide-review audit blocking.
6. Run narrow tests, full tests, context health, root coherence, generated-project inheritance/coherence checks.
7. Update durable report/state/handoff/summaries and rerun final verification.

## Expected token-efficiency impact

Normal context bundles should now save the tokens formerly consumed by broad project summaries when a task does not need Priority 3 context. In ProjectForge root this is modest, but in generated projects with mature summaries it should typically save hundreds to low-thousands of tokens per normal task. The larger impact is behavioral: future agents get a machine-readable hierarchy and tests that prevent repository-wide exploration, stale bundle reuse, and unjustified project-wide context from becoming defaults.
