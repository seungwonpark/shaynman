# -*- coding: utf-8 -*-
from functions import *

# Safely use access token
# execute as `bot_token="xoxb-abc-1232" python shaynman.py`
import os
bot_token = os.environ["bot_token"]

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
					level=logging.INFO)

logger = logging.getLogger(__name__)

def main():
	updater = Updater(bot_token)
	dp = updater.dispatcher
	conv_handler = ConversationHandler(
		entry_points=[CommandHandler('start', start)],
		states={
			MainMenu: [
				RegexHandler('^생성$', generate_feed),
				RegexHandler('^리스트$', show_list, pass_user_data=True),
				RegexHandler('^제거$', remove_feed),
			],
			Generate: [
				RegexHandler('^학부공지사항$', notice, pass_user_data=True),
				RegexHandler('^강의게시판$', semester),
				RegexHandler('^이전으로$', start)
			],
			Semester: [
				RegexHandler('^1학기$', lecture_1),
				RegexHandler('^여름학기$', under_s),
				RegexHandler('^2학기$', lecture_2),
				RegexHandler('^이전으로$', generate_feed)
			],
			Lecture_1: [
				RegexHandler('^학부 1학년$', under_1_1),
				RegexHandler('^학부 2학년$', under_1_2),
				RegexHandler('^학부 3학년$', under_1_3),
				RegexHandler('^학부 4학년$', under_1_4),
				RegexHandler('^석사/박사과정$', grad_1),
				RegexHandler('^이전으로$', lecture_1)
			],
			Lecture_2: [
				RegexHandler('^학부 1학년$', under_2_1),
				RegexHandler('^학부 2학년$', under_2_2),
				RegexHandler('^학부 3학년$', under_2_3),
				RegexHandler('^학부 4학년$', under_2_4),
				RegexHandler('^석사/박사과정$', grad_2),
				RegexHandler('^이전으로$', lecture_2)
			],
			Subscribe: [
				MessageHandler(Filters.text, subscribe, pass_user_data=True)
			]
		},
		fallbacks=[RegexHandler('^Done$', done)]
	)

	dp.add_handler(conv_handler)
	dp.add_error_handler(error)
	updater.start_polling()
	updater.idle()

if __name__ == '__main__':
	main()




