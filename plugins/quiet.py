#!/usr/bin/env python
# -*- coding: utf-8 -*-

from utils import *

print "Loading " + __name__ + "..."

# Quiet group

@bot.message_handler(commands=['quiet'])
def quiet_group(message):
	if intime(message):
		cid = getCID(message)
		cid = str(cid)
		if message.chat.type == 'group' or message.chat.type == 'supergroup':
			action = getContent(message)
			gName = (message.chat.title)
			if action:
				if action == "-add":
					if str(cid) in loadjson("quietlist") or gName in loadjson("quietlist"):
						bot.reply_to(message, "`This group is already on the quiet list, if you desire to remove it, send /quiet -remove`", parse_mode="Markdown")
					else:
						addUser(cid, gName, "quietlist")
						bot.reply_to(message, "`This group has been added to the quiet list, I will now only answer when called and to commands.`", parse_mode="Markdown")
				elif action == "-remove":
					if str(cid) in loadjson("quietlist"):
						deljson(cid, "quietlist")
						bot.reply_to(message, "`This group has been removed from the quiet list, I will now randomly beep, boop, repeat and broadcast!`", parse_mode="Markdown")
					else:
						bot.reply_to(message, "`Couldnt find this group on the quiet list, if you desire to add it, send /quiet -add`", parse_mode="Markdown")
				else:
					bot.reply_to(message, "`Invalid input, only -add and -remove accepted.`", parse_mode="Markdown")
			else:
				bot.reply_to(message, "`> There are to options available:\n/quiet -add\n/quiet -remove\n\nI will stop randomly beeping, booping, repeating and broadcasting if you add this group to the quiet list`", parse_mode="Markdown")
		else:
			bot.reply_to(message, "`This option is only available for groups.`", parse_mode="Markdown")
