from utils import *

print ('loading ' + __name__)

def action(bot, update, args):
	cid = getCID(update)
	url = "https://github.com/Tronikart/RadRetroRobot"
	bot.send_message(cid, "`> RadRetroRobot\n\nA multi-functional bot made by` @PEWPEWPEW\n\n[Source available here](" + url + ")\n\n`Please do report any bug you find, you can read the source page for a full list of all of RRRs functions and features.\n\nBeep boop!`", parse_mode="Markdown", disable_web_page_preview=True)


info = {	'triggers'	:	'about',
			'name'		:	"about",
			'help'		: 	"Returns basic information about the bot and developer.",
			'example'	:	"",
			'active'	: 	True,
			'admin'		: 	False,
			'arguments' :	""}