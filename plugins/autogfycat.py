from utils import *

print ('loading ' + __name__)

def action(bot, update):
	cid = getCID(update)
	try:
		bot.send_document(cid, getGfy(update.message.text))
	except:
		pass

info = {	'triggers' 	:	r'.+gfycat.com.+',
			'active'	: 	True,
			'admin'		: 	False}