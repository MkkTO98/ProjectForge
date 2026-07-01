# Project State

ProjectForge is a reusable, Hermes-native project initialization and governance framework. It creates file-backed project operating systems with explicit identity, context, governance, work methodology, validation, and recovery discipline.

Generated projects become autonomous at creation. ProjectForge improves itself and future inheritance, but does not own, manage, or silently mutate instantiated projects.

## Current operating status

- Current task: ProjectForge v1.0.0 architectural release has been committed and tagged.
- ProjectForge root: `/home/mkkto/srv/ProjectForge`.
- Active external MetaHarvest provider: `/home/mkkto/srv/EIP/projects/MetaHarvest`.
- Relocation provenance: `artifacts/reports/R-20260618-eip-relocation-retrospective.md`.
- Root current-state ledger cleanup provenance: `artifacts/reports/R-20260701-root-current-state-ledger-cleanup.md`.

## Current architectural operating system

ProjectForge v1 is organized around five complete systems:

1. Project Identity.
2. Context and Continuity.
3. Governance and Decision.
4. Work Execution Methodology.
5. Validation and Evidence.

No sixth subsystem is currently justified. Future work should refine these systems unless repeated implementation evidence proves a genuinely missing responsibility.

## Stable defaults

- Hermes is the primary operator and adaptive interviewer.
- `config/setup_questionnaire.yaml` is a coverage map, not a rigid user-facing questionnaire.
- `tools/new_project.py` is the deterministic scaffold renderer and manual fallback.
- Local execution / cloud governance remains the operating model: local tools/models for routine implementation and verification; cloud/Codex only for high-leverage governance with context audit.
- Raw logs are audit/debug artifacts only and are excluded from normal context.
- Local version-control snapshots may be allowed by policy after tests; remote push requires human approval.
- Specialized agents require explicit request/explanation before generation.

## Current framework doctrine

- ProjectForge is a reusable framework, not an active project manager or meta-controller.
- ProjectForge owns framework doctrine, project creation procedures, reusable structure/governance/standards/questioning/handoff/delegation infrastructure, and reusable verification/coherence expectations.
- ProjectForge does not own instantiated project goals, architecture, implementation, task execution, or adoption decisions.
- Framework improvements affect future inheritance by default. Existing projects receive recommendations or improvement notices and decide adoption through their own governance.
- Framework-level changes must be named explicitly when they affect inheritance, templates, governance, questioning, artifact standards, handoff standards, delegation/worker infrastructure, framework doctrine, or MetaHarvest doctrine.

## Current continuity and validation pointers

- Primary state artifacts are concise current-state pointers: `state/active_goal.md`, `state/project_state.md`, and `state/architecture.md`.
- `context/latest_handoff.md` is the short operational handoff for the next session.
- Folder `_SUMMARY.md` files support summary-first retrieval.
- `tools/build_context.py` builds explicit context bundles and audits for local/cloud use.
- `tools/context_health.py` is wired into coherence to catch oversized state/handoff, stale generated context bundles, and ledger-like current-state drift.
- `tools/check_coherence.py` validates structural invariants across the five systems.
- `tools/architecture_reality_audit.py` provides advisory architectural drift detection.

## Current governance boundaries

- ProjectForge uses a four-level permission ladder: L1 Operational, L2 Architectural, L3 Strategic, L4 Foundational.
- Project purpose is protected; Hermes may recommend expansion or extraction but must not silently expand, redefine, reinterpret, or absorb responsibilities that alter project identity.
- Confidence and priority are advisory metadata, not authority.
- The workspace registry is descriptive only and does not grant write authority or governance.
- New project creation remains a foundational ecosystem decision requiring explicit human approval.

## Current MetaHarvest boundary

- Active external provider: `/home/mkkto/srv/EIP/projects/MetaHarvest`.
- ProjectForge does not host an in-tree MetaHarvest fallback copy while provider status is active.
- MetaHarvest is advisory and non-domain. It may produce recommendations and candidate task proposals, but may not create tasks inside another project, decide adoption, modify target projects, or force implementation.
- Generated projects retain lightweight `architecture/architectureharvest/` compatibility placeholders for historical ArchitectureHarvest lineage and generated-project artifacts.
