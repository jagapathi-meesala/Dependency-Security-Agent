from core.audit import audit_dependencies

def test_high_finding_requires_action():
    result = audit_dependencies({"dependencies": [{"name": "a", "version": "1.0"}], "findings": [{"package": "a", "severity": "HIGH", "identifier": "CVE-test"}]})
    assert result["findings"][0]["action"] == "action_required"
    assert result["severity_counts"]["high"] == 1

def test_policy_violation_is_deterministic():
    result = audit_dependencies({"dependencies": [{"name": "a", "version": "1.0"}], "policy": {"allowed_versions": {"a": "2.0"}}})
    assert result["policy_violations"][0]["type"] == "policy_violation"

def test_missing_identifier_is_flagged():
    result = audit_dependencies({"dependencies": [{"name": "a", "version": "1.0"}], "findings": [{"package": "a", "severity": "low"}]})
    assert result["findings"][0]["evidence_quality"] == "identifier_missing"
