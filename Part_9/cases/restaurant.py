# Выполним упражнение 9.1, 9.2

class Restaurant():
	def __init__(self, restaurant_name, cuisine_type):
		"""Инициализирует атрибуты restaurant_name и cuisine_type"""
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type

	def describe_restaurant(self):
		"""Выводит два атрибута"""
		print(self.restaurant_name.capitalize())
		print(f'{self.cuisine_type}\n')

	def open_restaurant(self):
		"""Выводит сообщение, что ресторан открыт"""
		print(f'Ресторан {self.restaurant_name} открыт!\n')

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