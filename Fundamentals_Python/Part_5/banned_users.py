#Проверка вхождения значений в список при помощи "in"

requested_toppings = ['mushrooms', 'onions', 'pineapple']
print('mushrooms' in requested_toppings)
print('pepperoni' in requested_toppings)
print('\n')

#Проверка нескольких условий при помощи "and" и "or"

age_0 = 22
age_1 = 19
print((age_0 >= 21) and (age_1 >= 21))
age_1 = 22
print((age_0 >= 21) and (age_1 >= 21))
print('\n')

age_0 = 22
age_1 = 19
print((age_0 >= 21) or (age_1 >= 21))
age_0 = 18
print((age_0 >= 21) or (age_1 >= 21))

#Проверка отсутствия значения в списке при помощи "not"
#К примеру, рассмотрим ситуацию со списком пользователей, которым запрещено писать
#комментарии на форуме

banned_users = ['AndRew', 'carolina', 'david']
new_user = 'Andrew'

banned_users_1 = []
for user in banned_users:
	user = user.lower()
	banned_users_1.append(user)

if new_user.lower() not in banned_users_1:
	print(f'\n{new_user.title()}, you can post a response if you wish')
	#Вы можете опубликовать ответ, если хотите
else:
	print(f"\n{new_user.title()}, you are banned!")