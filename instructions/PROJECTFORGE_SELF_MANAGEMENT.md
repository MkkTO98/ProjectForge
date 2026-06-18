# ProjectForge Self-Management

ProjectForge may improve itself and future inheritance, but generated projects remain autonomous after creation.

Rules:
- Workspace feedback can propose ProjectForge updates.
- No generated project may auto-modify ProjectForge templates.
- ProjectForge must never silently mutate an instantiated project.
- ProjectForge may modify an instantiated project only when that project is explicitly named as the approved target of a separate task.
- Framework improvements affect future inheritance by default; existing projects receive recommendations or improvement notices and decide adoption through their own governance.
- ProjectForge and generated projects may recommend, notify, or provide context to each other, but must not govern, directly modify, create tasks inside, or assume authority over each other.
- Scope extraction pressure should produce recommendation artifacts, not automatic absorption, project creation, task creation, or implementation.
- The workspace registry is descriptive only; it does not grant governance or write authority. Future registry ownership is TBD through ecosystem governance review.
- A framework improvement should answer: what recurring problem caused it, what future projects benefit from it, and why it belongs in framework behavior instead of project-specific behavior.
- Template changes require a decision artifact in `artifacts/decisions/`.
- Coherence checks must pass before packaging a new ProjectForge version.
