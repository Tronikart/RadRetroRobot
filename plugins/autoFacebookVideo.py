from pprint import pprint
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
		if url[-2:] != "-f":
			bot.send_document(cid, mp4url, reply_to_message_id=update.message.message_id)
		else:
			bot.send_message(cid, "[direct link](" + mp4url + ")", parse_mode="Markdown", disable_web_page_preview=True,  reply_to_message_id=update.message.message_id)
	except Exception as e:
		raise e
	

info = {	'triggers' 	:	r'.*http[s]?://www.facebook.com/(groups|.*)/(videos|\S.+)/\d.+/.*',
			'active'	: 	True,
			'admin'		: 	False}

