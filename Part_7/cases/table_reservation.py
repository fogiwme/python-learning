# Выполним упражнение 7.2

prompt = 'Уточните, пожалуйста, на сколько человек хотите '
prompt += 'забронировать столик '

table_reservation = input(prompt)

people_number = int(table_reservation)

if people_number > 8:
	print("К сожалению, сейчас стоит подождать, когда такой столик будет свободен.")
else:
	print("Ваш столик готов!")

