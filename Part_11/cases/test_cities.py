import unittest
from city_functions import place

class CitiesTestCase(unittest.TestCase):
	"""Тесты для 'city_functions'"""

	def test_city_country(self):
		test_city = place('santiago', 'chile')
		self.assertEqual(test_city, 'Santiago, Chile')

	def test_city_country_population(self):
		test_city_population = place('santiago', 'chile', 5_000_000)
		self.assertEqual(
			test_city_population, 'Santiago, Chile -- population 5000000')

if __name__ == '__main__':
	unittest.main()