from pathlib import Path


def word_count(path):
    path = Path("chapter_10/alice.txt")

    try:
        contents = path.read_text(encoding="utf-8")
    except FileNotFoundError:
        # print(f"Sorry, the file {path} does not exist.")
        pass
    else:
        num_words = len(contents.split())
        print(f"The file {path} contains {num_words} words.")
