# Dependency Security Agent Explainability

## Inputs and Data Sources

The agent accepts a dependency inventory containing package names and versions, plus optional vulnerability findings and explicit version-policy data. Vulnerability evidence is treated as supplied input from an external scanner or other trusted source; this implementation does not silently query an external advisory database.

## Decision and Reasoning

The agent validates each dependency and finding, normalizes severity to lowercase, and maps severity to an action category using the deterministic rules in RULES.md. Critical and high findings become `action_required`, medium findings become `review`, and low or unknown findings become `monitor`; explicit version-policy mismatches become policy violations.

## Limits and Constraints

The agent cannot independently establish that an unreported dependency is vulnerability-free because it does not perform external advisory lookups. It also cannot guarantee application security, exploitability, remediation success, or compatibility of a proposed version change.

## Agent Purpose

The agent provides a reproducible dependency-security analysis layer that can consume dependency inventories and findings from other systems.

## Input Mechanisms

Inputs are passed to the portable tool contract as structured data. Framework adapters translate external calls into this same contract without changing the domain rules.

## Decision Mechanisms

Decision categories are derived from a fixed severity mapping and explicit version-policy comparisons. No probabilistic model is required for these classifications.

## Execution Limits

Only supplied dependency records, findings, and policy entries are analyzed. Network access, package installation, private registry access, and vulnerability-database enrichment are outside the implementation boundary.

## Output Contract

Outputs include counts, normalized findings, policy violations, and provenance. Each finding retains its supplied package, identifier when available, severity, action, evidence-quality indicator, and source.

## Complete Execution Lifecycle

The registry discovers the dependency-audit tool, validates the input, executes the deterministic audit, and returns a structured result. An invalid input stops execution with an explicit validation error rather than a fabricated result.

## Tool-by-tool Behavior

The `dependency_audit` tool validates dependency and finding structures before invoking the audit function. It computes severity counts and policy mismatches and returns the resulting structured object.

## Tool Inputs

The tool requires a `dependencies` array and optionally accepts `findings` and `policy`. Each dependency requires a non-empty name and version; finding severity must be one of the documented values.

## Tool Validation

Validation rejects non-object payloads, missing dependency lists, malformed dependency records, malformed finding records, and unsupported severity values. Validation occurs before domain processing.

## Tool Failure Behavior

Validation failures raise explicit `ValueError` exceptions, while unknown registry tools raise `KeyError`. The implementation does not convert errors into successful-looking outputs.

## Deterministic Rules

The severity-to-action mapping and version-policy comparison are fixed in RULES.md. Given the same input payload, the same rules produce the same structured classification.

## Formulas

Severity counts are calculated by incrementing one counter for each normalized finding. Policy violations are the set of dependency records whose installed version differs from the explicitly supplied allowed version.

## Worked Example

For a dependency with an externally supplied high-severity finding, the result normalizes the severity to `high` and assigns `action_required`. If a policy says package `example` must be version `2.0.0` while the input reports `1.9.0`, the result contains a `policy_violation` record.

## Explainability of Calculated Results

Every action category is traceable to the severity mapping in RULES.md, and every policy violation is traceable to a direct installed-versus-allowed version comparison. The agent does not infer hidden evidence.

## Provenance

The provenance field states that vulnerability evidence was supplied in the input payload and that no external advisory lookup was performed. This distinction prevents a supplied scanner result from being represented as independently verified intelligence.
