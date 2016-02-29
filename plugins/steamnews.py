#!/usr/bin/env python
# -*- coding: utf-8 -*-

from utils import *

print "Loading " + __name__ + "..."

# Get Steam News

@bot.message_handler(commands=['steamnews'])
def steam_news(message):
	if intime(message):
		cid = getCID(message)
		steamid = getContent(message)
		if steamid and steamid != "-?":
			url = "http://api.steampowered.com/ISteamNews/GetNewsForApp/v0002/?appid=" + steamid + "&count=3&maxlength=300&format=json"
			request = requests.get(url)
			data = request.json()
			if request.status_code == 200:
				title = data['appnews']['newsitems'][0]['title']
				content = data['appnews']['newsitems'][0]['contents']
				links = re.findall(r'<a[^>]*\shref="(.*?)"', content)
				for link in links:
					content = content.replace(link, "")
					content = content.replace('<', "")
					content = content.replace('>', "")
					content = content.replace('href=""', "")
				url = data['appnews']['newsitems'][0]['url']
				bot.send_message(cid, u'`> {title}\n\n{content}\n\n`'.format(title=title, content=content) + '[More info here]({url})'.format(url=url), parse_mode="Markdown", disable_web_page_preview=True)
			else:
				bot.reply_to(message, "`There has been an error, the number {error} to be specific.`".format(error=request.status_code), parse_mode="Markdown")
		else:
			bot.reply_to(message, "`Follow this command with the ID of a steam game and I will give you the last posted new, use /steamid if you dont know the ID of your game\n\nExample:\n  /steamnews 570`",parse_mode="Markdown")
