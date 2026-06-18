# Ecosystem Infrastructure Ownership Future Review Note

Date: 2026-06-15
Status: future-review note only
Scope: ownership question preservation; no infrastructure implementation

## Question

If EIP ecosystem infrastructure eventually becomes substantial, what should own it?

Current answer: undetermined.

## Terminology

`EIP` now means `Economic Intelligence Platform`: the future ecosystem as a whole, not a project.

The future user-facing intelligence project previously discussed as EIP is now conceptually `EII` — `Economic Intelligence Initiative`.

EII is a possible future project, not the ecosystem owner.

## Emerging infrastructure responsibilities

The ecosystem may eventually need neutral infrastructure for:

- project registries;
- recommendation registries;
- interface contracts;
- ecosystem lineage records;
- ecosystem metadata;
- ecosystem-level decision indexes;
- compatibility/versioning references;
- project relationship metadata.

## Current boundary

These responsibilities should not be assigned prematurely to:

- ProjectForge;
- MetaHarvest;
- EII;
- MacroForge;
- any other current or future project.

Temporary hosting by ProjectForge can remain acceptable when clearly marked as descriptive, transitional, and non-authoritative.

## Rationale for not solving now

Creating an infrastructure owner too early would risk:

- turning infrastructure into a project before the responsibility is mature;
- assigning governance authority by convenience;
- making EII a de facto ecosystem governor;
- making MetaHarvest a de facto standards authority;
- making ProjectForge a permanent ecosystem host;
- adding repository or operational complexity before there is enough evidence.

## Future-review criteria

Revisit ownership when one or more of the following becomes true:

- multiple autonomous projects depend on the same live registry or contract;
- ecosystem lineage cannot be understood from existing project-local artifacts;
- recommendation/adoption history spans several projects and becomes hard to audit;
- interface compatibility requires active versioning policy;
- project placement or root-level governance decisions recur;
- ProjectForge-hosted infrastructure creates misleading ownership assumptions;
- EII or another consumer needs ecosystem metadata but should not own it.

## Candidate future outcomes

Future review may conclude that ecosystem infrastructure should remain:

1. lightweight neutral files under an EIP root;
2. a shared infrastructure layer without project identity;
3. a dedicated infrastructure project, but only after explicit approval;
4. distributed across project-local artifacts with only a small index;
5. some hybrid approach.

No outcome is selected now.

## Explicit non-goals

This note does not:

- create infrastructure;
- create a registry;
- create interface contracts;
- create a project;
- assign ownership to EII;
- assign ownership to MetaHarvest;
- assign ownership to ProjectForge;
- implement repository restructuring;
- grant governance authority.

## Preserved question

Should ecosystem infrastructure remain shared neutral infrastructure, or eventually require a dedicated owner?

This remains an open foundational ecosystem question.
