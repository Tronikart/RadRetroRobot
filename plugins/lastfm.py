#!/usr/bin/env python
# -*- coding: utf-8 -*-

from utils import *

print "Loading " + __name__ + "..."

# Last FM

@bot.message_handler(commands=['lastfm'])
def last_commands(message):
	if intime(message):
		cid = getCID(message)
		bot.send_message(cid, "`Last FM related commands: \n\n  /fmuser <username> - sets your username for these commands\n  /fmtop - shows your top 5 artists from last week\n  /fmalbums - shows your top 5 albums from last week.\n  /np - shows what you are currently listening to\n  /fmgrid - shows a grid of your last week albums\n  send /fmgrid -? for more options`", parse_mode="Markdown")
