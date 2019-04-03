from utils import *

print ('loading ' + __name__)

def action(bot, update, args):
	uid = getUID(update)
	cid = getCID(update)
	if update.message.chat.type == 'private':
		if str(uid) not in loadjson("userlist"):
			addUser(uid, update.message.from_user.first_name, "userlist", newUser=True)
			bot.send_message(uid, text_messages['startfirst'], parse_mode="Markdown")
		else:
			bot.send_message(uid, text_messages['start'], parse_mode="Markdown")
	elif update.message.chat.type == 'group' or update.message.chat.type == 'supergroup':
		if uid not in loadjson("userlist"):
			bot.reply_to(message, text_messages['startfirstgroup'], parse_mode="Markdown")
		else:
			bot.send_message(cid, text_messages['startgroup'], parse_mode="Markdown")
			bot.send_message(uid, text_messages['startfromgroup'].format(title = message.chat.title), parse_mode="Markdown")
	else:
		pass
	


info = {	'triggers'	: 	'start',
			'name'		:	'start',
			'help'		: 	"Returns a simple greeting to open the chat with the bot.",
			'example'	:	'',
			'active'	: 	True,
			'admin'		: 	False,
			'arguments' :	""}