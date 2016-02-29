#!/usr/bin/env python
# -*- coding: utf-8 -*-

from utils import *

print "Loading " + __name__ + "..."

# Dota Live structures

@bot.message_handler(commands=['dotalivemap', 'dlmap'])
def dota_map(message):
	if intime(message):
		cid = getCID(message)
		content = getContent(message)
		if content and content != "-?":
			match_id = content[5:len(content)]
			url = "http://api.steampowered.com/IDOTA2Match_570/GetLiveLeagueGames/v1/?key=" + dota_key + "&format=JSON&language=en_us"
			hero_list = getJson("http://api.steampowered.com/IEconDOTA2_570/GetHeroes/v1/?key=" + dota_key + "&format=JSON&language=en_us")
			data = getJson(url)
			if validLink(url):
				games = ""
				found = False
				for game in data['result']['games']:
					# FOUND THE GAME
					if str(game['match_id']) == match_id:
						found = True
						dire_towers = dota_bin(game['scoreboard']['dire']['tower_state'])
						dire_rax = dota_bin(game['scoreboard']['dire']['barracks_state'])
						radiant_towers = dota_bin(game['scoreboard']['radiant']['tower_state'])
						radiant_rax = dota_bin(game['scoreboard']['radiant']['barracks_state'])
						duration = game['scoreboard']['duration']/60
						duration = str(int(duration))
						radiant_score = game['scoreboard']['radiant']['score']
						dire_score = game['scoreboard']['dire']['score']
						# NAME RADIANT TEAM
						try:
							radiant = game['radiant_team']['team_name']
							radiant_id = "(" + str(game['radiant_team']['team_id']) + ") "
						except:
							radiant = "Radiant Team"
							radiant_id = ""
						# NAME DIRE TEAM
						try:
							dire = game['dire_team']['team_name']
							dire_id = " (" + str(game['dire_team']['team_id']) + ")"
						except:
							dire = "Dire Team"
							dire_id = ""
						d_towers = init_towers(dire_towers)
						d_rax = init_rax(dire_rax)
						r_towers = init_towers(dire_towers)
						r_rax = init_rax(dire_rax)
						try:
							if "-map" in content:
								dota_map = """---------------------------------------------\n|         ({dire_top_1})      ({dire_top_2})    ({dire_top_3})({dire_top_melee})             |\n|                            ({dire_top_ranged})  ({dire_ancient_top})(_A_)   |\n|                                   ({dire_ancient_bot})      |\n|    \       \              ({dire_mid_melee})              |\n|      \       \            ({dire_middle_3})({dire_mid_ranged})    ({dire_bottom_melee})({dire_bottom_ranged}) |\n|        \       \                      ({dire_bottom_3})  |\n|  ({radiant_top_1})     \       \    ({dire_middle_2})                  |\n|            \                           ({dire_bottom_2}) |\n|              \     ({dire_middle_1})                     |\n|                                            |\n|               ({radiant_middle_1})           \              |\n|  ({radiant_top_2})                 \        \            |\n|             ({radiant_middle_2})        \       \       ({dire_bottom_1}) |\n|  ({radiant_top_3})                     \       \         |\n| ({radiant_top_melee})({radiant_top_ranged})   ({radiant_middle_3})               \       \       |\n|        ({radiant_mid_ranged})({radiant_mid_melee})                              |\n|    ({radiant_ancient_top})                                     |\n| (_A_)({radiant_ancient_bot})  ({radiant_bottom_ranged})                              |\n|           ({radiant_bottom_melee})({radiant_bottom_3})    ({radiant_bottom_2})      ({radiant_bottom_1})           |\n----------------------------------------------\n""".format(dire_bottom_1=d_towers[10], dire_middle_1=d_towers[7], dire_top_1=d_towers[4], dire_bottom_2=d_towers[9], dire_middle_2=d_towers[6], dire_top_2=d_towers[3], dire_bottom_3=d_towers[8], dire_middle_3=d_towers[5], dire_top_3=d_towers[2], dire_bottom_ranged=r_rax[4], dire_bottom_melee=r_rax[5], dire_mid_ranged=r_rax[2], dire_mid_melee=r_rax[3], dire_top_melee=r_rax[1], dire_top_ranged=r_rax[0], dire_ancient_bot=d_towers[1], dire_ancient_top=d_towers[0], radiant_bottom_1=r_towers[10], radiant_middle_1=r_towers[7], radiant_top_1=r_towers[4], radiant_bottom_2=r_towers[9], radiant_middle_2=r_towers[6], radiant_top_2=r_towers[3], radiant_bottom_3=r_towers[8], radiant_middle_3=r_towers[5], radiant_top_3=r_towers[2], radiant_bottom_ranged=r_rax[4], radiant_bottom_melee=r_rax[5], radiant_mid_ranged=r_rax[2], radiant_mid_melee=r_rax[3], radiant_top_melee=r_rax[1], radiant_top_ranged=r_rax[0], radiant_ancient_bot=r_towers[1], radiant_ancient_top=r_towers[0])
								map_details = "\nT = Tower, m = Melee Rax, r = Ranged Rax, X = Structure destroyed"
								header = radiant + " " + str(radiant_id) + str(radiant_score) + "| " + str(duration) + " minutes" + " |" + str(dire_score) + " " + dire + str(dire_id) + "\n"
								final_message = header + dota_map + map_details
								bot.send_message(cid, "`{final_message}`".format(final_message=final_message), parse_mode="Markdown")

							elif "-lis" in content:
								dota_match = "\n_Radiant Structures:\nRax:\n  Top melee: {radiant_top_melee}\n  Top ranged: {radiant_top_ranged}\n  Mid melee: {radiant_mid_melee}\n  Mid ranged: {radiant_mid_ranged}\n  Bot melee: {radiant_bottom_melee}\n  Bot ranged: {radiant_bottom_ranged}\nAncient Towers:\n  Top Ancient Tower: {radiant_ancient_top}\n  Bot Ancient Tower: {radiant_ancient_bot}\nTop Towers:\n  Tier 1: {radiant_top_1}\n  Tier 2: {radiant_top_2}\n  Tier 3: {radiant_top_3}\nMid Towers:\n  Tier 1: {radiant_middle_1}\n  Tier 2: {radiant_middle_2}\n  Tier 3: {radiant_middle_3}\n Bottom Towers:\n Tier 1: {radiant_bottom_1}\n  Tier 2: {radiant_bottom_2}\n  Tier 3: {radiant_bottom_3}\n\n_Dire Structures:\nRax:\n  Top melee: {dire_top_melee}\n  Top ranged: {dire_top_ranged}\n  Mid melee: {dire_mid_melee}\n  Mid ranged: {dire_mid_melee}\n  Bot melee: {dire_bottom_melee}\n  Bot ranged: {dire_bottom_ranged}\nAncient Towers:\n  Top Ancient Tower: {dire_ancient_top}\n  Bot Ancient Tower: {dire_ancient_bot}\nTop Towers:\n  Tier 1: {dire_top_1}\n  Tier 2: {dire_top_2}\n  Tier 3: {dire_top_3}\nMid Towers:\n  Tier 1: {dire_middle_1}\n  Tier 2: {dire_middle_2}\n  Tier 3: {dire_middle_3}\n Bottom Towers:\n Tier 1: {dire_bottom_1}\n  Tier 2: {dire_bottom_2}\n  Tier 3: {dire_bottom_3}".format(dire_bottom_1=d_towers[10], dire_middle_1=d_towers[7], dire_top_1=d_towers[4], dire_bottom_2=d_towers[9], dire_middle_2=d_towers[6], dire_top_2=d_towers[3], dire_bottom_3=d_towers[8], dire_middle_3=d_towers[5], dire_top_3=d_towers[2], dire_bottom_ranged=r_rax[4], dire_bottom_melee=r_rax[5], dire_mid_ranged=r_rax[2], dire_mid_melee=r_rax[3], dire_top_melee=r_rax[1], dire_top_ranged=r_rax[0], dire_ancient_bot=d_towers[1], dire_ancient_top=d_towers[0], radiant_bottom_1=r_towers[10], radiant_middle_1=r_towers[7], radiant_top_1=r_towers[4], radiant_bottom_2=r_towers[9], radiant_middle_2=r_towers[6], radiant_top_2=r_towers[3], radiant_bottom_3=r_towers[8], radiant_middle_3=r_towers[5], radiant_top_3=r_towers[2], radiant_bottom_ranged=r_rax[4], radiant_bottom_melee=r_rax[5], radiant_mid_ranged=r_rax[2], radiant_mid_melee=r_rax[3], radiant_top_melee=r_rax[1], radiant_top_ranged=r_rax[0], radiant_ancient_bot=r_towers[1], radiant_ancient_top=r_towers[0])
								details = "\n\nT = Tower, m = Melee Rax, r = Ranged Rax, X = Structure destroyed"
								header = radiant + " " + str(radiant_id) + str(radiant_score) + "| " + str(duration) + " |" + str(dire_score) + " " + dire + str(dire_id) + "\n"
								final_message = header + dota_match + details
								bot.send_message(cid, "`{final_message}`".format(final_message=final_message), parse_mode="Markdown")
							else:
								bot.reply_to(message, "`Please enter a valid option:\n-map for a view of the map\n-lis to get a list of the structures (recommended for small screens)\n\n then follow the option with a live tournament ID\n\nEx: /dlmap -map <ID> `", parse_mode="Markdown")
						except IndexError:
							bot.reply_to(message, "`There has been an error, this game probably is over by now, check in a while or use /dotamatch`", parse_mode="Markdown")

			if not found:
				bot.reply_to(message, "`I could not find any game with that ID.\n\nMaybe the game is already finished, try using /dmatch`", parse_mode="Markdown")
		else:
			bot.reply_to(message, "`Follow this command with\n-map for a view of the map\n-lis to get a list of the structures (recommended for small screens)\n\n then follow the option with a live tournament ID\n\n\n\nExample:\n  /dlmap -map 2155217045`", parse_mode="Markdown")
