class User:
    def __init__(self, first_name, last_name, age, gender, second_name=""):
        self.first_name = first_name
        self.second_name = second_name
        self.last_name = last_name
        self.age = age
        self.gender = gender

    def describe_user(self):
        user = {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "age": self.age,
            "gender": self.gender,
            "second_name": self.second_name,
        }
        return user

    def greet_user(self):
        return print(f"Hello {self.first_name} {self.second_name} {self.last_name}!")


me = User("Marek", "Kwitek", 33, "male", "Andrzej")

print(me.describe_user())
me.greet_user()

you = User("Adam", "Tadek", 23, "female")
print(you.describe_user())
you.greet_user()
