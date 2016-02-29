#!/usr/bin/env python
# -*- coding: utf-8 -*-

from utils import *

print "Loading " + __name__ + "..."

# Dota Live Details

@bot.message_handler(commands=['dotalivedetails', 'dldetails'])
def dota_league_detail(message):
	if intime(message):
		cid = getCID(message)
		url = "http://api.steampowered.com/IDOTA2Match_570/GetLiveLeagueGames/v1/?key=" + dota_key + "&format=JSON&language=en_us"
		hero_list = getJson("http://api.steampowered.com/IEconDOTA2_570/GetHeroes/v1/?key=" + dota_key + "&format=JSON&language=en_us")
		match_id = getContent(message)
		request = requests.get(url)
		data = request.json()
		if match_id and match_id != "-?":
			if request.status_code == 200:
				games = ""
				found = False
				for game in data['result']['games']:
					# FOUND THE GAME
					if str(game['match_id']) == match_id:
						found = True
						print "game found"
						match_id = game['match_id']
						spectators = game['spectators']
						league_id = game['league_id']
						duration = 0.0
						radiant_heroes = ""
						dire_heroes = ""
						dire = ""
						dire_players = ""
						radiant = ""
						radiant_players = ""
						# NAME RADIANT TEAM
						try:
							radiant = game['radiant_team']['team_name']
							radiant_id = "(" + str(game['radiant_team']['team_id']) + ")"
						except:
							radiant = "Radiant Team"
							radiant_id = ""
						# NAME DIRE TEAM
						try:
							dire = game['dire_team']['team_name']
							dire_id = "(" + str(game['dire_team']['team_id']) + ")"
						except:
							dire = "Dire Team"
							dire_id = ""	

						# IF THE GAME STARTED 
						if game['scoreboard']['duration'] > 0:
							duration = game['scoreboard']['duration']/60
							duration = str(int(duration)) + " minutes"
							radiant_score = game['scoreboard']['radiant']['score']
							dire_score = game['scoreboard']['dire']['score']
							rosh_timer = game['scoreboard']['roshan_respawn_timer']
							if rosh_timer == 0:
								rosh_timer_message = "\nRosh is up!"
							else:
								rosh_timer = rosh_timer/60.0
								rosh_timer = str(rosh_timer)[0:3]
								rosh_timer_message = "\nRosh timer: " + rosh_timer + " minutes."
							# RADIANT HEROES AND STATS
							for player in game['scoreboard']['radiant']['players']:
								for hero in hero_list['result']['heroes']:
									if player['hero_id'] == hero['id']:
										player_hero = hero['localized_name']
										break
								player_slot = player['player_slot']
								kills = player['kills']
								deaths = player['death']
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
									kda = "0"
								radiant_heroes += "> " + str(player_hero) +" " + str(level) + " " + str(kills) + "/" + str(deaths) + "/" + str(assists) + " " + kda + " " + str(gold) + " " + str(lh) + " " + str(denies) + " " + str(gpm) + " " + str(xpm) + "\n"							
							# DIRE HEROES AND STATS
							for player in game['scoreboard']['dire']['players']:
								for hero in hero_list['result']['heroes']:
									if player['hero_id'] == hero['id']:
										player_hero = hero['localized_name']
										break
								player_slot = player['player_slot']
								kills = player['kills']
								deaths = player['death']
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
									kda = "0"
								dire_heroes += "> " + str(player_hero) +" " + str(level) + " " + str(kills) + "/" + str(deaths) + "/" + str(assists) + " " + kda + " " + str(gold) + " " + str(lh) + " " + str(denies) + " " + str(gpm) + " " + str(xpm) + "\n"
							header = "|Hero|Level|K|D|A|KDA|Gold|LH|DN|GPM|XPM\n"
							divider = "\n"
							match = str(radiant_score) + "\n_" + radiant +"\n" + header + radiant_heroes + divider + str(dire_score) + "\n_" + dire  +"\n" + header + dire_heroes
							dotabuff = "http://www.dotabuff.com/matches/" + str(match_id)
							dotabuff = treatLink(dotabuff)
							player_name_error = False
							# PLAYERS WITH HEROES
							for player in game['players']:
								for hero in hero_list['result']['heroes']:
									if player['hero_id'] == hero['id']:
										player_hero = hero['localized_name']
										break
								player_name = player['name']
								if player['team'] == 0:
									try:
										radiant_players += "> " + player_name + " - " + player_hero + "\n"
									except:
										radiant_players += "> Radiant player " + player_hero + "\n"
										player_name_error = True
								elif player['team'] == 1:
									try:
										dire_players += "> " +  player_name + " - " + player_hero + "\n"
									except:
										dire_players += "> Radiant player " + player_hero + "\n"
										player_name_error = True
								else:
									pass
							total_players = "_" + radiant + " Players:\n" + radiant_players + "\n_" + dire + " Players:\n" + dire_players + "\n"
							if player_name_error:
								total_players = "_Radiant Players:\n" + radiant_players + "\n_Dire Players:\n" + dire_players + "\nI could not display some of these names correctly, sorry.\n"
							final_message = total_players + "\n" + "Time: " + duration + rosh_timer_message + "\nSpectators: " + str(spectators) + "\n\n" + match + "\n League ID: " + str(league_id)
							bot.send_message(cid, u"`{final_message}`".format(final_message=final_message), parse_mode="Markdown")
						else:
							bot.reply_to(message, "`This game is still on picking phase, lets wait until it starts!`", parse_mode="Markdown")
						break
				if not found:
					bot.reply_to(message, "`I could not find any game with that ID.\n\nMaybe the game is already finished, try using /dmatch`", parse_mode="Markdown")
		else:
			bot.reply_to(message, "`Follow this command with the ID of a live league game. \n\nUse /dotalive to see the list\n\nExample:\n  /dldetails 2155217045`", parse_mode="Markdown")
