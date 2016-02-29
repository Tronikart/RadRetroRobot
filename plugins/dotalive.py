#!/usr/bin/env python
# -*- coding: utf-8 -*-

from utils import *

print "Loading " + __name__ + "..."

# Dota Live League Games

@bot.message_handler(commands=['dotalive', 'dlive'])
def dota_leagues(message):
	if intime(message):
		cid = getCID(message)
		content = getContent(message)
		url = "http://api.steampowered.com/IDOTA2Match_570/GetLiveLeagueGames/v1/?key=" + dota_key + "&format=JSON&language=en_us"
		request = requests.get(url)
		data = request.json()
		if request.status_code == 200:
			games = ""
			total = 10
			if "-full" == content:
				for game in data['result']['games']:
					try:
						radiant = game['radiant_team']['team_name']
						radiant_id = "(" + str(game['radiant_team']['team_id']) + ")"
					except:
						radiant = "Radiant Team"
						radiant_id = ""
					try:
						dire = game['dire_team']['team_name']
						dire_id = "(" + str(game['dire_team']['team_id']) + ")"
					except:
						dire = "Dire Team"
						dire_id = ""
					match_id = game['match_id']
					league_id = game[u'league_id']
					try:
						dire_score = game[u'scoreboard']['dire']['score']
					except:
						dire_score = 0
					dire_score = str(dire_score)
					try:
						radiant_score = game[u'scoreboard']['radiant']['score']
					except:
						radiant_score = 0
					radiant_score = str(radiant_score)
					radiant_total = "{radiant} {radiant_id} {radiant_score}".format(radiant=radiant, radiant_id=radiant_id, radiant_score=radiant_score)
					dire_total = "{dire_score} {dire} {dire_id}".format(dire_score=dire_score, dire_id=dire_id, dire=dire)
					games += "`> {radiant_total} - {dire_total} \n\t\t\t Match ID: {match_id} - League ID: {league_id}`\n".format(radiant_total=radiant_total, dire_total=dire_total, match_id=match_id, league_id=league_id)
				bot.send_message(cid, "`These are the Live League Games currently: `\n" + games, parse_mode="Markdown")
			elif content == "-?":
				bot.reply_to(message, "`Send this command alone to get 10 Dota 2 Live Tournament games, send it with -full after the command to get the full list.`", parse_mode="Markdown")
			else:
				for game in data['result']['games']:
					if total > 0:
						try:
							radiant = game['radiant_team']['team_name']
							radiant_id = "(" + str(game['radiant_team']['team_id']) + ")"
						except:
							print 
							radiant = "Radiant Team"
							radiant_id = ""
						try:
							dire = game['dire_team']['team_name']
							dire_id = "(" + str(game['dire_team']['team_id']) + ")"
						except:
							dire = "Dire Team"
							dire_id = ""
						match_id = game['match_id']
						league_id = game[u'league_id']
						try:
							dire_score = game[u'scoreboard']['dire']['score']
						except:
							dire_score = 0
						dire_score = str(dire_score)
						try:
							radiant_score = game[u'scoreboard']['radiant']['score']
						except:
							radiant_score = 0
						radiant_score = str(radiant_score)
						radiant_total = "{radiant} {radiant_id} {radiant_score}".format(radiant=radiant, radiant_id=radiant_id, radiant_score=radiant_score)
						dire_total = "{dire_score} {dire} {dire_id}".format(dire_score=dire_score, dire_id=dire_id, dire=dire)
						games += "`> {radiant_total} - {dire_total} \n\t\t\t Match ID: {match_id} - League ID: {league_id}`\n".format(radiant_total=radiant_total, dire_total=dire_total, match_id=match_id, league_id=league_id)
					total -= 1
				bot.send_message(cid, "`These are the Live League Games currently: `\n" + games + "`\n\nSend your commmand as /dlive -full to get the full list of content.`", parse_mode="Markdown")
		else:
			bot.reply_to(message, "`There has been an error, the number {error} to be specific.`".format(error=request.status_code), parse_mode="Markdown")