# Познакомимся с функциями поближе

def greet_user():
	"""Выводит простое приветствие"""
	print('Hello!')

greet_user()

def greet_user(username):
	"""Выводит приветствие аргумента, которое входит в параметр"""
	print(f'Hello, {username.title()}!')

greet_user('jesse')
greet_user('sarah')

