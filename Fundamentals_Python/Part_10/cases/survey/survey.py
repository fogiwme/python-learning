# Упражнение 10.5

filename = 'survey.txt'

while True:
	answer = input('\nРасскажи, почему тебе нравится программировать?\n'
	'\t\t(Введи "q", чтобы выйти.)\n\n')

	if answer == 'q':
		break
	
	with open(filename, 'a') as file_object:
		file_object.write(f'{answer}\n\n')

