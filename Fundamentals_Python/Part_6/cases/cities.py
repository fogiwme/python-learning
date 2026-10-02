# Выполним упражнение 6.11

cities = {
	'Moscow': {
		'country': 'russia',
		'population_size': 13_274_085,
		'fact': 'Столица России – один из крупнейших городов Европы, входит в топ-10 ' 
		'самых крупных городов мира.',
		},

	'Tokyo': {
		'country': 'japan',
		'population_size': 14_064_696,
		'fact': 'До 1868 года город назывался Эдо, что переводится как «эстуарий» ' 
		'или «вход в реку».',
		},

	'Kioto': {
		'country': 'japan',
		'population_size': 1_464_890,
		'fact': 'Киото сохраняет около двух тысяч буддийских и синтоистских храмов, ' 
		'потому что город почти не пострадал во время Второй мировой войны.',
		}, 
	}

for city, information in cities.items():
	print(f'Немного информации о {city.title()}:')
	for info, value in information.items():
		if info == 'country':
			print(f'\tСтрана нахождения: {value.title()}')
		elif info == 'population_size':
			print(f'\tЧисленность населения: {value}')
		else:
			print(f'\tИнтересный факт об этом городе: \n\t\t{value}')
	print('\n')
