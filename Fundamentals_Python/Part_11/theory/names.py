from name_function import get_formatted_name

print("Напиши 'q', чтобы выйти")

while True:
	first = input('\nДай мне, пожалуйста, свое имя: ')
	if first == 'q':
		break

	last = input('Дай мне, пожалуйста, свою фамилию: ')
	if last == 'q':
		break

	formatted_name = get_formatted_name(first, last)
	print(f"\tОтформатированное имя: {formatted_name}")