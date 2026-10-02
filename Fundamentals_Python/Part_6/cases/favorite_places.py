# Выполним упражнение 6.9

favorite_places = {
	'alexey': ['japan', 'usa', 'dubai'],
	'vitya': ['new zeland', 'usa'],
	'sasha': ['russia'],
	}

for name, places in favorite_places.items():
	if name == 'sasha':
		print(f'{name.title()} very interesting in this country:')
	else:
		print(f'{name.title()} very interesting in these countries:')
	for place in places:
		print(f'\t{place.title()}')
	print('\n')