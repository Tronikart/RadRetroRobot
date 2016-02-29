#!/usr/bin/env python
# -*- coding: utf-8 -*-

from utils import *

print "Loading " + __name__ + "..."

# Print to console the list of users registered 

@bot.message_handler(commands=['userlist', 'stats'])
def user_list(message):
	uid = getUID(message)
	cid = getCID(message)
	if uid == adminid:
		users = str(len(loadjson("userlist")))
		lastfm_users = str(len(loadjson("fmuser")))
		groups = str(len(loadjson("grouplist")))
		now = datetime.now()
		diff = now - uptime
		days, seconds = diff.days, diff.seconds
		hours = days * 24 + seconds // 3600
		minutes = (seconds % 3600) // 60
		seconds = seconds % 60
		total_uptime = str(days) + "d " + str(hours) + "h " + str(minutes) + "m " + str(seconds) + "s"
		bot.send_message(cid,"`" + users + " registered users\n" + lastfm_users + " registered lastfm users\n" + groups + " registered groups\n\nTotal Uptime: " + total_uptime + "`", parse_mode="Markdown")