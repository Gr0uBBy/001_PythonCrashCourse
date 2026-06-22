def describe_pet(pet_name, animal_type="dog"):
    print(f"I have a {animal_type}")
    print(f"My {animal_type}'s name is {pet_name.title()}")


describe_pet("hamster", "harry")
describe_pet("cat", "bogdan")
describe_pet(animal_type="dog", pet_name="bombel")
describe_pet(pet_name="willie")
