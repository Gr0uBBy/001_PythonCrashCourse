class Dog:
    """A simple attempt to model a dog"""

    def __init__(self, name, age):
        """Inicialize name and age attributes."""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in the response to a command"""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """Simulate dog rolling over in response to a command"""
        print(f"{self.name} rolled over!")


my_dog = Dog("Willie", 6)
your_dog = Dog("Lucy", 3)

print(f"My dog name is {my_dog.name}.")
print(f"{my_dog.name} is {my_dog.age} yers old.")
my_dog.sit()
my_dog.roll_over()

print(f"Your dog name is {your_dog.name}")
print(f"Your dog, {your_dog.name}, is {your_dog.age} years old.")
your_dog.sit()
your_dog.roll_over()
