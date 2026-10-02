motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

#Изменим значение первого элемента этого списка

motorcycles[0] = 'ducati'
print(motorcycles)

#Добавим в конец списка еще одно значение

motorcycles.append('honda')
print(f'\n{motorcycles}')

#Метод .append() упрощает динамическое построение списка. Сейчас создадим пустой список и этой командой добавим элементы в список

motorcycles = []
motorcycles.append('suzuki')
motorcycles.append('ducati')
print(f'\n{motorcycles}')
motorcycles.append('yamaha')
motorcycles.append('honda')
print(motorcycles)

#Метод .insert() позволяет добавить новый элемент в произвольную позицию списка
#При этом можно задать положение и значение (положение, значение)

motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0, 'ducati')
print(f'\n{motorcycles}')
motorcycles.insert(-1, 'gold') #На место последнего элемента в списке добавляется заданный элемент и двигает последний вправо
print(motorcycles)