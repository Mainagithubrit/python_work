"""This program checks if number is even or odd"""

number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)

if number % 2 == 0:
    print("\nThe number {} is even.".format(number))
else:
    print("\nThe number {} is odd.".format(number))