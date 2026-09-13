# Выполним упражнение 8.14

def car_info(manufacturer, brand, **info):
	info['car_manufacturer'] = manufacturer
	info['car_brand'] = brand
	return info

car = car_info('nissan', 'skyline R34', 
				color='white-blue',
				neon_color='blue')
print(car)

# Переберу словарь

for key, value in car.items():
	print(f'\n{key}: {value}')
