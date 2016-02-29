#!/usr/bin/env python
# -*- coding: utf-8 -*-

from utils import *

print "Loading " + __name__ + "..."

# Last FM User Set

@bot.message_handler(commands=['fmuser'])
def fmuser(message):
	if intime(message):
		cid = unicode(message.chat.id)
		uid = unicode(message.from_user.id)
		hasUser = True
		fmUsers = loadjson("fmuser")
		user = getContent(message)
		if user and user != "-?":
			if uid not in fmUsers:
				addUser(uid, user, "fmuser")
				bot.send_message(cid, "`You've been registered into my data base as {username}.`".format(username=user), parse_mode="Markdown")
			elif uid in fmUsers:
				addUser(uid, user, "fmuser")
				bot.send_message(cid, "`Changing your username from: {olduser} to {username}.`".format(olduser=fmUsers[uid], username=user), parse_mode="Markdown")
		else:
			bot.reply_to(message, "`Follow this command with your last.fm username to be able to use now playing command.\n\nExample:\n  /fmuser RadRetroRobot`", parse_mode="Markdown")
