# Decision: Folder Summary Policy

Date: 2026-05-30
Status: Accepted

## Decision
Core folders must include `_SUMMARY.md` files that explain folder purpose, contents, status, open work, and local rules.

## Rationale
This follows the MacroForge-style context compression pattern: parent agents should not need to scan entire subtrees to understand what a folder contains or what remains to be done.

## Consequence
Generated projects include folder summaries, and agents should update them before handoffs or after material folder changes.
