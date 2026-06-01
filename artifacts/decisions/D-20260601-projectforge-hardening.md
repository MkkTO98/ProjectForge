# Decision: ProjectForge hardening pass

Date: 2026-06-01
Status: Accepted
Severity: L3

## Context
A full audit found that ProjectForge's root checks passed while generated projects, registry behavior, non-Hermes command wrapping, and verification hygiene still had operational gaps.

## Decision
ProjectForge should enforce a Hermes-native factory contract with separate root and generated-project coherence modes, deterministic/non-mutating verification behavior, clean workspace registry semantics, and explicit sufficiency validation before scaffolding.

## Accepted changes
- `python3` is the supported local interpreter command for ProjectForge operational docs, schedules, and allowlists on this host.
- `tools/new_project.py` derives workspace paths from the active ProjectForge root instead of hardcoding `/home/mkkto/srv/projectforge`.
- Temp or explicit noncanonical outputs do not register in the canonical workspace unless `--register` is passed.
- Must-pause sufficiency items such as `secrets` and `command_policy` block generation unless answered or explicitly overridden with `--allow-deferred-required`.
- Generated projects receive populated state files from setup answers and no longer receive the factory-only `tools/new_project.py`.
- `tools/check_coherence.py` supports root-vs-generated contracts through `--mode root|generated|auto`.
- `tools/update_context_summaries.py` is deterministic and avoids volatile timestamps and ignored dry-run reports.
- `tools/register_project.py` treats PyYAML/schema validity as required and rejects invalid `raw` registry fallback data.
- Project-local bootstrap/questionnaire skills define `setup_questionnaire.yaml` as a coverage map, not a rigid script.

## Consequences
Future Hermes sessions should create projects through adaptive questioning plus noninteractive rendering, verify generated projects with generated coherence mode, and avoid treating root ProjectForge invariants as the generated-project contract.

## Verification
- `uvx --from pytest --with pyyaml pytest tests -q`
- `python3 tools/check_coherence.py --project . --json`
- temp generated-project smoke check with root and project-local coherence
