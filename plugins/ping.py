#!/usr/bin/env python
# -*- coding: utf-8 -*-

from utils import *

print "Loading " + __name__ + "..."

# Ping user

@bot.message_handler(commands=['ping'])
def ping(message):
	if intime(message):
		uName = message.from_user.first_name
		lname = message.from_user.last_name
		usName = message.from_user.username
		if message.chat.type == 'private':
			uid = str(message.from_user.id)
			try:
				if lname != None:
					bot.reply_to(message, text_messages['ping'].format(name=uName, uname=usName, lname=lname, uid=uid), parse_mode="Markdown")
				else:
					lname = ''
					bot.reply_to(message, text_messages['ping'].format(name=uName, uname=usName, lname=lname, uid=uid), parse_mode="Markdown")
			except:
				bot.reply_to(message, "`Sorry your name contains unsupported characters, heres your ID at least `"+ uid, parse_mode="Markdown")

		elif message.chat.type == 'group' or message.chat.type == 'supergroup':
			uid = str(message.from_user.id)
			gid = str(message.chat.id).lstrip('-')
			gName = message.chat.title
			try:
				if lname != None:
					bot.reply_to(message, text_messages['pinggroup'].format(name=uName, uname=usName, lname=lname, uid=uid, gName=gName, gid=gid), parse_mode="Markdown")
				else:
					lname = ''
					bot.reply_to(message, text_messages['pinggroup'].format(name=uName, uname=usName, lname=lname, uid=uid, gName=gName, gid=gid), parse_mode="Markdown")
			except:
				bot.reply_to(message, "`Sorry your name contains unsupported characters, heres your ID `" + uid + " and the groups ID " + gid, parse_mode="Markdown")
		else:
			pass
