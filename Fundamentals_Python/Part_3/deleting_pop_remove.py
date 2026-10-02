motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

#Удалим из списка какой-нибудь элемент при помощи команды del

del motorcycles[0]
print(motorcycles)
del motorcycles[1]
print(motorcycles)

#Также удалить элемент можно командой .pop(), но с ним можно будет работать после удаления

motorcycles = ['honda', 'yamaha', 'suzuki']
print(f'\n{motorcycles}')

popped_motorcycles = motorcycles.pop()
print(motorcycles)
print(popped_motorcycles)

#.pop() может использоваться для того, чтобы обозначить какую-нибудь последнюю покупку или приобретение, к примеру
motorcycles = ['honda', 'yamaha', 'suzuki']
last_owned = motorcycles.pop()
print(f'\nПоследний купленный мотоцикл был {last_owned.title()}!')

#Также .pop() может удалить произвольный элемент из списка

motorcycles = ['honda', 'yamaha', 'suzuki']
first_owned = motorcycles.pop(0)
print(f'\nПервый купленный мотоцикл был {first_owned.title()}!')
print(motorcycles) #Помним, что после каждого вызова .pop() элемент, с которым работаем уже не находится в списке

#del - полностью удаляет элемент, а .pop() удаляет элемент, но с ним в будущем можно будет работать

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(f'\n{motorcycles}')

#Если мы знаем только значение элемента, то можно использовать .remove()

motorcycles.remove('ducati')
print(motorcycles)

#Пример того, как это можно использовать

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(f'\n{motorcycles}')
too_expesive = 'ducati'
motorcycles.remove(too_expesive)
print(motorcycles)
print(f'Для меня {too_expesive.title()} очень дорогой.')

#Также remove() удаляет только один элемент из списка, если нужно удалить все, то лучше использовать цикл
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati', 'yamaha']
print(f'\n{motorcycles}')
motorcycles.remove('yamaha')
print(motorcycles) 

#Как видим, yamaha, которая в конце находится никуда не исчезла












