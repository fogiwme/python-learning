for value in range(1,5): #range() - диапозон от 1 до 5 (5 не выводит)
	print(value)
print(f'\n')

for value in range(6): #тот же диапозон, только начинается с 0 и до 6 (6 не выводит)
	print(value)

numbers = list(range(1,6)) #заключим вызов range() в list(): результат будет представлять список чисел в заданном диапозоне
print(f'\n{numbers}')

