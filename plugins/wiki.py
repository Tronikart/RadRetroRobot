#!/usr/bin/env python
# -*- coding: utf-8 -*-

from utils import *

print "Loading " + __name__ + "..."

# Wiki

@bot.message_handler(commands=['wiki'])
def wiki_plug(message):
	if intime(message):
		query = getContent(message)
		cid = getCID(message)
		if getContent(message) and query != "-?" and query != "-random":
			result = ""
			try:
				bot.send_chat_action(cid, 'typing') 
				search = wikipedia.page(query)
				title = search.title
				image = ""
				for link in search.images:
					if link.split('.')[-1] != 'svg':
						image = treatLink(link)
						break
				url = (search.url)
				content = wikipedia.summary(query, sentences=3)
				result = u"[​](" + image + ")` > " + title + "\n\n" + unicode(content) + "`\n\n[More information](" + url + ")"
				if image:
					bot.send_message(cid, unicode(result), parse_mode="Markdown")
				else:
					bot.send_message(cid, unicode(result), parse_mode="Markdown", disable_web_page_preview=True)
			except wikipedia.exceptions.DisambiguationError as disambiguation:
				bot.send_chat_action(cid, 'typing') 
				result = query + " may refer to:\n"
				for option in disambiguation.options[0:10]:
					result += "  " + option + "\n"
				bot.reply_to(message, "`" + unicode(result) + "`", parse_mode="Markdown")
			except wikipedia.exceptions.PageError:
				result = "`Sorry, I could not find any result.`"
				bot.reply_to(message, result, parse_mode="Markdown")
		elif query == "-random":
			bot.send_chat_action(cid, 'typing') 
			random = wikipedia.random(pages=10)
			result = ""
			for page in random:
				result += "  " + page + "\n"
			result = "`10 random pages:\n" + result + "`"
			bot.send_message(cid, result, parse_mode="Markdown")
		else:
			bot.reply_to(message, "`Follow this command with your search, then I will print resumed info if the search finds results.\nSen /wiki -random to get 10 random page titles\n\nExample:\n  /wiki robot`", parse_mode="Markdown")
