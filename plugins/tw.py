from utils import *

print ('loading ' + __name__)

def action(bot, update, args):
	users = loadjson("userlist")
	uid = getUID(update)
	cid = getCID(update)

	if args:
		if args[0] == "-thread":
			tweet = ' '.join(args[1:])
			thread = True
		elif args[0] == "-addUser":
			thread = False
			tweet = ''
		elif args[0] == "-clearUser":
			addUser(uid, update.message.from_user.first_name, 'userlist', clearData=True)
			update.message.reply_text("`User has been cleared successfully!`", parse_mode="Markdown", reply_to_message_id=update.message.message_id)
			return
		else:
			tweet = ' '.join(args)
			thread = False
	else:
		bot.send_message(cid, get_help(info), parse_mode="Markdown")
		return

	if update.message.from_user.id == adminid:
		try:
			if not thread:
				if len(tweet) <= 280 and tweet:
					tweet = api.update_status(tweet)
					bot.send_message(adminid, "`Tweet sent.`\n\n[url](https://twitter.com/" + adminTwitterUser + "/status/" + str(tweet.id) + ")", parse_mode="Markdown")
				else:
					update.message.reply_text("`Tweet is " + str(len(tweet) - 280) + " characters longer than accepted length`", parse_mode="Markdown", reply_to_message_id=update.message.message_id)
			else:
				incorrectLength = False
				for part in tweet.split('/nextTweet'):
					if len(part) > 280:
						update.message.reply_text("`This part of the thread: " + part + " is " + str(len(part) - 280) + " characters longer than accepted length`", parse_mode="Markdown", reply_to_message_id=update.message.message_id)
						incorrectLength = True
				if incorrectLength:
					return
				status = api.update_status(tweet.split('/nextTweet')[0])
				bot.send_message(adminid, "`Tweets sent.`\n\n[url](https://twitter.com/" + adminTwitterUser + "/status/" + str(status.id) + ")", parse_mode="Markdown")
				for part in tweet.split('/nextTweet')[1:]:
					status = api.update_status(part, in_reply_to_status_id=status.id)
		except tweepy.error.TweepError as error:
			bot.send_message(cid, f"`ERROR:`\n\n\"{error}\"", parse_mode="Markdown")
			return
	else:
		currentUser = users[str(uid)]['twitter']

		# Registering an user
		if args[0] == '-addUser':
			verifier = args[1].split('oauth_verifier=')[1]
			currentUser['verifier'] = verifier
			addUser(uid, update.message.from_user.first_name, 'userlist', twitterVerifier=verifier)
			bot.send_message(cid, "`User added successfully, you can now use /tw!`", parse_mode="Markdown")
		else:
			userauth = OAuthHandler(consumer_key, consumer_secret)
			# Normal tweeting
			if currentUser['verifier']:

				try:
					userauth.request_token = currentUser['token']
					keys = userauth.get_access_token(currentUser['verifier'])
					userauth.set_access_token(keys[0], keys[1])
					userapi = tweepy.API(userauth)
					if not thread:
						if len(tweet) <= 280 and tweet:
							tweet = userapi.update_status(tweet)
							bot.send_message(cid, f"`Tweet sent.`\n\n[url](https://twitter.com/{userapi.me().screen_name}/status/{tweet.id})", parse_mode="Markdown")

						else:
							update.message.reply_text("`Tweet is " + str(len(tweet) - 280) + " characters longer than accepted length`", parse_mode="Markdown", reply_to_message_id=update.message.message_id)
					else:
						incorrectLength = False
						for part in tweet.split('/nextTweet'):
							if len(part) > 280:
								update.message.reply_text("`This part of the thread: " + part + " is " + str(len(part) - 280) + " characters longer than accepted length`", parse_mode="Markdown", reply_to_message_id=update.message.message_id)
								incorrectLength = True
						if incorrectLength:
							return
						status = userapi.update_status(tweet.split('/nextTweet')[0])

						bot.send_message(cid, f"`Tweet sent.`\n\n[url](https://twitter.com/{userapi.me().screen_name}/status/{status.id})", parse_mode="Markdown")
						for part in tweet.split('/nextTweet')[1:]:
							status = userapi.update_status(part, in_reply_to_status_id=status.id)
				except tweepy.error.TweepError as error:
					bot.send_message(cid, f"`There has been an error while trying to access Twitter, here is some info on the error:\n\n\"{error}\"\n\nPossible solutions: You can try waiting, or depending on the error, you could also try renewing the permissions, just send /tw -clearUser and repeat the initial process again.`", parse_mode="Markdown")
					return

				del userauth
				del userapi
			# Not a registered user
			else:
				redirect_url = userauth.get_authorization_url()
				button_list = [InlineKeyboardButton("login to twitter", url=redirect_url)]
				addUser(uid, update.message.from_user.first_name, 'userlist', requestToken=userauth.request_token)
				reply_markup = InlineKeyboardMarkup([button_list])
				bot.send_message(cid, "`You need to login.\n\nREAD CAREFULLY: Currently this is a bit complicated to do, maybe it will get improved in the future.\n\nSteps:\n\n1. Click on the button bellow\n2. Give permissions\n3. Copy the url by hand (it will take you to telegram, go back to the page) and send it to me as follows:\n    /tw -addUser \"url\"\n    (without the quoation marks).\n\nThis should be done only once, I won't store any information or passwords, those things are handled by Twitter.\n\n(If you are trying to add an user and this shows up, give it another try)`", reply_markup=reply_markup, parse_mode="Markdown")

		

info = {	'triggers'	: 	('tw', 'tweet'),
			'name'		:	'tweet',
			'help'		: 	"Will tweet text to your account.\nIf you want to tweet a thread, prepend -thead and then separate each tweet with /nextTweet",
			'example'	:	'/tw -thread A tweet /nextTweet another tweet /nextTweet in a never ending /nextTweet thread',
			'active'	: 	True,
			'admin'		: 	False,
			'arguments' :	"[-thread|-addUser|-clearUser] <Text>"}


