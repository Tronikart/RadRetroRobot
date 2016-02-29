#!/usr/bin/env python
# -*- coding: utf-8 -*-

from utils import *

print "Loading " + __name__ + "..."

# Cat api

@bot.message_handler(commands=['cat'])
def catapi(message):
	if intime(message):
		content = getContent(message)
		if content != "-?":
			cid = getCID(message)
			url = "http://thecatapi.com/api/images/get?format=html&api_key=" + catapi_key
			request = requests.get(url)
			data = re.findall(r'<img[^>]*\ssrc="(.*?)"', request.text)
			data = treatLink(data[0])
			if request.status_code == 200:
				bot.send_message(cid, u'[​]({data})'.format(data=data), parse_mode="Markdown")
			else:
				bot.reply_to(message, "`There has been an error, the number {error} to be specific.`".format(error=request.status_code), parse_mode="Markdown")
		else:
			bot.reply_to(message, "`Send this command alone and I will send you a random cat picture.`", parse_mode="Markdown")
