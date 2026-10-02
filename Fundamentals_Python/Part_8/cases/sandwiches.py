# Выполним упражнение 8.12

def components_sandwich(*components):
	print(f'\nВ сэндвиче содержатся следующие компоненты: ')
	for component in components:
		print(f'- {component}')

components_sandwich('помидоры', 'сыр')
components_sandwich('пармезан соус')
components_sandwich('огурцы', 'помидоры', 'пармезан соус', "сыр")