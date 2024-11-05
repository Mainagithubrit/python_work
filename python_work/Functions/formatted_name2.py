#!/usr/bin/env python3

def get_formatted_name(first_name, middle_name, last_name):
    """Return a full name, neatly formatted."""

    full_name = "{} {} {}".format(first_name, middle_name, last_name)

    return full_name.title()

musician = get_formatted_name('john', 'lee', 'hooker')
print(musician)
