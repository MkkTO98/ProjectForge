# T-20260615 MetaHarvest Interface-Boundary Review

Date: 2026-06-15
Status: completed
Scope: bounded architecture-boundary and extraction-readiness review

## Goal

Identify the minimum conceptual interface set required for MetaHarvest to become an autonomous sibling project within the future EIP ecosystem, without extraction or implementation.

## Explicit non-actions

This task did not perform:

- commits;
- staging;
- directory moves;
- directory renames;
- MetaHarvest extraction;
- project creation;
- MacroForge modification;
- EII modification;
- ecosystem infrastructure modification;
- contract implementation;
- service implementation;
- schema creation;
- protocol creation.

## Output

- Review artifact: `artifacts/reports/R-20260615-metaharvest-interface-boundary-review.md`

## Main conclusions

- MetaHarvest owns reusable non-domain knowledge, recommendation rationale, evidence pointers, and recommendation lineage.
- Consumer projects own adoption, rejection, modification, scheduling, implementation, priorities, local governance, and purpose interpretation.
- Potential future EIP ecosystem infrastructure owns active contracts, registries, compatibility definitions, and ecosystem metadata if/when approved; MetaHarvest should not own these by default.
- The minimum conceptual interface set is: consultation, recommendation, adoption outcome, rejection memory, evidence reference, relevance/context, staleness/update, and authority boundary.
- MetaHarvest is conceptually separable but not physically extraction-ready because path dependencies, active-contract ownership, evidence-reference strategy, and generated-project placeholder naming remain unresolved.

## Verification

Final verification should include:

- `git diff --check`
- `python3 tools/check_coherence.py --project . --json`
- `python3 tools/architecture_reality_audit.py --project . --json`
