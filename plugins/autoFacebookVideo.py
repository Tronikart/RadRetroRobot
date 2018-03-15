from utils import *

print ('loading ' + __name__)

def action(bot, update):
	cid = getCID(update)
	token = getFBToken()
	try:
		request_url = 'https://graph.facebook.com/'
		url = re.findall(r'(.*http[s]?://www.facebook.com/(groups|.*)/(videos|\S.+)/\d.+/.*)', update.message.text)[0][0]

		# Getting the post ID from either a /video/ url or a /groups/ url
		media_id = url.split('/')[5] if url.split('/')[4] == "videos" else url.split('/')[6]

		request = requests.get(request_url + media_id, {'access_token': token, 'fields' : 'source'})
		mp4url = request.json()['source']
		bot.send_document(cid, mp4url)
	except Exception as e:
		raise e
	

info = {	'triggers' 	:	r'.*http[s]?://www.facebook.com/(groups|.*)/(videos|\S.+)/\d.+/.*',
			'active'	: 	True,
			'admin'		: 	False}
