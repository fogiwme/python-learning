#Решаю задачку от ИИ -_-

numbers = list(range(1,11))
print(numbers)

for number in numbers:
	print(number)

even_numbers = []
for number in numbers:
	if number % 2 == 0:
		even_numbers.append(number)

print(even_numbers)