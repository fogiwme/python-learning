# Решим упражнение 7.5 и 7.6

prompt = 'Введи свой возраст, чтобы я определил цену на билет в кино: \n'
prompt += '(Напиши "выход", чтобы закончить цикл)\n'

active = True

while active:
	age = input(prompt)
	if age == 'выход':
		active = False
		print('\nВы закончили цикл!')
	elif int(age) < 0:
		break
	elif int(age) < 3:
		print('Вход бесплатный!\n')
	elif int(age) <= 12:
		print('Билет стоит $10!\n')
	else:
		print('Билет стоит $15!\n')