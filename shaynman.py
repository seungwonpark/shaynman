# -*- coding: utf-8 -*-
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, Job, CallbackQueryHandler
import logging

# Safely use access token
# execute as `bot_token="xoxb-abc-1232" python shaynman.py`
import os
bot_token = os.environ["bot_token"]

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


def start(bot, update):
	update.message.reply_text('\
		서울대 물리학과 강의 게시판 알리미 봇, 샤인만입니다.\n\
		This is Shaynman, the push-notification bot regarding SNU Physics lecture board.\n\
		\n\
		/subscribe 으로 시작해 주세요.\n\
		Please start with /subscribe.\
	')


def subscribe(bot, update):
	keyboard = [
		[
			InlineKeyboardButton("Option 1", callback_data='1'),
			InlineKeyboardButton("Option 2", callback_data='2')
		],
		[
			InlineKeyboardButton("Option 3", callback_data='3')
		]
	]
	reply_markup = InlineKeyboardMarkup(keyboard)

	update.message.reply_text('Please choose:', reply_markup=reply_markup)


def button(bot, update):
	query = update.callback_query

	bot.edit_message_text(
		text="Selected option: %s" % query.data,
		chat_id=query.message.chat_id,
		message_id=query.message.message_id
	)


def error(bot, update, error):
	logger.warning('Update %s caused error "%s"' % (update, error))


def main():
    # Create the EventHandler and pass it your bot's token.
	updater = Updater(bot_token)

	# Get the dispatcher to register handlers
	dp = updater.dispatcher

	# on different commands - answer in Telegram
	dp.add_handler(CommandHandler("start", start))
	dp.add_handler(CommandHandler("help", start))
	dp.add_handler(CommandHandler("subscribe", subscribe))
	dp.add_handler(CallbackQueryHandler(button))

	# log all errors
	dp.add_error_handler(error)

	# Start the bot
	updater.start_polling()

	# Block until you press Ctrl-C or the process receives SIGINT, SIGTERM or
    # SIGABRT. This should be used most of the time, since start_polling() is
    # non-blocking and will stop the bot gracefully.
	updater.idle()

if __name__ == '__main__':
	main()