from utils import *

print ('loading ' + __name__)

def action(bot, update, args):
	uid = getUID(update)
	if uid == adminid and args:
		cid = args[0]
		try:
			content = ' '.join(args[1:])
			bot.send_message(cid, "`{cid}`".format(cid=content), parse_mode="Markdown")
		except:
			pass

info = {	'triggers'	: 	('sendmessage', 'message'),
			'name'		:	'sendmessage',
			'help'		: 	"Send a message to a specific ID.",
			'active'	: 	True,
			'admin'		: 	True,
			'arguments' :	"<message>"}