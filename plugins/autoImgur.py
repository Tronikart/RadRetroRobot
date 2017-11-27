from utils import *

print ('loading ' + __name__)

def getImgur(url):
	url = re.findall(r'(http[s]?://i.imgur.com/.+.gif[v]?)', url)[0]
	request = requests.get(url)
	title = BeautifulSoup(request.text, 'html.parser').title.text
	url = url.replace('gifv', 'mp4').replace('gif', 'mp4')
	return url, title

def action(bot, update):
	cid = getCID(update)
	url, title = getImgur(update.message.text)
	bot.send_document(cid, url, caption=title)

info = {	'triggers' 	:	r'.*http[s]?://i.imgur.com/.+.gif[v]?.*',
			'active'	: 	True,
			'admin'		: 	False}
