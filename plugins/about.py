#!/usr/bin/env python
# -*- coding: utf-8 -*-

from utils import *

print "Loading " + __name__ + "..."

# About

@bot.message_handler(commands=['about'])
def about_bot(message):
	if intime(message):
		cid = getCID(message)
		url = "https://github.com/Tronikart/RadRetroRobot"
		bot.send_message(cid, "`> RadRetroRobot\n\nA multi-functional bot made by` @PEWPEWPEW\n\n[Source available here](" + url + ")\n\n[Update Channel](https://telegram.me/RRRUpdates)`\n\nPlease do report any bug you find, you can read the source page for a full list of all of RRRs functions and features.\n\nBeep boop!`", parse_mode="Markdown", disable_web_page_preview=True)