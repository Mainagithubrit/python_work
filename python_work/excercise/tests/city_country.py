def city_country(city_name, country_name):
    """This function creates neatly formatted names
    of a city and its country"""

    neat = f"{city_name}, {country_name}"

    return neat.title()

def get_formatted_city_country(city_name, country_name, population=None):
    """Generates a neatly formatted name"""
    neat = f"{city_name}, {country_name} - population {population}"

    return neat.title()

my_city_country_names = city_country('rome', 'italy')
my_new_city_country_pop = get_formatted_city_country('dar es salaam', 'tanzania', 5400000)
print(my_city_country_names)
print(my_new_city_country_pop)
