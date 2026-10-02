#Поработаем с сегментом списка

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
print(players[1:4])
print(players[:4])
print(players[2:])

print(players[-2:])

print(f'\n{players[0:5:2]}\n') #третье значение - сколько пропускать


players = ['charles', 'martina', 'michael', 'florence', 'eli']
print('Here are the first players on my team:')
for player in players[0:3]:
	print(player.title())