from utils import *

print ('loading ' + __name__)

def action(bot, update):
	cid = getCID(update)
	try:
		url = re.findall(r'(.+)media[2]?(.giphy.com/media/.+/giphy).+', update.message.text)[0]
		url = url[0] + "i" + url[1] + ".mp4"
		bot.send_document(cid, url)
	except:
		pass

info = {	'triggers' 	:	r'.+media[2]?.giphy.com/media/.+/giphy.+',
			'active'	: 	True,
			'admin'		: 	False}