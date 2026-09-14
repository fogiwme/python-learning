# Выполним упражнение 8.14

import function_car_info
car = function_car_info.car_info('nissan', 'skyline R34', 
				color='white-blue',
				neon_color='blue')
print(car)

from function_car_info import car_info
car = function_car_info.car_info('nissan', 'skyline R34', 
				color='white-blue',
				neon_color='blue')
print(car)

from function_car_info import car_info as ci
car = ci('nissan', 'skyline R34', 
				color='white-blue',
				neon_color='blue')
print(car)

import function_car_info as fci
car = fci.car_info('nissan', 'skyline R34', 
				color='white-blue',
				neon_color='blue')
print(car)

from function_car_info import *
car = function_car_info.car_info('nissan', 'skyline R34', 
				color='white-blue',
				neon_color='blue')
print(car)

# Переберу словарь

for key, value in car.items():
	print(f'\n{key}: {value}')