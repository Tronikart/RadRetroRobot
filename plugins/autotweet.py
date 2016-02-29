#!/usr/bin/env python
# -*- coding: utf-8 -*-

from utils import *

print "Loading " + __name__ + "..."

# auto tweet

@bot.message_handler(func=lambda message: "twitter.com" in message.text and "/status/" in message.text)
def tweepy_f(message):
	if intime(message):
		tweets= ""
		tweet_id = re.findall(r'/status/+(\d*)', unicode(message.text))
		try:
			status = api.get_status(tweet_id[0])
			tweet = status.text
			favs = str(status.favorite_count)
			RTs = str(status.retweet_count)
			user = unicode(status.user.screen_name)
			print user
			url = treatLink("https://twitter.com/" + user)
			print url
			#user = user.replace("_", "")
			print user
			username = unicode(status.user.name)
		except:
			pass
		try:
			try:
				quoted_tweet = status.quoted_status["text"]
				quoted_user = status.quoted_status["user"]["screen_name"]
				quoted_username = status.quoted_status["user"]["name"]
				url = treatLink("https://twitter.com/" + quoted_username)
				bot.reply_to(message, u"`_______quoted tweet_______\n  [" + quoted_username + " " + quoted_user + "](" + url + "`\n" + quoted_tweet + "`\n_____end of quoted tweet_____`\n\n`RTs:{" + RTs + "} | Likes: " + favs + "`", parse_mode="Markdown")
			except:
				if len(tweet) < 110:
					print "long"
					bot.reply_to(message, "[" + username + " - @" + user + "](" + url + ")" + "\n`RTs:" + RTs + " | Likes: " + favs +"`", parse_mode="Markdown", disable_web_page_preview=True)
				else:
					print "short"
					bot.reply_to(message, "[" + username + " - @" + user + "](" + url + ")\n" + tweet + "\n`RTs:" + RTs + " | Likes: " + favs + "`", parse_mode="Markdown", disable_web_page_preview=True)
		except:
			pass
