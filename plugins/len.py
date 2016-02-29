#!/usr/bin/env python
# -*- coding: utf-8 -*-

from utils import *

print "Loading len plugin..."

# Len

@bot.message_handler(commands=['len'])
def lenght(message):
	if intime(message):
		cid = getCID(message)
		content = getContent(message)
		if content != "-?" and content:
			no_spaces = str(len(content.replace(" ", "")))
			spaces = str(len(content))
			bot.send_message(cid, "`Your text is:\n"+ spaces + " characters long including spaces\n" + no_spaces +" characters long not including spaces.`", parse_mode="Markdown")
		elif content == "-?":
			bot.reply_to(message, "`Follow this command with a message and I will return its lenght\n\nExample:\n  /len Rad Retro Robot`", parse_mode="Markdown")
		else:
			try:
				rid = message.reply_to_message
				content = rid.text
				no_spaces = str(len(content.replace(" ", "")))
				spaces = str(len(content))
				bot.send_message(cid, "`Your text is:\n"+ spaces + " characters long including spaces\n" + no_spaces +" characters long not including spaces.`", parse_mode="Markdown")
			except:
				pass
