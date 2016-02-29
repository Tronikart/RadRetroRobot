#!/usr/bin/env python
# -*- coding: utf-8 -*-

from utils import *

print "Loading " + __name__ + "..."

# Help menu with reply

@bot.message_handler(commands=['help'])
def send_help_reply(message):
	if intime(message):
		uid = str(message.from_user.id)
		cid = str(message.chat.id)
		if message.chat.type == 'private':
			bot.send_message(uid, text_messages['help'], parse_mode="Markdown")
		elif message.chat.type == 'group' or message.chat.type == 'supergroup':
			if uid not in loadjson("userlist"):
				bot.reply_to(message, text_messages['help_group_first'], parse_mode="Markdown")
			else:
				bot.send_message(uid, text_messages['help'].format(title = message.chat.title), parse_mode="Markdown")
				bot.reply_to(message, text_messages['help_group'], parse_mode="Markdown")
		else:
			pass	
