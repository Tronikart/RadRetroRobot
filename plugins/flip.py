from utils import *

print ('loading ' + __name__)

def action(bot, update, args):
	cid = getCID(update)
	coin = ['`Heads`', '`Tails`']
	bot.send_message(cid, random.choice(coin), parse_mode="Markdown")

info = {	'triggers'	: 	('flip', 'coin'),
			'name'		:	'Coin flip',
			'help'		: 	'Flips a (virtual) coin and tells you the result.',
			'example'	:	'',
			'active'	: 	True,
			'admin'		: 	False,
			'arguments' :	''}