# ProjectForge v5 Coherence Report

## Summary
ProjectForge v5 strengthens the scaffold by moving key policies from prose-only conventions into enforcement utilities. The architecture remains deliberately boring: YAML, Markdown, JSONL, and small Python tools.

## Added
- Hybrid workspace inheritance policy.
- Generated-project `workspace_config.yaml` instead of nested global workspace copies.
- Soft-block enforcement policy.
- `tools/check_coherence.py`.
- `tools/validate_dry_run.py`.
- `tools/escalate.py`.
- `tools/review_metrics.py`.
- `tools/register_project.py`.
- Dry-run schema enforcement.
- Explicit `Context used:` requirement for agent reports.
- Canonical hardware profile under `hardware/profile.yaml`.

## Simplified
- Removed `models/hardware_profile.yaml` duplication.
- Removed legacy `tools/update_folder_summaries.py`; summary maintenance is now owned by the context system.
- Generated projects no longer inherit a full global `workspace/` tree by default.

## Coherence model
- `state/`: current truth.
- `artifacts/decisions/`: durable choices and deferred specifications.
- `_SUMMARY.md`: folder-local maps.
- `context/`: selected task input bundle.
- `logs/`: raw operational records.
- `metrics/`: derived performance evidence.
- `workspace/`: cross-project coordination.

## Remaining manual setup
- Hardware/model registry values.
- Actual Telegram notification credentials.
- Real workspace root path.
- Project-specific permission allowlist adjustments.
