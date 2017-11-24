from utils import *

print ('loading ' + __name__)

def action(bot, update, args):
	cid = getCID(update)
	if len(args) >= 2:
		content = ''.join(args[1:])
		content = content.replace(' ', '')
		try:
			if args[0] == '-2b':
				result = text_to_bin(content)
				result = "`{result}`".format(result=str(result))
			elif args[0] == '-2t':
				result = bin_to_text(content)
				result = "`{result}`".format(result=str(result))
			else:
				result = "`Please enter a valid option\n\n> -2b to translate to binary.\n> -2t to translate to text.`"
			update.message.reply_text(result, parse_mode="Markdown", reply_to_message_id=update.message.message_id)
		except:
			update.message.reply_text("`Unexpected error, only ascii characters can be translated to binary, please check your text.`", parse_mode="Markdown", reply_to_message_id=update.message.message_id)
	else:
		update.message.reply_text(get_help(info, __name__), parse_mode="Markdown", reply_to_message_id=update.message.message_id)

info = {	'triggers'	:	'bin',
			'name'		:	'binary',
			'help'		: 	"Convert binary to ASCII and ASCII to binary.",
			'example'	:	'/bin -2b beep',
			'active'	: 	True,
			'admin'		: 	False,
			'arguments' :	"<-2b | -2t> <content>"}