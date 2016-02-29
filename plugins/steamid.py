#!/usr/bin/env python
# -*- coding: utf-8 -*-

from utils import *

print "Loading " + __name__ + "..."

# Steam game ID

@bot.message_handler(commands=['steamid'])
def steam_id(message):
	if intime(message):
		name = getContent(message)
		if name and name != "-?":
			name = unicode(name)
			cid = getCID(message)
			url = "http://api.steampowered.com/ISteamApps/GetAppList/v2/?key=" + dota_key + "&format=JSON&language=en_us"
			request = requests.get(url)
			data = request.json()
			bot.send_chat_action(cid, 'typing') 
			found = False
			if request.status_code == 200:
				for app in data['applist']['apps']:
					if app['name'].lower() == name.lower():
						appid = app['appid']
						url = "http://store.steampowered.com/app/" + unicode(appid) + "/"
						bot.send_message(cid, u"`{name}: {appid}\n/steampage <ID>\n/steamdetails <ID>\n/steamnews <ID>`".format(appid=appid, name=name) + u"\n\n[Store Link]("+url+")", parse_mode="Markdown", disable_web_page_preview=True)
						found = True
						break
				if not found:					
					bot.send_message(cid, "`I did not find {name} on steams app list`".format(name=name), parse_mode="Markdown")
			else:
				bot.reply_to(message, "`There has been an error, the number {error} to be specific.`".format(error=request.status_code), parse_mode="Markdown")
		else:
			bot.reply_to(message, "`Follow this command with the name of a steam game and I will give you its ID, useful to use along with\n\n/steamnews\n/steampage\n\nExample:\n  /steamid Dota 2`", parse_mode="Markdown")
