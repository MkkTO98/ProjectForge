# ProjectForge v1.0.0

ProjectForge is a reusable, Hermes-native framework for creating and operating long-lived AI-native software projects.

It is an architectural operating system for AI-assisted development: a minimal, durable scaffold for initializing projects, preserving context and decisions, and enforcing governance behavior without being part of the generated project’s runtime.

It is **independent from EIP**. EIP is a separate ecosystem context where some generated projects may later be hosted, but it is not the identity of ProjectForge.

Generated projects are not owned by ProjectForge. After creation, they are project-owned and may only adopt framework improvements by their own decisions.

## What ProjectForge is

- A **framework for creating long-lived AI-native software projects**.
- An **architectural operating system** for AI-assisted development.
- A **project initialization and governance** framework.
- **Independent** from EIP.
- A platform that produces **autonomous generated projects** with their own project-owned governance.

## Core Principles

- Generated projects are expected to become fully project-owned immediately after creation.
- ProjectForge has **no runtime authority** over instantiated projects.
- Architecture is evolved from observed implementation evidence, not speculation.
- ProjectForge canonizes patterns that have been proven in real work and keeps them as defaults.

## Five-System Architecture

1. **Project Identity**
   - Project manifesting, naming, ownership boundaries, and baseline purpose for every generated project.

2. **Context and Continuity**
   - State files, handoffs, context summaries, and recovery workflows that preserve work across sessions.

3. **Governance and Decision**
   - Permission levels, decision records, escalation discipline, and governance contracts.

4. **Work Execution Methodology**
   - How work is run: interview, sufficiency, task execution, verification, and closure.

5. **Validation and Evidence**
   - Invariant checks, architecture-to-reality audits, dry-runs, tests, and evidence retention.

## Design Philosophy

ProjectForge is designed to be:

- Lightweight
- Local-first
- Deterministic
- Evidence-driven
- Project-owned by design
- Minimal and bounded in architectural growth

ProjectForge is intentionally **not**:

- An orchestration platform
- A CI/CD framework
- A project-management system
- A runtime agent platform
- A knowledge graph

## Current Status

ProjectForge v1.0.0

- Status: Architecturally Stable
- Architecture: Frozen, subject to constitutional evidence-based evolution

## Getting Started

1. Install dependencies in this repository per its local tooling conventions.
2. Choose or create a project output path.

```bash
cd /home/username/srv/ProjectForge
python3 tools/new_project.py --name "My New Project" --template default_project
```

ProjectForge is typically operated via Hermes-led adaptive interviewing; the command above is the manual fallback.

If you already have captured answers, you can render non-interactively:

```bash
cd /home/username/srv/ProjectForge
python3 tools/new_project.py \
  --name "My New Project" \
  --template default_project \
  --answers-json context/project_creation_answers_my_new_project.json
```

By default, generated projects are created under:

- `workspace/projects/<slug>/`

And each generated project is initialized as an independent project with its own governance and state artifacts.

## Repository cleanup notes

- References to being embedded inside EIP as the active runtime container were removed to reflect current architecture.
- Historical context and archived migration notes are preserved only where useful for audit continuity.
- The repository documentation now prioritizes user discovery and project governance boundaries over implementation plumbing details.

## Primary tools

- `tools/new_project.py`: deterministic project scaffold renderer.
- `tools/build_context.py`: builds explicit task context for local and cloud use.
- `tools/check_coherence.py`: validates core structural invariants.
- `tools/architecture_reality_audit.py`: identifies drift between architecture and implementation.
- `tools/context_health.py`: checks context-state size and continuity hygiene.
- `tools/update_context_summaries.py`: refreshes summary artifacts.

## Documentation and governance checks

Use standard verification commands from the project root before publishing or major changes.

```bash
python3 tools/check_coherence.py --project . --json
python3 tools/architecture_reality_audit.py --project . --json
uvx --from pytest --with pyyaml pytest tests -q
```

