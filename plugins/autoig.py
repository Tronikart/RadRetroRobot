from utils import *

print ('loading ' + __name__)

def action(bot, update):
	cid = getCID(update)
	try:
		url = re.findall(r'https.*instagram.com/p/[a-zA-Z0-9]+/', update.message.text)[0]
		soup = makesoup(url)
		for script in soup.find_all('script'):
			if re.findall(r'display_url\":\"([a-zA-Z/:0-9-._]*)' , script.text.replace('window._sharedData = ', '')[:-1]):
				unique_urls = list(set(re.findall(r'display_url\":\"([a-zA-Z/:0-9-._]*)' , script.text.replace('window._sharedData = ', '')[:-1])))
				break
			else:
				pass
		urls = []
		for url in unique_urls:
			urls.append({'url':url, 'caption': ""})
		photos, videos = urlsForAlbum(urls)
		print(photos)
		sendAlbums("photo", photos, cid)
	except:	
		pass

info = {	'triggers' 	:	r'.*http[s]?.*instagram.com/p/[a-zA-Z0-9]+/',
			'active'	: 	True,
			'admin'		: 	False}
