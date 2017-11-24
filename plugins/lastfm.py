from utils import *

print ('loading ' + __name__)

def action(bot, update, args):
	cid = getCID(update)
	uid = getUID(update)
	bot.send_message(cid, "`Last FM related commands: \n\n  /fmuser <username> - sets your username for these commands\n  /fmtop - shows your top 5 artists from last week\n  /fmalbums - shows your top 5 albums from last week.\n  /np - shows what you are currently listening to\n  /fmgrid - shows a grid of your last week albums\n  send /fmgrid -? for more options`", parse_mode="Markdown")


info = {	'triggers'	: 	'lastfm',
			'name'		:	'Last FM Commands',
			'help'		: 	'Get a list of all lastfm related commands.',
			'example'	:	'',
			'active'	: 	True,
			'admin'		: 	False,
			'arguments' :	""}