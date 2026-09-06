prompt = '\nPlese enter the name of a city you have visited:'
prompt += "\n(Enter 'quit when you are finished.') \n"

cities = []

while True: # Цикл будет выполняться до тех пор, пока не будет выполнен break
	city = input(prompt)

	if city == 'quit':
		break
	else:
		print(f"\nI'd love to go to {city.title()}!")
		cities.append(city)

# break так же работает с циклом for

for city in cities: 
	if city != 'tokyo':
		print(city.title())
	else:
		break

print(cities)