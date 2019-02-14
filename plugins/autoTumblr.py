from utils import *

print ('loading ' + __name__)

def action(bot, update):
	content = update.message.text
	cid = getCID(update)
	try:
		url = re.findall(r'.*(http[s]?://.*\.tumblr\.com/post/.*).*', content)[0]
		soup = makesoup(url)
		url = soup.iframe['src']
		soup = makesoup(url)
		video = soup.video.source['src']
		bot.send_chat_action(cid, 'upload_video') 
		download_video(video)
		bot.send_video(cid, open('@RadRetroRobot_Downloaded_Video.mp4', 'rb'), reply_to_message_id=update.message.message_id, supports_streaming=True)
		os.remove('@RadRetroRobot_Downloaded_Video.mp4')
	except:
		pass

info = {	'triggers' 	:	r'.*\n.*http[s]?://.+\.tumblr\.com/post/.+\s?',
			'active'	: 	True,
			'admin'		: 	False}