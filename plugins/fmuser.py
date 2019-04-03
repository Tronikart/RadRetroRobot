from utils import *

print ('loading ' + __name__)

def action(bot, update, args):
	cid = getCID(update)
	uid = str(getUID(update))
	fmUsers = loadjson("userlist")
	user = args[0]
	if user:
		if fmUsers[uid]['fmuser']:
			bot.send_message(cid, f"`Changing your username from: {fmUsers[uid]['fmuser']} to {user}.`", parse_mode="Markdown")
			addUser(uid, user, 'userlist', "fmuser")
		else:
			bot.send_message(cid, f"`You've been registered into my data base as {user}.`", parse_mode="Markdown")
			addUser(uid, user, 'userlist', "fmuser")
	else:
		update.message.reply_text("`Follow this command with your last.fm username to be able to use last.fm commands.\n\nExample:\n  /fmuser RadRetroRobot`", parse_mode="Markdown", reply_to_message_id=update.message.message_id)


info = {	'triggers'	: 	'fmuser',
			'name'		:	'Last FM Set User',
			'help'		: 	'Follow this command with your last.fm username to be able to use last.fm commands.',
			'example'	:	'/fmuser RadRetroRobot',
			'active'	: 	True,
			'admin'		: 	False,
			'arguments' :	"<username>"}

