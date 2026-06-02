# Decision: ProjectForge Batch 2 generated-project UX hardening

Date: 2026-06-01
Status: Accepted
Severity: L3

## Context
After the first Hermes-native hardening pass, root ProjectForge and direct generated-project coherence were clean, but a second audit found remaining generated-project UX and dependency pitfalls:

- generated projects' `tools/run.py` wrapper could not run their own coherence check through the safe allowlist;
- template runtime artifacts such as `__pycache__` and `*.pyc` could be copied into generated projects;
- `tools/install.sh` still used `python3 -m pip install --user`, which fails on this PEP 668/no-pip host;
- `_SUMMARY.md` refreshes overwrote curated folder context;
- generated agent prompts over-required `tools/run.py` even when Hermes native tools are available.

## Decision
ProjectForge now treats generated-project UX as part of the factory contract and tests it directly.

Accepted changes:

1. Generated project safe wrapper checks must allow read-only ProjectForge validation, especially `python3 tools/check_coherence.py`.
2. Mutating ProjectForge tools belong in the review allowlist level, not safe.
3. Template rendering must skip runtime/cache artifacts such as `__pycache__`, `*.pyc`, `.pytest_cache`, `.mypy_cache`, `.ruff_cache`, `htmlcov`, `dist`, and `build`.
4. ProjectForge installation guidance is uv/venv-first on this host. Do not recommend system/user pip as the default setup path.
5. Summary refreshes must preserve curated Purpose, Active Work, and Needs Attention sections; only the Contains inventory is generated.
6. Generated agent prompts should say Hermes sessions use Hermes tools directly and reserve `tools/run.py` for manual or explicitly audited wrapper use.

## Consequences
- `tools/run.py` remains a policy/audit wrapper, not a full sandbox.
- Safe allowlist entries must stay semantically low-risk/read-only. Prefix matching remains a known future hardening target.
- Generated project tests should cover all templates, not just the default template.
- Summary curation is now durable across routine context refreshes.

## Verification
The accepted implementation was verified with:

```bash
uvx --from pytest --with pyyaml pytest tests -q
python3 tools/check_coherence.py --project . --json
bash tools/install.sh && .venv/bin/python tools/check_coherence.py --project . --json
python3 -m py_compile tools/*.py templates/_shared_project/tools/*.py
git diff --check
```

An all-template smoke test generated `default_project`, `python_data_project`, `web_project`, and `research_project`, then verified each generated project passed generated coherence and its own safe wrapper coherence command without changing the canonical registry.
