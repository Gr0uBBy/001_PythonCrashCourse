from random import randint


class Dice:
    def __init__(self, number_of_sides):
        self.number_of_sides = number_of_sides

    def roll(self):
        return randint(1, self.number_of_sides)


dice_6 = Dice(6)
i = 1

while i <= 10:
    print(
        f"Roll {i} of dice with {dice_6.number_of_sides} sides rolled: {dice_6.roll()}"
    )
    i += 1

dice_10 = Dice(10)
n = 1

while n <= 10:
    print(
        f"Roll {n} of dice with {dice_10.number_of_sides} sides rolled: {dice_10.roll()}"
    )
    n += 1
dice_20 = Dice(20)
m = 1

while m <= 10:
    print(
        f"Roll {m} of dice with {dice_20.number_of_sides} sides rolled: {dice_20.roll()}"
    )
    m += 1
