#!/usr/bin/env python
# -*- coding: utf-8 -*-

from utils import *

print "Loading " + __name__ + "..."

# Lyrics

@bot.message_handler(commands=['lyrics'])
def lyrics(message):
	if intime(message):
		cid = getCID(message)
		search = getContent(message)
		if search and search != "-?":
			search = re.findall(r'(.*\S)\s?-\s?(.*)', search)
			try:
				artist = search[0][0].capitalize()
				song = search[0][1].capitalize()
				url = "https://www.musixmatch.com/lyrics/" + artist.replace("'", "-").replace(" ", "-") + "/" + song.replace("'", "-").replace(" ", "-")
				print url
				bot.send_chat_action(cid, 'typing')
				soup = makesoup(url)
				lyrics = soup.find('span', {'id' : 'lyrics-html'})
				if lyrics == None:
					url = "http://lyrics.wikia.com/wiki/" + artist + ":" + song
					print url
					soup = makesoup(url)
					lyrics = soup.find('div', class_='lyricbox')
					lyrics = lyrics.contents
					lyric = ""
					listlen = len(lyrics)
					for line in lyrics[1:listlen-5]:
					 	if line.string != None:
					 		lyric += line.string
				 		else:
					 		lyric += "\n"
					lyrics = lyric
				else:
					lyrics = lyrics.contents[0]
				if message.chat.type != "private":
					bot.send_message(cid, u"`> {artist} - {song}:\n\n{lyric}\n\n`*I suggest that you use this in private so we dont spam this group*".format(artist=artist, song=song, lyric=lyrics), parse_mode="Markdown")
				else:
					bot.send_message(cid, u"`> {artist} - {song}\n\n{lyric}`".format(artist=artist, song=song, lyric=lyrics), parse_mode="Markdown")
			except:
				bot.reply_to(message, "`Lyric not found, make sure the name of the song is well written and in the correct format\n\n<artist> - <song>.`", parse_mode="Markdown")
		else:
			bot.reply_to(message, "`Follow this message with <artist> - <song> and I will display the lyrics.\n\nI highly advice this to be used on private conversations instead of groups.`", parse_mode="Markdown")
