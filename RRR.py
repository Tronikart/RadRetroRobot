import plugins

from utils import *
from plugins import * 

updater = Updater(token=config['bot'])
dispatcher = updater.dispatcher

for plugin in plugins.__all__:
	active = eval(plugin).info['active']
	if "auto" not in plugin:
		if active:
			handler = CommandHandler(eval(plugin).info['triggers'], eval(plugin).action, pass_args=True)
			dispatcher.add_handler(handler)
		else:
			pass
	else:
		if active:
			handler = RegexHandler(eval(plugin).info['triggers'], eval(plugin).action)
			dispatcher.add_handler(handler)
		else:
			pass

handler = MessageHandler(Filters.text, plugins.autoMessages.action)
dispatcher.add_handler(handler)

class RegexFilter(BaseFilter):
	def filter(self, message):
		return '/s/' == message.text[0:3]

def regex(bot, update):
	try:
		cid = getCID(update)
		rid = update.message.reply_to_message
		content = update.message.text
		if content.split('/')[1] == 's':
			lookfor = r"" + content.split('/')[2]
			replacewith = r"" + content.split('/')[3]
			final_text = re.sub(lookfor, replacewith, rid.text)
			update.message.reply_text("`" + final_text + "`", parse_mode="Markdown", reply_to_message_id=update.message.message_id)
		else:
			pass
	except:
		pass

regex_filter = RegexFilter()
dispatcher.add_handler(MessageHandler(Filters.command & regex_filter, regex))
def help(bot, update, args):
	"""
	Returns the help for any given command, if more than one, will make a single message with them
	if no command, will return all the active commands
	"""
	UID = getUID(update)
	CID = getCID(update)
	# If theres only one command
	if len(args) == 1:
		# Check if exists
		try: 
			command = eval(args[0].lower())
			# Check if its active
			if command.info['active']:
				if type(command.info['triggers']) == tuple:
						triggers =  "\n\n    Alternative Triggers:"
						for trigger in command.info['triggers']:
							triggers += "\n        " + trigger
				else:
					triggers = ""
				# Check if its admin command and if user is admin
				if command.info['admin'] and UID == adminid:
					# Has example?
					if command.info['example']:
						bot.send_message(CID,"`> " + command.info['name'] + " [admin]`\n\n    /" + args[0] + " `" + command.info['arguments'] + "\n\n    " + command.info['help'].replace('\n', '\n    ') + "\n\n    Example:\n        " + command.info['example'].replace('\n', '\n        ') + triggers + "`", parse_mode="Markdown")
					else:
						bot.send_message(CID,"`> " + command.info['name'] + " [admin]`\n\n    /" + args[0] + " `" + command.info['arguments'] + "\n\n    " + command.info['help'].replace('\n', '\n    ') + triggers + "`", parse_mode="Markdown")
				elif not command.info['admin']:
					# Has example?
					if command.info['example']:
						bot.send_message(CID,"`> " + command.info['name'] + "`\n\n    /" + args[0] + " `" + command.info['arguments'] + "\n\n    " + command.info['help'].replace('\n', '\n    ') + "\n\n    Example:\n        " + command.info['example'].replace('\n', '\n        ') + triggers + "`", parse_mode="Markdown")
					else:
						bot.send_message(CID,"`> " + command.info['name'] + "`\n\n    /" + args[0] + " `" + command.info['arguments'] + "\n\n    " + command.info['help'].replace('\n', '\n    ') + triggers + "`", parse_mode="Markdown")
				else:
					pass
		except:
			bot.send_message(CID, "`Theres no " + args[0] +" command.`", parse_mode="Markdown" )

	# If theres more than one command
	elif len(args) > 1:
		message = ""
		for arg in args:
			try:
				# Check if exists
				command = eval(arg.lower())
				#Check if its still active
				if command.info['active']:
					if type(command.info['triggers']) == tuple:
						triggers =  "\n\n    Alternative Triggers:"
						for trigger in command.info['triggers']:
							triggers += "\n        " + trigger
					else:
						triggers = ""
					# Check if its admin command and if user is admin
					if command.info['admin'] and UID == adminid:
						# Has example?
						if command.info['example']:
							message += "`> " + command.info['name'] + " [admin]`\n\n    /" + arg + " `" + command.info['arguments'] + "\n\n    " + command.info['help'].replace('\n', '\n    ') + "\n\n    Example:\n        " + command.info['example'].replace('\n', '\n        ') + triggers + "`\n\n"
						else:
							message += "`> " + command.info['name'] + " [admin]`\n\n    /" + arg + " `" + command.info['arguments'] + "\n\n    " + command.info['help'].replace('\n', '\n    ') + triggers + "`\n\n"
					elif not command.info['admin']:
						# Has example?
						if command.info['example']:
							message += "`> " + command.info['name'] + "`\n\n    /" + arg + " `" + command.info['arguments'] + "\n\n    " + command.info['help'].replace('\n', '\n    ') + "\n\n    Example:\n        " + command.info['example'].replace('\n', '\n        ') + triggers + "`\n\n"
						else:
							message += "`> " + command.info['name'] + "`\n\n    /" + arg + " `" + command.info['arguments'] + "\n\n    " + command.info['help'].replace('\n', '\n    ') + triggers + "`\n\n"
					else:
						pass
			except:
				message += "`> " + arg + "\n\n Not found.`\n\n"

		bot.send_message(CID, message, parse_mode="Markdown")
	else:
		message = "`Heres a list of the currently active plugins:\n\n`"
		for plugin in plugins.__all__:
			if "auto" not in plugin:
				# If the plugin is active
				command = eval(plugin)
				if command.info['active']:
					# Check if its admin command and if user is admin
					if command.info['admin'] and UID == adminid:
						message += "`> `/" + plugin.lower() + "` " + command.info['arguments'] + " [admin]`\n"
					elif not command.info['admin']:
						message += "`> `/" + plugin.lower() + "` " + command.info['arguments'] + "`\n"
					else:
						pass
			else:
				pass

		bot.send_message(CID, message + "\n\n`Some of them will work right away, others need extra arguments, to know more about any command, send /help <command>`", parse_mode="Markdown")

def stop_and_restart():
	"""Gracefully stop the Updater and replace the current process with a new one"""
	updater.stop()
	os.execl(sys.executable, sys.executable, *sys.argv)

def restart(bot, update):
	cid = getCID(update)
	if cid == adminid:
		update.message.reply_text('`Bot is restarting...`', parse_mode="Markdown")
		Thread(target=stop_and_restart).start()
			
dispatcher.add_handler(CommandHandler('restart', restart))

help_handler = CommandHandler('help', help, pass_args=True)
dispatcher.add_handler(help_handler)

dispatcher.add_error_handler(error)

updater.start_polling(clean=True)
print ("Running")
bot.send_message(adminid, "*Bot loaded and ready for action!*", parse_mode="Markdown")
updater.idle()
