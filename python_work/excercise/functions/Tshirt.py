#!/usr/bin/env python3
"""A way to learn how use positional arguments and keyword arguments"""

def make_shirt(size, message):
    """This fuction prints size and message for a shirt"""

    print("\nThe T-shirt size is {}".format(size))
    print("The message to print on the T-shirt is \"{}\"".format(message.title()))

make_shirt(25, "jesus rocks")
make_shirt(size=32, message="jesus saves")
