from utils import *

print ('loading ' + __name__)

def action(bot, update, args):
	query = ' '.join(args)
	cid = getCID(update)
	if query:
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
			content = wikipedia.summary(query)
			result = u"[​](" + image + ")` > " + title + "\n\n" + content + "`\n\n[More information](" + url + ")"
			if image:
				bot.send_message(cid, result, parse_mode="Markdown")
			else:
				bot.send_message(cid, result, parse_mode="Markdown", disable_web_page_preview=True)
		except wikipedia.exceptions.DisambiguationError as disambiguation:
			bot.send_chat_action(cid, 'typing') 
			result = query + " may refer to:\n"
			for option in disambiguation.options[0:10]:
				result += "  " + option + "\n"
			update.message.reply_text("`" + result + "`", parse_mode="Markdown", reply_to_message_id = update.message.message_id)
		except wikipedia.exceptions.PageError:
			result = "`Sorry, I could not find any result.`"
			update.message.reply_text(result, parse_mode="Markdown", reply_to_message_id = update.message.message_id)
	elif query == "-random":
		bot.send_chat_action(cid, 'typing') 
		random = wikipedia.random(pages=10)
		result = ""
		for page in random:
			result += "  " + page + "\n"
		result = "`10 random pages:\n" + result + "`"
		bot.send_message(cid, result, parse_mode="Markdown")
	else:
		update.message.reply_text("`Follow this command with your search, then I will print resumed info if the search finds results.\nSen /wiki -random to get 10 random page titles\n\nExample:\n  /wiki robot`", parse_mode="Markdown", reply_to_message_id = update.message.message_id)

info = {	'triggers'	: 	('wiki', 'wikipedia', 'w'),
			'name'		:	'Wikipedia',
			'help'		: 	"Follow this command with your search, then I will print resumed info if the search finds results.\nSen /wiki -random to get 10 random page titles",
			'example'	:	'/wiki robot',
			'active'	: 	True,
			'admin'		: 	False,
			'arguments' :	"<search>"}