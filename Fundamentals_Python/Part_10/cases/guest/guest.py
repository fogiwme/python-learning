# Выполним упражнение 10.3

filename = 'guest.txt'
name = input('Ввведите свое имя:')

with open(filename, 'w') as file_object:
	file_object.write(f'Имя пользователя: {name.title()}')