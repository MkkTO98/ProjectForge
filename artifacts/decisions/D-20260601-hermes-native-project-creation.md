# Decision: Hermes-Native Project Creation

Date: 2026-06-01
Status: Accepted
Severity: L3

## Context

ProjectForge already had a strong file-first governance scaffold, but project creation was still documented and implemented primarily as a fixed terminal questionnaire through `tools/new_project.py`. The desired operating model is that Hermes Agent should act as the adaptive interviewer and orchestrator, while ProjectForge tools render, record, and verify.

## Decision

ProjectForge will be treated as Hermes-native:

1. Hermes is the primary operator and interviewer.
2. `config/setup_questionnaire.yaml` is a coverage map, not a rigid user-facing script.
3. `tools/new_project.py` remains the deterministic scaffold renderer and manual fallback.
4. The preferred creation path is: Hermes-led adaptive interview -> captured answers JSON -> noninteractive scaffold render -> verification -> state/decision/task updates.
5. ProjectForge and generated projects must include `AGENTS.md` so Hermes and other coding agents can discover local operating rules automatically.
6. ProjectForge model routing is advisory; Hermes remains the real execution framework for provider/model/tool selection.
7. `tools/run.py` remains useful for manual/non-Hermes command audit, but Hermes tools do not need to be artificially routed through it for normal read/write/search/test work.

## Consequences

- New projects should be started by asking Hermes to use ProjectForge, not by running the questionnaire directly unless Hermes is unavailable.
- Future updates should prefer Hermes skills, AGENTS.md, and ProjectForge artifacts over hidden chat prompts.
- Safety policy remains file-backed through permissions, decisions, and escalation rules.
- The ProjectForge Hermes skill at `~/.hermes/skills/software-development/projectforge/SKILL.md` is now part of the local operating workflow.

## Verification

- `python3 tools/check_coherence.py --project . --json` returned zero blocks and zero warnings.
- `uvx --from pytest --with pyyaml pytest tests -q` returned `26 passed`.
