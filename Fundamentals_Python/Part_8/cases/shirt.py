# Выполним упражнение 8.3 и 8.4

def make_shirt(size_shirt='L', text_shirt='I love Python'):
	print(f'Я заказал футболку {size_shirt} размера и надпись на ней "{text_shirt}"')

size = input('Напиши размер футболки ')
text = input('Напиши текст, который хочешь увидеть на футболке ')
make_shirt(size, text)
make_shirt(size_shirt=size, text_shirt=text)

make_shirt('L')
make_shirt(text_shirt='Freedom')