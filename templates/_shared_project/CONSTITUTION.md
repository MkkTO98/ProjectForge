# Project Identity

This file is the project-owned identity artifact. It defines what this project is, what it is for, what it should not become, and the authority boundaries agents must respect.

## Project identity

- Name: {project_name}
- Primary purpose: {identity_purpose}
- V1 success: {identity_success}
- Primary users or consumers: {identity_users}

## Scope

### In scope

{identity_scope}

### Explicit non-scope

{identity_non_goals}

## Responsibility boundaries

{identity_responsibility_boundaries}

Default boundaries when a more specific decision is absent:

- This repository owns only its local files, policies, decisions, source code, tests, documentation, and generated artifacts.
- This repository does not govern other projects, external ecosystems, advisory providers, or infrastructure outside this checkout.
- External services, paid resources, credentials, production data, destructive actions, publishing, and remote pushes require explicit human approval or an accepted local decision artifact.
- Missing or ambiguous project-wide policy must not be invented silently. Record a deferred decision or ask a blocking question when the ambiguity changes scope, safety, cost, or long-term responsibility.

## Operating principles

1. Keep the project understandable from ordinary files: Markdown, YAML, JSON, source code, and deterministic local outputs.
2. Prefer simple, reversible, project-owned changes over hidden automation or broad abstractions.
3. Preserve durable choices as local decision artifacts when they affect identity, scope, responsibility, policy, or architecture.
4. Treat generated scaffolding as a starting point, not an external authority.
5. Do not broaden project purpose or responsibility by convenience.

## Instruction hierarchy

When project instructions conflict, use this order:

1. Direct human instruction for the current task.
2. This Project Identity artifact for purpose, scope, responsibility boundaries, operating principles, and authority boundaries.
3. Accepted local decision artifacts that refine or amend identity/scope.
4. Project-local agent and instruction files for execution behavior.
5. Current-state files and summaries for orientation.
6. Historical reports, handoffs, logs, and generated artifacts as evidence only.

If a lower-priority artifact conflicts with a higher-priority artifact, follow the higher-priority artifact and record the conflict if it affects future work.

## Generated-project independence

This project is autonomous after creation. Its copied scaffold is project-owned.

- No external generator is required to run, modify, govern, validate, or understand this project.
- Template provenance is historical context only, not authority.
- Future template/framework changes elsewhere do not silently mutate this project.
- This project must not assume any consumer ecosystem, advisory provider, or parent workspace unless a local decision explicitly adopts one.
