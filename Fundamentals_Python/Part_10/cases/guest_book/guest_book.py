# Выполним упражнение 10.4

filename = 'guest_book.txt'
flag = True

while flag:
	name = input('\t\t\tВведите свое имя: \n\t\t(Нажмитие "q", чтобы выйти)\n\t\t\t\t')
	
	if name == 'q':
		break
	
	with open(filename, 'a') as file_object:
		file_object.write(f'Имя пользователя: {name.title()}\n')

	print(f'\nПривет, {name.title()}! Теперь мы тебя запомнили, переживать не стоит.\n')

