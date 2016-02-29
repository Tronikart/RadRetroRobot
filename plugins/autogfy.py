#!/usr/bin/env python
# -*- coding: utf-8 -*-

from utils import *

print "Loading " + __name__ + "..."

# gfy auto gif

@bot.message_handler(func=lambda message: "gfycat.com" in message.text.lower())
def gfy(message):
	if intime(message):
		cid = getCID(message)
		try:
			bot.send_message(cid, getGfy(message.text))
		except:
			pass
