# Выполним упражнение 9.7, 9.8

class User:
	def __init__(self, first, last, age, city):
		"""Инициализируем атрибуты first, last, age и city"""
		self.first_name = first.title()
		self.last_name = last.title()
		self.age = age
		self.city = city.title()
		self.login_attempts = 0

	def describe_user(self):
		"""Выводит информацию о пользователе"""
		print(f'Имя: {self.first_name}')
		print(f'Фамилия: {self.last_name}')
		print(f'Возраст: {self.age}')
		print(f'Город проживания: {self.city}')

	def greet_user(self):
		"""Выводит угрожающее сообщение пользователю"""
		message = f'\nПриветствую, {self.first_name} {self.last_name}! '
		message += f'Я знаю, что тебе {self.age} лет, и ты живешь в {self.city}\n'
		print(message)

	def increment_login_attempts(self):
		self.login_attempts += 1

	def reset_login_attempts(self):
		self.login_attempts = 0

class Privileges:
	def __init__(self):
		self.privileges = [
		'разрешено добавлять сообщения',
		'разрешено удалять пользователей',
		"разрешено банить пользователей",
		"разрешено запускать приложения от имени администратора"
		]

	def show_privileges(self):
		for privilege in self.privileges:
			if privilege == "разрешено запускать приложения от имени администратора":
				print(f"\t{privilege.capitalize()}.")
			else:
				print(f"\t{privilege.capitalize()};")

class Admin(User):
	def __init__(self, first, last, age, city):
		super().__init__(first, last, age, city)
		self.privileges = Privileges()

	def print_privileges(self):
		print(f"Пользователь {self.first_name} {self.last_name} имеет такие привелегии:")


alexey_krylov = Admin('Алексей', "Крылов", 22, "Пушкино")
alexey_krylov.print_privileges()
alexey_krylov.privileges.show_privileges()









