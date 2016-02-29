#!/usr/bin/env python
# -*- coding: utf-8 -*-

from utils import *

print "Loading " + __name__ + "..."

# Steam Commands

@bot.message_handler(commands=['steam'])
def steam_commands(message):
	if intime(message):
		cid = getCID(message)
		bot.send_message(cid, u'`> Steam related commands:\n\n  /steamid <game> - Returns the games ID\n  /steampage <ID> - Returns the games information\n  /steamdetails <ID> - Game details such as single player or multiplayer\n  /steamnews <ID> - Returns the last new from a game, it may contain weird formating.`\n\n`I will also auto detect steam store links and return the games information.`', parse_mode="Markdown")
