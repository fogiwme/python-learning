#Выполним упражнение 5.10

current_users = ['Alexey', 'vitya', 'valya', 'dmitriy', 'sasha', 'leSha']
new_users = ['pavel', 'mars', 'ilon', 'Alexey', 'Vitya', 'LeSHa']

current_users_copy = []
for user in current_users:
	user = user.lower()
	current_users_copy.append(user)

for name in new_users:
	if name.lower() in current_users_copy:
		print(f'{name.title()}, стоит выбрать уникальное имя')
	else:
		print(f'{name.title()}, имя доступно для использования')