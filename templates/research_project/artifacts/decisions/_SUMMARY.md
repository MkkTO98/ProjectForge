# Folder Summary: artifacts/decisions

Artifact role: durable governance history for decisions.

## Purpose
Decision artifacts record choices that affect scope, responsibility, architecture, policy, external dependencies, approval boundaries, or future agent behavior. A decision should preserve rationale, alternatives considered, consequences, and status: Proposed, Accepted, Rejected, Deferred, or Superseded.

## Decision record should answer
- What was decided?
- Why was it decided?
- What alternatives were considered?
- What consequences or follow-up constraints exist?
- What is the status: Proposed, Accepted, Rejected, Deferred, or Superseded?

## Rules
- Do not use decisions as hidden task plans.
- Do not rewrite accepted history to make it look cleaner; create a superseding decision when policy changes.
- Missing or ambiguous policy that affects safety, scope, cost, or responsibility should become a Deferred decision or blocking question.
