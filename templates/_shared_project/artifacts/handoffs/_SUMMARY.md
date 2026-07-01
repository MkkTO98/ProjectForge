# Folder Summary: artifacts/handoffs

Artifact role: durable governance history for handoffs.

## Purpose
This folder stores durable handoff snapshots when the latest handoff alone would become too large or when a milestone/session boundary needs historical preservation.

## Rules
- `context/latest_handoff.md` remains the concise current recovery handoff.
- Store older or milestone handoffs here when they matter for accountability.
- Handoffs preserve continuity, not complete project history.
