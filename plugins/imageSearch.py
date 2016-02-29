#!/usr/bin/env python
# -*- coding: utf-8 -*-

from utils import *

print "Loading " + __name__ + "..."

# Google Images Search

@bot.message_handler(commands=['i', 'insfw', 'image'])
def isearch(message):
	if intime(message):
		cid = getCID(message)
		search = getContent(message)
		command = getCommand(message)
		if command == 'insfw':
			safeSearch = True
		else:
			safeSearch = False
		if search != "-?" and search:
			url = ("https://www.googleapis.com/customsearch/v1?&searchType=image&imgSize=xlarge&alt=json&num=8&start=1&key=" + google_img_key + "&cx=017597791379160176083:kooipmedh98&q=")
			url = url + search
			if not safeSearch:
				url = url + "&safe=high"
			request = requests.get(url)
			if request.status_code == 200:
				try:
					if not safeSearch:
						data = request.json()
						link = data['items'][random.randrange(0, 7)]['link']
						link = treatLink(link)
						bot.send_message(cid, u"[​]({link})".format(link=link), parse_mode="Markdown")
					else:
						data = request.json()
						link = data['items'][random.randrange(0, 7)]['link']
						link = treatLink(link)
						bot.send_message(cid, u"[​]({link})".format(link=link), parse_mode="Markdown")
				except:
					bot.reply_to(message, "`Oops! Something went wrong, if you are trying to google something nsfw, try /insfw.`", parse_mode="Markdown")
			elif request.status_code == 403:
				bot.reply_to(message, "`Sorry, the daily limit for images search has been reached, blame Google for this.`", parse_mode="Markdown")
			else:
				bot.reply_to(message, "`There has been an error, the number {error} to be specific.`".format(error=request.status_code), parse_mode="Markdown")
		else:
			bot.send_message(cid, "`Follow this command with your search and I will get you an image.\n\nExample:\n  /i shiny robot`", parse_mode="Markdown")
