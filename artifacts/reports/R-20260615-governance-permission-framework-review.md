# Governance Permission Framework Review

Date: 2026-06-15
Status: bounded review and doctrine alignment
Scope: permissions, escalation, purpose protection, warning blocks, recommendation authority, and decision visibility

## Explicit non-actions

This review does not authorize or perform:

- commits;
- staging;
- project creation;
- MetaHarvest purpose changes;
- MacroForge purpose changes;
- EIP purpose changes;
- ecosystem infrastructure implementation;
- automation implementation;
- authority delegation;
- mandatory standards outside approved ProjectForge governance doctrine.

## 1. Permission ladder assessment

A four-level permission ladder is useful and should become ProjectForge governance doctrine because it makes human attention requirements explicit without adding friction to routine work.

Recommended ladder:

### L1 — Operational

Routine implementation inside the current approved scope.

Examples:

- tests;
- reports;
- documentation updates;
- small refactors;
- task creation inside the current project;
- implementation of already-approved work;
- local cleanup that does not alter architecture, purpose, governance, permissions, or ecosystem boundaries.

Behavior: no special escalation beyond normal safety, verification, and task discipline.

### L2 — Architectural

Project-local architectural change.

Examples:

- new subsystem;
- new storage model;
- major schema change;
- new integration layer;
- major workflow change;
- permission/model-routing/context architecture changes inside the project.

Behavior: explicit approval required before implementation. The proposal should state impact, risk, and verification path.

### L3 — Strategic

Scope expansion, ecosystem interaction, or cross-project implications.

Examples:

- significant cross-project recommendations;
- project-boundary changes;
- major governance additions below constitutional level;
- ecosystem-facing capabilities;
- extraction recommendations;
- new long-term responsibilities;
- recommendation patterns that could become implicit authority.

Behavior: approval required before implementation. Must produce a structured warning block.

### L4 — Foundational

Purpose, doctrine, ecosystem, constitutional, or authority-boundary change.

Examples:

- project purpose changes;
- project merges;
- project splits;
- new project creation;
- governance-doctrine changes;
- constitutional changes;
- ecosystem ownership changes;
- authority-boundary changes;
- project creation authority or cross-project control.

Behavior: stop implementation. Explicit approval required. Must produce highest-visibility warning block.

## 2. Purpose-protection assessment

A project purpose is protected. Purpose is not an implementation detail.

Hermes may:

- identify tensions;
- identify opportunities;
- recommend expansions;
- recommend extraction;
- document rationale, expected value, effort, architectural impact, confidence, and priority.

Hermes may not:

- silently expand purpose;
- redefine purpose;
- substantially reinterpret purpose;
- absorb new responsibilities that materially alter project identity.

Purpose changes require L4 foundational approval.

## 3. Warning-block design

Structured warning blocks should become doctrine for L3 and L4 work because they remain visible when copied into ChatGPT, pasted into another agent, or skimmed quickly.

### L3 format

```text
GOVERNANCE_WARNING
PERMISSION_LEVEL=L3
CATEGORY=STRATEGIC
PROJECT=<project-or-scope>
DECISION=<short decision name>

Impact:
<concise impact statement>

Risk:
<concise risk statement>

Required approval:
Explicit approval required before implementation.
END_GOVERNANCE_WARNING
```

### L4 format

```text
FOUNDATIONAL_GOVERNANCE_WARNING
PERMISSION_LEVEL=L4
CATEGORY=FOUNDATIONAL
PROJECT=<project-or-scope>
DECISION=<short decision name>

Impact:
Project purpose, doctrine, ecosystem structure, constitutional rule, or authority boundary may be affected.

Risk:
Implementation without explicit approval could silently change project identity, governance authority, or ecosystem architecture.

Required approval:
STOP. Implementation prohibited without explicit foundational approval.
END_FOUNDATIONAL_GOVERNANCE_WARNING
```

The format is intentionally plain text, human-readable, and machine-readable enough for future tooling.

## 4. ChatGPT visibility assessment

For L3 and L4 proposals, doctrine should require:

- concise explanation;
- explicit impact statement;
- explicit risk statement;
- explicit approval request.

This is useful because high-impact decisions often cross tool boundaries. If a proposal is pasted into ChatGPT or another agent, the warning must survive context loss.

## 5. Recommendation authority assessment

Confidence, priority, and authority are distinct.

- Confidence describes belief that the recommendation is correct or well-supported.
- Priority describes perceived value, urgency, or sequencing importance.
- Authority describes permission to decide or implement.

Confidence and priority do not imply authority.

Repeated high-confidence recommendations can create soft governance if users or projects treat them as defaults that require justification to reject. This risk was recorded in `R-20260615-soft-governance-risk-future-review-note.md` and should now be reflected in doctrine.

Recommended doctrine: recommendation acceptance remains project-local; repeated acceptance is evidence, not authority.

## 6. Decimal convention assessment

Decimal representation for confidence, priority, likelihood, and uncertainty is useful when meaningful.

Examples:

- `confidence = 0.83`
- `priority = 0.72`

Guidance:

- Use decimals for bounded estimates where a numeric estimate improves clarity.
- Avoid percentages unless externally required.
- Avoid false precision.
- Use qualitative labels when numeric estimates would be misleading.

## 7. Task-size normalized scale assessment

A normalized task-size scale could be useful later.

Potential example:

- `0.2 = small`
- `1.0 = average`
- `3.0 = large`

Usefulness:

- could improve planning and commit-boundary reasoning;
- could support workload estimation;
- could make task slicing more consistent.

Risks:

- false precision;
- extra cognitive overhead;
- gaming the scale;
- premature standardization;
- confusion with priority or effort estimates.

Recommendation: do not standardize now. Future exploration is justified only after repeated task-sizing failures or planning friction.

## 8. Recommendation rejection memory assessment

Rejected recommendations should remain discoverable.

Minimum retained fields should include:

- recommendation identifier or title;
- origin;
- date;
- target project or scope;
- review outcome;
- rejection rationale;
- context;
- supersession or revisit condition when useful.

This prevents repeated rediscovery and preserves negative knowledge.

## 9. Foundational decision registry assessment

A registry of foundational decisions could be useful later.

Candidate entries:

- project creation;
- project separation;
- project merges;
- ecosystem ownership decisions;
- MetaHarvest conceptual evolution;
- major governance changes;
- constitutional changes;
- authority-boundary changes.

Overlap with existing artifacts:

- ProjectForge already has durable decision artifacts under `artifacts/decisions/`.
- A registry would not replace decisions; it would index the highest-impact ones.

Recommendation: do not implement now. Record as future-review-worthy if foundational decisions become difficult to find or compare.

## 10. Risks and open questions

Risks:

- The permission ladder could become bureaucracy if applied to trivial work.
- L2/L3 distinction may be ambiguous for architecture that also has ecosystem implications.
- Warning blocks may be ignored if overused.
- Confidence/priority decimals may imply precision that does not exist.
- Rejection memory may become clutter if every minor suggestion is preserved.
- Foundational-decision registries may duplicate decision artifacts if implemented too early.

Open questions:

- Should future templates include a permission-level field for tasks/recommendations, or is doctrine enough for now?
- Should existing recommendation templates eventually add stronger advisory-only fields?
- What threshold makes an L2 architectural decision become L3 strategic?
- Should repeated L3 recommendations trigger periodic soft-governance review?
- What is the minimum useful foundational-decision index, if one is eventually needed?
