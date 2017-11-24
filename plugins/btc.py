from utils import *

print ('loading ' + __name__)

def action(bot, update, args):
		try:
			cid = getCID(update)
			url = "https://api.coindesk.com/v1/bpi/currentprice.json"
			data = getJson(url)
			USD = data['bpi']['USD']['rate']
			time = data['time']['updated']
			output = "`1 BTC = $" + USD + "\n\n" + time + "`"
			bot.send_message(cid, output, parse_mode="Markdown")
		except:
			bot.send_message(cid, "`Something went wrong, please wait a moment and try again.`", parse_mode="Markdown")

info = {	'triggers'	:	('btc', 'bitcoin'),
			'name'		:	'bitcoin',
			'help'		: 	"Returns the updated BTC rate from CoinDesk.",
			'example'	:	'',
			'active'	: 	True,
			'admin'		: 	False,
			'arguments' :	""}