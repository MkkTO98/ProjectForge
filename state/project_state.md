# Project State

ProjectForge is a reusable, Hermes-native project initializer and framework for agent-assisted projects. It creates file-backed project operating systems with explicit state, decisions, tasks, handoffs, recovery procedures, permissions, verification, and context discipline.

Generated projects become autonomous at creation. ProjectForge improves itself and future inheritance, but does not own, manage, or silently mutate instantiated projects.

## Stable defaults

- Hermes is the primary operator and adaptive interviewer.
- `config/setup_questionnaire.yaml` is a coverage map, not a rigid user-facing questionnaire.
- `tools/new_project.py` is the deterministic scaffold renderer and manual fallback.
- Local execution / cloud governance is the operating model: local tools/models for routine implementation and verification; cloud/Codex only for high-leverage governance with context audit.
- Standard logging is file-backed; raw logs are audit/debug artifacts only and are excluded from normal context.
- Auto-commit after tests may be allowed by policy; remote push requires human approval.
- Specialized agents require explicit request/explanation before generation.

## Current framework doctrine

- ProjectForge is a reusable framework, not an active project manager or meta-controller.
- ProjectForge owns framework doctrine, project creation procedures, reusable structure/governance/standards/questioning/handoff/delegation infrastructure, and reusable verification/coherence expectations.
- ProjectForge does not own instantiated project goals, architecture, implementation, task execution, or adoption decisions.
- Framework improvements affect future inheritance by default. Existing projects receive recommendations or improvement notices and decide adoption through their own governance.
- Framework-level changes must be named explicitly when they affect inheritance, templates, governance, questioning, artifact standards, handoff standards, delegation/worker infrastructure, framework doctrine, or MetaHarvest doctrine.

## Current continuity/recovery framework

- `tools/recover_session.py` provides bounded file-backed recovery from fixed startup files plus recent task/decision/question artifacts.
- `recovery/continuity_framework.md` defines the recovery contract, standard closeout contract, near-quota shutdown order, resume procedure, and existing-project adoption path.
- `context/context_policy.yaml` includes `continuity_recovery.standard_closeout_command` and `standard_closeout_order`.
- Coherence requires the recovery helper/framework and blocks missing standard closeout or fresh recovery command contracts.
- Future generated projects inherit the framework through `templates/_shared_project/`.
- MacroForge explicitly adopted the framework through its own project-local task because it was named in the user request.
- No database, vector store, embeddings, service, daemon, autonomous propagation, or parallel state system is part of this framework.

## Current context and verification systems

- Primary state artifacts are concise current-state pointers: `state/active_goal.md`, `state/project_state.md`, and `state/architecture.md`.
- `context/latest_handoff.md` is the short operational handoff for the next session.
- Folder `_SUMMARY.md` files support summary-first retrieval.
- `tools/build_context.py` builds explicit context bundles and audits for local/cloud use.
- `tools/context_health.py` is wired into coherence to catch oversized state/handoff and stale generated context bundles.
- Task completion policy is centralized: update task/state/handoff and affected summaries, inspect refreshed summaries for stale curated sections, then run final verification after governance/summary edits.
- `tools/architecture_reality_audit.py` provides recurring Architecture-to-Reality Audit coverage.

## Current governance permission framework

- ProjectForge uses a four-level permission ladder: L1 Operational, L2 Architectural, L3 Strategic, L4 Foundational.
- L2 requires explicit approval before project-local architecture implementation.
- L3 requires explicit approval and a `GOVERNANCE_WARNING` block before implementation.
- L4 requires stopping implementation until explicit foundational approval and a `FOUNDATIONAL_GOVERNANCE_WARNING` block.
- Project purpose is protected; Hermes may recommend expansion or extraction but must not silently expand, redefine, reinterpret, or absorb responsibilities that alter project identity.
- Confidence and priority are advisory metadata, not authority.
- Rejected recommendations remain discoverable when meaningful to preserve negative knowledge.

## Current MetaHarvest provider

- MetaHarvest has been copy-first extracted to `/home/mkkto/srv/EIP/projects/MetaHarvest`, and ProjectForge treats that path as the active external advisory provider.
- ProjectForge no longer hosts an in-tree MetaHarvest fallback copy; active provider validation must use the external sibling provider when status is active.
- MetaHarvest is a file-backed librarian, reference system, evidence repository, advisory subsystem, and feedback repository; it is not a controller and must not decide adoption, enforce standards, modify projects, force migration, create tasks inside projects, or bypass project-local approval, dry-run, tests, and coherence gates.
- It remains non-domain: domain conclusions such as GDP analysis, inflation analysis, energy-market knowledge, macroeconomic conclusions, investment theses, and company research belong to domain projects.
- Generated projects retain lightweight `architecture/architectureharvest/` compatibility placeholders for relevance maps, candidates, rejections, review history, and adoption outcomes.

## Current task status

- Current task: none open.
- EIP relocation and cleanup are complete.
- ProjectForge operates at `/home/mkkto/srv/EIP/projects/ProjectForge`.
- MacroForge operates at `/home/mkkto/srv/EIP/projects/MacroForge`.
- MetaHarvest operates at `/home/mkkto/srv/EIP/projects/MetaHarvest`.
- Obsolete nested MacroForge copy was removed from ProjectForge after relocation cleanup; current MacroForge operates at `/home/mkkto/srv/EIP/projects/MacroForge`, with relocation evidence retained in the retrospective and recovery backups.
- Stale generated ProjectForge `context/active_context.md` is archived under `context/archive/generated-context-bundles/`.
- Durable relocation retrospective: `artifacts/reports/R-20260618-eip-relocation-retrospective.md`.
- Relocation status: clean with warnings; no active relocation work remains.

## Current ecosystem autonomy doctrine

- Projects are autonomous and retain their own purpose, scope, governance, lifecycle, artifacts, and decision history.
- Projects may recommend, notify, expose interfaces, and provide context, but may not govern, directly modify, create tasks inside, or assume authority over other projects.
- Scope extraction pressure produces recommendation artifacts with rationale, expected value, implementation effort estimate, architectural impact estimate, confidence/priority when meaningful, and lineage; it does not produce automatic project creation, task creation, or implementation.
- New project creation remains a foundational ecosystem decision requiring explicit human approval.
- Recommendation records should preserve review outcomes, adoption outcomes, rejection/adoption rationale, and supersession lineage; adoption by one project does not imply adoption by another.
- The workspace registry is descriptive only and does not grant write authority or governance. Future ecosystem-registry ownership remains TBD through future governance review.
- Future concepts such as the EIP ecosystem, ResearchMemory, EconGraph, MonitorForge, ReportForge, EII, and future ecosystem infrastructure are non-binding architectural context only.
- EIP means Economic Intelligence Platform, the ecosystem as a whole, not a project. EII means Economic Intelligence Initiative, a possible future user-facing intelligence project and not an ecosystem owner.
- No project owns the EIP root by default; if adopted later, it represents ecosystem organization and neutral infrastructure, not project authority.
- Project extraction readiness has two layers: conceptual readiness depends on purpose, ownership, authority, and interface boundaries; physical extraction additionally requires path inventory, artifact ownership inventory, compatibility planning, verification planning, rollback planning, and evidence-reference stability.

## Current MetaHarvest boundary

- Active external provider: `/home/mkkto/srv/EIP/projects/MetaHarvest`.
- No embedded MetaHarvest fallback copy is hosted in ProjectForge when provider status is active.
- MetaHarvest may produce recommendations and candidate task proposals; it may not create tasks inside another project, decide adoption, modify target projects, or force implementation.
