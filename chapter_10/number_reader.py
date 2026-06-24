import json
from pathlib import Path

path = Path("chapter_10/numbers.json")
contents = path.read_text()
numbers = json.loads(contents)
