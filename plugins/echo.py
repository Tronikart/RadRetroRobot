from utils import *

print ('loading ' + __name__)

def action(bot, update, args):
	cid = getCID(update)
	msg = update.message.text.replace('/echo ', '').replace('/print ', '')
	if msg:
		bot.send_message(cid, u"`{msg}`".format(msg=msg), parse_mode="Markdown")
	else:
		bot.reply_to(message, "`Follow this command with some text and I will repeat it.\n\nExample:\n  /echo I repeat what humans say`", parse_mode="Markdown")

info = {	'triggers'	: 	('echo', 'print'),
			'name'		:	'Echo',
			'help'		: 	"Follow this command with some text and I will repeat it.",
			'example'	:	'/echo I repeat what humans say',
			'active'	: 	True,
			'admin'		: 	False,
			'arguments' :	"<text>"}
