# Framework Improvement Notice Doctrine Proposal

Status: proposed
Task type: Framework Improvement Notice Doctrine
Created: 2026-06-14T04:51:35Z
Project: ProjectForge

## Scope

This is a doctrine and governance proposal only.

This proposal does not implement automation, propagation, migration, background processes, existing-project modification, automatic notices, review workflows, template changes, or enforcement systems.

## 1. Framework improvement notice doctrine

A framework improvement notice is a lightweight advisory record that communicates a significant ProjectForge framework improvement to autonomous instantiated projects without changing those projects.

The notice exists to preserve this doctrine:

```text
ProjectForge improvement -> improvement notice -> project review -> project decision -> optional adoption
```

A notice is not a command. A notice is not a migration. A notice is not a task assignment. A notice is not evidence that an existing project is stale or non-compliant.

A notice says: ProjectForge learned something reusable; this may be relevant to projects that share the problem; each project should decide locally whether to adopt, partially adopt, defer, reject, or mark the notice superseded.

### Framework learning principle

Every framework improvement notice should answer:

1. What recurring problem caused this improvement?
2. What future projects benefit from it?
3. Why should this become framework behavior instead of project-specific behavior?

If those questions cannot be answered, the change is probably project-specific, experimental, or too weak for notice-level communication.

## 2. What constitutes a framework improvement

A framework improvement is a durable ProjectForge change that affects how future projects may be created, governed, structured, handed off, reviewed, delegated, or maintained as agent-assistable systems.

Framework improvement categories:

- constitutional or governance doctrine;
- project creation/questioning doctrine;
- artifact standards for decisions, tasks, reports, dry-runs, handoffs, summaries, or state;
- handoff and context standards;
- coherence, audit, verification, or dry-run expectations;
- delegation infrastructure or role/worker doctrine;
- worker infrastructure expectations, activation rules, or dormant-role doctrine;
- ArchitectureHarvest doctrine, recommendation rules, or advisory boundaries;
- inheritance behavior or scaffold expectations for future projects;
- permission, safety, or escalation defaults;
- local-execution/cloud-governance routing doctrine;
- recurring lessons that should shape future project scaffolds.

Not every ProjectForge edit is a framework improvement.

Notices are not needed for:

- typo fixes;
- local documentation cleanup with no governance meaning;
- internal implementation refactors that do not affect future project behavior;
- tests that only preserve existing behavior;
- one-off project-specific learning that has not been generalized;
- stale-summary cleanup;
- generated artifact refreshes;
- experimental ideas not yet accepted as ProjectForge doctrine or future inheritance behavior.

## 3. Which changes deserve notices

Notices should be created only for significant framework improvements.

Significance is determined by impact, not file count.

A change deserves a notice when at least one of these is true:

1. It changes future inheritance or generated-project expectations.
2. It changes how projects should create, store, review, or close out governance artifacts.
3. It changes task/handoff/context/summarization expectations in a way existing projects might benefit from adopting.
4. It changes safety, permission, escalation, dry-run, verification, or coherence expectations.
5. It changes project creation questioning or sufficiency doctrine.
6. It changes delegation/worker doctrine in a way existing projects may need to evaluate.
7. It changes ArchitectureHarvest advisory doctrine or adoption/recommendation semantics.
8. It captures a recurring problem seen in one or more projects and converts it into framework-level behavior.
9. It introduces a recommendation that could reduce drift, token waste, governance confusion, incorrect automation, or maintenance burden in existing projects.

A change should not create a notice merely because it touched ProjectForge.

Recommended significance levels:

- `minor`: useful but low-impact; document in ProjectForge state/recent changes only. No notice by default.
- `notable`: likely relevant to some existing projects; create a notice if the affected project class is clear.
- `major`: affects core governance, inheritance, safety, verification, context, or architecture doctrine; create a notice.
- `critical`: addresses correctness, safety, destructive-risk, security, or severe governance drift; create a notice and flag high review priority, but still do not force adoption.

Default rule: create notices for `notable`, `major`, and `critical` framework improvements only when there is a plausible existing-project audience.

## 4. Proposed notice artifact structure

Minimal useful structure:

```yaml
id: FIN-YYYYMMDD-short-slug
title: Short human title
status: proposed|active|superseded|retired
created: YYYY-MM-DD
source_change:
  projectforge_files:
    - path/to/file.md
  related_task: artifacts/tasks/optional.md
  related_decision: artifacts/decisions/optional.md
category:
  - governance
  - questioning
  - artifact_standard
  - handoff_standard
  - context
  - verification
  - delegation
  - worker_infrastructure
  - architectureharvest
  - inheritance
significance: minor|notable|major|critical
summary: One paragraph summary of the improvement.
recurring_problem: What repeated problem or risk caused this improvement?
future_projects_benefit: Which future project classes benefit?
why_framework_not_project_specific: Why does this belong in ProjectForge rather than one project?
project_relevance:
  likely_relevant_when:
    - Condition under which a project should review it
  likely_not_relevant_when:
    - Condition under which a project can ignore/reject it
adoption_impact:
  expected_effort: none|small|medium|large|unknown
  risk: low|medium|high|unknown
  compatibility_notes:
    - Note about compatibility or migration risk
recommendation:
  strength: weak|moderate|strong
  rationale: Why this recommendation strength is justified
review_expectation:
  priority: low|normal|high|urgent
  timing: during_next_relevant_work|before_related_architecture_change|before_next_major_task|immediate_if_safety_related
explicit_non_actions:
  - Does not automatically modify projects
  - Does not create project tasks
  - Does not force migration
```

Markdown may be used instead of YAML when the notice needs richer explanation. The required semantic fields should remain the same.

A notice should be short enough for summary-first context. Detailed evidence belongs in linked reports, decisions, or task artifacts.

## 5. Proposed notice lifecycle

Recommended lifecycle states:

1. `proposed`
   - Drafted after a ProjectForge improvement or governance review.
   - Not yet considered a stable framework communication.

2. `active`
   - Accepted as a valid advisory notice for existing projects.
   - Existing projects may review it during relevant future work.

3. `acknowledged_by_project`
   - A project has seen the notice and recorded that it may or may not be relevant.
   - This is project-local, not centrally enforced.

4. `project_decided`
   - A project records an outcome: adopt, partially adopt, defer, reject, not applicable, or superseded.
   - The decision belongs to the project.

5. `superseded`
   - A later framework notice or doctrine replaces this notice.

6. `retired`
   - The notice is retained for historical traceability but is no longer actively recommended.

Project-local review outcomes:

- `adopt`: project accepts the recommendation and may open a separate implementation task.
- `partially_adopt`: project accepts a bounded subset or adapts it to local constraints.
- `defer`: project sees possible relevance but chooses not to act now.
- `reject`: project explicitly decides the notice is not appropriate.
- `not_applicable`: project class/scope does not match the notice.
- `superseded`: a newer local or framework decision replaces the notice.

Outcome records should explain the local reason, not merely record a status.

## 6. Review and decision doctrine

Projects are autonomous. Their only obligation is review-at-relevance, not review-immediately.

Review-at-relevance means:

- A project does not need to scan all framework notices during ordinary work.
- A project should check relevant active notices when beginning work that touches the same category: governance, context, handoff, verification, delegation, worker roles, ArchitectureHarvest, inheritance-like structure, safety, or project creation assumptions.
- A project may batch notice review into major governance reviews, architecture reviews, post-audit remediation, or task-opening moments.
- A project may reject or defer a notice without penalty if local constraints do not justify adoption.
- A project should record a local decision only when the notice is actually reviewed.

Project decision records should include:

- notice id;
- local relevance assessment;
- decision outcome;
- rationale;
- expected local change, if any;
- whether a separate task is needed;
- verification or risk notes;
- date and agent/human context.

Adoption is never implicit. If adoption requires modifying project files, that is a separate project-local task with its own scope, dry-run/preflight if needed, tests/checks, and handoff.

## 7. Interaction with summaries, handoffs, and project context

Notice visibility should be lightweight and summary-first.

ProjectForge-level expectations:

- ProjectForge may keep notices in a future governance/design artifact family if implementation is approved later.
- The root ProjectForge summary should mention only active high-impact notice themes, not every notice.
- Notices should link to source decisions/tasks/reports instead of embedding long histories.

Instantiated-project expectations:

- A project may mention pending relevant notices in local `state/project_state.md`, `state/active_goal.md`, or a relevant `_SUMMARY.md` only when they are relevant to current or near-future work.
- `context/latest_handoff.md` should mention a notice only when it was reviewed, adopted, rejected, deferred, or is directly relevant to the next task.
- Adoption history should be tracked as local project decisions, not as centralized ProjectForge control.
- A broadly useful adoption outcome may be mirrored back to ProjectForge or ArchitectureHarvest as evidence, but only as feedback, not as enforcement.

Avoid making every notice part of normal startup context. Notices should be retrieved by relevance, not injected globally.

## 8. Explicit prohibitions

Framework improvement notices must not:

- automatically modify existing projects;
- silently propagate ProjectForge changes;
- force migration;
- create project tasks automatically;
- override project-local governance;
- decide adoption for a project;
- imply that non-adoption is failure;
- require projects to scan all notices during ordinary work;
- become mandatory startup context for every task;
- trigger background processes or daemons;
- create continuous scanners;
- mutate templates or generated-project layouts by themselves;
- bypass dry-run, verification, or human approval requirements;
- use ArchitectureHarvest recommendations as adoption authority;
- centralize project backlog control under ProjectForge.

## 9. Compatibility with current ProjectForge doctrine

This doctrine is compatible with current ProjectForge doctrine because it preserves:

- ProjectForge as reusable framework, not manager;
- generated project autonomy;
- no silent mutation of existing projects;
- project-local adoption decisions;
- file-backed state and durable decisions;
- summary-first context;
- deferred specification;
- clarification severity;
- human approval for risky actions;
- dry-run/preflight discipline;
- simple file formats;
- ArchitectureHarvest as advisory evidence, not controller;
- local-execution/cloud-governance;
- correctness over automation.

It also fills the explicit gap in current doctrine: how ProjectForge communicates reusable lessons to existing projects without controlling them.

## 10. Risks and failure modes

1. Notice spam
   - Too many minor notices could create noise and reduce trust.
   - Mitigation: notices only for notable/major/critical changes with a plausible existing-project audience.

2. Hidden control through “recommendations”
   - Strong recommendations could feel mandatory.
   - Mitigation: every notice states project-local adoption and explicit non-actions.

3. Startup context bloat
   - Loading all notices by default would violate summary-first context.
   - Mitigation: retrieve notices by relevance and mention only current relevant ones in handoffs/summaries.

4. Stale notices
   - Old notices may become misleading.
   - Mitigation: lifecycle states include superseded and retired.

5. Adoption without scope control
   - A project may treat notice review as approval to edit files.
   - Mitigation: adoption that modifies files requires a separate project-local task.

6. Centralized backlog creep
   - ProjectForge could become a manager by creating tasks in projects.
   - Mitigation: notices must not create project tasks automatically.

7. Under-communication
   - Important framework lessons might not reach projects.
   - Mitigation: use significance levels and review-at-relevance expectations.

8. Ambiguous relevance
   - Projects may not know whether a notice applies.
   - Mitigation: every notice includes likely relevant and likely not relevant conditions.

9. Premature implementation
   - Notice doctrine could pressure creation of automation too early.
   - Mitigation: this proposal recommends doctrine first, then a small manual artifact convention if approved.

## 11. Recommendation on implementation

Implementation is justified, but only as a small manual governance convention after this doctrine is approved.

Recommended next implementation scope, if approved later:

- Add a simple `artifacts/framework_notices/` or `artifacts/notices/` location.
- Add one short README or `_SUMMARY.md` explaining notice purpose and prohibitions.
- Add a minimal notice template in Markdown or YAML.
- Optionally record one notice for the recent ProjectForge framework-boundary doctrine as a pilot.

Do not implement automation, propagation, project scanning, generated-project mutation, migration, background jobs, or enforcement.

Preferred first implementation: manual, file-backed, low ceremony.

Implementation should not proceed until the notice doctrine and artifact location are explicitly approved.
