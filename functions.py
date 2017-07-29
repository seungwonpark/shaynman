from telegram import ReplyKeyboardMarkup
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters, RegexHandler,
							ConversationHandler)
import logging

from keyboards import *
from lecturelists import *

MainMenu, Generate, Lecture, Semester, Lecture_1, Lecture_2, Subscribe = range(7)

def start(bot, update):
	update.message.reply_text(
		'Hi! This is Shaynman. I will hold a conversation with you.\n\n'
		'Please reply.',
		reply_markup=ReplyKeyboardMarkup(keyboard_main, one_time_keyboard=True)
	)
	return MainMenu


def generate_feed(bot, update):
	update.message.reply_text(
		'어떤 피드를 생성하려 하십니까?',
		reply_markup=ReplyKeyboardMarkup(keyboard_generate, one_time_keyboard=True)
	)
	return Generate


def notice(bot, update, user_data):
	if 'feed' not in user_data:
		user_data['feed'] = []

	user_data['feed'] += ['notice']
	update.message.reply_text('학부 공지사항이 추가되었습니다.')
	return generate_feed(bot, update)


def semester(bot, update):
	update.message.reply_text(
		'어느 학기의 강의입니까? 현재 2017학년도 기준으로 피드가 제공되고 있습니다.',
		reply_markup=ReplyKeyboardMarkup(keyboard_semester, one_time_keyboard=True)
	)
	return Semester


def subscribe(bot, update, user_data):
	text = update.message.text
	lectureCode = lecturelist_all[text]
	if 'feed' not in user_data:
		user_data['feed'] = []

	user_data['feed'] += [lectureCode]
	update.message.reply_text('"%s" 가 구독되었습니다.' % text)
	return semester(bot, update)


def show_list(bot, update, user_data):
	feed_list = ', '.join(sorted([lecturelist_all_rev[x] for x in user_data['feed']]))
	update.message.reply_text(
		'현재 구독된 목록은 다음과 같습니다\n\n'
		'%s' % feed_list
	)
	return start(bot, update)

def remove_feed(bot, update):
	update.message.reply_text(str(user_data))
	return MainMenu

def done(bot, update):
	update.message.reply_text(
		'오늘도 샤인만을 이용해 주셔서 감사합니다. 새로운 글이 올라올 때마다 알림을 드리겠습니다.\n\n'
		'다시 시작하려면 /start 로 시작해 주세요.'
	)
	return ConversationHandler.END

def error(bot, update, error):
	logger.warn('Update "%s" caused error "%s"' % (update, error))





def lecture_1(bot, update):
	update.message.reply_text(
		'강의의 과정이..? 현재 2017학년도 기준으로 피드가 제공되고 있습니다.',
		reply_markup=ReplyKeyboardMarkup(keyboard_grade, one_time_keyboard=True)
	)
	return Lecture_1


def lecture_2(bot, update):
	update.message.reply_text(
		'강의의 과정이..? 현재 2017학년도 기준으로 피드가 제공되고 있습니다.',
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

