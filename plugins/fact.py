#!/usr/bin/env python
# -*- coding: utf-8 -*-

from utils import *

print "Loading " + __name__ + "..."

# Facts

@bot.message_handler(commands=['fact'])
def fact(message):
	if intime(message):
		cid = getCID(message)
		content = getContent(message)
		if content != "-?":
			request = requests.get("http://freehostedscripts.net/fq.php")
			url = "http://freehostedscripts.net/fq.php"
			if request.status_code == 200:
				soup = makesoup(url)
				fact = re.findall(r'("{1}.*)+(Interesting Facts)', soup.get_text())
				fact = fact[0][0] + '"'
				fact = unicode(fact)
				try:
					bot.send_message(cid, u"`{fact}`".format(fact=fact), parse_mode="Markdown")
				except:
					bot.send_message(cid, u"`This in fact, is not a fact, something went wrong, please try again.`", parse_mode="Markdown")
			else:
				bot.reply_to(message, "`There has been an error, the number {error} to be specific.`".format(error=request.status_code), parse_mode="Markdown")
		else:
			bot.reply_to(message, "`Send this command alone and I will send you a random fact.`", parse_mode="Markdown")
