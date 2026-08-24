digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

print(min(digits)) #выведет минимальное число из списка
print(max(digits)) #выведет максимальное число из списка
print(sum(digits)) #выведет сумму чисел списка

#Разберемся с генератором списка

squares = [value**2 for value in range(1,11)]
print(f'{squares}\n')

#Свой пример

thousand = [number for number in range(1,101)]
print(thousand)