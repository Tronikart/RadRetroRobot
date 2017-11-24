from utils import *

print ('loading ' + __name__)

def action(bot, update, args):
	cid = getCID(update)
	uid = getUID(update)
	fmUsers = loadjson("fmuser")
	if str(uid) in fmUsers:
		url = "http://ws.audioscrobbler.com/2.0/?method=user.getTopAlbums&format=json&user=" + fmUsers[str(uid)] + "&api_key=" + lastfm_key + "&limit=5&period=7day"
		request = requests.get(url)
		data = request.json()
		artists = ""
		if request.status_code == 200:
			if data['topalbums']['@attr']['totalPages'] != "0":
				i = 0
				artists = ""
				for album in data['topalbums']['album']:
					album_name = album['name']
					playcount = album['playcount']
					artist_name = album['artist']['name']
					artists += u"`> {artist} - {album} - {playcount}` \n".format(artist=artist_name, playcount=playcount, album=album_name)
					i += 1
				if i > 1:
					artist = "album"
				else:
					artist = "albums"
				update.message.reply_text(u"`{name}'s last week Top {playcount} {artist} and its playcount:` \n".format(artist=artist, name=update.message.from_user.first_name, playcount=i) + artists, parse_mode="Markdown", reply_to_message_id=update.message.message_id)
			else: 
				update.message.reply_text("`Theres has been an error, I found no information from your user.`", parse_mode="Markdown", reply_to_message_id=update.message.message_id)
		else:
			update.message.reply_text("`Theres has been an error, heres some info from lastfm: {error}`".format(error=data['message']), parse_mode="Markdown", reply_to_message_id=update.message.message_id)
	else:
		update.message.reply_text("`Please set your username with /fmuser, preferably from PM.`", parse_mode="Markdown", reply_to_message_id=update.message.message_id)
		return

info = {	'triggers'	: 	'fmalbums',
			'name'		:	'Last FM Top Albums',
			'help'		: 	"Will give you your top 5 of the last 7 days.\nYou need to setup your username with /.",
			'example'	:	'',
			'active'	: 	True,
			'admin'		: 	False,
			'arguments' :	""}

