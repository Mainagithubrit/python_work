#!/usr/bin/env python3

def city_country(city, country):
    """This function prints a city and the country its from"""
    
    place = "\n\"{}, {}\"".format(city, country)
    return place.title()

places = city_country('nairobi', 'kenya')
print(places)

places = city_country('cape town', 'south africa')
print(places)

places = city_country('zanzibar', 'tanzania')
print(places)
