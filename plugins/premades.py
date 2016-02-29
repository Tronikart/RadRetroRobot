#!/usr/bin/env python
# -*- coding: utf-8 -*-

from utils import *

print "Loading " + __name__ + "..."

@bot.message_handler(commands=['premades'])
def prem(message):
	if intime(message):
		cid = getCID(message)
		bot.send_message(cid, text_messages['premade'])

#	Excelente meme

@bot.message_handler(commands=['ememe', 'em'])
def prem_ememe(message):
	if intime(message):
		cid = getCID(message)
		try:
			rid = message.reply_to_message
			bot.reply_to(rid, premade['ememe'], parse_mode="Markdown")
		except:
			bot.send_message(cid, premades['ememe'], parse_mode="Markdown")

# Nice Meme

@bot.message_handler(commands=['nmeme', 'nm'])
def prem_nmeme(message):
	if intime(message):
		cid = getCID(message)
		try:
			rid = message.reply_to_message
			bot.reply_to(rid, premade['nmeme'], parse_mode="Markdown")
		except:
			bot.send_message(cid, premades['nmeme'],parse_mode="Markdown")

# Thanks

@bot.message_handler(commands=['thanks'])
def say_thanks(message):
	if intime(message):
		if message.from_user.id == adminid:
			try:
				rid = message.reply_to_message
				bot.reply_to(rid, "`We both thank you and love you!`", parse_mode="Markdown")
			except:
				pass
		else:
			pass