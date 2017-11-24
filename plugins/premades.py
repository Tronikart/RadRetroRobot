from utils import *

print ('loading ' + __name__)

def action(bot, update, args):
	cid = getCID(update)
	command = update.message.text
	if command == '/premades':
		bot.send_message(cid, text_messages['premade'])
	elif command == '/top':
		if cid == degeneratesgroup:
			try:
				rid = update.message.reply_to_message
				update.message.reply_text(random.choice(top_response_degen), parse_mode="Markdown", reply_to_message_id=update.message.message_id)
			except:
				bot.send_message(cid, random.choice(top_response_degen), parse_mode="Markdown")
		else:
			try:
				rid = update.message.reply_to_message
				update.message.reply_text(random.choice(top_response), parse_mode="Markdown", reply_to_message_id=update.message.message_id)
			except:
				bot.send_message(cid, random.choice(top_response), parse_mode="Markdown")
	elif command == '/lenny' and cid is not degeneratesgroup:
		try:
			rid = update.message.reply_to_message
			update.message.reply_text(premades['lenny'], parse_mode="Markdown", reply_to_message_id=update.message.message_id)
		except:
			bot.send_message(cid, premades['lenny'], parse_mode="Markdown")
	elif command == '/stare' and cid is not degeneratesgroup:
		try:
			rid = update.message.reply_to_message
			update.message.reply_text(premades['stare'], parse_mode="Markdown", reply_to_message_id=update.message.message_id)
		except:
			bot.send_message(cid, premades['stare'], parse_mode="Markdown")

	elif command == '/shrug' and cid is not degeneratesgroup:
		try:
			rid = update.message.reply_to_message
			update.message.reply_text(premades['shrug'], parse_mode="Markdown", reply_to_message_id=update.message.message_id)
		except:
			bot.send_message(cid, premades['shrug'], parse_mode="Markdown")

info = {	'triggers'	:	('premades', 'top', 'lenny', 'stare', 'shrug'),
			'name'		:	'Premades',
			'help'		: 	'Premade text messages, send this command alone to get a list of them',
			'example'	:	'',
			'active'	: 	True,
			'admin'		: 	False,
			'arguments' :	''}