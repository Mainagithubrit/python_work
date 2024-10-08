#!/usr/bin/env python3
"""a program that takes in user input to fill a dictionary"""

responses = {}

# set a flag to indicate that polling is active

polling_active = True

while polling_active:
    # prompt for the person's name and response.
    name = input('\nWhat is your name? ')
    response = input('Which mountain would you like to climb someday? ')

    # store the response in the dictionary
    responses[name] = response

    # Find out if anyone else is going to take the poll
    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat == 'no':
        polling_active = False

# polling is complete show results.
print("\n\t\t*** Poll Results ***")
for name, response in responses.items():
    print("{} would like to climb {}.".format(name.title(), response.title()))

print(responses)
