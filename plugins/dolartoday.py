#!/usr/bin/env python
# -*- coding: utf-8 -*-

from utils import *

print "Loading " + __name__ + "..."

# Dolar today

@bot.message_handler(commands=['dt', 'dolartoday', 'dolortoday'])
def dolar_today_message(message):
	if intime(message):
		cid = getCID(message)
		content = getContent(message)
		if content != "-?":
			url = "https://s3.amazonaws.com/dolartoday/data.json"
			request = requests.get(url)
			data = request.json()
			if request.status_code == 200:
				dolartoday_usd = data['USD']['dolartoday']
				implicito_usd = data['USD']['efectivo']
				simadi_usd = data['USD']['sicad2']
				dolartoday_eur = data['EUR']['dolartoday']
				implicito_eur = data['EUR']['efectivo']
				simadi_eur = data['EUR']['sicad2']
				date = data['_timestamp']['fecha']
				bot.send_message(cid, u"`$ Dolar Today, {date}\n > USD\nDolar Today: BsF. {dolartoday_usd}\nImplicito: BsF. {implicito_usd}\nSimadi: BsF. {simadi_usd}\n> EUR \nDolar Today: BsF. {dolartoday_eur}\nImplicito: BsF. {implicito_eur}\nSicad: BsF. {simadi_eur}`".format(date=date, dolartoday_usd=dolartoday_usd, implicito_usd=implicito_usd, simadi_usd=simadi_usd, dolartoday_eur=dolartoday_eur, implicito_eur=implicito_eur, simadi_eur=simadi_eur), parse_mode="Markdown")
			else:
				bot.reply_to(message, "`There has been an error, the number {error} to be specific.`".format(error=request.status_code), parse_mode="Markdown")
		else:
			bot.reply_to(message, "`Venezuela exclusive commmand\n\nInformacion basica desde dolartoday.`", parse_mode="Markdown")
