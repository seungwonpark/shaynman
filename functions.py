from telegram import ReplyKeyboardMarkup
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters, RegexHandler,
							ConversationHandler)
# Enable logging
import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
					level=logging.INFO)

logger = logging.getLogger(__name__)


from keyboards import *
from lecturelists import *

MainMenu, Generate, Lecture, Semester, Lecture_1, Lecture_2, Subscribe, Remove = range(8)

import os

def start(bot, update, user_data):
	update.message.reply_text(
		'안녕하세요! 서울대 물리학과 게시판 염탐꾼, 샤인만입니다.\n\n'
		'소식을 받고 싶은 공지/강의게시판을 "새로운 구독 설정"으로 설정해 주세요.'
		'"내 구독 리스트"에서 현재의 구독한 게시판 리스트를 확인할 수 있으며, "구독 취소"를 통해 구독을 취소할 수 있습니다.\n\n'
		'구독 설정을 마쳤다면 "이제 볼 일을 다 봤어요!"을 눌러 설정을 종료하세요.'
		'그 후 구독한 게시판에 새로운 글이 올라올 때마다 여기로 메시지가 옵니다.',
		reply_markup=ReplyKeyboardMarkup(keyboard_main, one_time_keyboard=True)
	)

	user_id = str(update.message.chat_id)

	if(os.path.exists('data/user/%s.txt' % user_id)):
		with open('data/user/%s.txt' % user_id, 'r') as f:
			user_data['feed'] = f.read().split(',')[1:] # .,first,second,third
	else:
		user_data['feed'] = []
		with open('data/user/%s.txt' % user_id, 'w') as f:
			f.write('.')

	return MainMenu


def generate_feed(bot, update):
	update.message.reply_text(
		'어떤 공지/강의게시판을 구독하고 싶으신가요?',
		reply_markup=ReplyKeyboardMarkup(keyboard_generate, one_time_keyboard=True)
	)
	return Generate


def notice(bot, update, user_data):
	user_id = str(update.message.chat_id)

	if 'notice' in user_data['feed']:
		update.message.reply_text(
			'"학부 공지사항"은 이미 구독되어 있는 게시판입니다.'
		)
	else:
		with open('data/user/%s.txt' % user_id, 'a') as f:
			f.write(',%s' % 'notice')

		user_data['feed'] += ['notice']
		with open('data/course/notice.txt', 'r') as f:
			temp = f.read().split(',')[1:]
		if user_id not in temp: # to avoid duplication
			with open('data/course/notice.txt', 'a') as f:
				f.write(',%s' % user_id)

		update.message.reply_text(
			'"학부 공지사항" 게시판이 구독되었습니다.\n'
			'원문은 여기에서 보실 수 있습니다 : \n\n'
			'phya.snu.ac.kr/xe/underbbs'
		)
	return generate_feed(bot, update)


def semester(bot, update):
	update.message.reply_text(
		'새로 구독하려는 강의가 열리는 학기를 선택해 주세요.\n'
		'현재 %d년도 기준으로 피드가 제공되고 있습니다.\n'
		'처음으로 돌아가려면 "처음으로"를 눌러주세요.' % year,
		reply_markup=ReplyKeyboardMarkup(keyboard_semester, one_time_keyboard=True)
	)
	return Semester


def subscribe(bot, update, user_data):
	text = update.message.text
	lectureCode = lecturelist_all[text]
	user_id = str(update.message.chat_id)

	if lectureCode in user_data['feed']:
		update.message.reply_text(
			'"%s"은 이미 구독되어 있는 과목 게시판입니다.' % text
		)
	else:
		with open('data/user/%s.txt' % user_id, 'a') as f:
			f.write(',%s' % lectureCode)

		user_data['feed'] += [lectureCode]
		with open('data/course/%s.txt' % lectureCode, 'r') as f:
			temp = f.read().split(',')[1:]
		if user_id not in temp: # to avoid duplication
			with open('data/course/%s.txt' % lectureCode, 'a') as f:
				f.write(',%s' % user_id)

		update.message.reply_text(
			'"%s"의 과목 게시판이 구독되었습니다.\n'
			'원문은 여기에서 보실 수 있습니다 : \n\n'
			'phya.snu.ac.kr/php/subject_list/Notice/list.php?id=%d_%s' % (text, year, lecturelist_all[text])
		)
	return semester(bot, update)


def show_list(bot, update, user_data):
	if len(user_data['feed']) == 0:
		update.message.reply_text('현재 구독중인 공지/강의 게시판이 없습니다.')
	else:
		feed_list = []
		for x in user_data['feed']:
			if(x == 'notice'):
				feed_list.append('학부공지사항 - phya.snu.ac.kr/xe/underbbs\n')
			else:
				feed_list.append(
					'%s - phya.snu.ac.kr/php/subject_list/Notice/list.php?id=%d_%s\n'
					% (lecturelist_all_rev[x], year, x)
				)
		feed_list.sort()
		update.message.reply_text(
			'현재 구독된 목록은 다음과 같습니다.\n\n'
			'%s' % ''.join(feed_list)
		)
		
	return start(bot, update, user_data)


def remove_feed_select(bot, update, user_data):
	if len(user_data['feed']) == 0:
		update.message.reply_text('현재 구독중인 공지/강의 게시판이 없습니다.')
		return start(bot, update, user_data)
	else:
		rm_keyboard = [[lecturelist_all_rev[x]] for x in user_data['feed']]
		update.message.reply_text(
			'구독을 취소할 게시판을 선택해 주세요.',
			reply_markup=ReplyKeyboardMarkup(rm_keyboard, one_time_keyboard=True)
		)
	return Remove


def remove_feed_remove(bot, update, user_data):
	text = update.message.text
	lectureCode = lecturelist_all[text]
	user_id = str(update.message.chat_id)

	user_data['feed'].remove(lecturelist_all[text])
	with open('data/user/%s.txt' % user_id, 'w') as f:
		f.write(','.join(['.'] + user_data['feed']))

	with open('data/course/%s.txt' % lectureCode, 'r') as f:
		temp = f.read().split(',')[1:]
	temp.remove(user_id)
	with open('data/course/%s.txt' % lectureCode, 'w') as f:
		f.write(','.join(['.'] + temp))

	update.message.reply_text(
		'"%s"의 구독이 정상적으로 취소되었습니다.' % text
	)
	return start(bot, update, user_data)


def credits(bot, update, user_data):
	update.message.reply_text(
		'서울대 물리학과 게시판 염탐꾼, 샤인만. (샤 + Feynman)\n\n'
		'만든이 : 박승원(서울대학교 물리천문학부)\n'
		'소스 링크 : github.com/seungwonpark/shaynman\n'
		'버그 제보 : github.com/seungwonpark/shaynman/issues\n\n'
		'사용법 문의는 받지 않습니다.'
	)
	return start(bot, update, user_data)


def done(bot, update):
	update.message.reply_text(
		'오늘도 샤인만을 이용해 주셔서 감사합니다. 새로운 글이 올라올 때마다 메시지를 드리겠습니다.\n\n'
		'설정을 수정하려면 다시 /start 로 시작해 주세요.'
	)
	return ConversationHandler.END




def error(bot, update, error):
	logger.warn('Update "%s" caused error "%s"' % (update, error))





def lecture_1(bot, update):
	update.message.reply_text(
		'강의가 몇 학년 과정인가요? 대학원 과목은 석사/박사 과정을 이용해 주세요.',
		reply_markup=ReplyKeyboardMarkup(keyboard_grade, one_time_keyboard=True)
	)
	return Lecture_1


def lecture_2(bot, update):
	update.message.reply_text(
		'강의가 몇 학년 과정인가요? 대학원 과목은 석사/박사 과정을 이용해 주세요.',
		reply_markup=ReplyKeyboardMarkup(keyboard_grade, one_time_keyboard=True)
	)
	return Lecture_2


def under_1_1(bot, update):
	update.message.reply_text(
		'구독하고자 하는 강의를 선택해 주십시오.',
		reply_markup=ReplyKeyboardMarkup(keyboard_under_1_1, one_time_keyboard=True)
	)
	return Subscribe


def under_1_2(bot, update):
	update.message.reply_text(
		'구독하고자 하는 강의를 선택해 주십시오.',
		reply_markup=ReplyKeyboardMarkup(keyboard_under_1_2, one_time_keyboard=True)
	)
	return Subscribe


def under_1_3(bot, update):
	update.message.reply_text(
		'구독하고자 하는 강의를 선택해 주십시오.',
		reply_markup=ReplyKeyboardMarkup(keyboard_under_1_3, one_time_keyboard=True)
	)
	return Subscribe


def under_1_4(bot, update):
	update.message.reply_text(
		'구독하고자 하는 강의를 선택해 주십시오.',
		reply_markup=ReplyKeyboardMarkup(keyboard_under_1_4, one_time_keyboard=True)
	)
	return Subscribe


def grad_1(bot, update):
	update.message.reply_text(
		'구독하고자 하는 강의를 선택해 주십시오.',
		reply_markup=ReplyKeyboardMarkup(keyboard_grad_1, one_time_keyboard=True)
	)
	return Subscribe


def under_2_1(bot, update):
	update.message.reply_text(
		'구독하고자 하는 강의를 선택해 주십시오.',
		reply_markup=ReplyKeyboardMarkup(keyboard_under_2_1, one_time_keyboard=True)
	)
	return Subscribe


def under_2_2(bot, update):
	update.message.reply_text(
		'구독하고자 하는 강의를 선택해 주십시오.',
		reply_markup=ReplyKeyboardMarkup(keyboard_under_2_2, one_time_keyboard=True)
	)
	return Subscribe


def under_2_3(bot, update):
	update.message.reply_text(
		'구독하고자 하는 강의를 선택해 주십시오.',
		reply_markup=ReplyKeyboardMarkup(keyboard_under_2_3, one_time_keyboard=True)
	)
	return Subscribe


def under_2_4(bot, update):
	update.message.reply_text(
		'구독하고자 하는 강의를 선택해 주십시오.',
		reply_markup=ReplyKeyboardMarkup(keyboard_under_2_4, one_time_keyboard=True)
	)
	return Subscribe


def grad_2(bot, update):
	update.message.reply_text(
		'구독하고자 하는 강의를 선택해 주십시오.',
		reply_markup=ReplyKeyboardMarkup(keyboard_grad_2, one_time_keyboard=True)
	)
	return Subscribe


def under_s(bot, update):
	update.message.reply_text(
		'구독하고자 하는 강의를 선택해 주십시오.',
		reply_markup=ReplyKeyboardMarkup(keyboard_under_s, one_time_keyboard=True)
	)
	return Subscribe

