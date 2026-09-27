# Упражнение 10.10

filename = 'moby_dick.txt'

with open(filename) as file_object:
	lines = file_object.readlines()

"""Посмотрим, сколько в этом тектсе слов 'the'"""

quantity = 0

for line in lines:
	quantity += line.count("the ")

print(quantity)