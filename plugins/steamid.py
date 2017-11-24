from utils import *

print ('loading ' + __name__)

def action(bot, update, args):
	name = ' '.join(args)
	if name:
		name = name.capitalize()
		cid = getCID(update)
		try:
			url = "https://api.datamarket.azure.com/Bing/Search/v1/Web?Query=%27" + name.replace(' ', '+') + "+steam%27&$format=json&$skip=0&$top=10"
			headers = { 'Authorization' : bing_key}
			request = requests.get(url, headers=headers)
			data = request.json()
			found = False
			for result in data['d']['results']:
				print (result['Url'])
				if "http://store.steampowered.com/app/" in result['Url']:
					appid = re.findAll(r'http://store.steampowered.com/app/(\d.*)/', result['Url'])
					print (appid)
					found = True
					title = result['Title'].split(' on Steam')[0]
					url = "http://store.steampowered.com/app/" + str(appid) + "/"
					bot.send_message(cid, u"`{title}: {appid}\n/steampage <ID>\n/steamdetails <ID>\n/steamnews <ID>`".format(appid=appid, title=title) + u"\n\n[Store Link]("+url+")", parse_mode="Markdown", disable_web_page_preview=True)
					break
			if not found:
				bot.send_message(cid, "`I did not find {name} on steams app list`".format(name=name), parse_mode="Markdown")

		except:
			url = "http://api.steampowered.com/ISteamApps/GetAppList/v2/?key=" + steam_key + "&format=JSON&language=en_us"
			request = requests.get(url)
			data = request.json()
			found = False
			bot.send_chat_action(cid, 'typing') 
			if request.status_code == 200:
				for app in data['applist']['apps']:
					if app['name'].lower() == name.lower():
						appid = app['appid']
						url = "http://store.steampowered.com/app/" + str(appid) + "/"
						bot.send_message(cid, u"`{name}: {appid}\n/steampage <ID>\n/steamdetails <ID>\n/steamnews <ID>`".format(appid=appid, name=name) + u"\n\n[Store Link]("+url+")", parse_mode="Markdown", disable_web_page_preview=True)
						found = True
						break
				if not found:
					bot.send_message(cid, "`I did not find {name} on steams app list`".format(name=name), parse_mode="Markdown")
	else:
		update.message.reply_text ("`Follow this command with the name of a steam game and I will give you its ID, useful to use along with\n\n/steamnews\n/steampage\n\nExample:\n  /steamid Dota 2`", parse_mode="Markdown", reply_to_message_id=update.message.message_id)

info = {	'triggers'	: 	('steamid', 'sid'),
			'name'		:	'Steam ID',
			'help'		: 	"Follow this command with the name of a steam game and I will give you its ID, useful to use along with\n\n/steamnews\n/steampage",
			'example'	:	'/steamid Battlerite',
			'active'	: 	True,
			'admin'		: 	False,
			'arguments' :	"<Steam Game>"}