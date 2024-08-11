#!/usr/bin/env python3
"""This program creates different greetings for different users"""

usernames = ['admin', 'juliet', 'peter', 'davi', 'tom']
if usernames:
    for username in usernames:
        if username == 'admin':
            print("Hello {}, would you like to see a status report".format(username))
        elif username != 'admin':
            print("\nHello {}, thank you for logging in again\n".format(username))
else:
    print("We need to find some users!")