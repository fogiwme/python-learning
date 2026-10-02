# Выполним упражнение 8.6

def city_country(name_city, name_country):
	pair = f"{name_city.title()} in {name_country.title()}"
	return pair

print(city_country('kyoto', 'japan'))
print(city_country('tokyo', 'japan'))
print(city_country('nagano', 'japan'))
