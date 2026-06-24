import json
from pathlib import Path


def greet_user():
    path = Path("chapter_10/username.json")
    username = get_stored_username(path)
    if username:
        print(f"Welcome back {username}!")
    else:
        username = set_new_username(path)
        print(f"We will remember you when you come back, {username}!")


def get_stored_username(path):
    if path.exists():
        contents = path.read_text()
        username = json.loads(contents)
        return username
    else:
        return None


def set_new_username(path):
    username = input("What is your name? ")
    contents = json.dumps(username)
    path.write_text(contents)
    return username


greet_user()
