from utils import *

print ('loading ' + __name__)

def action(bot, update):
	cid = getCID(update)
	try:
		url, url2, url3, title = getGfy(update.message.text)
		# Thank you telegram for making me do this
		# Fix your documentation please
		if title:
			try:
				bot.send_document(cid, url, caption=title)
			except:
				try:
					bot.send_document(cid, url2, caption=title)
				except:
					bot.send_document(cid, url3, caption=title)

		else:
			try:
				bot.send_document(cid, url)
			except:
				try:
					bot.send_document(cid, url2)
				except:
					bot.send_document(cid, url3)
	except:
		pass

info = {	'triggers' 	:	r'.*gfycat\.com.*',
			'active'	: 	True,
			'admin'		: 	False}