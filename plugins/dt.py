from utils import *

print ('loading ' + __name__)

def action(bot, update, args):
	uid = getUID(update)
	cid = getCID(update)
	url = "https://s3.amazonaws.com/dolartoday/data.json"
	request = requests.get(url)
	data = request.json()
	if request.status_code == 200:
		dolartoday_usd = data['USD']['dolartoday']
		implicito_usd = data['USD']['efectivo']
		simadi_usd = data['USD']['sicad2']
		btc = data['USD']['bitcoin_ref']
		dolartoday_eur = data['EUR']['dolartoday']
		implicito_eur = data['EUR']['efectivo']
		simadi_eur = data['EUR']['sicad2']
		date = data['_timestamp']['fecha']
		bot.send_message(cid, u"`$ Dolar Today, {date}\n > USD\nDolar Today: Bs. {dolartoday_usd}\nImplicito: Bs. {implicito_usd}\nSimadi: Bs. {simadi_usd}\nDolar Bitcoin: Bs. {btc}\n> EUR \nDolar Today: Bs. {dolartoday_eur}\nImplicito: Bs. {implicito_eur}\nSicad: Bs. {simadi_eur}`".format(date=date, dolartoday_usd=dolartoday_usd, implicito_usd=implicito_usd, simadi_usd=simadi_usd, dolartoday_eur=dolartoday_eur, implicito_eur=implicito_eur, simadi_eur=simadi_eur, btc=btc), parse_mode="Markdown")
	else:
		update.message.reply_text("`There has been an error, the number {error} to be specific.`".format(error=request.status_code), parse_mode="Markdown", reply_to_message_id=update.message.message_id)

info = {	'triggers'	:	('dt', 'dolartoday', 'dolortoday'),
			'name'		:	'DolarToday',
			'help'		: 	'Valores actualizados de dolartoday. Exclusive for Venezuela',
			'example'	:	'',
			'active'	: 	True,
			'admin'		: 	False,
			'arguments' :	''}
