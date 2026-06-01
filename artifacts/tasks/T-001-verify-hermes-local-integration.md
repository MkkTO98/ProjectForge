# Task: Verify Hermes Local Integration

Status: Completed
Priority: Medium
Completed: 2026-06-01

## Goal
Verify local Hermes Agent paths, skill registration behavior, and command execution behavior on the target machine.

## Definition of Done
- Confirm Hermes skill directory.
- Confirm whether project-local skills can be referenced directly or should be symlinked.
- Confirm how Hermes handles permissions and tool calls.
- Record findings in `artifacts/decisions/` if they affect ProjectForge defaults.

## Findings
- Hermes user-local skills live under `~/.hermes/skills/`.
- A local ProjectForge Hermes skill was created at `~/.hermes/skills/software-development/projectforge/SKILL.md`.
- Project-local skills under `/home/mkkto/srv/projectforge/skills/` are useful project artifacts, but they are not a substitute for a real Hermes skill.
- Hermes should use its native file/search/patch/terminal/delegation/cron tools directly during Hermes sessions.
- `tools/run.py` remains a ProjectForge audit/policy wrapper for manual or non-Hermes command execution, not a mandatory wrapper around every Hermes tool call.
- ProjectForge and generated projects now include `AGENTS.md` entry points so Hermes can discover local operating rules from the workdir.

## Resulting Decision
See `artifacts/decisions/D-20260601-hermes-native-project-creation.md`.

## Verification
- `python3 tools/check_coherence.py --project . --json` returned zero blocks and zero warnings.
- `uvx --from pytest --with pyyaml pytest tests -q` returned `26 passed`.
