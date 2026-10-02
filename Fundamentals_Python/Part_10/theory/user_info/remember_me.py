import json

# Программа загружает имя пользователя, если оно было сохранено ранее.
# В противном случае она запрашивает имя пользователя и сохраняет его.

filename = 'username_alexey.json'

def get_stored_username():
	"""Получает хранимое имя пользователя, если оно существует"""
	try:
		with open(filename) as f:
			username = json.load(f)
	except FileNotFoundError:
		return None
	else:
		return username

def get_new_username():
	"""Запрашивает новое имя пользователя"""
	username = input("\nWhat is your name? ")

	with open(filename, 'w') as f:
		json.dump(username, f)
	return username

def greet_user():
	"""Приветствует пользователя по имени"""
	
	username = get_stored_username()

	if username:
		question = f"{username}, tell me please, "
		question += "did I identify your name correctly?\nYes / No\n"
		answer = input(question)

		if answer.lower() == 'yes':
			print(f'\nCool! Welcome back, {username}!')
		else:
			username = get_new_username()
			print(f"We'll remember you when you come back, {username}!")

	else:
		username = get_new_username()
		print(f"We'll remember you when you come back, {username}!")

greet_user()





















