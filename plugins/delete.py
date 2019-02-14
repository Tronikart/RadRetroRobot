from utils import *

print ('loading ' + __name__)

def action(bot, update, args):
	cid = getCID(update)
	if update.message.from_user.id == adminid:
		replyID = update.message.reply_to_message.message_id
		bot.delete_message(cid, replyID)
	else:
		pass

info = {	'triggers'	:	('del', 'delete'),
			'name'		:	'delete',
			'help'		: 	"Deletes the bot's message this command replies to",
			'example'	:	'/del',
			'active'	: 	True,
			'admin'		: 	True,
			'arguments' :	""}