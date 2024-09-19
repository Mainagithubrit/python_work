"""This program checks the number of people in a group
to assign a dinner table"""

group = input("How many people are there in your dinner group? ")

group = int(group)

if group <= 8:
    print("\nCongratulations! There is a table ready for {}".format(group))
else:
    print("\nThere is no available table for {} people".format(group))
    print("\nPlease wait for a table to be available")