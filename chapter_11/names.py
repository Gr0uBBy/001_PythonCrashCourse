from name_function import get_formatted_name

print("Enter 'q' anytime to quit.")
while True:
    first = input("Please provide your first name: ")
    if first == "q":
        break
    last = input("Please provide your last name: ")
    if last == "q":
        break

    formatted_name = get_formatted_name(first, last)
    print(f"Neatly formatted name: {formatted_name}.")
