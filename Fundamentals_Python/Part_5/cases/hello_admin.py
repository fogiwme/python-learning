#Выполним упражнение 5.8

names = ['alexey', 'vitya', 'admin', 'dmitriy', 'sasha']
	
for name in names:
	if name == 'admin':
		print('\nHello admin, would you like to see a status report?\n')
	else:
		print(f'Hello {name.title()}, thank you for logging in again.')

#Выполним упражнение 5.9
#Проверим есть ли элементы в списке

if names:
	pass #говорит программе ничего не делать
else:
	print('We need to find some users!')

#Сделаем чуть проще

if not names:
	print('We need to find some users!')
