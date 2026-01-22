"""A simple class representing a dice"""

from random import randint

class Dice:

    def __init__(self, sides=6):
        """Initializing our key attribute sides components"""
        self.sides = sides

    def roll_die(self):
        """This randomly prints a number from 1 to 6"""
        rand = randint(1, self.sides)

        return rand


die6 = Dice()
die6.sides = 6

print("Rolling a 6-sided Dice 10-times....")

for rand_num in range(10):
    rand_num = die6.roll_die()

    print(rand_num)
print("\n")

print("Rolling a 10-sided Dice 10-times...")

die10 = Dice()
die10.sides = 10

for rand_num10 in range(10):
    rand_num10 = die10.roll_die()

    print(rand_num10)

print("\n")
print("Rolling a 20-sided Dice 10-times...")

die20 = Dice()
die20.sides = 20

for rand_num20 in range(10):
    rand_num20 = die20.roll_die()

    print(rand_num20)
