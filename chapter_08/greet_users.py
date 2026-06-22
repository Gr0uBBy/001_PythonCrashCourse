def greet_users(users):
    for user in users:
        print(f"Hello {user.title()}! How are you doing today?")


users_list = ["Marek", "Adam", "Wojtek"]

greet_users(users_list)
