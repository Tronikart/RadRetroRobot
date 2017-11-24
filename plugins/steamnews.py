from utils import *

print ('loading ' + __name__)

def action(bot, update, args):
	cid = getCID(update)
	steamid = ' '.join(args)
	if steamid:
		url = "http://api.steampowered.com/ISteamNews/GetNewsForApp/v0002/?appid=" + steamid + "&count=3&maxlength=300&format=json"
		request = requests.get(url)
		data = request.json()
		if request.status_code == 200:
			title = data['appnews']['newsitems'][0]['title']
			content = data['appnews']['newsitems'][0]['contents']
			links = re.findall(r'<a[^>]*\shref="(.*?)"', content)
			for link in links:
				content = content.replace(link, "")
				content = content.replace('<', "")
				content = content.replace('>', "")
				content = content.replace('href=""', "")
			url = data['appnews']['newsitems'][0]['url']
			bot.send_message(cid, u'`> {title}\n\n{content}\n\n`'.format(title=title, content=content) + '[More info here]({url})'.format(url=url), parse_mode="Markdown", disable_web_page_preview=True)
		else:
			update.message.reply_text("`There has been an error, the number {error} to be specific.`".format(error=request.status_code), parse_mode="Markdown", reply_to_message_id=update.message.message_id)
	else:
		update.message.reply_text("`Follow this command with the ID of a steam game and I will give you the last posted new, use /steamid if you dont know the ID of your game\n\nExample:\n  /steamnews 570`",parse_mode="Markdown", reply_to_message_id=update.message.message_id)

info = {	'triggers'	: 	('steamnews', 'sn'),
			'name'		:	'Steam News',
			'help'		: 	"Follow this command with the ID of a steam game and I will give you the last posted new, use /steamid if you dont know the ID of your game",
			'example'	:	'/steamnews 504370',
			'active'	: 	True,
			'admin'		: 	False,
			'arguments' :	"<steamid>"}