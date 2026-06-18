# Report: ArchitectureHarvest first-class integration

Date: 2026-06-06

## Summary

ArchitectureHarvest was integrated as ProjectForge's architectural advisory service and feedback repository. The integration adds ProjectForge lifecycle consultation points, generated-project architecture placeholders, review templates, adoption outcome templates, MacroForge relevance scaffolding, and negative rules preventing advisory recommendations from becoming automatic implementation.

## Integration points

- Governance: ProjectForge constitution and context policy now define ArchitectureHarvest consultation triggers, non-triggers, statuses, feedback loop, and negative rules.
- Operating instructions: Root and generated-project agent instructions now tell Hermes when to consult ArchitectureHarvest and when not to.
- Project creation: generated projects receive lightweight `architecture/` and `architecture/architectureharvest/` scaffolding.
- Review loop: architecture review templates record material architecture change, relevance changes, simplification/replacement/deletion opportunities, recurring failures, and report-back candidates.
- Feedback: adoption outcome templates support local project records and central `ArchitectureHarvest/adoption_log/` mirroring.
- MacroForge: a relevance-map scaffold now captures future data-platform pattern categories and unapproved future candidates.

## Safety

No external repositories were cloned, approved, installed, built, or executed. MacroForge was not modified.
