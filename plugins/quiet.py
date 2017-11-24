from utils import *

print ('loading ' + __name__)

def action(bot, update, args):
	cid = getCID(update)
	cid = str(cid)
	if update.message.chat.type == 'group' or update.message.chat.type == 'supergroup':
		action = args[0]
		gName = (update.message.chat.title)
		if action:
			if action == "-add":
				if cid in loadjson("quietlist") or gName in loadjson("quietlist"):
					update.message.reply_text("`This group is already on the quiet list, if you desire to remove it, send /quiet -remove`", parse_mode="Markdown", reply_to_message_id = update.message.message_id)
				else:
					addUser(cid, gName, "quietlist")
					update.message.reply_text("`This group has been added to the quiet list, I will now only answer when called and to commands.`", parse_mode="Markdown", reply_to_message_id = update.message.message_id)
			elif action == "-remove":
				if cid in loadjson("quietlist"):
					deljson(cid, "quietlist")
					update.message.reply_text("`This group has been removed from the quiet list, I will now randomly beep, boop, repeat and broadcast!`", parse_mode="Markdown", reply_to_message_id = update.message.message_id)
				else:
					update.message.reply_text("`Couldnt find this group on the quiet list, if you desire to add it, send /quiet -add`", parse_mode="Markdown", reply_to_message_id = update.message.message_id)
			else:
				update.message.reply_text("`Invalid input, only -add and -remove accepted.`", parse_mode="Markdown", reply_to_message_id = update.message.message_id)
		else:
			update.message.reply_text("`> There are two options available:\n/quiet -add\n/quiet -remove\n\nI will stop randomly beeping, booping, repeating and broadcasting if you add this group to the quiet list`", parse_mode="Markdown", reply_to_message_id = update.message.message_id)
	else:
		update.message.reply_text("`This option is only available for groups.`", parse_mode="Markdown", reply_to_message_id = update.message.message_id)

info = {	'triggers'	: 	'quiet',
			'name'		:	'Quiet',
			'help'		: 	"This command will add(-add) or remove(-remove) a group from the quiet list, and I will only talk when commands are given to me.",
			'example'	:	'/quiet -add',
			'active'	: 	True,
			'admin'		: 	False,
			'arguments' :	"<option>"}