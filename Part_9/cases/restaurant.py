# Выполним упражнение 9.1, 9.2, 9.4

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
		print(f'Ресторан {self.restaurant_name} открыт!\n')

	def set_number_served(self, number):
		self.number_served = number

	def increment_number_served(self, changing_number):
		self.number_served += changing_number

	def print_number_served(self):
		print(f"In {self.restaurant_name} served {self.number_served}")



# Напишем экземпляр на основе своего класса:

restaurant = Restaurant("Krylov's", 'japanese')
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)

restaurant.describe_restaurant()
restaurant.open_restaurant()

restaurant1 = Restaurant("Janga's", "italiano")
restaurant2 = Restaurant("Gershe's", "korean")
restaurant3 = Restaurant("Kuper's", "mexicano")

restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()

restaurant.set_number_served(5)
restaurant.print_number_served()

restaurant.increment_number_served(3)
restaurant.print_number_served()










