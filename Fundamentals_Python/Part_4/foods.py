my_foods = ['курица', 'рамен', 'кацу-карри', 'пельмени', 'бигмак', 'двойной чизбургер']
friends_foods = my_foods[:] #копируем список моей любимой еды
#friends_foods = my_foods - не работает, так как оба списки приравниваются, поэтому лучше убедиться, что сегмент при копировании присутствует

my_foods.insert(0, 'рис')
friends_foods.insert(0, 'картошка')

print('Моя любимая еда:')
for food in my_foods:
	print(food.capitalize())

print(f'\nЛюбимая еда моего друга:')
for food in friends_foods:
	print(food.capitalize())

