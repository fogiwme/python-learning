# Выполним упражнение 9.6

class Restaurant():
	def __init__(self, restaurant_name, cuisine_type):
		"""Инициализирует атрибуты restaurant_name и cuisine_type"""
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
		self.number_served = 0

	def describe_restaurant(self):
		"""Выводит два атрибута"""
		print(self.restaurant_name.capitalize())
		print(f'{self.cuisine_type}\n')

	def open_restaurant(self):
		"""Выводит сообщение, что ресторан открыт"""
		print(f'Restaurant {self.restaurant_name} opened!\n')

	def set_number_served(self, number):
		self.number_served = number

	def increment_number_served(self, changing_number):
		self.number_served += changing_number

	def print_number_served(self):
		print(f"In {self.restaurant_name} served {self.number_served}\n")

class IceCreamStand(Restaurant):
	def __init__(self, restaurant_name, cuisine_type):
		"""
		Инициализирует атрибуты класса-родителя
		Инициализирует атрибут flavors для хранения списка сортов мороженного
		"""
		super().__init__(restaurant_name, cuisine_type)
		self.flavors = ["banana", "apple", "strawberry", "raspberry"]

	def describe_flavors(self):
		print(f"Also in {self.restaurant_name} restaurant ice creams has these flavors: ")
		for flavor in self.flavors:
			print(f"\t{flavor.title()}")

krylov_restaurant = IceCreamStand("Krylov's", "japanese")
krylov_restaurant.open_restaurant()
krylov_restaurant.set_number_served(40)
krylov_restaurant.increment_number_served(5)
krylov_restaurant.print_number_served()
krylov_restaurant.describe_flavors()
















