from utils import *


print ('loading ' + __name__)

data = ""
def countItems(data):
	gifs, videos, images, other = 0, 0, 0, 0
	for element in data:
		if element['type'] == "image/gif":
			gifs += 1
		elif "image" in element['type']:
			images += 1
		elif "video" in element['type']:
			videos += 1
		else:
			other += 1
	return gifs, videos, images, other


def action(bot, update, args):
	if args:
		album = args[0]
		if ".com" in album:
			albumID = re.findall(r'imgur.com/(a|gallery)/(.*)\s*', album)[0][1]
		else:
			albumID = album

		url = "https://api.imgur.com/3/album/" + albumID + "/images?client_id=" + imgur_id
		global data
		request = requests.get(url)
		data = request.json()
		if requests.codes.ok == request.status_code:
			if len(data['data']) > 1:
				gifs, videos, images, other = countItems(data['data'])
				gifs = str(gifs) + " gifs, " if gifs else ""
				videos = str(videos) + " videos, " if videos else ""
				images = str(images) + " images, " if images else ""
				other =" and " + str(other) + " other, " if other else ""
				keyboard = [[InlineKeyboardButton("Accept", callback_data="True"),
							InlineKeyboardButton("Cancel", callback_data="False")]]
				
				reply_markup = InlineKeyboardMarkup(keyboard)
				update.message.reply_text("`This album has " + gifs + videos + images + other + "do you want to proceed?\n\nKeep in mind that the bigger the album, the longer it will take, be patient please.`", reply_markup=reply_markup, parse_mode="Markdown")
			else:
				update.message.reply_text("`This album only has 1 element, no action required.`", parse_mode="Markdown")
		else:
			update.message.reply_text("`Something went wrong:" + str(request.status_code)  + "\n" + data['data']['error'] + "`", parse_mode="Markdown")
	else:
		update.message.reply_text("`" + get_help(info) +  "`", parse_mode="Markdown", reply_to_message_id=update.message.message_id)
	


def button(bot, update):
	global data
	query = update.callback_query
	if query.message.chat.type == "private":
		sender = "NA"
		clicker = "NA"
	else:
		sender = query.message.reply_to_message.from_user.id
		clicker = query.from_user.id
	cid = query.message.chat_id
	if eval(query.data) and clicker == sender:
		if data:
			for post in data['data']:
				if "image" in post['type'] and not "gif" in post['type']:
					caption = post['description'] if post['description'] else ""
					if len(caption) < 200:
						bot.send_photo(cid, post['link'], caption=treatTitle(caption), timeout=60)
					else:
						bot.send_photo(cid, post['link'], timeout=60)
						bot.send_message(cid, treatTitle(caption))
				elif "video" in post['type'] or "gif" in post['type']:
					caption = post['description'] if post['description'] else ""
					if len(caption) < 200:
						bot.send_document(cid, post['link'], caption=treatTitle(caption), timeout=60)
					else:
						bot.send_document(cid, post['link'], timeout=60)
						bot.send_message(cid, treatTitle(caption))
				else:
					pass
			bot.edit_message_text("`Album sent.`", query.message.chat_id, message_id=query.message.message_id, parse_mode="Markdown", reply_markup=None)
			data = ""
		else: 
			bot.edit_message_text("`Expired.`", query.message.chat_id, message_id=query.message.message_id, parse_mode="Markdown")
			bot.answer_callback_query(query.id, "The request has expired, please try again.")
	elif not eval(query.data):
		bot.edit_message_text("`Your request has been canceled.`", query.message.chat_id, message_id=query.message.message_id, parse_mode="Markdown")
		data = ""
	else:
		bot.answer_callback_query(query.id, "Only the original sender can accept or cancel this")


info = {	'triggers'	: 	('imgur', 'i'),
			'name'		:	'Imgur',
			'help'		: 	'Returns every image from an imgur album after a confirmation.',
			'example'	:	'/imgur https://imgur.com/a/stuff',
			'active'	: 	True,
			'admin'		: 	False,
			'arguments' :	'<album or gallery ID>|<album or gallery url>'}



