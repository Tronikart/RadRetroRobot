#!/usr/bin/env python
# -*- coding: utf-8 -*-

from utils import *

print "Loading " + __name__ + "..."

# Dota Streams

@bot.message_handler(commands=['dotastreams', 'dstreams'])
def dota_streams(message):
	if intime(message):
		content = getContent(message)
		cid = getCID(message)
		if content != "-?":
			url = "http://www.gosugamers.net/dota2/streams"
			soup = makesoup(url)
			streams = soup.findAll("a", class_="box-item-overlay news-overlay")
			streamlist = ""
			for stream in streams:
				channel = stream.find('label', class_="channel")
				channel = channel.string
				channel = treatTitle(channel.replace("\n",""))
				streamurl = stream.attrs['href']
				streamurl = "http://www.gosugamers.net/" + streamurl
				streamlist += "`> `" + "[" + channel + "]" + "(" + streamurl + ")" + "\n"
			final_message = "`These are the available streams:`\n\n" + streamlist
			bot.send_message(cid, final_message, parse_mode="Markdown")
		else:
			bot.reply_to(message, "`Send this command alone and I will show you the list of streams currently available`", parse_mode="Markdown")

