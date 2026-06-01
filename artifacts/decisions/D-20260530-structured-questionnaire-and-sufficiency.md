# Decision: Structured Questionnaire and Sufficiency Policy

Date: 2026-05-30
Status: Accepted

## Decision
ProjectForge uses `config/setup_questionnaire.yaml` as the deterministic question source and `config/sufficiency_policy.yaml` to decide when enough has been specified to bootstrap a project.

## Rationale
Pure model inference is too inconsistent for reusable project initialization. The agent may ask contextual follow-up questions, but the baseline interview must be file-backed and reproducible.

## Consequence
Generated projects should store accepted and deferred answers as decision artifacts. Missing later specifications must use deferred decisions and clarification severity levels.
