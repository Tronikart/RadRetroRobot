#!/usr/bin/env python
# -*- coding: utf-8 -*-

from utils import *

print "Loading " + __name__ + "..."

# Flip

@bot.message_handler(commands=['flip'])
def flip_coin(message):
	if intime(message):
		content = getContent(message)
		if content != "-?" or not content:
			cid = getCID(message)
			coin = ['`Heads`', '`Tails`']
			bot.send_message(cid, random.choice(coin), parse_mode="Markdown")
		else:
			bot.reply_to(message, "`This command will flip a coin (virtually) and tell you its result`", parse_mode="Markdown")
