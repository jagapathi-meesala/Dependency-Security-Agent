from pathlib import Path

def test_required_docs_exist():
    for name in ["SOUL.md", "AGENTS.md", "DUTIES.md", "RULES.md", "EXPLAINABILITY.md", "README.md"]:
        assert Path(name).exists()

def test_explainability_headings():
    text = Path("EXPLAINABILITY.md").read_text()
    assert "## Inputs and Data Sources" in text
    assert "## Decision and Reasoning" in text
    assert "## Limits and Constraints" in text
    assert "## Inputs\n" not in text
    assert "## Decision\n" not in text
    assert "## Limits\n" not in text
