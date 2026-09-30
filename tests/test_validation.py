import pytest
from core.validation import validate_dependency_input

def test_missing_dependencies_rejected():
    with pytest.raises(ValueError):
        validate_dependency_input({})

def test_bad_severity_rejected():
    with pytest.raises(ValueError):
        validate_dependency_input({"dependencies": [{"name": "a", "version": "1"}], "findings": [{"severity": "extreme"}]})
