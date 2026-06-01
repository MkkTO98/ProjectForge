# Context Policy

`_SUMMARY.md` files are folder-local maps. `context/active_context.md` is the selected task bundle. `state/` contains current project truth. `artifacts/decisions/` contains durable choices and deferred specifications.

Rules:
- Context building should use `tools/build_context.py`.
- Summary maintenance should use `tools/update_context_summaries.py`.
- Agents must report `Context used:` in every run report.
- Agents must not treat summaries as authoritative when they conflict with decisions or state.
- Cross-module changes must consult `knowledge/dependencies.yaml`.
