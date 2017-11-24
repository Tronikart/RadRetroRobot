from utils import *

print ('loading ' + __name__)

def action(bot, update, args):
	cid = getCID(update)
	if update.message.chat.type == "private":
		bot.send_message(cid, u'`> Steam related commands:`\n\n`I will also auto detect steam store links and return the games information.`', parse_mode="Markdown", reply_markup=markup)
	else:
		bot.send_message(cid, "`> Steam related commands:`\n\n`/steamid <game> - Returns the games ID\n  /steampage <ID> - Returns the games information\n  /steamdetails <ID> - Game details such as single player or multiplayer\n  /steamnews <ID> - Returns the last new from a game, it may contain weird formating.`", parse_mode="Markdown")

info = {	'triggers'	: 	'steam',
			'name'		:	'Steam',
			'help'		: 	"Returns every Steam related command.",
			'active'	: 	True,
			'admin'		: 	False,
			'arguments' :	""}