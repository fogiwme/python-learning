# Выполним упражнение 9.3

class User:
	def __init__(self, first, last, age, city):
		"""Инициализируем атрибуты first, last, age и city"""
		self.first_name = first.title()
		self.last_name = last.title()
		self.age = age
		self.city = city.title()

	def describe_user(self):
		"""Выводит информацию о пользователе"""
		print(f'Имя: {self.first_name}')
		print(f'Фамилия: {self.last_name}')
		print(f'Возвраст: {self.age}')
		print(f'Город проживания: {self.city}')

	def greet_user(self):
		"""Выводит угрожающее сообщение пользователю"""
		message = f'\nПриветствую, {self.first_name} {self.last_name}! '
		message += f'Я знаю, что тебе {self.age} лет, и ты живешь в {self.city}\n'
		print(message)

user1 = User('алексей', 'крылов', 22, 'пушкино')
user2 = User('виктор', "крылов", 30, "пушкино")
user3 = User('дмитрий', "крылов", 56, "пушкино")

user1.describe_user()
user1.greet_user()

user2.describe_user()
user2.greet_user()

user3.describe_user()
user3.greet_user()