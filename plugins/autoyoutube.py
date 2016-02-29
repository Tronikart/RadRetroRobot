#!/usr/bin/env python
# -*- coding: utf-8 -*-

from utils import *

print "Loading " + __name__ + "..."

# auto youtube
@bot.message_handler(func=lambda message: "youtube.com/watch" in message.text or "https://youtu.be/" in message.text)
def autoyoutube(message):
	if intime(message):
		cid = getCID(message)
		try:
			url = re.findall(r'(http[s]?://www\.youtube\.com/watch\?v.*)\s?|(http[s]?://youtu\.be/.*)\s?', message.text)
			url = url[0][0] if url[0][0] else url[0][1]
			bot.send_chat_action(cid, "typing")
			soup = makesoup(url)
			channel_info = soup.find("div", class_="yt-user-info")
			channel_name = channel_info.a.string
			channel_url = "http://www.youtube.com" + channel_info.a['href']
			view_count = soup.find('div', class_="watch-view-count").string
			subs = soup.find('span', class_="yt-subscription-button-subscriber-count-branded-horizontal yt-subscriber-count").string
			bot.reply_to(message, "[" + channel_name + "](" + channel_url + ")" + "\n`Subs: " + subs + "\nViews on video: " + view_count + "`", parse_mode="Markdown", disable_web_page_preview=True)
		except:
			pass
