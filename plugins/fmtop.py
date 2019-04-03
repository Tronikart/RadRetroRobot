from utils import *

print ('loading ' + __name__)

def action(bot, update, args):
	cid = getCID(update)
	uid = str(getUID(update))
	fmUsers = loadjson("userlist")
	if fmUsers[uid]['fmuser']:
		url = "http://ws.audioscrobbler.com/2.0/?method=user.getTopArtists&format=json&user=" + fmUsers[uid]['fmuser'] + "&api_key=" + lastfm_key + "&period=7day&limit=5"
		request = requests.get(url)
		data = request.json()
		artists = ""
		if request.status_code == 200:
			try:
				if data['topartists']['@attr']['totalPages'] != "0":
					i = 0
					artists = ""
					for artist in data['topartists']['artist']:
						artist_name = artist['name']
						playcount = artist['playcount']
						artists += u"`> {artist} - {playcount}` \n".format(artist=artist_name, playcount=playcount)
						i += 1
					if i > 1:
						artist = "artist"
					else:
						artist = "artists"
					update.message.reply_text(u"`{name}'s last week Top {playcount} {artist} and its playcount:` \n".format(artist=artist, name=update.message.from_user.first_name, playcount=i) + artists, parse_mode="Markdown", reply_to_message_id=update.message.message_id)
				else: 
					update.message.reply_text("`Theres has been an error, I found no information from your user.`", parse_mode="Markdown", reply_to_message_id=update.message.message_id)
			except:
				update.message.reply_text("`Theres has been an error, I found no information from your user.`", parse_mode="Markdown", reply_to_message_id=update.message.message_id)
		else:
			update.message.reply_text("`Theres has been an error, heres some info from lastfm: {error}`".format(error=data['message']), parse_mode="Markdown", reply_to_message_id=update.message.message_id)
	else:
		update.message.reply_text("`Please set your username with /fmuser, preferably from PM.`", parse_mode="Markdown", reply_to_message_id=update.message.message_id)
		return
		


info = {	'triggers'	: 	'fmtop',
			'name'		:	'Last FM Top Artists',
			'help'		: 	'This command will return your top 5 artists from 7 days ago.\nYou need to set up your Last fm user with /fmuser',
			'example'	:	'',
			'active'	: 	True,
			'admin'		: 	False,
			'arguments' :	""}

