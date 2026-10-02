#Начнем изучение словарей

alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])

#Словари состоят из "ключ-значение"
#'color' - это ключ, 'green' - значение

#Как это может выглядеть при построении игры

new_points = alien_0['points']
print(f'You just earned {new_points} points!')

#Добавим в словарь еще значения

print(f'\n{alien_0}')
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

#Создадим пустой словарь

alien_0 = {}
print(f'\n{alien_0}')

alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0)

#Теперь поменяем значение в ключе словаря

alien_0 = {'color': 'green'}
print(f'\nThe alien is {alien_0['color']}.')

alien_0['color'] = 'yellow'
print(f'The alien is now {alien_0['color']}.')

#Рассмотрим более интересный пример с пришельцем, который может двигаться
#с разной скоростью

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'fast'}
print(f'\n\nOriginal position: {alien_0['x_position']}')

#Пришелец перемещается вправо.
#Вычисляем величину смещения на основании текущей скорости.

if alien_0['speed'] == 'slow':
	x_increment = 1
elif alien_0['speed'] == 'medium':
	x_increment = 2
else:
	#Пришелец двигается быстро
	x_increment = 3

#Новая позиция равна сумме старой позиции и приращения

alien_0['x_position'] = alien_0['x_position'] = x_increment
print(f'New position: {alien_0['x_position']}')	

del alien_0['y_position'] #Можно удалить любой ключ-значение, но отменить не получится
print(alien_0)


















