from adapters.openai_adapter import OpenAIAdapter
from adapters.crewai_adapter import CrewAIAdapter
from adapters.claude_code_adapter import ClaudeCodeAdapter
from adapters.lyzr_adapter import LyzrAdapter

def test_all_adapters_share_portable_contract():
    payload = {"dependencies": [{"name": "a", "version": "1.0"}]}
    for adapter in [OpenAIAdapter(), CrewAIAdapter(), ClaudeCodeAdapter(), LyzrAdapter()]:
        assert adapter.invoke("dependency_audit", payload)["dependencies_analyzed"] == 1
