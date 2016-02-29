#!/usr/bin/env python
# -*- coding: utf-8 -*-

from utils import *

print "Loading " + __name__ + "..."

# diceroll

@bot.message_handler(commands=['diceroll'])
def dice_roll(message):
	if intime(message):
		faces = getContent(message)
		cid = getCID(message)
		if faces != "-?" or not faces:
			if faces == "4" or faces == "d4":
				roll = random.randrange(1, 5, 1)
				bot.send_message(cid, "`" + str(roll) + "`", parse_mode="Markdown")
			elif faces == "6" or faces == "d6" or not faces:
				roll = random.randrange(1, 7, 1)
				bot.send_message(cid, "`" + str(roll) + "`", parse_mode="Markdown")
			elif faces == "8" or faces == "d8":
				roll = random.randrange(1, 9, 1)
				bot.send_message(cid, "`" + str(roll) + "`", parse_mode="Markdown")
			elif faces == "10" or faces == "d10":
				roll = random.randrange(1, 11, 1)
				bot.send_message(cid, "`" + str(roll) + "`", parse_mode="Markdown")
			elif faces == "12" or faces == "d12":
				roll = random.randrange(1, 13, 1)
				bot.send_message(cid, "`" + str(roll) + "`", parse_mode="Markdown")
			elif faces == "20" or faces == "d20":
				roll = random.randrange(1, 21, 1)
				bot.send_message(cid, "`" + str(roll) + "`", parse_mode="Markdown")
			else:
				roll = random.randrange(1, 7, 1)
				bot.send_message(cid, "`No valid dice detected, rolling a 6d:\n\n    " + str(roll) + "\n\n/diceroll -?`", parse_mode="Markdown")
		else:
			bot.reply_to(message, "`Valid dices:\nd4\nd6\nd10\nd12\nd20\n\n  /diceroll d20`", parse_mode="Markdown")
