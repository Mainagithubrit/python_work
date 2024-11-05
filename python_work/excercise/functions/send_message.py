#!/usr/bin/env python3

def show_messages(text, to_be_printed):
    """A function that copies a list of short messages
    to another list and prints the messages"""

    while text:
        the_messages = text.pop()
        to_be_printed.append(the_messages)

    print("\n{}".format(text))

def to_print(to_be_printed):

	for txt in to_be_printed:
		print("\n{}!!!".format(txt.title()))

	print("\n{}".format(to_be_printed))


text = ["Jesus loves me", "Because he died for me", "long may he reign"]
to_be_printed = []

show_messages(text[:], to_be_printed)
to_print(to_be_printed)
