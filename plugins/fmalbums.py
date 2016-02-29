#!/usr/bin/env python
# -*- coding: utf-8 -*-

from utils import *

print "Loading " + __name__ + "..."

# Last FM Top albums

@bot.message_handler(commands=['fmalbums'])
def top_album_fm(message):
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
			url = "http://ws.audioscrobbler.com/2.0/?method=user.getTopAlbums&format=json&user=" + fmUsers[uid] + "&api_key=" + lastfm_key + "&limit=5&period=7day"
			request = requests.get(url)
			data = request.json()
			artists = ""
			if request.status_code == 200:
				if data['topalbums']['@attr']['totalPages'] != "0":
					i = 0
					artists = ""
					for album in data['topalbums']['album']:
						album_name = unicode(album['name'])
						playcount = unicode(album['playcount'])
						artist_name = unicode(album['artist']['name'])
						artists += u"`> {artist} - {album} - {playcount}` \n".format(artist=artist_name, playcount=playcount, album=album_name)
						i += 1
					if i > 1:
						artist = "album"
					else:
						aritst = "albums"
					bot.reply_to(message, u"`{name}'s last week Top {playcount} {artist} and its playcount:` \n".format(artist=artist, name=message.from_user.first_name, playcount=i) + artists, parse_mode="Markdown")
				else: 
					bot.reply_to(message, "`Theres has been an error, I found no information from your user.`", parse_mode="Markdown")
			else:
				bot.reply_to(message, "`Theres has been an error, heres some info from lastfm: {error}`".format(error=data['message']))
		else:
			bot.reply_to(message, "`Send this command after setting up your user with /fmuser to show your top 5 album from last week`", parse_mode="Markdown")
