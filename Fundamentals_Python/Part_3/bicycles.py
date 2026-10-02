#Создаем первую программу со списком

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

#Выведем необходимый элемент из списка
print(f'\n{bicycles[0]}')
print(bicycles[1])

#Также можно вывести необходимый элемент отформатировав строковым методом
print(bicycles[2].title())

#Запомним, что индексы начинаются с 0

#Еще можно вывести последний элемент списка при помощи [-1], к примеру, если точно не знаем сколько в списке элементов
print(bicycles[-1])
print(bicycles[-2].upper())

#Сейчас выведем сообщение через строку, в которой извлечем элемент из списка
message = f"\nMy first bicycle was a {bicycles[0].title()}"
print(message)