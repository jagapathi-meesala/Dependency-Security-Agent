# Dependency Security Agent

A framework-independent OpenGAP-style agent for deterministic analysis of dependency inventories, supplied vulnerability findings, and explicit version policies.

## Scope

The implementation validates structured dependency data, normalizes supplied severity values, classifies actions, detects explicit version-policy mismatches, and preserves provenance. It does not independently query vulnerability databases or perform exploitation.

## Structure

- `agent.yaml` — OpenGAP manifest
- `SOUL.md` — agent identity and boundaries
- `skills/dependency-audit/` — skill documentation
- `tools/` — executable domain tool and registry
- `contracts/` — portable tool contracts and registry
- `core/` — framework-independent validation and audit logic
- `adapters/` — OpenAI, CrewAI, Claude Code, and Lyzr compatibility boundaries
- `verification/` — structural checks
- `tests/` — pytest suite

## Local Validation

Run `python verification/documentation_audit.py` and `pytest -q`.

If the OpenGAP CLI is installed, run `opengap validate` from this repository. Do not treat pytest as a substitute for official OpenGAP validation.

## Runtime Configuration

Optional runtime settings are represented in `.env.example`. Real `.env` files and secrets are excluded from Git.
