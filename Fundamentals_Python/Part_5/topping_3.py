#Поработаем со if в списках

requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
	if requested_topping == 'green peppers':
		print('Sorry, we are out of green peppers right now.')
	else:	
		print(f'Adding {requested_topping}.')

print('\nFinished making your pizza!')

print('\n')

#Составим программу, которая сначала проверяет пуст ли список

requested_toppings = []
if requested_toppings:
	for requested_topping in requested_toppings:
		print(f'Adding {requested_topping}.')
	print('\nFinished making your pizza!')
else:
	print('Are you sure you want a plain puzza?')

print('\n')


#Список доступных добавок
available_toppings = [
'mushrooms', 'olives', 'green peppers',
'pepperoni', 'extra cheese', 'pineapple'
]

#Список запрошенных добавок
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
	if requested_topping in available_toppings:
		print(f'Adding {requested_topping}!')
	else:
		print(f"Sorry, we don't have {requested_topping}.")

print('\nFinished making your pizza!')





















