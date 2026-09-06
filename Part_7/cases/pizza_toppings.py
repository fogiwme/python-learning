# Выполним упражнение 7.4

prompt = '\nВведите добавку, которую хотите видеть в пицце: '
prompt += '\n(Напишите "выход", когда закончите с добавками)\n\n'

pizza_topping = True

while pizza_topping:
	pizza_topping = input(prompt)
	if pizza_topping == 'выход':
		pizza_topping = False
	else:
		print(f'\n{pizza_topping.title()} был добавлен в вашу пиццу!')	
	