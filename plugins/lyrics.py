from utils import *

print ('loading ' + __name__)

def action(bot, update, args):
	cid = getCID(update)
	uid = getUID(update)
	search = ' '.join(args)
	if search:
		search = re.findall(r'(.*\S)\s?-\s?(.*)', search)
		try:
			artist = search[0][0].capitalize()
			song = search[0][1].capitalize()
			bot.send_chat_action(cid, 'typing')
			url = "http://lyrics.wikia.com/wiki/" + artist + ":" + song
			soup = makesoup(url)
			redirect = soup.find('div', class_='redirectMsg')
			if redirect:
				url = 'http://lyrics.wikia.com' + redirect.a['href']
				soup = makesoup(url)
				song = redirect.a['href'].split(':')[1].replace("_", " ")
				artist = redirect.a['href'].split(':')[0].replace("_", " ").replace('/wiki/', '')
			else:
				pass 
			lyrics = soup.find('div', class_='lyricbox')
			lyrics = lyrics.contents
			lyric = ""
			listlen = len(lyrics)
			for line in lyrics[1:listlen-2]:
			 	if line.string != None:
			 		lyric += line.string
		 		else:
			 		lyric += "\n"
			lyrics = lyric
			if update.message.chat.type != "private":
				bot.send_message(cid, u"`> {artist} - {song}:\n\n{lyric}\n\n`*I suggest that you use this in private so we dont spam this group*".format(artist=artist, song=song, lyric=lyrics), parse_mode="Markdown")
			else:
				bot.send_message(cid, u"`> {artist} - {song}\n\n{lyric}`".format(artist=artist, song=song, lyric=lyrics), parse_mode="Markdown")
		except:
			update.message.reply_text( "`Lyric not found, make sure the name of the song is well written and in the correct format\n\n<artist> - <song>.`", parse_mode="Markdown", reply_to_message_id=update.message.message_id)
	else:
		update.message.reply_text( "`Follow this message with <artist> - <song> and I will display the lyrics.\n\nI highly advice this to be used on private conversations instead of groups.`", parse_mode="Markdown", reply_to_message_id=update.message.message_id)

info = {	'triggers'	: 	'lyrics',
			'name'		:	'Lyrics',
			'help'		: 	'Follow this message with <artist> - <song> and I will display the lyrics.\n\nI highly advice this to be used on private conversations instead of groups.',
			'example'	:	'/lyrics kraftwerk - The Robots',
			'active'	: 	True,
			'admin'		: 	False,
			'arguments' :	"<artist> - <song>"}

