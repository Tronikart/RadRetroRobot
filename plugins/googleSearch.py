#!/usr/bin/env python
# -*- coding: utf-8 -*-

from utils import *

print "Loading " + __name__ + "..."
		
# Google search

@bot.message_handler(commands=['g', 'google', 'gnsfw'])
def gsearch(message):
	if intime(message):
		cid = getCID(message)
		safeSearch = True
		if cid != degeneratesgroup:
			command = getCommand(message)
			search = getContent(message)
			if command == 'gnsfw':
				safeSearch = False
			if search != "-?" and search:
				url = "https://ajax.googleapis.com/ajax/services/search/web?v=1.0&rsz=5"
				if safeSearch:
					url = url +  "&safe=active"
				url = url + "&q=" + search
				request = requests.get(url)
				if request.status_code == 200:
					data = request.json()
					if data['responseData'] != None:
						links = ""
						for link in data['responseData']['results']:
							url = treatLink(link['url'])
							title = treatTitle(link['titleNoFormatting'])
							links += u"`> `[{title}]({url})\n".format(url=url, title=title)
						if links:
							bot.reply_to(message,  u"`Results for: \"{query}\"\n`".format(query=search) + links, parse_mode="Markdown", disable_web_page_preview=True)
						else:
							bot.reply_to(message, "`Results not found, if you are trying to google something nsfw, try /gnsfw.`", parse_mode="Markdown")
					else:
						bot.reply_to(message, "`There has been an issue with Google, here's a message from them:\n\n{details}`".format(details=data['responseDetails']), parse_mode="Markdown")
				else:
					bot.send_message(cid, "`There has been an issue with your request, I'm really sorry.`")
			else:
				bot.send_message(cid, "`Follow this command with your search and I will show you some results of said search.\n\nExample:\n  /g robots`", parse_mode="Markdown")
