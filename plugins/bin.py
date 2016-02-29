#!/usr/bin/env python
# -*- coding: utf-8 -*-

from utils import *

print "Loading " + __name__ + "..."

# Binary

@bot.message_handler(commands=['bin'])
def binarytranslate(message):
	if intime(message):
		content = getContent(message)
		cid = getCID(message)
		if content != "-?" and content:
			content = content.replace(' ', '')
			try:
				if content[0:3] == '-2b':
					result = text_to_bin(content[4:len(content)])
					result = "`{result}`".format(result=result)
				elif content[0:3] == '-2t':
					content = content[4:len(content)]
					result = bin_to_text(content)
					result = "`{result}`".format(result=result)
				else:
					result = "`Please enter a valid option\n\n> -2b to translate to binary.\n> -2t to translate to text.`"
				bot.reply_to(message, result, parse_mode="Markdown")
			except:
				bot.reply_to(message, "`Unexpected error, only ascii characters can be translated to binary, please check your text.`", parse_mode="Markdown")
		else:
			bot.reply_to(message, "`Use this command to translate from binary to text and from text to binary\n\n'/bin -2t' to translate from binary to text\n'/bin -2b' to translate from text to binary `", parse_mode="Markdown")
