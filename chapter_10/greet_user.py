import json
from pathlib import Path

path = Path("chapter_10/username.json")
contents = path.read_text()
username = json.loads(contents)

print(f"Welcome back {username}, nice to see you again.")
