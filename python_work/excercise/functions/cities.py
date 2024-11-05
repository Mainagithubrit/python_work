#!/usr/bin/env python3

def describe_city(city, country="kenya"):
    """This is a function that prints a city of a country"""

    print("\n{} is in {}".format(city.title(), country.title()))

describe_city("nairobi")
describe_city("kisumu")
describe_city("lagos", country='nigeria')
