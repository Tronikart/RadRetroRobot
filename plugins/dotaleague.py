#!/usr/bin/env python
# -*- coding: utf-8 -*-

from utils import *

print "Loading " + __name__ + "..."

# Dota League info

@bot.message_handler(commands=['dotaleague', 'dleague', 'dtournament', 'dotatournament'])
def dota_league_info(message):
	if intime(message):
		cid = getCID(message)
		league_id = getContent(message)
		url = "http://api.steampowered.com/IDOTA2Match_570/GetLeagueListing/v1/?key=" + dota_key + "&format=JSON&language=en_us"
		leagues = getJson(url)
		if league_id and league_id != "-?":
			found = False
			for league in leagues['result']['leagues']:
				if str(league['leagueid']) == league_id:
					found = True
					name = league['name']
					description = league['description']
					league_url = league['tournament_url']
					league_url = treatLink(league_url)
					if league_url != "":
						league_url = "[Tournament Webpage]({league_url})".format(league_url=league_url)
					else:
						league_url = ""
					bot.send_message(cid, "`> {name}\n\n{description}\n`\n{league_url}".format(name=name, description=description, league_url=league_url), parse_mode="Markdown", disable_web_page_preview=True)
					break
			if not found:
				bot.reply_to(message, "`Couldnt find a league with that ID.`", parse_mode="Markdown")
		else:
			bot.reply_to(message, "`Follow this command with a Dota 2 league ID to get its basic info\n\nExample:\n  /dleague 2155217045`", parse_mode="Markdown")
