from utils import *

print ('loading ' + __name__)

def action(bot, update, args):
	cid = getCID(update)
	uid = str(getUID(update))
	fmUsers = loadjson("fmuser")
	user = args[0]
	if user:
		if uid not in fmUsers:
			addUser(uid, user, "fmuser")
			bot.send_message(cid, "`You've been registered into my data base as {username}.`".format(username=user), parse_mode="Markdown")
		elif uid in fmUsers:
			addUser(uid, user, "fmuser")
			bot.send_message(cid, "`Changing your username from: {olduser} to {username}.`".format(olduser=fmUsers[uid], username=user), parse_mode="Markdown")
	else:
		update.message.reply_text("`Follow this command with your last.fm username to be able to use last.fm commands.\n\nExample:\n  /fmuser RadRetroRobot`", parse_mode="Markdown", reply_to_message_id=update.message.message_id)


info = {	'triggers'	: 	'fmuser',
			'name'		:	'Last FM Set User',
			'help'		: 	'Follow this command with your last.fm username to be able to use last.fm commands.',
			'example'	:	'/fmuser RadRetroRobot',
			'active'	: 	True,
			'admin'		: 	False,
			'arguments' :	"<username>"}

