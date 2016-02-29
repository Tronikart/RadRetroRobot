#!/usr/bin/env python
# -*- coding: utf-8 -*-

from utils import *

print "Loading " + __name__ + "..."

# Calc

@bot.message_handler(commands=['calc', 'c'])
def calc(message):
	if intime(message):
		cid = getCID(message)
		uName = (message.from_user.first_name)
		error = False
		exp = getContent(message)
		if exp != "-?" and exp:
			payload = {
				'expr': exp,
				'precision': 5
			}
			url = "http://api.mathjs.org/v1/"
			request = requests.get(url, params=payload)
			if request.status_code == 200:
				result_str = "`Result:\n  {data}`"
				result_str = str(result_str)
				data = request.text
				bot.send_message(cid, result_str.format(data=data), parse_mode="Markdown")
			else:
				error_message = "`Theres has been an error, here's some information to help you fix it:\n\n{error}`"
				bot.send_message(cid, error_message.format(error=request.text), parse_mode="Markdown")
		else:
			bot.send_message(cid, "`Please enter your expression after the command to get the result\n\nExample:\n  /calc 2 + 2`", parse_mode="Markdown")
