from utils import *

print ('loading ' + __name__)

def action(bot, update):
	cid = getCID(update)
	try:
		url = re.findall(r'(https?://.+\.tumblr\.com/post/.+) ?', update.message.text)[0]
		soup = makesoup(url)
		url = soup.iframe['src']
		soup = makesoup(url)
		video = soup.video.source['src']
		bot.send_document(cid, video)
	except:
		pass

info = {	'triggers' 	:	r'.*https?://.+\.tumblr\.com/post/.+\s?',
			'active'	: 	True,
			'admin'		: 	False}
