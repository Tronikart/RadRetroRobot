from utils import *

print ('loading ' + __name__)

def action(bot, update):
	cid = getCID(update)
	try:
		url, title = getGfy(update.message.text)
		bot.send_document(cid, url, caption=title)
	except:
		pass

info = {	'triggers' 	:	r'.+gfycat.com.+',
			'active'	: 	True,
			'admin'		: 	False}
