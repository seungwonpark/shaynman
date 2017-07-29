from telegram import ReplyKeyboardMarkup
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters, RegexHandler,
							ConversationHandler)
import logging

from keyboards import *

MainMenu, Generate, Lecture, Semester, Lecture_1, Lecture_2 = range(6)

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
	update.message.reply_text(str(user_data))
	if 'feed' not in user_data:
		user_data['feed'] = []

	user_data['feed'] += ['notice']
	return Generate


def semester(bot, update):
	update.message.reply_text(
		'어느 학기의 강의입니까? 현재 2017학년도 기준으로 피드가 제공되고 있습니다.',
		reply_markup=ReplyKeyboardMarkup(keyboard_semester, one_time_keyboard=True)
	)
	return Semester


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

def undergrad_1_1(bot, update):
	lecturelist = {
		'물리의 기본1 001' : 'fp001',
		'물리의 기본1 002' : 'fp002',
		'기초물리학1' : 'bp',
		'고급물리학1' : 'hphy',
		'물리학의 개념과 역사' : 'cpfhp',
		'양자개념과 인류문명' : 'qthc',
		# '미시세계와 거시세계' : ''
		'에너지' : 'energy'
	}
	for i in range(1,13):
		lecturelist['물리학1 %03d' % i] = 'gp1_%03d' % i

	for i in range(1,4):
		lecturelist['(단)물리학 %03d' % i] = 'phy%03d' % i

def undergrad_1_2(bot, update):
	lecturelist = {
		'단학기 역학' : 'mech_s',
		'역학1' : 'mech1',
		'현대 물리학의 기초' : 'fmp'
	}

def undergrad_1_3(bot, update):
	lecturelist = {
		'(단)양자물리 1' : 'qp_s',
		'양자물리1' : 'qphy1',
		'전자기파와 광학' : 'emwave',
		'물리수학' : 'mmp',
		'중급물리실험 1' : 'ipl'
	}

def undergrad_1_4(bot, update):
	lecturelist = {
		'생물계 물리입문' : 'ibp',
		'물리연구 1' : 'is1',
		'상대론과 시공간' : 'rst',
		'고체의 성질' : 'ps',
		'고급광학' : 'ao',
		'고급물리실험' : 'spb'
	}

def grad_1(bot, update):
	lecturelist = {
		'대학원연구입문' : 'idra',
		'양자역학 1' : 'qm',
		'전기역학 1' : 'electro',
		'고전역학' : 'cm',
		'고급실험' : 'alab',
		'응집물질물리학 1' : 'cmp1',
		'기본 핵 및 입자물리학' : 'bnpp',
		'레이저물리학' : 'lp',
		'상전이와 임계현상' : 'ptcp',
		'양자장론 1' : 'qft1',
		'응용물리특강 1' : 'atap1',
		'응집물질물리특강 1' : 'atcmp1',
		'고급장 및 입자이론' : 'atfp',
		'고급응집물질물리학' : 'acmp'
		# '석좌교수 특강' : 
	}

def grad_2(bot, update):
	lecturelist = {
		'통계역학' : 'sm',
		'양자역학 2' : 'qm2',
		'핵물리학' : 'np',
		'전기역학 2' : 'electro2',
		'응용전산물리' : 'cp',
		'양자장론 2' : 'qft2',
		'물리학특강 001' : 'stp_001',
		'물리학특강 002' : 'stp_002',
		'핵입자특강 2' : 'atnp',
		'입자물리학' : 'pp',
		'일반상대론' : 'gr',
		'수리물리학(이론물리의 해석학적 방법)' : 'mp',
		'복잡계물리' : 'pcs',
		'응집물질물리학 2' : 'cmp2',
		'원자물리학' : 'ap',
		'응용물리특강 2' : 'atap2',
		'고급현대물리학특강' : 'satmp',
		'생물계 물리' : 'biop',
		'끈이론' : 'st'
	}


def lecture_s(bot, update):
	lecturelist = {
		'(계절)물리학1' : 'sphy1',
		'(계절)물리학2' : 'sphy2'
	}

def undergrad_2_1(bot, update):
	lecturelist = {
		'기초물리학2' : 'bp2',
		'물리의 기본2 002' : 'fp2_002',
		'물리의 기본2 003' : 'fp2_003',
		'고급물리학1' : 'hphy2',
		'인문사회계를 위한 물리학' : 'pfh_ss',
		'미시세계와 거시세계' : 'mi_ma'
	}
	for i in range(1,13):
		lecturelist['물리학2 %03d' % i] = 'gp2_%03d' % i

	for i in range(1,4):
		lecturelist['(단)물리학 %03d' % i] = 'phy2_%03d' % i

def undergrad_2_2(bot, update):
	lecturelist = {
		'역학2' : 'mech2',
		'역학2 연습' : 'exer_mech2',
		'전기와 자기' : 'em',
		'전기와 자기 연습' : 'exer_em',
		'전자학 및 계측론' : 'emtse',
		'기본물리수학' : 'rmmp'
	}

def undergrad_2_3(bot, update):
	lecturelist = {
		'(단)전자기학' : 'esc',
		'양자물리2' : 'qp2',
		'양자물리2 연습' : 'exer_qp2',
		'열과 통계물리' : 'tsp',
		'전산물리' : 'cp',
		'중급물리실험 2' : 'iplab2'
	}

def undergrad_2_4(bot, update):
	lecturelist = {
		'응짐물질과 집단현상' : 'cpcmp',
		'유체역학' : 'f_mech',
		'물리연구 2' : 'is2',
		'핵과 기본입자' : 'nap',
		'물리학의 산업응용' : 'iap',
		'물리학과 신기술' : 'pnt',
		'역사적 물리논문 탐구' : 'shap'
	}


def show_list(bot, update, user_data):
	update.message.reply_text(str(user_data))
	return MainMenu

def remove_feed(bot, update):
	update.message.reply_text(str(user_data))
	return MainMenu

def done(bot, update):
	update.message.reply_text(str(user_data))
	return MainMenu

def error(bot, update, error):
	logger.warn('Update "%s" caused error "%s"' % (update, error))
