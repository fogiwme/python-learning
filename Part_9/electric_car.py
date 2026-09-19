# Выполним упражнение 9.9

class Car():
	"""Простая модель автомобиля"""

	def __init__(self, make, model, year):
		"""Инициализирует атрибуты описания автомобиля"""
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0

	def get_descriptive_name(self):
		"""Возвращает аккуратно отформатированное описание"""
		long_name = f'{self.year} {self.make} {self.model}'
		return long_name.title()

	def read_odometer(self):
		"""Выводит пробег машины в милях"""
		print(f"This car has {self.odometer_reading} miles on it!")

	def update_odometer(self, mileage):
		"""
		Устанавливает заданное значение на одометре.
		При попытке обратной подкрутки изменение отклоняется
		"""
		if mileage >= self.odometer_reading:	
			self.odometer_reading = mileage
		else:
			print("\nYou can't roll back an odometer!")

	def increment_odometer(self, mileas):
		"""Увеличивает показания одометра с заданным приращением"""
		self.odometer_reading += mileas

class Battery():
	"""Простая модель аккумулятора электромобиля"""	
	def __init__(self, battery_size=75):
		"""Инициализирует атрибуты аккумулятора"""
		self.battery_size = battery_size

	def describe_battery(self):
		"""Выводит информацию о мощности аккамулятора"""
		print(f'This car has a {self.battery_size}-kWh bettery.')

	def get_range(self):
		"""Выводит приблизительный запас хода для аккумулятора"""
		if self.battery_size == 75:
			range = 260
		elif self.battery_size == 100:
			range = 315

		print(f"This car can go about {range} miles on a full charge\n")

	def upgrade_battery(self):
		if self.battery_size != 100:
			self.battery_size = 100


class ElectricCar(Car):
	"""Представляет аспекты машины, специфические для электромобилей."""

	def __init__(self, make, model, year):
		"""
		Инициализирует атрибуты класса-родителя
		Затем инициализирует атрибуты, специфические для электромобиля
		"""
		super().__init__(make, model, year)
		self.battery = Battery()

	def fill_gas_tank(self):
		"""У электромобилей нет бензобака"""
		print('This car does not need a gas tank!')

my_tesla = ElectricCar('tesla', 'model S', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.fill_gas_tank()
my_tesla.battery.get_range()

my_gtr = ElectricCar('nissan', 'GTR R-34', 2011)
my_gtr.battery.get_range()
my_gtr.battery.upgrade_battery()
my_gtr.battery.get_range()
















