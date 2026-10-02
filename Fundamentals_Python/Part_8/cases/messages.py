# Выполним упражнение 8.9, 8.10, 8.11

def show_messages(messages):
	for message in messages:
		print(message)

def send_messages(messages, sent_messages):
	while messages:
		message = messages.pop()
		print(message)
		sent_messages.append(message)

messages = ['yo, wassap', 'how are u', 'gg', 'glhf']
sent_messages = []

show_messages(messages)
send_messages(messages, sent_messages)

print(f'\n{sent_messages}\n{messages}')

messages = ['yo, wassap', 'how are u', 'gg', 'glhf']
sent_messages = []

send_messages(messages[:], sent_messages)
print(f'\n{messages}\n{sent_messages}')

