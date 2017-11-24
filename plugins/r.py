from utils import *

print ('loading ' + __name__)

def action(bot, update, args):
	cid = getCID(update)
	sub = ''.join(args)
	if sub:
		sub = re.findall(r'\S*', sub)
		sub = "r/" + sub[0] if sub[0:2] != "r/" else sub[0]
		url = "http://www.reddit.com/" + sub + "/.json?limit=6"
		subreddit =  "http://www.reddit.com/" + sub
		request = requests.get(url, headers = {'User-agent': reddit_user})
		data = request.json()
		posts = ""
		if request.status_code == 200:
			for post in data['data']['children']:
				domain = post['data']['domain']
				title = treatTitle(post['data']['title'])
				pUrl = treatLink(post['data']['url'])
				isNsfw_bool = post['data']['over_18']
				permalink =  "http://www.reddit.com" + post['data']['permalink']
				if isNsfw_bool:
					isNsfw = "nsfw"
				else:
					isNsfw = "sfw"
				post = (u"`> `[{title}]({pUrl})` <{nsfw}> - `[comments]({permalink})\n").format(title=title, permalink=permalink, nsfw=isNsfw, pUrl=pUrl, domain=domain)
				posts += post
			if posts:
				bot.send_message(cid, u"[{sub}]({subreddit})`:`\n\n".format(sub=sub, subreddit=subreddit) + posts, parse_mode="Markdown", disable_web_page_preview=True)
			else:
				bot.send_message(cid, u"`I couldnt find {sub}, please try again`".format(sub=sub), parse_mode="Markdown",disable_web_page_preview=True)
		elif request.status_code == 403:
			update.message.reply_text( "`Subreddit not found, please verify your input.`", parse_mode="Markdown", reply_to_message_id=update.message.message_id)
		else:
			update.message.reply_text("`There has been an error, the number {error} to be specific.`".format(error=request.status_code), parse_mode="Markdown", reply_to_message_id=update.message.message_id)
	else:
		bot.send_message(cid, "`Follow this command with the name of a subreddit to see the top 6 posts.\nExample: /r Awww`", parse_mode="Markdown")

info = {	'triggers'	: 	('r', 'reddit'),
			'name'		:	'Reddit',
			'help'		: 	"Follow this command with the name of a subreddit to see the top 6 posts.",
			'example'	:	'/r Awww',
			'active'	: 	True,
			'admin'		: 	False,
			'arguments' :	"<subreddit>"}