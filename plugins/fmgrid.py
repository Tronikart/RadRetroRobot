from utils import *

print ('loading ' + __name__)

def action(bot, update, args):
	cid = getCID(update)
	uid = str(getUID(update))
	options = args
	fmUsers = loadjson("userlist")
	validTypes = ["7days", "1month", "3month", "6month", "12month", "overall"]
	validSizes = ["3x3", "4x4", "5x5"]
	if fmUsers[uid]['fmuser']:
		try:
			if options:
				print (options)
				gridtype = ''.join(options[0:1]) if len(options) > 2 else options[0]
				gridsize = options[2] if len(options) > 2 else options[1]
				if gridtype.lower() in validTypes:
					pass
				else:
					gridtype = "7day"
				if gridsize.lower() in validSizes:
					pass
				else:
					gridsize = "3x3"
			else:
				gridtype = "7day"
				gridsize = "3x3"
			url = "http://www.tapmusic.net/collage.php?type=" + gridtype + "&size=" + gridsize + "&user=" + fmUsers[uid]['fmuser']
			soup = makesoup(url)
			if "Error" in soup.text:
				update.message.reply_text("`There has been an error, heres some info:`\n\n" + "`" + soup.text + "`", parse_mode="Markdown", reply_to_message_id=update.message.message_id)
			else:
				update.message.reply_text(url, reply_to_message_id=update.message.message_id)
		except:
			update.message.reply_text("`Something went wrong, sorry try again later.`", parse_mode="Markdown", reply_to_message_id=update.message.message_id)
	else:
		update.message.reply_text("`Please set your username with /fmuser, preferably from PM.`", parse_mode="Markdown", reply_to_message_id=update.message.message_id)
		return

info = {	'triggers'	: 	'fmgrid',
			'name'		:	'Last FM Grid',
			'help'		: 	'This command will return a grid with your last listened albums here are the options you can set\n\n /fmgrid <type> <size>\nTypes: 7 day, 1 month, 3 months, 6 months, 12 months, Overall.\nSize: 3x3, 4x4, 5x5\n\nBy default this command will give you a 3x3 grid from last week\nYou need to set up your Last fm user with /fmuser',
			'example'	:	'/fmgrid 1 month 5x5',
			'active'	: 	True,
			'admin'		: 	False,
			'arguments' :	"[type] [size]"}

