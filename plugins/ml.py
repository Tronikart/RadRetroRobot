from utils import *

print ('loading ' + __name__)

def action(bot, update, args):
	search = ' '.join(args)
	cid = getCID(update)
	try:
		if search:
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
				titulo = result['title']
				state = result['seller_address']['state']['name']
				precio = str(result['price'])
				precio = " Bs. " + precio  
				listing += u"`> `" + "[" + titulo + "]" +"(" + perma + ")" + "`\n" + precio + "`\n  `" + state + " - `" + condicion + "\n  `Cant: " + cantidad + " | Vendidos: " + vendidos + "`" + mercadopago + "\n"
			final_message = u"`Top 5 resultados para "+ query + ": `\n" + listing
			if listing:
				bot.send_message(cid, final_message, parse_mode="Markdown")
			else:
				update.message.reply_text("`La busqueda no arrojo ningun resultado.`", parse_mode="Markdown", reply_to_message_id=update.message.message_id)
		else:
			update.message.reply_text( "`Spanish exclusive command\n\nBusqueda de articulos en MercadoLibre.com.ve`", parse_mode="Markdown", reply_to_message_id=update.message.message_id)
	except:
		update.message.reply_text( "Something went wront, please try again later.", parse_mode="Markdown", reply_to_message_id=update.message.message_id)

info = {	'triggers'	: 	('ml', 'mercadolibre'),
			'name'		:	'MercadoLibre',
			'help'		: 	'Spanish exclusive command\n\nBusqueda de articulos en MercadoLibre.com.ve',
			'example'	:	'/ml Marcadores',
			'active'	: 	True,
			'admin'		: 	False,
			'arguments' :	"<Producto>"}

