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