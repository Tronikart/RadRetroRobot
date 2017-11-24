from utils import *

print ('loading ' + __name__)

# Reddit comment thing

def action(bot, update):
	cid = getCID(update)
	sub = ""
	try:
		url = re.findall(r'(http[s]?://(?:www.reddit.com/r/+.*/comments/+\S*))+', str(update.message.text))
		url = url[0] + ".json"
		request = requests.get(url, headers = {'User-agent': reddit_user})
		data = request.json()
		if request.status_code == 200:
			try:
				post = data[0]['data']['children'][0]['data']
				selftext = post['selftext']
				poster = post['author']
				sub = post['subreddit']
				title = post['title']
				up = post['ups']
				comments = post['num_comments']
				isNsfw = "nsfw" if post['over_18'] else "sfw"
				if post['is_self']:
					if len(selftext) <= 4999:
						if post['over_18']:
							self_post = "`" + title+"\nby /u/"+poster+" on /r/"+sub+"`\n\n"+selftext+"`\n<"+isNsfw+">" +" | "+up+" upvotes"+" | "+comments+" comments`"
						else:
							if len(title) > 57:
								self_post = "`"+title+"\nby /u/"+poster+"`\n\n"+selftext+"`\n<"+isNsfw+">" +" | "+up+" upvotes"+" | "+comments+" comments`"
							else:
								self_post = "`by /u/"+poster+"`\n\n"+selftext+"\n`<"+isNsfw+">" +" | "+up+" upvotes"+" | "+comments+" comments`"
						update.message.reply_text(self_post, parse_mode="Markdown", reply_to_message_id=update.message.message_id, disable_web_page_preview=True)

					else:
						if post['over_18']:
							self_post = "`"+title+"\nby /u/"+poster+" on /r/"+sub+"`\n\n`"+"The text from this post excedes my text message limit\n\n"+"<"+isNsfw+">" +" | "+up+" upvotes"+" | "+comments+" comments`"
						else:
							if len(title) > 57:
								self_post_long = "`"+title+"\nby /u/"+poster+"`\n\n`"+"The text from this post excedes my text message limit\n\n"+"<"+isNsfw+">" +" | "+up+" upvotes"+" | "+comments+" comments`"	
							else:
								self_post_long = "`by /u/"+poster+"`\n\n`"+"The text from this post excedes my text message limit\n\n"+"<"+isNsfw+">" +" | "+up+" upvotes"+" | "+comments+" comments`"
						update.message.reply_text(self_post_long, parse_mode="Markdown", reply_to_message_id=update.message.message_id, disable_web_page_preview=True)

				elif not post['is_self']:
					if post['over_18']:
						not_self_post = "`"+title+"\nby /u/"+poster+" on /r/"+sub+"\n<"+isNsfw+">" +" | "+up+" upvotes"+" | "+comments+" comments`"
					else:
						if len(title) > 57:
							not_self_post = "`"+title+"\nby /u/"+poster+" - <"+isNsfw+">`"
						else:
							not_self_post = "`by /u/"+poster+" - <"+isNsfw+">`"
					update.message.reply_text(not_self_post, parse_mode="Markdown", reply_to_message_id=update.message.message_id, disable_web_page_preview=True)
				else:
					pass
			except:
				pass
		else:
			pass
	except:
		pass


info = {	'triggers' 	:	r'.*http[s]?://www.reddit.com/r/+.*/comments/+\S*.*',
			'active'	: 	True,
			'admin'		: 	False}