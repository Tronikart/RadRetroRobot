from utils import *

print ('loading ' + __name__)

def action(bot, update):
	print("beep")
	cid = getCID(update)
	try:
		cid = getCID(update)
		url = re.findall(r'(http[s]?://www.facebook.com/.*/videos/\d.+[/\S+]?)', update.message.text)[0]
		url = url.replace('www', 'm')
		soup = makesoup(url)
		for link in soup.find_all('a'):
			if "/video" in link['href']:
				mp4url = link['href']
				break
    
    # I know this looks ugly
		mp4url = re.findall(r'src=(.*)$', mp4url)[0].replace('%3A', ':').replace('%2F', '/').replace('%3F', '?').replace('%3D', '=').replace('%26', '&')
		bot.send_document(cid, mp4url)
	except:
		pass

info = {	'triggers' 	:	r'.*http[s]?://www.facebook.com/.*/videos/\d.+/.*',
			'active'	: 	True,
			'admin'		: 	False}

