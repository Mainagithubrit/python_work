#!/usr/bin/env python3

def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted"""

    full_name = "{} {}".format(first_name, last_name)
    return full_name.title()

# An infinte loop!
while True:
    print("\nPlease tell me your name:")
    print('Enter \'q\' to quit any time')
    
    f_name = input("First name: ")
    if f_name == 'q':
        break

    l_name = input("Last name: ")
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print("\nHello, {}!".format(formatted_name))
