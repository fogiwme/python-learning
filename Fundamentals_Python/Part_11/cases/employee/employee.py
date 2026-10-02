# Упражнение 11.3

class Employee:

	def __init__(self, first_name, last_name, annual_salary):
		"""Назначим вводные дефолтные данные"""

		self.first_name = first_name.title()
		self.last_name = last_name.title()
		self.annual_salary = annual_salary

		self.full_name = f'{self.first_name} {self.last_name}'

	def give_raise(self, raise_salary=5000):
		"""Напишем сообщение текущей зп"""
		message = (f'\n{self.full_name} ')
		message += (f'сейчас получает {self.annual_salary} долларов')
		print(message)

		"""Прибавим к текущей зп надбавку и выведем результат"""
		self.annual_salary += raise_salary
		message_raise = f'А после надбавки в {raise_salary}, '
		message_raise += f'{self.full_name} стал получать {self.annual_salary} долларов\n'
		print(message_raise)
		
# person = Employee('алексей', 'крылов', 10_000)

# person.give_raise()
