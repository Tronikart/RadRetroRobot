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
							self_post = "`" + title+"\nby /u/"+poster+" on /r/"+sub+"`\n\n"+selftext+"`\n<"+isNsfw+">" +" | "+str(up)+" upvotes"+" | "+str(comments)+" comments`"
						else:
							if len(title) > 57:
								self_post = "`"+title+"\nby /u/"+poster+"`\n\n"+selftext+"`\n<"+isNsfw+">" +" | "+str(up)+" upvotes"+" | "+str(comments)+" comments`"
							else:
								self_post = "`by /u/"+poster+"`\n\n"+selftext+"\n`<"+isNsfw+">" +" | "+str(up)+" upvotes"+" | "+str(comments)+" comments`"
						update.message.reply_text(self_post, parse_mode="Markdown", reply_to_message_id=update.message.message_id, disable_web_page_preview=True)
					else:
						if post['over_18']:
							self_post = "`"+title+"\nby /u/"+poster+" on /r/"+sub+"`\n\n`"+"The text from this post excedes my text message limit\n\n"+"<"+isNsfw+">" +" | "+str(up)+" upvotes"+" | "+str(comments)+" comments`"
						else:
							if len(title) > 57:
								self_post_long = "`"+title+"\nby /u/"+poster+"`\n\n`"+"The text from this post excedes my text message limit\n\n"+"<"+isNsfw+">" +" | "+str(up)+" upvotes"+" | "+str(comments)+" comments`"	
							else:
								self_post_long = "`by /u/"+poster+"`\n\n`"+"The text from this post excedes my text message limit\n\n"+"<"+isNsfw+">" +" | "+str(up)+" upvotes"+" | "+str(comments)+" comments`"
						update.message.reply_text(self_post_long, parse_mode="Markdown", reply_to_message_id=update.message.message_id, disable_web_page_preview=True)

				else:
					if post['over_18'] or 'post_hint' not in post.keys():
						not_self_post = "`"+title+"\nby /u/"+poster+" on /r/"+sub+"\n<"+isNsfw+">" +" | "+str(up)+" upvotes"+" | "+str(comments)+" comments`"
					else:
						if len(title) > 57:
							not_self_post = "`"+title+"\nby /u/"+poster+" - <"+isNsfw+">`"
						else:
							not_self_post = "`by /u/"+poster+" - <"+isNsfw+">`"
					if 'post_hint' in post.keys():
						if post['post_hint'] == 'image' and not post['over_18']:
							bot.send_photo(cid, post['url'], caption=not_self_post.replace('`', '').replace('/u/',''), parse_mode="Markdown", reply_to_message_id=update.message.message_id, disable_web_page_preview=True)
						elif (post['post_hint'] == 'link' or post['post_hint'] == 'rich:video') and not post['over_18']:
							if "gifv" in post['url']:
								url, title = getImgur(post['url'])
								bot.send_document(cid, url, caption=not_self_post.replace('`', '').replace('/u/',''), parse_mode="Markdown", reply_to_message_id=update.message.message_id, disable_web_page_preview=True)
							elif "gfycat" in post['url']:
								url, title = getGfy(post['url'])
								bot.send_document(cid, url, caption=not_self_post.replace('`', '').replace('/u/',''), parse_mode="Markdown", reply_to_message_id=update.message.message_id, disable_web_page_preview=True)
							else:
								url = post['url']
								# I know that this looks awful
								update.message.reply_text(not_self_post.replace('by /u/', '`[' + post['domain'] + ' link](' + url + ')`\nby /u/'), parse_mode="Markdown", reply_to_message_id=update.message.message_id, disable_web_page_preview=True)
								# In fact, this whole section is a disaster
								# This is barely readable in case it is, Im sorry and I appreciate you if you understand it
						else:
							update.message.reply_text(not_self_post, parse_mode="Markdown", reply_to_message_id=update.message.message_id, disable_web_page_preview=True)
					else:
						update.message.reply_text(not_self_post, parse_mode="Markdown", reply_to_message_id=update.message.message_id, disable_web_page_preview=True)


			except:
				pass
		else:
			pass
	except:
		pass


info = {	'triggers' 	:	r'.*http[s]?://www.reddit.com/r/+.*/comments/+\S*.*',
			'active'	: 	True,
			'admin'		: 	False}