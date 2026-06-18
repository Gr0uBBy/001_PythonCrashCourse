first_name = "ada"
last_name = "lovelace"

full_name = f"{first_name} {last_name}"

# print(full_name)
print(f"Hello, {full_name.title()}!")
print("Hello, " + full_name.title() + "!")

message = f"Hello, {full_name.title()}!"
print(message)

nostarch_url = "https://nostarch.com"

print(nostarch_url.removeprefix("https://"))

p_name = "eric"
print(f"Hello, {p_name.title()} would you like to learn some Python today?")

quote_author = "albert einstein"
print(
    f"{quote_author.title()} once said, 'A person who never made a mistake nwever tried anything new.'"
)

filename = "python_notes.txt"

print(filename.removesuffix(".txt"))
