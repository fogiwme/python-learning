#Выполним упражнение 4.8

cube_numbers = []

for value in range(1,11):
	number = value**3
	cube_numbers.append(number)
	print(number)

print(cube_numbers)

#Немного упростим, наверно^_^

cube_numbers = [number for number in range(1,11)]

for value in cube_numbers:
	print(value**3)

#Выполним упражнение 4.9

cube_numbers_2 = [value**3 for value in range(1,11)]
print(cube_numbers_2)