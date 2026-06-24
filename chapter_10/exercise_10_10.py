from pathlib import Path

file_path = Path("chapter_10/pride_and_prejudice.txt")

try:
    content = file_path.read_text(encoding="utf-8")
except FileExistsError:
    pass

word = "the"
count_word = content.count(word)
print(f"The word '{word}' appears in the {file_path} {count_word} times.")
