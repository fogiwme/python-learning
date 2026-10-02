#Выполним задание 3.4

guest_list = ['Дедушка', 'Витя', 'Павел Дуров', 'Илон Маск']
print(f'Привет, {guest_list[0]}! Приглашаю тебя на обед!')
print(f'Привет, {guest_list[1]}! Приглашаю тебя на обед!')
print(f'Привет, {guest_list[2]}! Приглашаю тебя на обед!')
print(f'Привет, {guest_list[3]}! Приглашаю тебя на обед!')

#Выполним задание 3.5

print(f'\n{guest_list[3]} прийти, к сожалению, не сможет.')

del guest_list[3] #удалили
guest_list.append('Nix') #заменили

print(f'\nПривет, {guest_list[0]}! Приглашаю тебя на обед!')
print(f'Привет, {guest_list[1]}! Приглашаю тебя на обед!')
print(f'Привет, {guest_list[2]}! Приглашаю тебя на обед!')
print(f'Привет, {guest_list[3]}! Приглашаю тебя на обед!')

#Выполним задание 3.6

print(f'\nКупил стол побольше, поэтому приглашаю еще 3 человек!')

guest_list.insert(0, 'Пол Уокер')
guest_list.insert(3, 'Саша')
guest_list.insert(6, 'Месси')

print(f'\nПривет, {guest_list[0]}! Приглашаю тебя на обед!')
print(f'Привет, {guest_list[1]}! Приглашаю тебя на обед!')
print(f'Привет, {guest_list[2]}! Приглашаю тебя на обед!')
print(f'Привет, {guest_list[3]}! Приглашаю тебя на обед!')
print(f'Привет, {guest_list[4]}! Приглашаю тебя на обед!')
print(f'Привет, {guest_list[5]}! Приглашаю тебя на обед!')
print(f'Привет, {guest_list[6]}! Приглашаю тебя на обед!')

#Выполним задание 3.7

print(f'\nК сожалению, стол не успеют привезти, поэтому гостей всего могу допустить только двоих.')

deleting_guest_1 = guest_list.pop(0)
deleting_guest_2 = guest_list.pop(-1)
deleting_guest_3 = guest_list.pop(-1)
deleting_guest_4 = guest_list.pop(-1)
deleting_guest_5 = guest_list.pop(-1)

print(f'\nПрости, {deleting_guest_1}, из-за неприятных событий, я отменяю обед.')
print(f'Прости, {deleting_guest_2}, из-за неприятных событий, я отменяю обед.')
print(f'Прости, {deleting_guest_3}, из-за неприятных событий, я отменяю обед.')
print(f'Прости, {deleting_guest_4}, из-за неприятных событий, я отменяю обед.')
print(f'Прости, {deleting_guest_5}, из-за неприятных событий, я отменяю обед.')

print(f'\n{guest_list[0]}, пишу сообщить, что обед в силе!')
print(f'{guest_list[1]}, пишу сообщить, что обед в силе!')

del guest_list[0]
del guest_list[0]
print(f'\n{guest_list}')

print(len(guest_list))