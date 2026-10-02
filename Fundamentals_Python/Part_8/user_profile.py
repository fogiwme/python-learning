def build_profile(first, last, **user_info):
	"""Строит словарь с информацией о пользователе"""
	user_info['first_name'] = first.title()
	user_info['last_name'] = last.title()
	return user_info

user_profile = build_profile('albert', 'einstein',
							location='princeton',
							field='physics')
print(user_profile)

# Выполним упражнение 8.13

my_profile = build_profile('alexey', 'krylov',
							city="Pushkino",
							age=22,
							hobby='computer gaming')
print(my_profile)

