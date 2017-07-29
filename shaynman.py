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
