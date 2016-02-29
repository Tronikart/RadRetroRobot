#!/usr/bin/env python
# -*- coding: utf-8 -*-

from utils import *

print "Loading " + __name__ + "..."

# Last FM Now playing

@bot.message_handler(commands=['np'])
def nowplaying(message):
	if intime(message):
		uid = unicode(message.from_user.id)
		fmUsers = loadjson("fmuser")
		isUser = False
		content = getContent(message)
		if uid in fmUsers:
			isUser = True
		else:
			#bot.reply_to(message, "`Please set your username with /fmuser, preferably from PM.`", parse_mode="Markdown")
			pass
		if isUser and content != "-?":
			url = "http://ws.audioscrobbler.com/2.0/?method=user.getRecentTracks&format=json&user=" + fmUsers[uid] + "&api_key=" + lastfm_key + "&limit=1"
			request = requests.get(url)
			data = request.json() 
			if request.status_code == 200:
				try:
					artist = data['recenttracks']['track'][0]['artist']['#text']
					song = data['recenttracks']['track'][0]['name']
					album = data['recenttracks']['track'][0]['album']['#text']
					if '@attr' in data['recenttracks']['track'][0]:
						bot.reply_to(message, u"`> {user} is currently listening:\nsong: {song}\nartist: {artist}\nalbum: {album}\n\t\t\t\t\t\t\t\t♪   ♫   ♪   ♫`".format(user=message.from_user.first_name, song=song, artist=artist, album=album), parse_mode="Markdown")
					else:
						bot.reply_to(message, u"`> {user} listened to:\nsong: {song}\nartist: {artist}\nalbum: {album}\n\t\t\t\t\t\t\t\t♫   ♪   ♫   ♪`".format(user=message.from_user.first_name, song=song, artist=artist, album=album), parse_mode="Markdown")
				except:
					bot.reply_to(message, "`Theres has been an error, please verify that your username is valid`", parse_mode="Markdown")
			else:
				bot.reply_to(message, "`Theres has been an error, heres some info from lastfm: {error}`".format(error=data['message']), parse_mode="Markdown")
		else:
			bot.reply_to(message, "`Send this command after setting up your user with /fmuser to show what you are currently listening to`", parse_mode="Markdown")
