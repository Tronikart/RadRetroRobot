#!/usr/bin/env python
# -*- coding: utf-8 -*-

from utils import *

print "Loading " + __name__ + "..."

# Start bot

@bot.message_handler(commands=['start'])
def send_welcome(message):

	uid = str(message.from_user.id)
	cid = str(message.chat.id)

	if message.chat.type == 'private':
		if uid not in loadjson("userlist"):
			addUser(uid, message.from_user.first_name, "userlist")
			about_bot(message)
			bot.send_message(uid, text_messages['startfirst'], parse_mode="Markdown")
		else:
			bot.send_message(uid, text_messages['start'], parse_mode="Markdown")
	elif message.chat.type == 'group' or message.chat.type == 'supergroup':
		if uid not in loadjson("userlist"):
			bot.reply_to(message, text_messages['startfirstgroup'], parse_mode="Markdown")
			about_bot(message)
		else:
			bot.send_message(cid, text_messages['startgroup'], parse_mode="Markdown")
			bot.send_message(uid, text_messages['startfromgroup'].format(title = message.chat.title), parse_mode="Markdown")
	else:
		pass