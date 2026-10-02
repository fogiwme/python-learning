from survey import AnonymousSurvey

# Определение вопроса с созданием экземпляра AnonymousSurvey.
question = 'Какой язык ты выучил впервые?'
my_survey = AnonymousSurvey(question)

# Вывод вопроса и сохранение ответа.
my_survey.show_question()
print('Нажми "q", чтобы выйти\n')
while True:
	response = input('Первый язык: ')
	if response == 'q':
		break
	my_survey.store_response(response)

# Вывод результатов опроса.
print("\nСпасибо всем, кто поучаствовал в опросе!")
my_survey.show_results()