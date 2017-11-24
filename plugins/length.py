from utils import *

print ('loading ' + __name__)

def action(bot, update,args):
	cid = getCID(update)
	content = ' '.join(args)
	if content:
		no_spaces = str(len(content.replace(" ", "")))
		spaces = str(len(content))
		bot.send_message(cid, "`Your text is:\n"+ spaces + " characters long including spaces\n" + no_spaces +" characters long not including spaces.`", parse_mode="Markdown")
	else:
		try:
			rid = update.message.reply_to_message
			content = rid.text
			no_spaces = str(len(content.replace(" ", "")))
			spaces = str(len(content))
			bot.send_message(cid, "`Your text is:\n"+ spaces + " characters long including spaces\n" + no_spaces +" characters long not including spaces.`", parse_mode="Markdown")
		except:
			update.message.reply_text('`Follow this command with words and the length will be returned, with spaces and without them`', parse_mode="Markdown", reply_to_message_id=update.message.message_id)

info = {	'triggers'	: 	('len', 'lenght'),
			'name'		:	'Length',
			'help'		: 	'Follow this command with words and the length will be returned, with spaces and without them',
			'example'	:	'/len How long is this sentence?',
			'active'	: 	True,
			'admin'		: 	False,
			'arguments' :	"<text>"}

