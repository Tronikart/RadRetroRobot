from utils import *

print ('loading ' + __name__)

def action(bot, update, args):
	uName = update.message.from_user.first_name
	lname = update.message.from_user.last_name
	usName = update.message.from_user.username
	if update.message.chat.type == 'private':
		uid = str(update.message.from_user.id)
		if lname != None:
			update.message.reply_text(text_messages['ping'].format(name=uName, uname=usName, lname=lname, uid=uid), parse_mode="Markdown", reply_to_message_id=update.message.message_id)
		else:
			lname = ''
			update.message.reply_text(text_messages['ping'].format(name=uName, uname=usName, lname=lname, uid=uid), parse_mode="Markdown", reply_to_message_id=update.message.message_id)

	elif update.message.chat.type == 'group' or update.message.chat.type == 'supergroup':
		uid = str(message.from_user.id)
		gid = str(message.chat.id).lstrip('-')
		gName = update.message.chat.title
		if lname != None:
			update.message.reply_text(text_messages['pinggroup'].format(name=uName, uname=usName, lname=lname, uid=uid, gName=gName, gid=gid), parse_mode="Markdown", reply_to_message_id=update.message.message_id)
		else:
			lname = ''
			update.message.reply_text(text_messages['pinggroup'].format(name=uName, uname=usName, lname=lname, uid=uid, gName=gName, gid=gid), parse_mode="Markdown", reply_to_message_id=update.message.message_id)
	else:
		pass

info = {	'triggers'	: 	'ping',
			'name'		:	'Ping',
			'help'		: 	"Returns basic information about you and the chat.",
			'example'	:	'',
			'active'	: 	True,
			'admin'		: 	False,
			'arguments' :	""}