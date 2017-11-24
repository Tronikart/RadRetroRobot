from utils import *

print ('loading ' + __name__)

def action(bot, update, args):
	appid = ' '.join(args)
	cid = getCID(update)
	if appid:
		url = "http://store.steampowered.com/app/" + appid + "/"
		request = requests.get(url)
		if request.status_code == 200:
			if len(request.history) < 1:
				try: 
					soup = makesoup(url)
					details = soup.findAll('div', class_="block responsive_apppage_details_left")
					detlist = ""
					for detail in details[0].find_all('div'):
						if detail.text:
							detlist += "> " + detail.text + "\n"
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
					title = soup.findAll('div', class_='apphub_AppName')
					title = title[0].string
					bot.send_message(cid,u"`- {title} {price}\n{detlist}`".format(title=title, price=price, detlist=detlist) + "\n\n[More info]({url})".format(url=url) , parse_mode="Markdown", disable_web_page_preview=True)
				except:
					bot.send_message(cid, "`Sorry, I did not find any game with that ID, please try again or look it up with /steamid`", parse_mode="Markdown")					
			else:
				bot.send_message(cid, u"`This game requires you to pass an age check, Im so sorry user but Im not even a year old, all I can do is give you this link `[steam page](" + url + ")", parse_mode="Markdown", disable_web_page_preview=True)
		else:
			update.message.reply_text("`There has been an error, the number {error} to be specific.`".format(error=request.status_code), parse_mode="Markdown", reply_to_message_id=update.message.message_id)
	else:
		update.message.reply_text("`Follow this command with the ID of a steam game and I will give you its details, use /steamid if you dont know the ID of your game.\n\nExample:\n  /steamdetails 570`", reply_to_message_id=update.message.message_id)

info = {	'triggers'	: 	('steamdetails', 'sd'),
			'name'		:	'Steam Details',
			'help'		: 	"Follow this command with the ID of a steam game and I will give you its details, use /steamid if you dont know the ID of your game.",
			'example'	:	'/steamdetails 504370',
			'active'	: 	True,
			'admin'		: 	False,
			'arguments' :	"<steamid>"}