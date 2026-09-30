from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TEXT = (ROOT / "EXPLAINABILITY.md").read_text()
REQUIRED = ["## Inputs and Data Sources", "## Decision and Reasoning", "## Limits and Constraints"]
FORBIDDEN = ["## Inputs\n", "## Decision\n", "## Limits\n"]
for heading in REQUIRED:
    assert heading in TEXT, heading
for heading in FORBIDDEN:
    assert heading not in TEXT, heading
for heading in REQUIRED:
    start = TEXT.index(heading) + len(heading)
    tail = TEXT[start:].lstrip()
    section = tail.split("\n## ", 1)[0]
    assert section.count(".") >= 2, heading
print("documentation structural audit passed")
