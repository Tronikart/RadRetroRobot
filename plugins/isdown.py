#!/usr/bin/env python
# -*- coding: utf-8 -*-

from utils import *

print "Loading " + __name__ + "..."

# Is it down

@bot.message_handler(commands=['isdown'])
def isdown(message):
	if intime(message):
		cid = getCID(message)
		page = getContent(message)
		if page != "-?" and page:
			page = page.replace("http://", "").replace("https://", "")
			url = "http://downornotworking.com/" + page
			soup = makesoup(url)
			down = soup.findAll('div', class_='col-md-8')
			down = down[1]
			if down.span.text.replace("\n", "").replace(" ", "") == "ok":
				lastping = "\n" + down.contents[-2].text.split(".")[-3]
				avgping = "\n" + down.contents[-2].text.split(".")[-2]
			else:
				lastping = ""
				avgping = ""
			down = down.span.text.replace("\n", "").replace(" ", "")
			down = down + lastping + avgping
			bot.send_message(cid, "`" + page + " is currently " + down + "`", parse_mode="Markdown")
		else:
			bot.reply_to(message, "`Follow this command with an URL to know if its down for everyone or its just you\n\nExample:\n  /isdown google.com`", parse_mode="Markdown")
