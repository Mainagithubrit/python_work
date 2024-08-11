#!/usr/bin/env python3
"""Checks if a user has been banned from commenting in a forum"""

banned_users = ['andrew', 'carl', 'tracy']
user = 'marie'

if user not in banned_users:
    print("{}, you can post a response if you wish.".format(user))