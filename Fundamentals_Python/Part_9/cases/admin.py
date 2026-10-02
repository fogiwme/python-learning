# Выполним упражнение 9.7, 9.8

from user_method import User

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


"""alexey_krylov = Admin('Алексей', "Крылов", 22, "Пушкино")
alexey_krylov.print_privileges()
alexey_krylov.privileges.show_privileges()"""









