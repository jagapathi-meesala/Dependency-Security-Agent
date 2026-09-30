from typing import Any

SEVERITY_ACTION = {"critical": "action_required", "high": "action_required", "medium": "review", "low": "monitor", "unknown": "monitor"}


def audit_dependencies(payload: dict[str, Any]) -> dict[str, Any]:
    dependencies = payload["dependencies"]
    findings = payload.get("findings", [])
    policy = payload.get("policy", {})
    allowed_versions = policy.get("allowed_versions", {}) if isinstance(policy, dict) else {}

    normalized = []
    for finding in findings:
        severity = str(finding.get("severity", "unknown")).lower()
        item = {
            "package": finding.get("package"),
            "identifier": finding.get("identifier"),
            "severity": severity,
            "action": SEVERITY_ACTION[severity],
            "evidence_quality": "complete" if finding.get("identifier") else "identifier_missing",
            "source": finding.get("source", "supplied_input"),
        }
        normalized.append(item)

    violations = []
    for dependency in dependencies:
        expected = allowed_versions.get(dependency["name"])
        if expected is not None and dependency["version"] != expected:
            violations.append({
                "package": dependency["name"],
                "installed_version": dependency["version"],
                "allowed_version": expected,
                "type": "policy_violation",
            })

    counts = {severity: 0 for severity in SEVERITY_ACTION}
    for item in normalized:
        counts[item["severity"]] += 1

    return {
        "dependencies_analyzed": len(dependencies),
        "findings_analyzed": len(normalized),
        "severity_counts": counts,
        "findings": normalized,
        "policy_violations": violations,
        "provenance": "All vulnerability evidence was supplied in the input payload; no external advisory lookup was performed.",
    }
