from utils import *

print ('loading ' + __name__)

def action(bot, update, args):
	tweet = ' '.join(args)
	if update.message.from_user.id == adminid:
		if len(tweet) <= 280 and tweet:
			api.update_status(tweet)
			bot.send_message(adminid, "`Tweet sent.`", parse_mode="Markdown")
		else:
			update.message.reply_text("`Tweet is " + str(len(tweet) - 140) + " characters longer than accepted lenght`", parse_mode="Markdown", reply_to_message_id=update.message.message_id)
	else:
		pass

info = {	'triggers'	: 	('tw', 'tweet'),
			'name'		:	'tweet',
			'help'		: 	"Will tweet text to your account.",
			'example'	:	'',
			'active'	: 	True,
			'admin'		: 	True,
			'arguments' :	"<Text>"}