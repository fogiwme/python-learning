#Создадим приложение, которое проверяет все условия
#Это удобно делать функциями if без elif или else, потому что
#если мы найдем одну истину в синтаксисе if-elif-else, то он прекратится и не доберется
#до конца.

requested_toppings = ['mushrooms', 'extra cheese']

if 'mushrooms' in requested_toppings:
	print('Adding mushrooms.')
if 'pepperoni' in requested_toppings:
	print('Adding pepperoni.')
if 'extra cheese' in requested_toppings:
	print('Adding extra cheese.')

print('\nFinished making your pizza!')