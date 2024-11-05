#!/usr/bin/env python3
"""A program that polls users about their dream vacation"""

responses = {}

active_poll = True

while active_poll:
    name = input("\nWhat is your name? ")
    response = input("\nWhere is your dream vacation? ")

    responses[name] = response
    print(responses)

    repeat = input("\nIs there anyone else to fill the poll (yes/no)? ")

    if repeat == 'no':
        active_poll = False

for name, response in responses.items():
    print("\n{} would like to go to {} as a dream vacation".format(name.title(), response.title()))
