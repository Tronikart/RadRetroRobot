#!/usr/bin/env python
# -*- coding: utf-8 -*-

from utils import *

print "Loading " + __name__ + "..."

# Comic

@bot.message_handler(commands=['comic','comics'])
def comics(message):
	if intime(message):
		cid = getCID(message)
		content = getContent(message)
		if content != "-?" and content:
			if content:
				content = content.lower()
			if content == "c&h":
				bot.send_message(cid, comic.getCH(), parse_mode="Markdown")
			elif content == "xkcd":
				bot.send_message(cid, comic.getxkcd(), parse_mode="Markdown")
			elif content == "mrlove" or content == "mr lovenstein":
				bot.send_message(cid, comic.getmrlove(), parse_mode="Markdown")
			elif content == "loading artist":
				bot.send_message(cid, comic.getla(), parse_mode="Markdown")
			elif content == "the awkward yeti":
				bot.send_message(cid, comic.gettay(), parse_mode="Markdown")
			elif content == "nerf now":
				bot.send_message(cid, comic.getnn(), parse_mode="Markdown")
			elif content == "heart and brain":
				bot.send_message(cid, comic.gethab(), parse_mode="Markdown")
			elif content == "piecomic":
				bot.send_message(cid, comic.getpieco(), parse_mode="Markdown")
			elif content == "joan cornella":
				bot.send_message(cid, comic.getjoan(), parse_mode="Markdown")
			elif content == "extra fabulous comics" or content == "extrafabulouscomics":
				bot.send_message(cid, comic.getefc(), parse_mode="Markdown")
			elif content == "poorly draw lines":
				bot.send_message(cid, comic.getpld(), parse_mode="Markdown")
			elif content == "optipess":
				bot.send_message(cid, comic.getoptipess(), parse_mode="Markdown")
			else:
				bot.reply_to(message, "Follow your message with one of the following to get a random message from that page:\n  C&H\n  xkcd\n  Mr Lovenstein\n  Loading Artist\n  Heart and brain\n  Awkward yeti\n  Nerf Now\n  piecomic\n  Joan Cornella\n  ExtraFabulousComics\n  Badly Drawn Lines\n  Optipess.`", parse_mode="Markdown")
		elif not content:
			bot.send_message(cid, comic.randomcomic(), parse_mode="Markdown")
		else:
			bot.reply_to(message, "`Send this command by itself and get a random comic from this list: \n  C&H\n  xkcd\n  Mr Lovenstein\n  Loading Artist\n  Heart and brain\n  Awkward yeti\n  Nerf Now\n  piecomic\n  Joan Cornella\n  ExtraFabulousComics\n  Badly Drawn Lines\n  Optipess.`", parse_mode="Markdown")
