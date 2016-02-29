#!/usr/bin/env python
# -*- coding: utf-8 -*-

from utils import *

print "Loading " + __name__ + "..."

# Roll

@bot.message_handler(commands=['roll'])
def roll_number(message):
	if intime(message):
		cid = getCID(message)
		number = getContent(message)
		if number and number != '-?':
			options = number.split('\n')
			nb = re.findall(r'(\d+)\s?-?\s?(\d+)\s?-?|(\d+)\s?-?', number)
			nb = nb[0]
			if nb[2]:
				rollfrom = 1
				rollto = int(nb[2]) + 1
				roll = random.randrange(rollfrom, rollto, 1) if rollfrom < rollto else random.randrange(rollto, rollfrom, 1)
			elif nb[0] and nb[1]:
				rollfrom = int(nb[0])
				rollto = int(nb[1]) + 1
				roll = random.randrange(rollfrom, rollto, 1) if rollfrom < rollto else random.randrange(rollto, rollfrom, 1)
			else:
				bot.reply_to(message, "`Invalid form of range, send either\n\n  /roll <min> <max>\n  /roll <max>\n  /roll <min> - <max>\n\nFor option selection, input them this way:\n  /roll [min] <max> -\n  <Option1>\n  <Option2>`", parse_mode="Markdown")
			if len(options) > 1:
				options = options[1:len(options)]
				if rollto-1 == len(options):
					roll = options[roll-1]

					bot.reply_to(message, "`" + str(roll) + "`", parse_mode="Markdown")
				else:
					bot.reply_to(message, "`Send a range that matches the number of options`", parse_mode="Markdown")
			else:
				bot.reply_to(message, "`" +  str(roll) + "`", parse_mode="Markdown")
		elif number == "-?":
			bot.reply_to(message, "`Send this command alone to get a random number from 1 to 100, send it with either a range or a number to set a new range`", parse_mode="Markdown")
		else:
			roll = random.randrange(100)
			bot.reply_to(message, "`" + str(roll) + "`", parse_mode="Markdown")
