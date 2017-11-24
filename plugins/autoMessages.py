from utils import *

print ('loading ' + __name__)

def action(bot, update):
	cid = getCID(update)
	uid = getUID(update)
	lower_message = update.message.text.lower()

	if str(cid) not in loadjson("grouplist"):
		gName = (update.message.chat.title)
		addUser(cid, gName, "grouplist")

	# Beep 

	if 'beep' == lower_message:
		bot.send_message(cid, "`Boop`", parse_mode="Markdown")

	# Boop

	if 'boop' == lower_message:
		bot.send_message(cid, "`Beep`", parse_mode="Markdown")

	# Bop

	if 'bop' == lower_message and uid == adminid:
		bot.send_message(cid, "`Stop it, you are embarrassing​ me`", parse_mode="Markdown")

	# Goodnight

	if 'good night' in lower_message or 'buenas noches' in lower_message or 'good night, rrr' in lower_message:
		if str(cid) not in loadjson("quietlist"):
			if uid == adminid:
				bot.send_message(cid, random.choice(good_night_admin), parse_mode="Markdown")
			else:
				bot.send_message(cid, random.choice(good_night), parse_mode="Markdown")


	# Lazily copied from previous module handlers, might improve them later on, too tired now
	# I love you

	if lower_message == 'i love you, rad retro robot' or lower_message == 'i love you, radretrorobot' or lower_message == 'i love you, rrr' or lower_message == 'i love you rrr' or lower_message == 'i love you, radretrorobot' or lower_message == 'i love you rad retro robot':
		if str(cid) not in loadjson("quietlist"):
			if uid == adminid:
				bot.send_message(cid, random.choice(love_admin), parse_mode="Markdown")
			else:
				bot.send_message(cid, random.choice(love), parse_mode="Markdown")

	# Fuck you

	if lower_message == "fuck you, rrr" or lower_message == "fuck you, radretrorobot" or lower_message == "fuck you, rad retro robot" or lower_message == "fuck you rrr" or lower_message == "fuck you radretrorobot" or lower_message == "fuck you rad retro robot":
		if str(cid) not in loadjson("quietlist"):
			bot.send_message(cid, random.choice(fuckyou_response), parse_mode="Markdown")
			return

	# Hello

	if lower_message == 'hello, rad retro robot' or lower_message == 'hello, rrr' or lower_message == 'hi, rad retro robot' or lower_message == 'hi, rrr' or  lower_message == 'hello, radretrorobot' or  lower_message == 'hi, radretrorobot':
		if str(cid) not in loadjson("quietlist"):
			bot.send_message(cid, random.choice(hello), parse_mode="Markdown")
			return

	# Top

	if '/top' in lower_message:
		try:
			update.message.reply_text(random.choice(top_response), parse_mode="Markdown", reply_to_message_id=update.message.message_id)
		except:
			bot.send_message(cid, random.choice(top_response), parse_mode="Markdown")
		return
	
	# Shrug

	if '/shrug' in lower_message:
		try:
			update.message.reply_text(premades['shrug'], parse_mode="Markdown", reply_to_message_id=update.message.message_id)
		except:
			bot.send_message(cid, premades['shrug'], parse_mode="Markdown")
		return

	# Lenny

	if '/lenny' in lower_message:
		try:
			update.message.reply_text(premades['lenny'], parse_mode="Markdown", reply_to_message_id=update.message.message_id)
		except:
			bot.send_message(cid, premades['lenny'], parse_mode="Markdown")
		return

	# Stare

	if '/stare' in lower_message:
		try:
			update.message.reply_text(premades['stare'], parse_mode="Markdown", reply_to_message_id=update.message.message_id)
		except:
			bot.send_message(cid, premades['stare'], parse_mode="Markdown")
		return
	
	# Mentioned

	if 'RRR' in update.message.text or 'RadRetroRobot' in update.message.text:
		if str(cid) not in loadjson("quietlist"):
			bot.send_message(cid, random.choice(mentioned), parse_mode="Markdown")
		return

	# Random beeps

	if (random.randrange(1, repeatMax) == 1):
		try:
			if str(cid) not in loadjson("quietlist"):
				bot.send_message(cid, random.choice(repeat_message).format(message=message_to_repeat) , parse_mode="Markdown")
		except:
			pass

		if (random.randrange(1, beepMax) == 1):	
			try:
				if str(cid) not in loadjson("quietlist"):
					bot.send_message(cid, random.choice(beeps), parse_mode="Markdown")
			except:
				pass

info = {	'active'	: 	False,
			'admin'		: 	False}