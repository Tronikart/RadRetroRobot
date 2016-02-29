#!/usr/bin/env python
# -*- coding: utf-8 -*-

from utils import *

print "Loading " + __name__ + "..."

# print

@bot.message_handler(commands=['print', 'echo'])
def echo_message(message):
	if intime(message):
		cid = getCID(message)
		error = False
		msg = getContent(message)
		if msg:
			try:
				bot.send_message(cid, u"`{msg}`".format(msg=msg), parse_mode="Markdown")
			except:
				bot.send_message(cid, unicode(msg))
		else:
			bot.reply_to(message, "`Follow this command with some text and I will repeat it\n\nExample:\n  /print I repeat what humans say`", parse_mode="Markdown")

