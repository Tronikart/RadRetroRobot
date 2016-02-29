#!/usr/bin/env python
# -*- coding: utf-8 -*-

from utils import *

print "Loading " + __name__ + "..."

# Urban Dictionary definitions

@bot.message_handler(commands=['ud'])
def ud(message):
	if intime(message):
		cid = getCID(message)
		isSearch = False
		if not cid == degeneratesgroup:
			search = getContent(message)
			if search != "-?" and search:
				url = "http://api.urbandictionary.com/v0/define?term=" + search
				request = requests.get(url)
				if request.status_code == 200:
					data = request.json()
					if data['result_type'] == 'exact':
						if len(data['list'][0]['definition']) < 1000:
							definition = data['list'][0]['definition']
							definition = definition.replace("`", "'")
							example = "Example:\n" + data['list'][0]['example']
						else:
							definition = "Some idiot thought it was a nice idea to write a wall of text as definition, please refer to the link below.\n"
							example = ""
						permalink = data['list'][0]['permalink']
						word = data['list'][0]['word']
						definition = unicode(definition.rstrip('].').lstrip('['))
						message_ub = u"[" + word + "](" + permalink + ")\n\n`" + definition + "\n\n" + example + "`"
						bot.send_message(cid, message_ub, parse_mode="Markdown", disable_web_page_preview=True)
					else:
						bot.send_message(cid, u"`No results found for {search}.`".format(search=search), parse_mode="Markdown")
				else:
					bot.send_message(cid, '`{error}`'.format(error=data.raise_for_status()), parse_mode="Markdown")
			else:
				bot.send_message(cid, "`Follow this command with your search and I will show you the definition of it.\n\nExample:\n  /ud Robot`", parse_mode="Markdown")
