user_0 = {
	'username': 'kraldison',
	'first': 'alexey',
	'last': 'krylov'
	}

# Используем метод .items(), который дает понять программе, что я хочу получить и ключ,
# и значение.

for key, value in user_0.items(): 
	print(f'\nKey: {key}')
	print(f'Value: {value.title()}')