responses = {}

pool_active = True

while pool_active:
    name = input("Please provide your name:\n")
    response = input("Which town would you like to visit:\n")

    responses[name] = response

    continuing = input("Would you like to continue (yes/no)?")
    if continuing == "no":
        pool_active = False

for name, response in responses.items():
    print(f"User {name.title()} would like to visit {response.title()}")
