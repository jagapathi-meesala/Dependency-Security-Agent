---
name: dependency-audit
description: Analyze dependency inventories and trusted vulnerability findings to identify security risks and explicit version policy violations.
---

# Dependency Audit Skill

## Purpose

Analyze a dependency inventory, normalize supplied vulnerability findings, and identify explicit version-policy violations.

## Inputs

The skill accepts a `dependencies` list containing package names and versions. It may also accept `findings` supplied by an external scanner and a `policy.allowed_versions` mapping.

## Behavior

Inputs are validated before analysis. Severity is normalized deterministically, action categories are derived from RULES.md, and provenance is retained in the result.

## Outputs

The result contains dependency and finding counts, severity counts, normalized findings, policy violations, and a provenance statement.

## Invalid Inputs

Missing or malformed dependency records and unsupported severity values cause validation errors. The skill does not silently repair invalid data.
