from utils import *

print ('loading ' + __name__)

def action(bot, update, args):
	uid = getUID(update)
	cid = getCID(update)
	if uid == adminid:
		userlist = loadjson("userlist")
		users = str(len(userlist))
		temp = []
		for user in userlist:
			if userlist[user]['fmuser']:
				temp.append(user)
			else:
				continue
		lastfm_users = str(len(temp))
		groups = str(len(loadjson("grouplist")))
		now = datetime.now()
		diff = now - uptime
		days, seconds = diff.days, diff.seconds
		hours = days * 24 + seconds // 3600
		minutes = (seconds % 3600) // 60
		seconds = seconds % 60
		total_uptime = str(days) + "d " + str(hours) + "h " + str(minutes) + "m " + str(seconds) + "s"
		bot.send_message(cid,"`" + users + " registered users\n" + lastfm_users + " registered lastfm users\n" + groups + " registered groups\n\nTotal Uptime: " + total_uptime + "`", parse_mode="Markdown")

info = {	'triggers'	: 	'stats',
			'name'		:	'statistics',
			'help'		: 	"General information of the bot's activity.",
			'example'	:	'',
			'active'	: 	True,
			'admin'		: 	True,
			'arguments' :	""}