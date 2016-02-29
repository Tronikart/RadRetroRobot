#!/usr/bin/env python
# -*- coding: utf-8 -*-

from utils import *

print "Loading " + __name__ + "..."

# Tweet

@bot.message_handler(commands=['tw'])
def tweetadm(message):
	tweet = getContent(message)
	if message.from_user.id == adminid:
		if len(tweet) <= 140:
			api.update_status(unicode(tweet))
			bot.send_message(adminid, "`Tweet sent.`", parse_mode="Markdown")
		else:
			bot.reply_to(message, "`Tweet is " + str(len(tweet) - 140) + " characters longer than accepted lenght`", parse_mode="Markdown")
	else:
		bot.reply_to(message, "`Access Denied.`", parse_mode="Markdown")

# Broadcast
@bot.message_handler(commands=['broadcast'])
def broadcast_group(message):
	if intime(message):
		uid = getUID(message)
		if uid == adminid:
			content = getContent(message)
			for group in loadjson("grouplist").keys():
				if str(group) not in loadjson("quietlist"):
					bot.send_message(group, "`{content}`".format(content=content), parse_mode="Markdown")
			bot.send_message(adminid, "`{content}`".format(content=content), parse_mode="Markdown")
			bot.send_message(adminid,  "`{content}`".format(content=content) + "`\n\nBroadcasted`", parse_mode="Markdown")


# Py

@bot.message_handler(commands=['py'])
def pypy(message):
	uid = getUID(message)
	content = getContent(message)
	if uid == adminid:
		try:
			eval(content)
		except SyntaxError as e:
			bot.send_message(adminid, e)
		except:
			bot.reply_to(message, "_error_", parse_mode="Markdown")


# Update comic list

@bot.message_handler(commands=['updatecomics'])
def updatecomics(message):
	if intime(message):
		uid = getUID(message)
		cid = getCID(message)
		if uid == adminid:
			with open('comics.json') as f:
				comiclist = json.load(f)
			# Explosm
			url = "http://explosm.net/comics/archive"
			soup = makesoup(url)
			lastch = re.findall(r'/+comics/(\d+)', soup.h3.a['href'])
			comiclist['explosm'] = lastch[0]
			bot.send_message(cid, "`Explosm updated`", parse_mode="Markdown")
			# xkcd
			url = "http://xkcd.com/info.0.json"
			data = getJson(url)
			comiclist['xkcd'] = str(data['num'])
			bot.send_message(cid, "`xkcd updated`", parse_mode="Markdown")
			# Mr Lovenstein
			url = "http://www.mrlovenstein.com/archive"
			soup = makesoup(url)
			comic = soup.find('div', class_='comic_title')
			lastml = re.findall(r'/+comic/(\d+)', comic.a['href'])
			comiclist['mrlove'] = lastml[0]
			bot.send_message(cid, "`Mr Lovenstein updated`", parse_mode="Markdown")
			# Nerf Now
			url = "http://www.nerfnow.com/archives"
			soup = makesoup(url)
			comic = soup.find('li').a['href']
			lastnn = re.findall(r'/+comic/(\d+)', comic)
			comiclist['NN'] = lastnn[0]
			bot.send_message(cid, "`Nerf Now updated`", parse_mode="Markdown")
			# Extrafabulouscomics
			url = "http://extrafabulouscomics.com/feed/"
			soup = makesoup(url)
			comic = soup.channel.item.title.contents[0]
			lastefc = comic.replace("s", "")
			comiclist['EFC'] = lastefc
			bot.send_message(cid, "`Extrafabulouscomics updated`", parse_mode="Markdown")
			with open('comics.json', 'w') as f:
				json.dump(comiclist, f)



# Send Message

@bot.message_handler(commands=['message', 'sendmessage'])
def sendmessageto(message):
	if intime(message):
		uid = getUID(message)
		if uid == adminid:
			cid = re.findall(r'\w+[@RadRetroRobot]*\s+(\S+)\s+(.*)', message.text, re.DOTALL)
			try:
				content = cid[0][1]
				content = content.encode('utf-8')
				cid = cid[0][0]
				bot.send_message(cid, "`{cid}`".format(cid=content), parse_mode="Markdown")
			except:
				print "error"
				print cid
				print content

# Votekick init

@bot.message_handler(commands=['votekick'])
def votekick_init(message):
	if intime(message):
		cid = getCID(message)
		uid = getUID(message)
		userToKick = getContent(message)
		isUser = True
		voteKick_keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
		voteKick_keyboard.add('Yes', "No")
		if uid == adminid:
			try:
				rid = message.reply_to_message
				user = (rid.from_user.first_name)
				if user != "None" and user != "Rad Retro Robot":
					bot.send_message(cid, "`Voting to kick {user}, the vote will be open for 30 seconds`\n".format(user=user), reply_markup=voteKick_keyboard ,parse_mode="Markdown") 
					bot.register_next_step_handler(message, vote_step)
				elif user == "Rad Retro Robot":
					bot.send_message(cid, "`No, I dont want to go.`", parse_mode="Markdown")
			except:
				user = userToKick
				if isUser:
					bot.send_message(cid, "`Voting to kick {user}, the vote will be open for 30 seconds`\n".format(user=user), reply_markup=voteKick_keyboard ,parse_mode="Markdown") 
					bot.register_next_step_handler(message, vote_step)
		else:
			bot.send_message(cid, "`Access Denied.`", parse_mode="Markdown")

def vote_step(message):
	cid = getCID(message)
	vote = message.text
	votes = {}
	yes = 0
	no = 0
	#bot.send_message(cid, "`Input your vote:`", parse_mode="Markdown", reply_markup=voteKick_keyboard)
	voteKick_keyboard_hide = types.ReplyKeyboardHide()
	print "vote_step"

	time.sleep(10)
	print "Time"
	print votes
	if message.text == "Yes":
		yes += 1
		print "yes+"
		votes.update({message.from_user.id:vote})
	elif message.text == "No":
		no += 1
		print "+no"
		votes.update({message.from_user.id:vote})
	else:
		pass

	print votes
	bot.send_message(cid, "`No more votes allowed, you can now count the votes.`", parse_mode="Markdown", reply_markup=voteKick_keyboard_hide)


