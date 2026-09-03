# Выполним упражнение 6.6

favorite_languages = {
	'alexey': 'python',
	'vitya': 'swift',
	'dima': 'c#',
	'edward': 'ruby',
	'sasha': 'go',
	'gosha:': 'python',
	}

priority_users = ['alexey', 'vitya', 'sasha', 'anya', 'pavel']

for name in priority_users:
	if name in favorite_languages.keys():
		print(f'{name.title()}, thank you for participate in the survey!\n')
	else:
		print(f'{name.title()}, I invite you for participate in the survey!\n')
