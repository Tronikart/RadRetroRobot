#!/usr/bin/env python
# -*- coding: utf-8 -*-

from utils import *

print "Loading " + __name__ + "..."

# Dota Update

@bot.message_handler(commands=['dotanews', 'dotanew', 'dnews', 'dnew'])
def dota_news(message):
	if intime(message):
		cid = getCID(message)
		content = getContent(message)
		url = "http://api.steampowered.com/ISteamNews/GetNewsForApp/v0002/?appid=570&count=3&maxlength=300&format=json"
		request = requests.get(url)
		data = request.json()
		if content != "?":
			if request.status_code == 200:
				title = data['appnews']['newsitems'][0]['title']
				content = data['appnews']['newsitems'][0]['contents']
				url = data['appnews']['newsitems'][0]['url']
				bot.send_message(cid, u'`> {title}\n\n{content}\n\n`'.format(title=title, content=content) + '[More info here]({url})'.format(url=url), parse_mode="Markdown", disable_web_page_preview=True)
			else:
				bot.reply_to(message, "`There has been an error, the number {error} to be specific.`".format(error=request.status_code), parse_mode="Markdown")
		else:
			bot.reply_to(message, "`Send this command alone and I will show you the last Dota 2 blog entry`", parse_mode="Markdown")
