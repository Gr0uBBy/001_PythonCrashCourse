confirmed_users = []
unconfirmed_users = ["dan", "thomas", "monika", "sophia"]

while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print(f"Currently veryfying user: {current_user.title()}.")
    confirmed_users.append(current_user)
    print(f"User: {current_user.title()} has been verified.")

for user in confirmed_users:
    print(f"User {user.title()} has been added to the veryfied user list.")
