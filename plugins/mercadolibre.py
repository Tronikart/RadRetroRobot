#!/usr/bin/env python
# -*- coding: utf-8 -*-

from utils import *

print "Loading " + __name__ + "..."

# Mercadolibre

@bot.message_handler(commands=['ml', 'mercadolibre', 'ML','MercadoLibre'])
def mercadolibre(message):
	if intime(message):
		search = getContent(message)
		cid = getCID(message)
		try:
			if search and search != "-?":
				url = "https://api.mercadolibre.com/sites/MLV/search?q=" + search + "#json"
				data = getJson(url)
				query = data['query']
				listing = ""
				for result in data['results'][0:5]:
					if result['accepts_mercadopago']:
						mercadopago = "\n` MercadoPago`"
					else:
						mercadopago = ""
					cantidad = str(result['available_quantity'])
					if result['condition'] == 'new':
						condicion = "`Nuevo`"
					else:
						condicion = "`Usado`"
					perma = result['permalink']
					perma = treatLink(perma)
					vendidos = str(result['sold_quantity'])
					titulo = unicode(result['title'])
					state = result['seller_address']['state']['name']
					precio = str(result['price'])
					precio = " Bs. " + precio  
					listing += u"`> `" + "[" + titulo + "]" +"(" + perma + ")" + "`\n" + precio + "`\n  `" + state + " - `" + condicion + "\n  `Cant: " + cantidad + " | Vendidos: " + vendidos + "`" + mercadopago + "\n"
				final_message = u"`Top 5 resultados para "+ query + ": `\n" + listing
				if listing:
					bot.send_message(cid, final_message, parse_mode="Markdown")
				else:
					bot.reply_to(message, "`La busqueda no arrojo ningun resultado.`", parse_mode="Markdown")
			else:
				bot.reply_to(message, "`Spanish exclusive command\n\nBusqueda de articulos en MercadoLibre.com.ve`", parse_mode="Markdown")
		except:
			bot.reply_to(message, "Something went wront, please try again later.", parse_mode="Markdown")
		