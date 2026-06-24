from pathlib import Path

# path = Path("pi_digits.txt")
path = Path(
    "D:/003_Programowanie/001_Nauka/001_PythonCrashCourse/chapter_10/pi_digits.txt"
)

# content = path.read_text().rstrip()
# print(path)
# print(content)

# contents = path.read_text()
# lines = contents.splitlines()

# for line in lines:
#     print(line)

for line in path.read_text().splitlines():
    print(f"{line.lstrip()}")
