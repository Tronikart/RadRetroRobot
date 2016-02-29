#!/usr/bin/env python
# -*- coding: utf-8 -*-

from utils import *

print "Loading " + __name__ + "..."

# CAH SEND

@bot.message_handler(commands=['cartica'])
def cartica(message):
	if intime(message):
		content = getContent(message)
		if content:
			number = str(datetime.now()) + " " + message.from_user.first_name 
			addUser(number, content, "suggestion")

			cahhelp = (u"""Carta añadida, recuerde que para que se adapte al juego, es preferible que siga lo siguiente:\n
						*Placeholders:*
						-An underscore (*_*) indicates where a response fits into a call. Use up to three.
						\t\t\t*Good*: I always say *_* makes a great gift.
						\t\t\t*Good*: *_* is the best thing about *_*.
						\t\t\t*Good*: What makes a great gift? *_*
						\t\t\t*Bad*: What makes a great gift?

						*Capitalization:*
						-Calls: Write as sentences using proper punctuation and capitalization.
						\t\t\t*Good*: The latest Californian fad is *_*.
						\t\t\t*Bad*: the latest Californian fad is *_*.
						\t\t\t*Bad*: The latest californian fad is *_*
						-Responses: Only capitalize proper nouns and generally exclude punctuation.
						\t\t\t*Good*: yoga classes with Batman
						\t\t\t*Bad*: yoga classes with Batman.
						\t\t\t*Bad*: Yoga classes with Batman

						*Phrasing:*
						-Call and response phrasing must match. Ideally, calls should prompt noun-like responses.
						\t\t\t*Bad*: last night we jump up and down.
						\t\t\t*OK*: last night we decided to jump up and down.
						\t\t\t*Best*: last night was full of jumping up and down.
						""")
			if message.chat.type == 'private':
				bot.send_message(message.chat.id, cahhelp, parse_mode="Markdown")
			else:
				bot.reply_to(message, "Por favor haga esto en un chat privado.", parse_mode="Markdown")
		else:
			bot.send_message(message.chat.id, u"`No se registro ninguna carta, por favor escriba su carta luego del comando`",parse_mode="Markdown")

# CAH SHOW

@bot.message_handler(commands=['printcarticas', 'showcarticas'])
def printcartica(message):
	if intime(message):
		if "/printcarticas@radretrorobot " in message.text.lower():
			content = unicode (message.text[29:len(message.text)])
		elif "/printcarticas " in message.text:
			content = unicode(message.text[15:len(message.text)])
		lista =  loadjson("suggestion")
		uid = getUID(message)
		if (uid == 11010564 or uid == adminid):
			wholelist = ""
			for suggestion in lista:
				key = suggestion
				wholelist += "- " + lista[key] + "\n"
			bot.send_message(message.chat.id, u"`{wholelist}`".format(wholelist=wholelist),parse_mode="Markdown")
		else:
			pass

# CAH CLEAN

@bot.message_handler(commands=['cleancarticas'])
def cleancartas(message):
	uid = getUID(message)
	if intime(message):
		if (uid == 11010564 or uid == adminid) and message.chat.type == 'private':
			data = {}
			with open('suggestion.json', 'w') as f:
				json.dump(data, f)
			bot.send_message(message.chat.id, u"`Lista eliminada`",parse_mode="Markdown")
