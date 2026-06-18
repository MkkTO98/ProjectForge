# PF-AH-REC-010 lifecycle/checkpoint validation results

Created UTC: 2026-06-06T11:57:25Z

Status: completed

Recommendation under test:
- PF-AH-REC-010 — Test whether the lifecycle/checkpoint vocabulary actually reduces handoff ambiguity in one real long-running ProjectForge task before standardizing it.

Final recommendation:
- Adopt, narrowly.

Adoption outcome record:
- `ArchitectureHarvest/adoption_log/O-20260606-lifecycle-checkpoint-vocabulary.yaml`

Experiment task:
- `artifacts/tasks/T-20260606-lifecycle-checkpoint-validation.md`

Checkpoint sidecar:
- `artifacts/tasks/T-20260606-lifecycle-checkpoint-validation.checkpoints.yaml`

## Scope compliance

The experiment used only the experiment-specific artifacts defined in the proposal:

- `artifacts/tasks/T-20260606-lifecycle-checkpoint-validation.md`
- `artifacts/tasks/T-20260606-lifecycle-checkpoint-validation.checkpoints.yaml`
- `state/active_goal.md`
- `context/latest_handoff.md`
- `ArchitectureHarvest/adoption_log/O-20260606-lifecycle-checkpoint-vocabulary.yaml`
- `artifacts/reports/R-20260606-lifecycle-checkpoint-validation-results.md`

No templates, governance frameworks, generated-project structures, ArchitectureHarvest frameworks, ProjectForge operating procedures, external source records, or external source clones were modified.

No broader ArchitectureHarvest harvesting was performed.

## Baseline measurements

Baseline workflow:

- Normal ProjectForge startup and task-context reconstruction before the checkpoint sidecar existed.

Baseline files read to resume/understand task state:

1. `CONSTITUTION.md`
2. `state/active_goal.md`
3. `state/project_state.md`
4. `state/architecture.md`
5. `context/latest_handoff.md`
6. `ArchitectureHarvest/experiments/PF-AH-REC-010-lifecycle-checkpoint-validation-experiment.yaml`

Baseline metrics:

- files_read_to_resume: 6
- resume_steps_to_current_phase: 4
- ambiguous_questions_count: 3
- session_search_or_broad_context_needed: false
- handoff_chars: 2650
- resume_confidence_rating_1_to_5: 3
- answerable_resume_questions_percent: 62.5

Baseline resume-question coverage:

1. Current lifecycle status: partly answerable; active status came from current user request, not a durable lifecycle field.
2. Completed since previous checkpoint: not answerable; no checkpoint existed.
3. Exact next action: answerable from user request and experiment proposal.
4. Verification remains: answerable from experiment proposal.
5. Decisions or approvals changed plan: partly answerable; approval came from current user request, not a durable file-backed checkpoint.
6. Files in scope: answerable from experiment proposal.
7. What should not be touched: answerable from experiment proposal.
8. What would make the task complete: answerable from user request and proposal.

Baseline observation:

The normal workflow was workable, but resume clarity depended on combining current chat context with the experiment proposal. Missing or ambiguous areas were current lifecycle phase, completed-since-prior state, and file-backed approval/interruption state.

## Experiment measurements

Treatment workflow:

- Priority 1 context plus checkpoint sidecar.

Treatment files read:

1. `state/active_goal.md`
2. `state/project_state.md`
3. `state/architecture.md`
4. `context/latest_handoff.md`
5. `artifacts/tasks/T-20260606-lifecycle-checkpoint-validation.checkpoints.yaml`

Treatment metrics:

- files_read_to_resume: 5
- resume_steps_to_current_phase: 2
- ambiguous_questions_count: 1
- session_search_or_broad_context_needed: false
- handoff_chars: 1197
- resume_confidence_rating_1_to_5: 4
- answerable_resume_questions_percent: 87.5
- checkpoint_update_overhead_minutes: 8
- contradiction_count: 0

Treatment resume-question coverage:

1. Current lifecycle status: answerable from `lifecycle_status: active` / `verifying`.
2. Completed since previous checkpoint: answerable from `completed_since_parent`.
3. Exact next action: answerable from `next_action`.
4. Verification remains: answerable from `verification_state` and latest handoff.
5. Decisions or approvals changed plan: answerable from `decisions_since_parent`.
6. Files in scope: partly answerable; resume files and task/report/outcome pointers were clear, but the complete exact file set was split across artifacts.
7. What should not be touched: answerable from active goal, latest handoff, and context budget hint.
8. What would make the task complete: answerable from next action and validation plan.

## Reviewer observations

Positive observations:

- The checkpoint sidecar made the current phase, next action, completed work, verification state, and context budget explicit.
- The resume pointer shortened reconstruction.
- Treatment required fewer files than baseline.
- The vocabulary stayed within the approved terms.
- No graph/runtime vocabulary was introduced.
- No external source inspection or broad project exploration was needed.

Negative observations:

- The sidecar creates duplicate state if not kept compact and current.
- The `files in scope` question remained partly ambiguous because the exact output paths were not all present in the sidecar.
- The YAML language server associated the `artifacts/tasks/*.yaml` path with an Ansible schema and reported diagnostics, even though the YAML parsed correctly. This is a tooling-location friction point, not a semantic failure.

## Threshold evaluation

### Adopt threshold

Required:

- answerable_resume_questions_percent >= 80: met, 87.5
- ambiguous_questions_count_after <= 1: met, 1
- files_read_to_resume_after <= files_read_to_resume_before: met, 5 <= 6
- checkpoint_update_overhead_minutes <= 10: met, 8
- contradiction_count == 0: met, 0
- verification_passed == true: met

Adopt threshold result:

- Met.

### Modify threshold

Some evidence also supports a future modification:

- The `files in scope` field was not fully answerable from the checkpoint sidecar alone.
- If this ambiguity repeats, future vocabulary should add an exact in-scope-files field or require `context_budget_hint` to include output artifact paths.

This does not block narrow Adopt because the predefined Adopt threshold allows one ambiguous question.

### Reject threshold

Reject conditions were not met:

- answerable coverage was not below 60%.
- ambiguity improved from 3 to 1.
- files read decreased from 6 to 5.
- contradiction count was zero.
- overhead was below 20 minutes.

### Retire threshold

Retire conditions were not met:

- The selected task type was suitable.
- The recommendation did not only solve a hypothetical failure mode.
- The experiment produced measurable evidence.

## Outcome weighting

Appropriate weighting update:

- Record `ecosystem_outcome_class: proven_successful_in_ecosystem` and `recommendation_delta: increase` in the adoption outcome record.

Central outcome model file update:

- Not performed.

Reason:

The user explicitly constrained the experiment to the experiment-specific artifacts defined in the proposal and prohibited ArchitectureHarvest framework changes. The adoption outcome record carries the weighting effect for future ArchitectureHarvest reviews without changing the central outcome model/framework.

## Final recommendation

Recommendation:

- Adopt, narrowly.

Meaning:

- Adopt the minimal checkpoint sidecar concept as proven useful for this single ProjectForge architecture/governance closeout experiment.
- Do not generalize it to ordinary tasks.
- Do not modify templates or ProjectForge operating procedures yet.
- Treat the result as medium-confidence local ecosystem evidence, not universal proof.

Suggested future interpretation:

- One more long-running ProjectForge governance task should repeat the experiment before any broader policy/template change.
- If the file-scope ambiguity repeats, classify the next result as Modify and narrow the vocabulary.

## Final validation

Initial validation after creating outcome/report:

- Dry-run validation: `valid: simulation/dry_runs/20260606_135706-dry-run.md`.
- YAML parse: checkpoint, outcome, and experiment YAML artifacts parsed successfully; experiment YAML checks passed.
- Full ProjectForge tests: `66 passed in 6.06s`.
- Context health: `blocks: []`, `warnings: []`.
- ProjectForge coherence: `blocks: []`, `warnings: []`.
- Architecture-to-Reality audit JSON mode: `blocks: []`, `warnings: []`.

Final post-closeout validation after updating active goal, latest handoff, task status, checkpoint sidecar, and this report:

- Dry-run validation: `valid: simulation/dry_runs/20260606_135706-dry-run.md`.
- YAML parse: `parsed final experiment artifacts: 3 checkpoints, outcome adopted`.
- Full ProjectForge tests: `66 passed in 6.07s`.
- Context health: `blocks: []`, `warnings: []`.
- ProjectForge coherence: `blocks: []`, `warnings: []`.
- Architecture-to-Reality audit JSON mode: `blocks: []`, `warnings: []`.
