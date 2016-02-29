#!/usr/bin/env python
# -*- coding: utf-8 -*-

from utils import *

print "Loading " + __name__ + "..."

# Dota Commands

@bot.message_handler(commands=['dota'])
def dota_commands(message):
	if intime(message):
		cid = getCID(message)
		bot.send_message(cid, "`> Dota related commands: \n\n  /dotanews - Sends you the last dota new on the blog\n  /dmatch <Match ID> - Displays the info for a dota match\n  /dlive - Displays a list of up to 10 live tournament games\n  /dleague <League ID> - Displays the info of a League\n  /dldetails <MatchID> - displays live information from a tournament match\n  /dlmap <option> <MatchID> - displays live map information from a tournament match`", parse_mode="Markdown")
