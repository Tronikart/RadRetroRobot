#!/usr/bin/env python
# -*- coding: utf-8 -*-

from utils import *

print "Loading " + __name__ + "..."

# Dota Match ID

@bot.message_handler(commands=['dotamatch', 'dmatch'])
def dota_match(message):
	if intime(message):
		cid = getCID(message)
		match_id = getContent(message)
		if match_id and match_id != "-?":
			url ="http://api.steampowered.com/IDOTA2Match_570/GetMatchDetails/v1/?key=" + dota_key + "&format=JSON&language=en_us&match_id=" + match_id
			if validLink(url):
				game = getJson(url)
				game = game['result']
				hero_list = getJson("http://api.steampowered.com/IEconDOTA2_570/GetHeroes/v1/?key=" + dota_key + "&format=JSON&language=en_us")
				if 'players' in game:
					dire = ""
					radiant = ""
					for player in game['players']:
						for hero in hero_list['result']['heroes']:
							if player['hero_id'] == hero['id']:
								player_hero = hero['localized_name']
								break
						player_slot = player['player_slot']
						kills = player['kills']
						deaths = player['deaths']
						assists = player['assists']
						lh = player['last_hits']
						denies = player['denies']
						gpm = player['gold_per_min']
						xpm = player['xp_per_min']
						level = player['level']
						gold = player['gold']
						if deaths != 0:
							kda = float(kills+assists)/float(deaths)
							kda = str(kda)
							kda = kda[0:3]
						else:
							kds = 0
						if player_slot < 10:
							radiant += "> " + str(player_hero) +" " + str(level) + " " + str(kills) + "/" + str(deaths) + "/" + str(assists) + " " + kda + " " + str(gold) + " " + str(lh) + " " + str(denies) + " " + str(gpm) + " " + str(xpm) + "\n"
						else:
							dire += "> " + str(player_hero) +" " + str(level) + " " + str(kills) + "/" + str(deaths) + "/" + str(assists) + " " + kda + " " + str(gold) + " " + str(lh) + " " + str(denies) + " " + str(gpm) + " " + str(xpm) + "\n"
					header = "|Hero|Level|K|D|A|KDA|Gold|LH|DN|GPM|XPM\n"
					divider = "\n"
					match = "_Radiant Team\n" + header + radiant + divider + "_Dire team\n" + header + dire
					dotabuff = "http://www.dotabuff.com/matches/" + match_id
					dotabuff = treatLink(dotabuff)
					bot.send_message(cid, '`{match}`'.format(match=match) + '\n\t[Dota Buff Page]({dotabuff})'.format(dotabuff=dotabuff), parse_mode="Markdown", disable_web_page_preview=True)
				else:
					bot.reply_to(message, "`Match not found.\n\nRemember that it cant be a live match.`", parse_mode="Markdown")
			else:
				error = validLink(url)
				bot.reply_to(message, "`There has been an error, the number {error} to be specific.`".format(error=error), parse_mode="Markdown")
		else:
			bot.reply_to(message, "`Follow this command with a match ID and I will send the final scoreboard of the match, remember that it cant be a live match.\n\nExample:\n  /dmatch 2155217045`", parse_mode="Markdown")
