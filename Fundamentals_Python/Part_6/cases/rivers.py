# Выполним упражнение 6.5

rivers = {
	'амазонка': 'бразилия', 
	'нил': 'египет',
	'янцзы': 'китай',
}

for river, country in rivers.items():
	print(f'{river.title()} протекает в {country.title()}')

print('\n')

for river in rivers.keys():
	print(river.title())

print('\n')

for country in rivers.values():
	print(country.title())