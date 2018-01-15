from utils import *

print ('loading ' + __name__)

def action(bot, update, args):
		try:
			search = ' '.join(args)
			cid = getCID(update)
			if search:
				url = "https://api.coinmarketcap.com/v1/ticker/"
				data = getJson(url)
				found = False
				for coin in data:
					if coin['symbol'].lower() == search.lower():
						result = coin
						found = True
						break
					else:
						pass
				if found:
					output = "`" + result['name'] + " - " + result['symbol'] + "\n\nPrice USD: $" + result['price_usd'] + "\nPrice BTC: ฿" + result['price_btc'] + "\n\nVolume (24h): $" + result['24h_volume_usd'] + "\nMarket Cap: $" + result['market_cap_usd'] + "\nCirculating Supply:" + result['available_supply'] + " " + result['symbol']  + "\n\nChanges:\n    1h: " + result['percent_change_1h'] + "\n    24h: " + result['percent_change_24h'] + "\n    7d:" + result['percent_change_7d'] + "\n\nLast updated: " + datetime.fromtimestamp(int(result['last_updated'])).strftime('%Y-%m-%d %H:%M:%S') + "`"
					bot.send_message(cid, output, parse_mode="Markdown")
				else:
					bot.send_message(cid, "`Couldnt find the coin, make sure you are using the abbreviation or symbol instead of the full name. i.e. BTC instead of Bitcoin.`", parse_mode="Markdown")
			else:
				bot.send_message(cid, get_help(info), parse_mode="Markdown")
		except:
			bot.send_message(cid, "`Something went wrong, please wait a moment and try again.`", parse_mode="Markdown")

info = {	'triggers'	:	'crypto',
			'name'		:	'crypto',
			'help'		: 	"Returns updated information of a given cryptocurrency symbol.",
			'example'	:	'/crypto BTC',
			'active'	: 	True,
			'admin'		: 	False,
			'arguments' :	"<crypto symbol>"}
