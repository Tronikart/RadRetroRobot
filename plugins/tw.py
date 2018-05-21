from utils import *

print ('loading ' + __name__)

def action(bot, update, args):
	if args[0] == "-thread":
		tweet = ' '.join(args[1:])
		thread = True
	else:
		tweet = ' '.join(args)
		thread = False
	if update.message.from_user.id == adminid:
		if not thread:
			if len(tweet) <= 280 and tweet:
				tweet = api.update_status(tweet)
				bot.send_message(adminid, "`Tweet sent.`\n\n[url](https://twitter.com/_Abrah/status/" + str(tweet.id) + ")", parse_mode="Markdown")
			else:
				update.message.reply_text("`Tweet is " + str(len(tweet) - 140) + " characters longer than accepted lenght`", parse_mode="Markdown", reply_to_message_id=update.message.message_id)
		else:
			status = api.update_status(tweet.split('/nextTweet')[0])
			bot.send_message(adminid, "`Tweets sent.`\n\n[url](https://twitter.com/_Abrah/status/" + str(status.id) + ")", parse_mode="Markdown")
			for part in tweet.split('/nextTweet')[1:]:
				status = api.update_status(part, in_reply_to_status_id=status.id)
	else:
		pass

info = {	'triggers'	: 	('tw', 'tweet'),
			'name'		:	'tweet',
			'help'		: 	"Will tweet text to your account.",
			'example'	:	'',
			'active'	: 	True,
			'admin'		: 	True,
			'arguments' :	"<Text>"}
