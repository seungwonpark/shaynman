# -*- coding: utf-8 -*-
from telegram import ReplyKeyboardMarkup
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters, RegexHandler,
							ConversationHandler)

import logging

# Safely use access token
# execute as `bot_token="xoxb-abc-1232" python shaynman.py`
import os
bot_token = os.environ["bot_token"]

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
					level=logging.INFO)

logger = logging.getLogger(__name__)

# State numbers
CHOOSING, TYPING_REPLY, TYPING_CHOICE = range(3)

# Configure keyboard
reply_keyboard = [
	['Age', 'Favourite colour'],
	['Number of siblings', 'Something else...'],
	['Done']
]
markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)


def facts_to_str(user_data):
	facts = list()

	for key, value in user_data.items():
		facts.append('%s - %s' % (key, value))

	return "\n".join(facts).join(['\n', '\n'])


def start(bot, update):
	update.message.reply_text(
		"Hi! My name is Doctor Botter. I will hold a more complex conversation with you. "
		"Why don't you tell me something about yourself?",
		reply_markup=markup)

	return CHOOSING


def regular_choice(bot, update, user_data):
	text = update.message.text
	user_data['choice'] = text
	update.message.reply_text('Your %s? Yes, I would love to hear about that!' % text.lower())

	return TYPING_REPLY


def custom_choice(bot, update):
	update.message.reply_text('Alright, please send me the category first, '
							  'for example "Most impressive skill"')

	return TYPING_CHOICE


def received_information(bot, update, user_data):
	text = update.message.text
	category = user_data['choice']
	user_data[category] = text
	del user_data['choice']

	update.message.reply_text("Neat! Just so you know, this is what you already told me:"
							  "%s"
							  "You can tell me more, or change your opinion on something."
							  % facts_to_str(user_data),
							  reply_markup=markup)

	return CHOOSING


def done(bot, update, user_data):
	if 'choice' in user_data:
		del user_data['choice']

	update.message.reply_text("I learned these facts about you:"
							  "%s"
							  "Until next time!" % facts_to_str(user_data))

	user_data.clear()
	return ConversationHandler.END


def error(bot, update, error):
	logger.warn('Update "%s" caused error "%s"' % (update, error))


def main():
	# Create the Updater and pass it your bot's token.
	updater = Updater(bot_token)

	# Get the dispatcher to register handlers
	dp = updater.dispatcher

	# Add conversation handler with the states GENDER, PHOTO, LOCATION and BIO
	conv_handler = ConversationHandler(
		entry_points=[CommandHandler('start', start)],

		states={
			CHOOSING: [RegexHandler('^(Age|Favourite colour|Number of siblings)$',
									regular_choice,
									pass_user_data=True),
					   RegexHandler('^Something else...$',
									custom_choice),
					   ],

			TYPING_CHOICE: [MessageHandler(Filters.text,
										   regular_choice,
										   pass_user_data=True),
							],

			TYPING_REPLY: [MessageHandler(Filters.text,
										  received_information,
										  pass_user_data=True),
						   ],
		},

		fallbacks=[RegexHandler('^Done$', done, pass_user_data=True)]
	)

	dp.add_handler(conv_handler)

	# log all errors
	dp.add_error_handler(error)

	# Start the bot
	updater.start_polling()

	# Run the bot until you press Ctrl-C or the process receives SIGINT,
	# SIGTERM or SIGABRT. This should be used most of the time, since
	# start_polling() is non-blocking and will stop the bot gracefully.
	updater.idle()


if __name__ == '__main__':
	main()