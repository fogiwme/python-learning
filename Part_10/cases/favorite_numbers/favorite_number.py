# Упражнения 10.11, 10.12

import json
filename = 'favorite_number_10.json'

try:
	with open(filename) as f:
		favorite_number = json.load(f)
except FileNotFoundError:
	favorite_number = input('Какое твое любимое число? ')
	with open(filename, 'w') as f:
		json.dump(favorite_number, f)
		print('Я запомню ваше число!')
else:
	print(f"Я знаю ваше любимое число! Это {favorite_number}")