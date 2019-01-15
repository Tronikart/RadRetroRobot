from utils import *

print ('loading ' + __name__)

def action(bot, update, args):
	cid = getCID(update)
	search = ' '.join(args)
	if search:
		url = "http://api.urbandictionary.com/v0/define?term=" + search
		request = requests.get(url)
		if request.ok:
			data = request.json()
			if data['list']:
				if len(data['list'][0]['definition']) < 1000:
					definition = data['list'][0]['definition'].replace("`", "'")
					example = f"Example:\n{data['list'][0]['example']}"
				else:
					definition = "Some idiot thought it was a nice idea to write a wall of text as definition, please refer to the link below.\n"
					example = ""
				permalink = data['list'][0]['permalink']
				word = data['list'][0]['word']
				definition = definition.rstrip('].').lstrip('[')
				message_ub = f"[{word}]({permalink})\n\n`{definition}\n\n{example}`"
				bot.send_message(cid, message_ub, parse_mode="Markdown", disable_web_page_preview=True)
			else:
				bot.send_message(cid, f"`No results found for {search}.`", parse_mode="Markdown")
		else:
			bot.send_message(cid, '`There has been an error, please wait before trying again.`', parse_mode="Markdown")
	else:
		bot.send_message(cid, "`Follow this command with your search and I will show you the definition of it.\n\nExample:\n  /ud Robot`", parse_mode="Markdown")

info = {	'triggers'	: 	('ud', 'urbandictionary'),
			'name'		:	'Urban Dictionary',
			'help'		: 	"Follow this command with your search and I will show you the definition of it.",
			'example'	:	'/ud Robot',
			'active'	: 	True,
			'admin'		: 	False,
			'arguments' :	""}
