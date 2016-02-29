#!/usr/bin/env python
# -*- coding: utf-8 -*-

from utils import *

print "Loading " + __name__ + "..."

# Steam Game page

@bot.message_handler(commands=['steampage'])
def steam_page(message):
	if intime(message):
		appid = getContent(message)
		cid = getCID(message)
		if appid and appid != "-?":
			url = "http://store.steampowered.com/app/" + appid + "/"
			request = requests.get(url)
			if request.status_code == 200:
				try:
					soup = makesoup(url)
					description = soup.find('div', class_='game_description_snippet').string.replace("\t","")
					review_points = soup.find('span', class_='game_review_summary')
					review_points = review_points.string if review_points else ""
					release_date = soup.find('span', class_='date').string
					price = soup.find('div', class_="game_purchase_action_bg")
					game_state = price.div['class'][0] if price else ""
					future_release = soup.find('div', class_="game_area_comingsoon game_area_bubble")
					if game_state == "discount_block" and not future_release:
						discounted = price.find('div', class_="discount_original_price").string.replace('\t', '').replace("\n","")
						discount = price.find('div', class_="discount_pct").string
						price = price.find('div', class_="discount_final_price").string.replace('\t','').replace('\n','')
						price = discounted + " " + discount + " " + price  
					elif not price:
						price = soup.find('div', class_="game_area_comingsoon game_area_bubble")
						price = price.h1.string
						price = price.replace("\t", "").replace("\n", "")
					else:
						try:
							price = price.div.string
							price = price.replace("\t","")
							price = "- " + price.replace("\n","")
						except:
							price = ""
					img = soup.find('img', class_='game_header_image_full')['src']
					title = soup.find('div', class_='apphub_AppName').string
					bot.send_message(cid,u"`> {title} {price} \n {description}\n\nUser reviews: {reviews}\nRelease date: {release_date}`".format(title=title, price=price, description=description, reviews = review_points, release_date=release_date) + u"[​]({image_prev})\n\n [More info]({url})".format(image_prev=img, url=url), parse_mode="Markdown")
				except:
					bot.send_message(cid, u"`Sorry, I did not find any game with that ID, please try again or look it up with /steamid`", parse_mode="Markdown")
			else:
				bot.reply_to(message, "`There has been an error, the number {error} to be specific.`".format(error=request.status_code), parse_mode="Markdown")

		else:
			bot.reply_to(message, "`Follow this command with the ID of a steam game and I will give you its basic information, use /steamid if you dont know the ID of your game.\n\nExample:\n  /steampage 570`", parse_mode="Markdown")
	