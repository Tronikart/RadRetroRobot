from utils import *

print ('loading ' + __name__)

def action(bot, update):
	cid = getCID(update)
	url, title = getImgur(update.message.text)
	bot.send_document(cid, url, caption=title)

info = {	'triggers' 	:	r'.*http[s]?://i.imgur.com/.+.gif[v]?.*',
			'active'	: 	True,
			'admin'		: 	False}

			