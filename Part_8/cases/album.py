# Выполним упражнение 8.7 и 8.8

def make_album(name_artist, name_album, number_tracks=None):
	music_album = {
		'artist': name_artist, 
		'album': name_album,
		}

	if number_tracks:
		music_album['audio_tracks'] = number_tracks

	return music_album

album_1 = make_album('лсп', 'tragic city')
album_2 = make_album('morgenshtern', 'alisher')
album_3 = make_album('ado', "UTA'S SONGS ONE PIECE FILM RED")
album_4 = make_album('DAMONA', 'the melody', 80)

print(f'{album_1}')
print(f'\n{album_2}')
print(f'\n{album_3}')
print(f'\n{album_4}\n')

# Создадим цикл, в котором будем получать имя и название альбома + вывод

while True:
	print('\n---Напиши твоего любимого исполнителя и его лучший альбом, на твой взгляд---')
	print('                (Завершить цикл можно вписав "-")            ')
	name = input('\nВведи имя исполнителя: ')
	if name == '-':
		break
	
	album = input('Введи название альбома: ')
	if album == '-':
		break
	
	dictionary = make_album(name, album)
	print(f"\n{dictionary}")
	print(f'\n{name.title()} создал альбом: {album.title()}')