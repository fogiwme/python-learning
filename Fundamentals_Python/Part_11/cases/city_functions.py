# Упражнение 11.1

def place(country, city, population=''):
	if population:
		city_name = f'{country.title()}, {city.title()} -- population {population}'
	else:
		city_name = f'{country.title()}, {city.title()}'
	
	return city_name