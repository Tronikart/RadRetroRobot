from utils import *

print ('loading ' + __name__)

def action(bot, update, args):
	uid = str(getUID(update))
	fmUsers = loadjson("fmuser")
	content = ' '.join(args)
	if uid in fmUsers:
		url = "http://ws.audioscrobbler.com/2.0/?method=user.getRecentTracks&format=json&user=" + fmUsers[uid] + "&api_key=" + lastfm_key + "&limit=1"
		request = requests.get(url)
		data = request.json() 
		if request.status_code == 200:
			try:
				artist = data['recenttracks']['track'][0]['artist']['#text']
				song = data['recenttracks']['track'][0]['name']
				album = data['recenttracks']['track'][0]['album']['#text']
				if '@attr' in data['recenttracks']['track'][0]:
					update.message.reply_text(u"`> {user} is currently listening to:\nsong: {song}\nartist: {artist}\nalbum: {album}\n\t\t\t\t\t\t\t\t♪   ♫   ♪   ♫`".format(user=update.message.from_user.first_name, song=song, artist=artist, album=album), parse_mode="Markdown", reply_to_message_id=update.message.message_id)
				else:
					update.message.reply_text(u"`> {user} listened to:\nsong: {song}\nartist: {artist}\nalbum: {album}\n\t\t\t\t\t\t\t\t♫   ♪   ♫   ♪`".format(user=update.message.from_user.first_name, song=song, artist=artist, album=album), parse_mode="Markdown", reply_to_message_id=update.message.message_id)
			except:
				update.message.reply_text("`Theres has been an error, please verify that your username is valid`", parse_mode="Markdown", reply_to_message_id=update.message.message_id)
		else:
			update.message.reply_text("`Theres has been an error, heres some info from lastfm: {error}`".format(error=data['message']), parse_mode="Markdown", reply_to_message_id=update.message.message_id)
	else:
		update.message.reply_text("`Please set your username with /fmuser, preferably from PM.`", parse_mode="Markdown", reply_to_message_id=update.message.message_id)
		pass
	pass


info = {	'triggers'	: 	('np', 'nowplaying'),
			'name'		:	'Last FM Now Playing',
			'help'		: 	'This command will return your last listened song registered on last.fm, you need to set your user with /fmuser in order for it to work',
			'example'	:	'',
			'active'	: 	True,
			'admin'		: 	False,
			'arguments' :	""}

