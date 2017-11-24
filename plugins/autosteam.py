from utils import *

print ('loading ' + __name__)

def action(bot, update):
	cid = getCID(update)
	url = re.findall(r'(http[s]?://(?:store.steampowered.com/app+.*\S*))+', update.message.text)
	url = url[0]
	request = requests.get(url)
	print (url)
	if request.status_code == 200:
		# try:
		soup = makesoup(url)
		description = soup.find('div', class_='game_description_snippet').string.replace("\t","")
		review_points = soup.find('span', class_='game_review_summary')
		review_points = review_points.string if review_points else ""
		release_date = soup.find('div', class_='date').string
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
		bot.send_message(cid, u"`> {title} {price} \n\n {description}\n\nUser reviews: {reviews}\nRelease date: {release_date}`".format(title=title, price=price, description=description, reviews = review_points, release_date=release_date) + u"[​]({image_prev})\n\n [More info]({url})".format(image_prev=img, url=url), parse_mode="Markdown")
		# except:
		# 	pass
	else:
		pass

info = {	'triggers' 	:	r'.*http[s]?://store.steampowered.com/app+.*\S*.*',
			'active'	: 	True,
			'admin'		: 	False}