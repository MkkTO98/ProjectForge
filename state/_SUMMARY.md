# Folder Summary: state

## Purpose
This folder is part of the ProjectForge file-backed operating system for `state`.

## Contains
<!-- PROJECTFORGE:BEGIN-CONTAINS -->
- `.gitkeep`
- `active_goal.md`
- `architecture.md`
- `known_issues.md`
- `lessons.md`
- `project_state.md`
- `recent_changes.md`
<!-- PROJECTFORGE:END-CONTAINS -->

## Active Work
- Active state now records the EIP sibling-project boundary: ProjectForge uses the external MetaHarvest provider, no embedded MetaHarvest fallback, and no obsolete nested MacroForge archive.

## Needs Attention
- The stale generated `context/active_context.md` warning remains non-blocking; regenerate a task-specific context bundle before future context/model-routing work.
- Broad uncommitted ProjectForge recovery changes may remain in the working tree; use hunk-level staging and preserve commit boundaries.
