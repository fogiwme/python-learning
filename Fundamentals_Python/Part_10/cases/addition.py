# Упражнение 10.6, 10.7

while True:
	print('Введи два числа и я их сложу')
	print('(Введи "q", чтобы выйти)\n')

	first_number = input('Введи первое число: ')
	if first_number == 'q':
		break

	second_number = input('Введи второе число: ')
	if second_number == 'q':
		break

	try:
		result = int(first_number) + int(second_number)
	except ValueError:
		print('Так не получится! Вы ввели текст. Стоит вводить цифры. Формат: 2\n')
	else:
		print(f'При сложении получилось: {result}!\n')



