# T-20260606 lifecycle/checkpoint validation

Status: completed

Created UTC: 2026-06-06T11:57:25Z

## Task

Execute the PF-AH-REC-010 validation experiment exactly as designed.

Goal: determine whether a minimal lifecycle/checkpoint vocabulary improves ProjectForge task handoff, interruption recovery, and resume clarity.

## Scope boundaries

Allowed experiment-specific files:

- `artifacts/tasks/T-20260606-lifecycle-checkpoint-validation.md`
- `artifacts/tasks/T-20260606-lifecycle-checkpoint-validation.checkpoints.yaml`
- `state/active_goal.md`
- `context/latest_handoff.md`
- `ArchitectureHarvest/adoption_log/O-20260606-lifecycle-checkpoint-vocabulary.yaml`
- `artifacts/reports/R-20260606-lifecycle-checkpoint-validation-results.md`

Do not modify:

- templates
- governance frameworks
- generated-project structures
- ProjectForge operating procedures
- ArchitectureHarvest frameworks
- external source records or clones

## Baseline workflow measurement

Baseline measurement was taken before creating the checkpoint sidecar, using normal ProjectForge startup and task context.

Files read to resume/understand task state:

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

1. Current lifecycle status: partly answerable; active task came from current user request, not a durable lifecycle field.
2. Completed since previous checkpoint: not answerable; no checkpoint existed.
3. Exact next action: answerable from user request and experiment proposal.
4. Verification remains: answerable from experiment proposal.
5. Decisions or approvals changed plan: partly answerable; approval came from current user request, not a durable file-backed checkpoint.
6. Files in scope: answerable from experiment proposal.
7. What should not be touched: answerable from experiment proposal.
8. What makes the task complete: answerable from user request and proposal.

Baseline observations:

- The normal ProjectForge artifacts were sufficient to start work.
- Resume clarity depended on combining current chat, the experiment proposal, and startup context.
- The missing fields were mostly current lifecycle phase, completed-since-prior state, and approval/interruption state.

## Experiment checkpoints

Checkpoint sidecar:

- `artifacts/tasks/T-20260606-lifecycle-checkpoint-validation.checkpoints.yaml`

Current checkpoint:

- `CKPT-20260606-lifecycle-checkpoint-01`

## Measurement plan

Treatment measurement will use Priority 1 context plus the checkpoint sidecar:

- `state/active_goal.md`
- `state/project_state.md`
- `state/architecture.md`
- `context/latest_handoff.md`
- `artifacts/tasks/T-20260606-lifecycle-checkpoint-validation.checkpoints.yaml`

Treatment will score the same eight resume questions and compare against baseline.
