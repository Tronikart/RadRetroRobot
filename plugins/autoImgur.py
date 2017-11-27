from utils import *

print ('loading ' + __name__)

def getImgur(url):
	url = re.findall(r'(http[s]?://i.imgur.com/.+.gif[v]?)', url)[0].replace('gifv', 'mp4').replace('gif', 'mp4')
	return url

def action(bot, update):
	cid = getCID(update)
	bot.send_document(cid, getImgur(update.message.text))

info = {	'triggers' 	:	r'.*http[s]?://i.imgur.com/.+.gif[v]?.*',
			'active'	: 	True,
			'admin'		: 	False}
