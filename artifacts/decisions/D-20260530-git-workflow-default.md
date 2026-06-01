# Decision: Git Workflow Default

Date: 2026-05-30
Status: Accepted

## Decision
ProjectForge uses a MacroForge-style git workflow by default.

## Policy
- Agents may inspect status and diffs.
- Agents may prepare commits with clear messages.
- Agents may commit automatically only if project policy allows it.
- Pushes require explicit approval by default.
- Branching starts simple and evolves only when needed.

## Branch default
Single main branch until the project has enough complexity to justify feature branches or agent branches.

## Rationale
Premature branch complexity creates friction. Simple defaults are better until multiple concurrent workstreams exist.
