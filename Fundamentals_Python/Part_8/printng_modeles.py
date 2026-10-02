from printing_functions import print_models as pm
from printing_functions import show_completed_models as scm

# Список моделей, которые необходимо напечатать

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

# Цикл последовательно печатает каждую модель до конца списка.
# После печати каждая модель перемещается в список completed_models.

while unprinted_designs:
	current_design = unprinted_designs.pop()
	print(f'Printing model: {current_design}')
	completed_models.append(current_design)

# Вывод всех готовых моделей.

print('\nThe following models have been printed:')
for completed_model in completed_models:
	print(completed_model)
print('\n')


# При помощи функций, это можно сделать вот так:

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

pm(unprinted_designs[:], completed_models)
scm(completed_models)

print(unprinted_designs)














