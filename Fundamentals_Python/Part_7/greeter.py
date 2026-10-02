name = input('Please enter your name: ')
print(f'\nHello, {name.title()}!')

prompt = '\nIf you tell us who you are, we can personalize the messages you see.'
prompt += '\nWhat is your first name? ' # Оператор += объеденяет текст, хранящийся в
# prompt, с новым фрагментом текста

name = input(prompt)
print(f'\nHello, {name.title()}!\n')

# int() преобразует строковое представленние числа в само число

age = input("How old are you? ")
age = int(age)
print(age >= 18)