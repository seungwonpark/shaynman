import requests
import os
with open('token.txt', 'r') as f:
	bot_token = f.read().replace('\n','')

print('Enter a text message to send:')
text = input()

print('Are you sure to send: %s to %d users? [y/n]' % (text, len(os.listdir('data/user'))))
yesno = input()

if(yesno == 'y'):
	for x in os.listdir('data/user'):
		if(x[-4:] != '.txt'):
			continue
		userNo = int(x[:-4])
		print(userNo)
		requests.get('https://api.telegram.org/bot%s/sendMessage?chat_id=%s&text=%s' % (bot_token, userNo, text))
else:
	print('Cancelled.')