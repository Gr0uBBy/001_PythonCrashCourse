from pathlib import Path

path = Path(
    "D:/003_Programowanie/001_Nauka/001_PythonCrashCourse/chapter_10/pi_milion_digits.txt"
)
content = path.read_text()

print("Let's check if your birht date appears in first 1 000 000 numbers of pi. ")
birthday_date = input("Please insert your birth date in format DDMMYYYY.")

if birthday_date in content:
    print("Your birth date appears in first milion numbers of PI.")
else:
    print("Your birth date does not appears in first milion numbers of PI.")

# Idea to find all possible dates in first 1 milion numbers of pi
# Format DD MM YYYY

# int(content.replace(".", ""))
