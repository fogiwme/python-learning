# Выполним упражнение 10.1

filename = '/Users/kraldison/Desktop/python-learning/Part_10/theory/text_files/learning_python.txt'

with open(filename) as file_object:
	lines = file_object.readlines()

for line in lines:
	print(line.strip())

string = ''

for line_1 in lines:
	string += line_1

print(f"\n{string}\n")

message = string.replace('python', 'C')
message_1 = string.replace('В', 'In')
print(message)
print(message_1)