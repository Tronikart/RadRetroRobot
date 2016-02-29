#!/usr/bin/env python
# -*- coding: utf-8 -*-

from utils import *

print "Loading " + __name__ + "..."

# Last FM Top 5

@bot.message_handler(commands=['fmtop'])
def top_artist_fm(message):
	if intime(message):
		cid = unicode(message.chat.id)
		uid = unicode(message.from_user.id)
		fmUsers = loadjson("fmuser")
		isUser = False
		content = getContent(message)
		if uid in fmUsers:
			isUser = True
		else:
			bot.reply_to(message, "`Please set your username with /fmuser, preferably from PM.`", parse_mode="Markdown")
		if isUser and content != "-?":
			url = "http://ws.audioscrobbler.com/2.0/?method=user.getTopArtists&format=json&user=" + fmUsers[uid] + "&api_key=" + lastfm_key + "&period=7day&limit=5"
			request = requests.get(url)
			data = request.json()
			artists = ""
			if request.status_code == 200:
				try:
					if data['topartists']['@attr']['totalPages'] != "0":
						i = 0
						artists = ""
						for artist in data['topartists']['artist']:
							artist_name = unicode(artist['name'])
							playcount = unicode(artist['playcount'])
							artists += u"`> {artist} - {playcount}` \n".format(artist=artist_name, playcount=playcount)
							i += 1
						if i > 1:
							artist = "artist"
						else:
							aritst = "artists"
						bot.reply_to(message, u"`{name}'s last week Top {playcount} {artist} and its playcount:` \n".format(artist=artist, name=message.from_user.first_name, playcount=i) + artists, parse_mode="Markdown")
					else: 
						bot.reply_to(message, "`Theres has been an error, I found no information from your user.`", parse_mode="Markdown")
				except:
					bot.reply_to(message, "`Theres has been an error, I found no information from your user.`", parse_mode="Markdown")
			else:
				bot.reply_to(message, "`Theres has been an error, heres some info from lastfm: {error}`".format(error=data['message']), parse_mode="Markdown")
		else:
			bot.reply_to(message, "`Send this command after setting up your user with /fmuser to show your top 5 artists from last week`", parse_mode="Markdown")
