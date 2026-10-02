# Словарь, который хранит любимые языки программирования друзей

favorite_language = {
	'alexey': 'python',
	'vitya': 'swift',
	'dima': 'c#',
	'edward': 'ruby',
	'sasha': 'go',
	'gosha:': 'python',
	}

language = favorite_language['vitya'].title()
print(f"Vitya's favorite language is {language}\n")

# Переберем этот список

for name, language in favorite_language.items():
	print(f"{name.title()}'s favorite language is {language.title()}")

print('\n')

# Переберем только ключи словаря при помощи метода .keys()

for name in favorite_language.keys():
	print(name.title())

print('\n')

# При этом метод .keys() можно опустить, а использовать чтобы код читался проще
# Следующие строки будут работать так же

for name in favorite_language:
	print(name.title())
print('\n')



friends = ['vitya', 'alexey']
for name in favorite_language.keys():
	print(name.title())
	if name in friends:
		language = favorite_language[name].title()
		print(f'\t{name.title()}, I see you love {language}!')



if 'gosha' not in favorite_language:
	print('Gosha, please take our poll!')
print('\n')

# Можно перебирать ключи в определенном порядке

for name in sorted(favorite_language.keys()):
	print(f'{name.title()}, thank you for taking the poll.')

print('\n')

# Также можно перебирать все значения в словаре

print('The following languages have been mentioned:')
for language in favorite_language.values():
	print(language.title())

print('\n')

# Только значения не проходят проверку на повторения, поэтому воспользуемся
# множеством set (оно похоже на список, но все его элементы должны быть уникальными)

print('The following languages have been mentioned:')
for language in set(favorite_language.values()):
	print(language.title())

# Множества можно записать вот так:

languages = {'python', 'ruby', 'etc', 'ruby', 'etc'}
print(languages)
# Очень похоже на словарь, но тут нет конструкции ключ-значение


favorite_languages = {
	'alexey': ['python', 'c++', 'html'],
	'vitya': ['swift', 'css'],
	'dima': ['c#'],
	'edward': ['ruby'],
	'sasha': ['go'],
}


for name, languages in favorite_languages.items():
	if len(languages) == 1:
		print(f"\n{name.title()}'s favorite language are:")
	else: 
		print(f"\n{name.title()}'s favorite languages are:")
	for language in languages:
		print(f'\t{language.title()}')







