#!/usr/bin/env python
# -*- coding: utf-8 -*-

from utils import *

print "Loading " + __name__ + "..."

# Reddit comment thing

@bot.message_handler(func=lambda message: "www.reddit.com/r/" in message.text and "/comments/" in message.text)
def reddit_selfpost(message):
	if intime(message):
		cid = getCID(message)
		sub = ""
		try:
			url = re.findall(r'(http[s]?://(?:www.reddit.com/r/+.*/comments/+\S*))+', str(message.text))
			url = url[0] + ".json"
			request = requests.get(url, headers = {'User-agent': reddit_user})
			data = request.json()
			if request.status_code == 200:
				try:
					post = data[0]['data']['children'][0]['data']
					selftext = unicode(post['selftext'])
					poster = unicode(post['author'])
					sub = unicode(post['subreddit'])
					title = unicode(post['title'])
					up = unicode(post['ups'])
					comments = unicode(post['num_comments'])
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
							bot.reply_to(message, self_post, parse_mode="Markdown", disable_web_page_preview = True)
						else:
							if post['over_18']:
								self_post = "`"+title+"\nby /u/"+poster+" on /r/"+sub+"`\n\n`"+"The text from this post excedes my text message limit\n\n"+"<"+isNsfw+">" +" | "+up+" upvotes"+" | "+comments+" comments`"
							else:
								if len(title) > 57:
									self_post = "`"+title+"\nby /u/"+poster+"`\n\n`"+"The text from this post excedes my text message limit\n\n"+"<"+isNsfw+">" +" | "+up+" upvotes"+" | "+comments+" comments`"	
								else:
									self_post = "`by /u/"+poster+"`\n\n`"+"The text from this post excedes my text message limit\n\n"+"<"+isNsfw+">" +" | "+up+" upvotes"+" | "+comments+" comments`"
							bot.reply_to(message, self_post_long, parse_mode="Markdown", disable_web_page_preview = True)
					elif not post['is_self']:
						if post['over_18']:
							not_self_post = "`"+title+"\nby /u/"+poster+" on /r/"+sub+"\n<"+isNsfw+">" +" | "+up+" upvotes"+" | "+comments+" comments`"
						else:
							if len(title) > 57:
								not_self_post = "`"+title+"\nby /u/"+poster+" - <"+isNsfw+">`"
							else:
								not_self_post = "`by /u/"+poster+" - <"+isNsfw+">`"
						bot.reply_to(message, not_self_post, parse_mode="Markdown", disable_web_page_preview = True)
					else:
						pass
				except:
					pass
			else:
				pass
		except:
			pass
