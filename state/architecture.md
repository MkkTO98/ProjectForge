# Architecture

ProjectForge has four layers.

## 1. Global Foundation
Reusable skills, agent role documents, permissions, logging utilities, and project templates.

## 2. Bootstrap Layer
`tools/new_project.py` conducts an extensive setup interview or consumes a config file, then generates a new project instance.

## 3. Project Instance Layer
Generated projects include state files, decision/task artifacts, logging, permissions, and optional specialized agents.

## 4. Task Layer
Temporary task context is stored in `state/active_goal.md`, `artifacts/tasks/`, and run logs.

## Deferred specification
If a decision cannot be made during setup, it must be written as a deferred decision artifact. Agents should later ask for specification when that decision becomes relevant.

## Clarification severity
Questions are classified as:

- L1: Silent autonomy. The agent may proceed.
- L2: Batched clarification. Ask later; continue if safe.
- L3: Blocking clarification. Pause and ask immediately.
- L4: Emergency stop. Stop execution and require explicit human action.
