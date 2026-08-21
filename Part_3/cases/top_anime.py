#Подойдем к заданию 3.10 немного креативно

print('Привет! Давай составим топ из любимых аниме')

top_anime = []

print(f'\n{top_anime}')
print('Как видишь, сейчас список пуст. Давай начнем добавлять то, что всплывает в голове')

top_anime.append('Ван Пис')
top_anime.append('Наруто')
top_anime.append('Атака Титанов')
top_anime.append('Острые козырьки')
print(f'\n{top_anime}')

print(f'\nДаа, теперь список пополнился. Только вот... Почему "Острые козырьки" ты внес в топ любимых аниме?) Это же сериал!')

del top_anime[3]
print(f'\n{top_anime}')
print('Вооот, теперь лучше! Давай в конец добавим еще пару анимешек')

top_anime.insert(3, 'MF Ghost')
top_anime.insert(4, 'Лукизм')
print(f'\n{top_anime}')

print('Теперь наш список однозначно стал больше! Только вот "Лукизм" мне не очень понравился. Давай ты его уберешь, а я подробнее объясню почему')

deleting_anime = 'Лукизм'
top_anime.remove(deleting_anime)
print(f'\n{top_anime}')

print(f'Замечательно! "{deleting_anime}" мне не очень понравился потому что прослеживается грязь общества, которая показана не очень красиво. Давай добавим еще пару анимешек')

top_anime.insert(3, 'Призматическое рондо')
top_anime.append('Ковбой Бибоп')
top_anime.insert(3, 'Аватар: Легенда о Корре')
top_anime.insert(5, 'Первый шаг')


print(f'\n{top_anime}')

#Использовал уже append(), insert(), remove(), del
#Осталось поработать с элементом из списка ([0/1/2...]), pop(), sort(), reverse(), len(), sorted()

print(f'\nОтлично! Теперь у нас есть {len(top_anime)} аниме. Я думаю, что можно сделать топ-7 аниме, чтобы было красиво.')
print(f'Я думаю, что можно убрать "{top_anime[-1]}" из этого списка.')

popped_anime = top_anime.pop()
print(f'\n{top_anime}')

print(f'\nХорошо, теперь у нас есть {len(top_anime)} аниме. Жаль, что "{popped_anime}" не смог войти в наш топ, но давай двигаться дальше!')

really_top_anime = top_anime.copy() #Так как мне придется использовать sort(), который не возвращает список к изначальному виду, копирую настоящий топ-7

print('Хочу увидеть наш топ-7 в алфавитном порядке')
print(sorted(top_anime))
print(f'\nВернемся!')
print(top_anime)

print(f'\nЗамечательно! Теперь я хочу увидеть в обратном порядке')
top_anime.reverse()
print(top_anime)
print(f'\nВернемся!')
top_anime.reverse()
print(top_anime)

print(f'\nХорошо, теперь хочу видеть список обратный алфавитному порядку')
top_anime.sort(reverse = True)
print(top_anime)

print(f'\nОтлично, давай выведем топ в алфавитном порядке')
top_anime.sort()
print(top_anime)

print(f'\nШикос! На этом закончим. Выведи получившийся топ-{len(really_top_anime)} моих анимешек!')
print(really_top_anime)
