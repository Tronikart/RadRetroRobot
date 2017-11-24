from utils import *

print ('loading ' + __name__)

def action(bot, update):
	cid = getCID(update)
	try:
		url = re.findall(r'(http[s]?://www\.youtube\.com/watch\?v.*)\s?|(http[s]?://youtu\.be/.*)\s?', update.message.text)
		url = url[0][0] if url[0][0] else url[0][1]
		bot.send_chat_action(cid, "typing")
		soup = makesoup(url)
		channel_info = soup.find("div", class_="yt-user-info")
		channel_name = channel_info.a.string
		channel_url = "http://www.youtube.com" + channel_info.a['href']
		duration = int(re.findall(r'dur%3D(\d+).+', soup.text)[0])
		m, s = divmod(duration, 60)
		h, m = divmod(m, 60)
		duration = "%d:%02d:%02d" % (h, m, s) if h > 0 else "%02d:%02d" % (m, s)
		view_count = soup.find('div', class_="watch-view-count").string
		subs = soup.find('span', class_="yt-subscription-button-subscriber-count-branded-horizontal yt-subscriber-count").string
		update.message.reply_text("\n[" + channel_name + "](" + channel_url + ")" + "`\nDuration: " + duration + "\nSubs: " + subs + "\nViews on video: " + view_count + "`", parse_mode="Markdown", reply_to_message_id=update.message.message_id, disable_web_page_preview=True)		
	except:
		pass


info = {	'triggers' 	:	r'.*http[s]?://www\.youtube\.com/watch\?v.*\s?|http[s]?://youtu\.be/.*',
			'active'	: 	True,
			'admin'		: 	False}