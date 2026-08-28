#Простая программа с использованием if

cars = ['audi', 'bmw', 'porshe', 'tesla']
for car in cars:
	if car == 'bmw':
		print(car.upper())
	else:
		print(car.title())