#Выполним упражнение 4.1

pizzas = ['pepperoni pizza', 'margherita pizza', 'cheese pizza']

for pizza in pizzas:
	print(f"I like {pizza.capitalize()}") #capitalize() делает букву первого слова в элементе списка заглавной, остальные не трогает

print('\nI really love pizza!\n')


friend_pizzas = pizzas[:]
pizzas.append('just pizza')
friend_pizzas.append('hawaiian pizza')

print(f'\nMy favorite pizzas are:')
for pizza in pizzas:
	print(pizza.capitalize())

print(f"\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
	print(pizza.capitalize())