# Выполним упражнение 9.14

from random import choice

"""Создадим список случайных чисел и букв"""

letters_and_numbers = ['A', 'Y', 'D', 'J', 'K', 1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
winning_combination = []

"""Сформируем выигрышную рандомную комбинацию"""

for _ in range(4):
	random_symbol = choice(letters_and_numbers)
	winning_combination.append(random_symbol)

print(f"Комбинация {winning_combination[0]}"
				f"{winning_combination[1]}"
				f"{winning_combination[2]}"
				f"{winning_combination[3]} является выигрышной!\n")

"""Проверим, насколько сложно выиграть в моей лотерее с первого раза"""

attempts = 0

flag = True

while flag:
	my_ticket = []
	for _ in range(4):
		random_symbol = choice(letters_and_numbers)
		my_ticket.append(random_symbol)

	attempts += 1

	if my_ticket == winning_combination:
		flag = False


print(f"Для выигрыша понадобилось {attempts} попыток")
