magicians = ['alice', 'david', 'carolina']
magicians.append('victor')

for magician in magicians:
	print(f'{magician.title()}, that was a great trick!')
	print(f"I can't wait to see your next trick, {magician.title()}.\n") #Если убрать таб в начале, то это не будет входить в тело цикла

print('Thank you, everyone. That was a great magic show!')