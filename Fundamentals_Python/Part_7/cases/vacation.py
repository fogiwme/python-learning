# Выполним упражнение 7.10

# Создадим словарь с юзерами и результатом опроса про отпуск
vacation = {}

# Флаг активности
responses_active = True

# Зададим цикл опроса
while responses_active:
	name = input('Как тебя зовут? ')
	response = input('Где бы ты хотел провести свой лучший отпуск? ')
	vacation[name] = response

	# Продолжение или конец цикла
	coninue_response = input('Хочешь передать слово другому? (да/ нет) ')
	print('\n')
	if coninue_response == 'нет':
		responses_active = False

# Выведем результаты
print('--- Подведем итоги опроса! ---\n')
for name, response in vacation.items():
	print(f"{name.title()} говорит о своем лучшем отпуске вот так: \n{response.capitalize()}\n")

