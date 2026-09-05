# Выполним упражнение 6.2

favorite_numbers = {
	'vitya': [7, 3],
	'alexey': [3, 5],
	'dima': [5, 7],
	'sasha': [353, 1],
	'jordan': [9, 10],
}

print(f"Favorite number Vitya's is {favorite_numbers['vitya']}")
print(f"Favorite number Alexey's is {favorite_numbers['alexey']}")
print(f"Favorite number Dima's is {favorite_numbers['dima']}")
print(f"Favorite number Sasha's is {favorite_numbers['sasha']}")
print(f"Favorite number Jordan's is {favorite_numbers['jordan']}")

print('\n')

# Выполним упражнение 6.10

for name, numbers in favorite_numbers.items():
	print(f"{name.title()}'s favorite numbers:")
	for number in numbers:
		print(f'\t{number}')
	print('\n')