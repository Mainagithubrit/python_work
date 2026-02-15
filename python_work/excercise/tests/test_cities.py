import unittest
from city_country import city_country, get_formatted_city_country

class NamesTestCase(unittest.TestCase):
    """Tests for 'city_country.py' """

    def test_city_country(self):
        """This tests city_country function"""
        neatly_formatted = city_country('nairobi', 'kenya')
        self.assertEqual(neatly_formatted, 'Nairobi, Kenya')

    def test_city_country_population(self):
        """Checks if population is included in city_county.py"""
        neatly_formatted = get_formatted_city_country('tokyo', 'japan', 37000000)
        self.assertEqual(neatly_formatted, 'Tokyo, Japan - Population 37000000')

if __name__ == '__main__':
    unittest.main()

