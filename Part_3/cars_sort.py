#Метод .sort() позволяет легко отсортировать список

cars = ['bmw', 'audi', 'toyota', 'subaru']

cars.sort()
print(cars)

#Также методу sort() можно передать какой-нибудь аргумент, к примеру reverse = True (сортировка обратная алфавитному)

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse = True)
print(cars)

#Интересно, работает ли с русским)

cars = ['бмв', 'ауди', 'тойота', 'субару']
cars.sort(reverse = True)
print(f'\n{cars}')

#Попробуем сделать временную сортировку при помощи метода sorted()

cars = ['bmw', 'audi', 'toyota', 'subaru']
print('\nЗдесь оригинальный список:')
print(cars)

print('Здесь отсортированный список:')
print(sorted(cars))

print('Здесь отсортированный список, обратный алфавитному:')
print(sorted(cars, reverse = True))

print('Здесь оригинальный список:')
print(cars)

#Методом .reverse() можно перевернуть список (постоянно), чтобы вернуть, можно снова прийти к методу

cars = ['bmw', 'audi', 'toyota', 'subaru']
print(f'\n{cars}')

cars.reverse()
print(cars)

cars.reverse()
print(cars)

#Метод len() позволяет определить сколько элементов в списке

print(f'\nВ списке {len(cars)} элемента.')
