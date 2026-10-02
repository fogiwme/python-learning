# Выполним упражнение 8.5

def describe_city(city, country='japan'):
	print(f'{city.title()} is in {country.title()}.')

describe_city('tokyo')
describe_city('kyoto')
describe_city('moscow', 'russia')