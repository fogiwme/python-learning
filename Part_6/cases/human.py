# Выполним упражнение 6.1

human = {
	'name': 'Vitya',
	'surname': 'Krylov',
	'age': 30,
	'city': 'Moscow',
	}

print(human['name'], human['surname'], human['city'], human['age'])


# Выполним упражнение 6.7

person_0 = {
	'name': 'Alexey',
	'surname': 'Krylov',
	'age': 22,
	'city': 'Moscow',
}

person_1 = {
	'name': 'Sasha',
	'surname': 'Ivashencev',
	'age': 35,
	'city': 'Moscow',
}

people = [human, person_0, person_1]

for person in people:
	print(person)