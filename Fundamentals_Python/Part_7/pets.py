pets = ['dog', 'cat', 'dog', 'goldfish','cat', 'rabbit', 'cat']
print(pets)

pets.remove('cat') # remove удаляет только одно заданное значение
print(pets)

while 'cat' in pets:
	pets.remove('cat')

print(pets)