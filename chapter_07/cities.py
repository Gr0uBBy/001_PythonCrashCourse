prompt = "\nTell me which cities you would like to visit."
prompt += "\n(Enter 'quit' whenever you would like to finish)\n"

while True:
    city = input(prompt)

    if city == "quit":
        break
    else:
        print(f"I would like to visit {city.title()} too.")
