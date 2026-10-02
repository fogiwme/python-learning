# Упражнение 10.11

import json
filename = 'favorite_number.json'

with open(filename) as f:
	favorite_number = json.load(f)
	print(f"Я знаю ваше любимое число! Это {favorite_number}")