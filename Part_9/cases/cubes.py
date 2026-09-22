# Выполним упражнение 9.13

from random import randint

class Die:
	def __init__(self, sides=6):
		"""Идентифицируем атрибут sides"""
		self.sides = sides

	def roll_die(self, value):
		"""
		Выводит рандомные числа в заданном диапазоне чисел списком, 
		чтобы красиво выглядело.
		"""
		results = []
		for _ in range(value):
			number = randint(1, self.sides)
			result.append(number)
		
		print(f"{results}\n")

hexagonal = Die()
hexagonal.roll_die(10)

ten_sided = Die(10)
ten_sided.roll_die(10)

twenty_sided = Die(20)
twenty_sided.roll_die(10)