#!/usr/bin/env python
# -*- coding: utf-8 -*-

from utils import *

print "Loading " + __name__ + "..."

# Look for and replace

@bot.message_handler(func=lambda message: "/s/" in message.text[0:3])
def replacewith(message):
	if intime(message):
		cid = getCID(message)
		rid = message.reply_to_message
		if rid and cid != degeneratesgroup:
			content = message.text
			if content.split('/')[1] == 's':
				lookfor = r"" + content.split('/')[2]
				replacewith = r"" + content.split('/')[3]
				final_text = re.sub(lookfor, replacewith, rid.text)
				bot.reply_to(rid, "`" + unicode(final_text) + "`", parse_mode="Markdown")
		else:
			pass


