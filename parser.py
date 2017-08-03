from lecturelists import *
import requests
import re
import schedule
import time

with open('token.txt', 'r') as f:
	bot_token = f.read().replace('\n','')

def job():
	print('Started Working...')
	for x in ['notice']:
		url = 'http://physics.snu.ac.kr/xe/underbbs'
		req = requests.get(url)
		html = req.text
		srl_list = sorted(re.findall(r'/xe/underbbs/([0-9]*)"\>', html))

		with open('data/parsed/notice.txt', 'r') as f:
			temp = f.read().split(',')[1:]

		for srl in srl_list:
			if srl not in temp:
				title = html.split('/xe/underbbs/%s">' % srl)[1].split('</a>')[0]
				title = title.replace('\t','').replace('\n','').replace('\r','')
				title = title.replace('<span style="font-weight:bold;">','').replace('</span>','')
				title = title.replace('[','').replace(']','')
				link = 'http://physics.snu.ac.kr/xe/underbbs/%s' % srl
				message = '*학부공지사항*\n[%s](%s)' % (title, link)

				with open('data/parsed/notice.txt', 'a') as f:
					f.write(',%s' % srl)

				with open('data/course/notice.txt', 'r') as f:
					user_list = f.read().split(',')[1:]

				for user in user_list:
					requests.get('https://api.telegram.org/bot%s/sendMessage?chat_id=%s&text=%s&parse_mode=Markdown' % (bot_token, user, message))

	for x in lecturelist_all_rev.keys():
		if(x == 'notice'):
			continue
		url = 'http://physics.snu.ac.kr/php/subject_list/Notice/list.php?id=%d_%s' % (year, x)
		req = requests.get(url)
		html = req.text
		uid_list = sorted(re.findall(r'uid=(.*)&keyfield', html))

		with open('data/parsed/%s.txt' % x, 'r') as f:
			temp = f.read().split(',')[1:]
		for uid in uid_list:
			if uid not in temp:
				title = html.split('uid=%s' % uid)[1].split('</a>')[0].split('key=">')[1].replace('\t','').replace('\n','').replace('\r','')
				link = 'http://physics.snu.ac.kr/php/subject_list/Notice/view.php?id=%d_%s' % (year, x) + '%26' + 'uid=%s' % uid
				message = '*%s*\n[%s](%s)' % (lecturelist_all_rev[x], title, link)

				with open('data/parsed/%s.txt' % x, 'a') as f:
					f.write(',%s' % uid)

				with open('data/course/%s.txt' % x, 'r') as f:
					user_list = f.read().split(',')[1:]

				for user in user_list:
					requests.get('https://api.telegram.org/bot%s/sendMessage?chat_id=%s&text=%s&parse_mode=Markdown' % (bot_token, user, message))

	print('Finished working...')

schedule.every(10).minutes.do(job)

while True:
	schedule.run_pending()
	time.sleep(1)

