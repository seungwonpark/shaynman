# -*- coding: utf-8 -*-
from functions import *

with open('token.txt', 'r') as f:
	bot_token = f.read().replace('\n','')

def main():
	updater = Updater(bot_token)
	dp = updater.dispatcher
	conv_handler = ConversationHandler(
		entry_points=
			[CommandHandler('start', start, pass_user_data=True)],
			# Performance issue : passing user data to start()
			# [CommandHandler('help', guide)],
		states={
			MainMenu: [
				CommandHandler('start', start, pass_user_data=True),
				RegexHandler('^새로운 구독 설정$', generate_feed),
				RegexHandler('^내 구독 리스트$', show_list, pass_user_data=True),
				RegexHandler('^구독 취소$', remove_feed_select, pass_user_data=True),
				RegexHandler('^봇 정보, 만든이$', credits, pass_user_data=True),
				RegexHandler('^면책 조항$', disclaimer, pass_user_data=True)
			],
			Generate: [
				RegexHandler('^학부공지사항$', notice, pass_user_data=True),
				RegexHandler('^강의게시판$', semester),
				RegexHandler('^이전으로$', start, pass_user_data=True),
				RegexHandler('^.*$', start, pass_user_data=True)
			],
			Semester: [
				RegexHandler('^1학기$', lecture_1),
				RegexHandler('^여름학기$', under_s),
				RegexHandler('^2학기$', lecture_2),
				RegexHandler('^이전으로$', generate_feed),
				RegexHandler('^처음으로$', start, pass_user_data=True),
				RegexHandler('^.*$', start, pass_user_data=True)
			],
			Lecture_1: [
				RegexHandler('^1학년$', under_1_1),
				RegexHandler('^2학년$', under_1_2),
				RegexHandler('^3학년$', under_1_3),
				RegexHandler('^4학년$', under_1_4),
				RegexHandler('^석사/박사과정$', grad_1),
				RegexHandler('^이전으로$', semester),
				RegexHandler('^처음으로$', start, pass_user_data=True),
				RegexHandler('^.*$', start, pass_user_data=True)
			],
			Lecture_2: [
				RegexHandler('^1학년$', under_2_1),
				RegexHandler('^2학년$', under_2_2),
				RegexHandler('^3학년$', under_2_3),
				RegexHandler('^4학년$', under_2_4),
				RegexHandler('^석사/박사과정$', grad_2),
				RegexHandler('^이전으로$', semester),
				RegexHandler('^처음으로$', start, pass_user_data=True),
				RegexHandler('^.*$', start, pass_user_data=True)
			],
			Subscribe: [
				MessageHandler(Filters.text, subscribe, pass_user_data=True)
			],
			Remove: [
				MessageHandler(Filters.text, remove_feed_remove, pass_user_data=True)
			]
		},
		fallbacks=[RegexHandler('^이제 볼 일을 다 봤어요!$', done)]
	)

	dp.add_handler(conv_handler)
	dp.add_error_handler(error)
	updater.start_polling()
	updater.idle()

if __name__ == '__main__':
	main()




