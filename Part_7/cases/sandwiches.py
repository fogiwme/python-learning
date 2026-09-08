# Выполним упражнение 7.8 и 7.9

sandwich_orders = [
	'pastrami',
	'classic sandwich', 
	'club sandwich', 
	'panini', 
	'pastrami',
	'Reuben sandwich', 
	'Sub sandwich',
	'pastrami'
]

finished_sandwiches = []

print('---Pastrami is out!---\n')

while 'pastrami' in sandwich_orders:
	sandwich_orders.remove('pastrami')

while sandwich_orders:
	finished_sandwich = sandwich_orders.pop()
	print(f'I made your {finished_sandwich.title()}')
	finished_sandwiches.append(finished_sandwich)

print('\n---List of finished sandwiches---')
for sandwich in finished_sandwiches:
	print(sandwich)

