def get_formatted_name(first_name, last_name):
	"""Возвращает аккуратно отформатированное полное имя."""
	full_name = f'{first_name} {last_name}'
	return full_name.title()

musician = get_formatted_name('jimi','hendrix')
print(musician)

def get_formatted_name_2(first_name_2, last_name_2, middle_name_2=''):
	"""Возвращает аккуратно отформатированное полное имя."""
	if middle_name_2:
		full_name = f'{first_name_2} {middle_name_2} {last_name_2}'
	else:
		full_name = f'{first_name_2} {last_name_2}'
	return full_name.title()

musician_2 = get_formatted_name_2('jhon', 'hooker', 'lee')
print(musician_2)

musician_2 = get_formatted_name_2('jimi', 'hendrix')
print(musician_2)

# Бесконечный цикл

while True:
	print("\nPlease tell me your name.")
	print("\n(enter 'q' at any time to quit)")
	
	f_name = input('First name: ')
	if f_name == 'q':
		break

	l_name = input('Last name: ')
	if l_name == 'q':
		break

	formatted_name = get_formatted_name(f_name, l_name)
	print(f'\nHello, {formatted_name}!')