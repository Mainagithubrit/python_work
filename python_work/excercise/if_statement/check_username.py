#!/usr/bin/env python3
"""This program simulates how a website ensures everyone has a unique username"""
current_users = ['naomi', 'ben', 'lisa', 'maureen', 'francis']

new_users = ['peter', 'francis', 'richard', 'elizabeth', 'luna']

lowercase_current_users = [current_user.lower() for current_user in current_users]
for new_user in new_users:
    if new_user.lower() in current_users:
        print("{} already exists, enter new username".format(new_user))
    else:
        print("This username {} is available to use!".format(new_user))