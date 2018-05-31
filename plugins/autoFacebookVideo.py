from utils import *

print ('loading ' + __name__)

def action(bot, update):
	cid = getCID(update)
	token = getFBToken()
	try:
		print (update.message.text)
		request_url = 'https://graph.facebook.com/v3.0/'
		url = re.findall(r'(.*http[s]?://www.facebook.com/(groups|.*)/(videos|\S.+)/\d.+/.*|http[s]?://m.facebook.com/story.php\S+)', update.message.text)[0][0]
		print('beep')
		# Getting the post ID from either a /video/ url or a /groups/ url
		try:
			media_id = url.split('/')[5] if url.split('/')[4] == "videos" else url.split('/')[6]
			request = requests.get(request_url + media_id, {'access_token': token, 'fields' : 'source'})
			ok = request.ok
		except:
			ok = False

		if ok:
			mp4url = request.json()['source']
			downloaded = False
		else:
			soup = makesoup(url)
			video_url = soup.find_all('meta', {'property':'og:video'})[0]['content']
			download_video(video_url)
			downloaded = True

		if url[-2:] != "-f":
			response = bot.send_document(cid, mp4url, reply_to_message_id=update.message.message_id) if ok else {'ok' : False}
			if not response['ok']:
				print('not ok')
				soup = makesoup(url)
				video_url = soup.find_all('meta', {'property':'og:video'})[0]['content']
				bot.send_chat_action(cid, 'upload_video') 
				if downloaded:
					pass
				else:
					download_video(video_url)
				bot.send_document(cid, open('@RadRetroRobot_Downloaded_Video.mp4', 'rb'), reply_to_message_id=update.message.message_id)
				os.remove('@RadRetroRobot_Downloaded_Video.mp4')
		else:
			response = bot.send_message(cid, "[direct link](" + mp4url + ")", parse_mode="Markdown", disable_web_page_preview=True,  reply_to_message_id=update.message.message_id)


	except Exception as e:
		raise e
	

info = {	'triggers' 	:	r'.*(http[s]?://www.facebook.com/(groups|.*)/(videos|\S.+)/\d.+/.*|http[s]?://m.facebook.com/story.php.*).*',
			'active'	: 	True,
			'admin'		: 	False}

