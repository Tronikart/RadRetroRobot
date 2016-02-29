#!/usr/bin/env python
# -*- coding: utf-8 -*-

from utils import *
 
print "Loading " + __name__ + "..."

# Reddit

@bot.message_handler(commands=['r'])
def reddit(message):
	if intime(message):
		cid = getCID(message)
		isSub = False
		sub = message.text
		sub = getContent(message)
		sub = re.findall(r'/*r*\s*(\S*)', sub)
		print sub
		try:
			sub = "r/" + sub[0]
		except:
			sub = "r/" + sub
		print sub
		if sub != "-?" and sub:
			url = "http://www.reddit.com/" + sub + "/.json?limit=6"
			subreddit =  "http://www.reddit.com/" + sub
			request = requests.get(url, headers = {'User-agent': reddit_user})
			data = request.json()
			posts = ""
			if request.status_code == 200:
				for post in data['data']['children']:
					domain = post['data']['domain']
					title = treatTitle(post['data']['title'])
					pUrl = treatLink(post['data']['url'])
					isNsfw_bool = post['data']['over_18']
					permalink =  "http://www.reddit.com" + post['data']['permalink']
					if isNsfw_bool:
						isNsfw = "nsfw"
					else:
						isNsfw = "sfw"
					post = (u"`> `[{title}]({pUrl})` <{nsfw}> - `[comments]({permalink})\n").format(title=title, permalink=permalink, nsfw=isNsfw, pUrl=pUrl, domain=domain)
					posts += post
				if posts:
					bot.send_message(cid, u"[{sub}]({subreddit})`:`\n\n".format(sub=sub, subreddit=subreddit) + posts, parse_mode="Markdown", disable_web_page_preview=True)
				else:
					bot.send_message(cid, u"`I couldnt find {sub}, please try again`".format(sub=sub), parse_mode="Markdown",disable_web_page_preview=True)
			elif request.status_code == 403:
				bot.reply_to(message, "`Subreddit not found, please verify your input.`", parse_mode="Markdown")
			else:
				bot.reply_to(message, "`There has been an error, the number {error} to be specific.`".format(error=request.status_code), parse_mode="Markdown")
		else:
			bot.send_message(cid, "`Follow this command with r/ and the name of a subreddit to see the top 6 posts.\nExample: /r r/Aww`", parse_mode="Markdown")
