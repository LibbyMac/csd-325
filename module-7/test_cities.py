import unittest
from city_functions import city_country

class test_city_country(unittest.TestCase):
    def test_city_country(self):
        formatted_city_country = city_country("Dublin", "Ireland")
        self.assertEqual(formatted_city_country, "Dublin, Ireland")

if __name__ == '__main__':
       unittest.main()