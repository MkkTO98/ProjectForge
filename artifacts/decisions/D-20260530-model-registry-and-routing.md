# Decision: Model Registry and Routing

Date: 2026-05-30
Status: Accepted

## Decision
ProjectForge includes a model registry and routing policy under `models/`.

## Rationale
Different agents need different capabilities. The default policy is not to choose the largest model, but the smallest sufficient model, with escalation to Codex/OpenAI for high-value supervision or repeated local failure.

## Consequence
Agents should consult `models/registry.yaml`, `models/routing.yaml`, and `models/selection_policy.yaml` before selecting a model.
