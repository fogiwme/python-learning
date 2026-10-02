# Упражнения 10.8, 10.9
filename_dogs = 'dogs.txt'
filename_cats = 'cat.txt'

try:
	with open(filename_dogs) as file_dogs:
		lines_dogs = file_dogs.readlines()

except FileNotFoundError:
	print(f'Файл {filename_dogs} не найден, попробуй ввести точное местоположение.')
else:
	print(f"В списке 'dogs.txt' введены такие клички собак:")
	for line_dog in lines_dogs:
		print(line_dog.rstrip())

try:
	with open(filename_cats) as file_cats:
		lines_cats = file_cats.readlines()

except FileNotFoundError:
	pass
else:
	print(f"\nВ списке 'cats.txt' введены такие клички кошек:")
	for line_cat in lines_cats:
		print(line_cat.rstrip())
