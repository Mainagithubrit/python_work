#!/usr/bin/python 3
"""This programs shows the ordinal position of numbers 1 through 9"""

my_num = list(range(1, 10))

for num in my_num:
    if num == 1:
        print("{}st".format(num))
    elif num == 2:
        print("{}nd".format(num))
    elif num == 3:
        print("{}rd".format(num))
    else:
        print("{}th".format(num))