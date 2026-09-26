filename = "text_files/pi_million_digits.txt"

with open(filename) as file_object:
	lines = file_object.readlines()

pi_string = ''

for line in lines:
	pi_string += line.strip()

flag = True

while flag:
	birthday = input("\nEnter your birthday, in the from mmddyy: \n"
		"\t\t\t('q' for exit)\n\t\t\t\t")
	if birthday in pi_string:
		print("Your birthday appears in the first million digits of pi!")
	elif birthday == 'q':
		flag = False
	else:
		print("Your birthday does not appear in the first million digits of pi")