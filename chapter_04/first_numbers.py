numbers = list(range(1, 11, 2))

print(numbers)

squares = []

for value in range(1, 11):
    squares.append(value**2)

print(squares)

squares_v2 = [value**2 for value in range(1, 11)]

print(squares_v2)

milion_list = list(range(1, 1_000_001))
print(f"min value: {min(milion_list)} and max value: {max(milion_list)}")

threes = list(range(3, 33, 3))
for three in threes:
    print(three)

cubes = [value**3 for value in range(1, 11)]
print(cubes)
