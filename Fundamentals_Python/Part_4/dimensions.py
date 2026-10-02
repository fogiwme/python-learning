#Неизменяемые списки называются кортежами

dimensions = (200, 50) #Работает как список, только не изменяется
print(dimensions[0])
print(dimensions[1])

#dimensions[0] = 250 возникает ошибка, потому что кортеж нельзя изменить
#print(dimensions[0])

for dimension in dimensions:
	print(dimension)

#Кортеж - это список, только в круглых скобках и с наличием запятой
#Можно в кортеж вложить только один элемент:

cortege = (3,)
print(f'\n{cortege[0]}\n') #Но такой формат кортежа мало где используется и почти не имеет смысла


#Так как кортеж нельзя поменять, можно сохранить в переменную другой кортеж
dimensions = (200, 50)
print('Original dimensions:')
for dimension in dimensions:
	print(dimension)

dimensions = (400, 100)
print('\nModified dimensions:')
for dimension in dimensions:
	print(dimension)
