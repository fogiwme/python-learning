def build_person(first_name, last_name, age=None): # None == False
	"""Возвращает словарь с информацией о человеке"""
	person = {'first': first_name, 'last': last_name}
	if age:
		person['age'] = age
	return person

musician = build_person('john', 'inomata', age=27)
print(musician)