from utils import *

print ('loading ' + __name__)

def action(bot, update, args):
	cid = getCID(update)
	error = False
	exp = ' '.join(args)
	if exp and cid != main_group:
		payload = {
			'expr': exp,
			'precision': 5
		}
		url = "http://api.mathjs.org/v1/"
		request = requests.get(url, params=payload)
		if request.status_code == 200:
			result_str = "`Result:\n  {data}`"
			result_str = str(result_str)
			data = request.text
			bot.send_message(cid, result_str.format(data=data), parse_mode="Markdown")
		else:
			error_message = "`Theres has been an error, here's some information to help you fix it:\n\n{error}`"
			bot.send_message(cid, error_message.format(error=request.text), parse_mode="Markdown")
	elif cid == main_group:
		pass
	else:
		update.message.reply_text("`" + get_help(info) +  "`", parse_mode="Markdown", reply_to_message_id=update.message.message_id)



info = {	'triggers'	:	'calc',
			'name'		:	'calc',
			'help'		: 	'Returns the result of a math expression.',
			'example'	:	'/calc 2 + 2\n/calc 2 m to in',
			'active'	: 	True,
			'admin'		: 	False,
			'arguments' :	'<expression>'}