# Упражнение 11.3

import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
	"""Тесты для класса Employee"""

	def setUp(self):
		self.personality = Employee('алексей', "крылов", 10_000)

	def test_give_default_raise(self):
		"""Проверим работу при вводе дефолтного значения надбавки"""
		self.personality.give_raise()
		self.assertEqual(self.personality.annual_salary, 15_000)

	def test_give_custom_raise(self):
		"""Проверим работу при вводе заданного значения надбавки"""
		self.personality.give_raise(3_000)
		self.assertEqual(self.personality.annual_salary, 13_000)

if __name__ == '__main__':
	unittest.main()

