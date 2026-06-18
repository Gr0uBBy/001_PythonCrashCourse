motorcycles = ["honda", "yamaha", "suzuki"]

print(motorcycles)

motorcycles.append("ducati")

print(motorcycles)

motorcycles.insert(0, "bmw")

print(motorcycles)

popped_motorcycle = motorcycles.pop()

print(motorcycles)
print(popped_motorcycle)

first_owned = motorcycles.pop(0)

print(f"The first motorcycle I owned was a {first_owned.title()}.")

motorcycles.remove("yamaha")

print(motorcycles)

invited_guests = ["Marlon Blando", "Jackie Chan", "Chris Bumpstep", "Arnold"]

print(
    f"Dear guests liste belove\n{invited_guests}\nI am pleased to invite you to my party"
)
