import pytest
from tools.registry import build_registry

def test_registry_discovers_tool():
    assert build_registry().discover() == ["dependency_audit"]

def test_registry_executes_tool():
    result = build_registry().execute("dependency_audit", {"dependencies": [{"name": "a", "version": "1.0"}]})
    assert result["dependencies_analyzed"] == 1

def test_unknown_tool_fails():
    with pytest.raises(KeyError):
        build_registry().execute("missing", {})
