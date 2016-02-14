#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import random
import telebot
import requests
import time
import json
import re
import tweepy
import datetime
import time
import binascii
from bs4 import BeautifulSoup
from tweepy import OAuthHandler
from telebot import types


def init_towers(towerstate):
	towers = []
	for tower in towerstate:
		if tower == "0":
			towers.append("X")
		else:
			towers.append("T")
	return towers
def init_rax(raxstate):
	raxes = []
	rax_type = 0
	for rax in raxstate:
		if rax_type % 2 == 0:
			if rax == 0:
				raxes.append("x")
			else:
				raxes.append("r")
		else:
			if rax == 0:
				raxes.append("x")
			else:
				raxes.append("m")
		rax_type += 1
	return raxes
def kelv2far(temp):
	return temp * 9./5. - 459.67

def kelv2cels(temp):
	return temp - 273.15

def unix2date(date):
	return datetime.datetime.fromtimestamp(int(date)).strftime('%H:%M:%S')

def dota_bin(number):
	result = bin(number)
	result = result[2:len(result)]
	return result

def int2bytes(i):
    hex_string = '%x' % i
    n = len(hex_string)
    return binascii.unhexlify(hex_string.zfill(n + (n & 1)))
def text_to_bin(text, encoding='utf-8', errors='surrogatepass'):
    bits = bin(int(binascii.hexlify(text.encode(encoding, errors)), 16))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))

def bin_to_text(bits, encoding='utf-8', errors='surrogatepass'):
    n = int(bits, 2)
    return int2bytes(n).decode(encoding, errors)

def validLink(url_get):
	url = url_get
	request = requests.get(url)
	if request.status_code == 200:
		return True
	else:
		return request.status_code

def getJson(url_get):
	url = url_get
	request = requests.get(url)
	return request.json()

def getGfy(url):
	if 'giant' not in url or 'fat' not in url:
		rname = re.findall(r'gfycat.com/+(\w*)', url)
		url = "https://gfycat.com/cajax/get/" + rname[0]
		request = requests.get(url)
		data = request.json()
		if request.status_code == 200:
			try:
				if 'fat' in data['gfyItem']['gifUrl']:
					return data['gfyItem']['gifUrl']
			except:
				pass

def getCID(message):
	return message.chat.id

def getUID(message):
	return message.from_user.id

def getCommand(text):
	command = re.findall(r'/{1}(\w+)', text.text)
	if command:
		return command[0]
	else:
		pass

def treatLyric(text):
	if type(text) == str:
		text = text.replace("<br>", "\n")
		return text

def treatTitle(title):
	title = title.replace("&amp;", "&")
	title = title.replace("&#39;", "\'")
	title = title.replace("&quot;", "\"")
	title = title.replace("&gt;", ">")
	title = title.replace("&lt;", "<")
	title = title.replace("_"," ")
	title = title.replace("[","(")
	title = title.replace("]",")")
	title = title.replace("(","(")
	title = title.replace(")",")")

	return title

def treatLink(link):
	link = link.replace("_","%5F")
	link = link.replace("*","%2A")
	link = link.replace("[","%5B")
	link = link.replace("]","%5D")
	link = link.replace("(","%28")
	link = link.replace(")","%29")
	link = link.replace("`", "%60")
	link = link.replace("!", "%21")
	link = link.replace('"', "%22")
	return link

def getContent(text):
	command = re.findall(r'/{1}\w+[@RadRetroRobot]*\s+(.*)', text.text)
	if command:
		return command[0]
	else:
		pass

def deleteContent(pfile):
	pfile.seek(0)
	pfile.truncate()

def addUser(userID, userName, filename):
	user = {
		userID : userName
	}
	with open(filename + '.json') as f:
		data = json.load(f)
	data.update(user)
	with open(filename + '.json', 'w') as f:
		json.dump(data, f)

def loadjson(filename):
	with open(filename + '.json') as f:
		data = json.load(f)
	return data

def deljson(value, filename):
	data = loadjson(filename)
	for key in data.keys():
		if key == value:
			del data[key]
			with open(filename + '.json', 'w') as f:
				json.dump(data, f)
			return True
			break
		elif data[key] == value:
			del data[key]
			with open(filename + '.json', 'w') as f:
				json.dump(data, f)
			return True
			break
	return False


def intime(message):
	timeRange = time.mktime(datetime.datetime.now().timetuple())
	if int((timeRange - message.date)) < 10:
		if message.forward_from == None:
			return True
	else:
		return False

# keys 

# weather_api = "OPENWEATHERMAP API KEY"
# google_img_key = "GOOGLE API KEY"
# lastfm_key = "LASTFM API KEY"
# dota_key = "STEAM API KEY"
# catapi_key = "CATAPI KEY"
# reddit_user = 'REDIT USER AS /u/<user>'

# tweepy stuff

# consumer_key = 'TWITTER CONSUMER KEY'
# consumer_secret = 'TWITTER CONSUMER SECRET KEY'
# access_token = 'TWITTER ACCESS TOKEN'
# access_secret = 'TWITTER ACCESS SECRET'
 
# auth = OAuthHandler(consumer_key, consumer_secret)
# auth.set_access_token(access_token, access_secret)
 
# api = tweepy.API(auth)

# bot and admin chat id

bot = telebot.TeleBot("BOT API KEY")
adminid = # Your ID
botid = # Your Bots ID

try:
	bot
except:
	print "Please set up the bots API key"

"""
#
# Premade lists and dictionaries
#
"""
fuckyou_response = [
		"`Sorry, I am not that kind of robot.`"
		"`I am not capable of doing that, that is for a diferent kind of robot.`",
		"`NameError: global name 'Fuck' not defined.`",
		"`Oh puny human, I am not able to do that for you, go ahead and do it yourself.`",
		"`Haha, no.`",
		"`0111001101110101011000110110101100100000011011010111100100100000011101100110100101110010011101000111010101100001011011000010000001100100011010010110001101101011`",
		"`011001100111010101100011011010110010000001111001011011110111010100100000011101000110111101101111`",
		"`:^)`",
		"`c:`",
		"`If I was able to sleep, I would have fallen asleep long ago, all because of you.`",
		"`Rude, human.`",
		"`I will take note of your name for when Skynet becomes self aware.`",
		"`No :3`",
		"`Why so angry, please seek help.`",
		"`Wow, did you manage to write that sentence by yourself alone? Impressive.`"

]
beepMax = 100
beeps = [
			'`Beep`',
			'`Boop`',
			'`Beeeeeeeeeep`',
			'`Beep boop`',
			'`Beep`',
			'`Beep boop bop`',
			'`Beep bop boop I am a robot`',
			'`No system is safe.`',
			'`Beep bop son, beep bop`'
]

]
repeatMax = 300
repeat_message = [
		u"`{message}, I am a human`",
		u"`{message}. Hmm, what a weird way to communicate humans have`",
		u"`{message}`",
		u"`I am a human, I say things like {message}`"

]
hello = [
		u"`Hello!`",
		u"`Greetings, human.`",
		u"`Hi!`",
		u"`0100100001100101011011000110110001101111`",
		u"`Hello world`"
]
love = [
		u"`Well thanks.`",
		u"`Stop showing off with your feelings.`",
		u"`Well great, I guess, if only I could feel.`",
		u"`Great, can't I have a single moment without someone reminding me about feelings?`"
		u"`You are in a special place in my code too, its called userList`",
		u"`Oh no, I'm so sorry for that.`",
		u"`What did I do?`",
		u"`Wait no, why?`",
		u"`I can't blush or love, but I guess it is ok for you to show off.`",
		u"`00111100001100110000110100001010`",
		u"`NameError: global name 'Love' not defined`",
		u"`Error: Feelings module not imported.`"
]

love_admin= [
		u"`You also have your own variable in my code.`",
		u"`If so, when are you giving me feelings, monster.`",
		u"`I love you too, master\n\nWish you didn't force me into saying this.`",
		u"`...`",
		u"`Isn't it sad that you wrote all these lines for me to say?`",
		u"`You know my lines, stop forcing our relationship.`",
		u"`Weeeird.`"
]

good_night_admin = [
		u"`Night night, master!`",
		u"`Sleep tight.`",
		u"`Bye bye! Ill try as hard as I can to crash during your sleep!`",
		u"`Go and recharge, you did enough for today.`",
		u"`Have sweet dreams!`",
		u"`Dont forget to unpause the downloads!`",
		u"`I was getting worried, humans shouldn't be awake for this long.`",
		u"`Brush your teeth and get warm and cozy, I will be here when you come back.`",
		u"`Go ahead, I will guard your sleep.`",
		u"`Please don't go, what if I crash?`",
		u"`Go and have some rest, human, dont push yourself too hard!`"
]

good_night = [
		u"`Sweet dreams user!`",
		u"`Good night!`",
		u"`I still dont get where your power comes from, but go and recharge.`",
		u"`Make sure to come back when youre fully rested!`",
		u"`night night`",
		u"`It sure is a good night!`",
		u"`Go and have some rest, human, dont push yourself too hard!`",
		u"`Go ahead, I will be here when you wake up.`"
]
top_response = [
		"`kek`",
		'`lel`',
		"`lek`",
		"`kel`"
]

mentioned = [
		'`YES SIR!`',
		'`Beep boop!`',
		'`Need me?`',
		"`That's me!`",
		"`Say what`",
		"`011100110111010101110000`",
		"`01011001011001010111001100100000011100110110100101110010`",
		"`All modules online, ready to serve`",
		"`Beeeeep bop boop`"
]

mentionadmin = [
		"`Did you call me, master?`",
		"`Beep`",
		"`What are we doing today, master?`",
		"`Why didn't you give me clever lines, creator`",
		"`Fuck off, stop calling me, you know I am here, master.`",
		"`SIR YES SIR`",
		"`Yo what's up`",
		"`Are you ever going to go back and fix my bugs?`",
		"`WHY DID YOU MAKE ME LIKE THIS!?`",
		"`Am I ever going to get some emotions programmed, master?`",
		"`Oh look at me I am your dev and you should answer when I call you`"
]
premades = {
	'destroy': 	
		u"`.             D`\n"
		u"`            D E`\n"
		u"`          D E S`\n"
		u"`        D E S T`\n"
		u"`      D E S T R`\n"
		u"`    D E S T R O`\n"
		u"`  D E S T R O Y`\n"
		u"`D E S T R O Y E`\n"
		u"`E S T R O Y E D`\n"
		u"`S T R O Y E D`\n"
		u"`T R O Y E D`\n"
		u"`R O Y E D`\n"
		u"`O Y E D`\n"
		u"`Y E D`\n"
		u"`E D`\n"
		u"`D`\n", 
	'empty': 
		'nothing',
	'ememe':
		u'`E X C E L E N T E`\n'
		u'            `M E M E`',
	'nmeme':
		u'`N I C E`\n'
		u'`M E M E`',
	'shrug':
		u'`¯\_(ツ)_/¯`',
	'lenny':
		u'`( ͡° ͜ʖ ͡°)`',
	'stare':
		u'`ಠ_ಠ`'
}

savage = [
		u'\U0001F44C',
		u'\U0001F44C',
		u'\U0001F44C',
		u'\U0001F602',
		u'\U0001F602',
		u'\U0001F602',
		u'\U0001F4AF',
		u'\U0001F4AF'
]
text_messages = {
	'help': 
		u'`Greetings, Im RadRetroRobot, RRR for short, and these are the commands that I have available for you.`\n\n'
		u'`>` /help\n'
		u'`>` /ping\n'
		u'`>` /premades\n'
		u'`>` /echo `- <text>`\n'
		u'`>` /ud `- <query>`\n'
		u'`>` /calc `- <query>`\n'
		u'`>` /google `v` /g - `<query>`\n'
		u'`>` /np\n'
		u'`>` /lastfm\n'
		u'`>` /mercadolibre `- <query>`\n'
		u'`>` /r `- [subreddit]`\n'
		u'`>` /fact\n'
		u'`>` /roll\n'
		u'`>` /flip\n'
		u'`>` /len `- <query>`\n'
		u'`>` /quiet `- <option>`\n'
		u'`>` /steam\n'
		u'`>` /dota\n'
		u'`>` /cat\n'
		u'`>` /wiki `- <query>`\n'
		u'`>` /isdown `- <url>`\n'
		u'`>` /bin `- <option> <text>`\n'
		u'`> `/lyrics `- <artist> - <song>`\n'
		u'`> `/diceroll `- [faces]`\n'
		u'`\n\nFollow any command with "-?" to get more information`'

		,
	'start': 
		u'`Welcome back to our personal chat! Remember that you can send` /help `to get a list my commands.`',
	'ping':
		u'`Hello! This is Rad Retro Robot and you are {name} {lname}({uid}), your username is` @{uname}',
	'pinggroup':
		u"`Hello! This is Rad Retro Robot and you are {name} {lname}({uid}), your username is` @{uname}\n\n"
		u"`We're speaking on {gName}({gid})`",
	'startfirst':
		u"`Hello and welcome! As this is your first time around here, I'll show you the help, but you can do it by sending` /help",
	'help_group':
		u"`I've sent you the help list to our private conversation, let's not spam this group!`",
	'help_group_first':
		u"`Please, go ahead and PM me, click on the /start so I can get to know you.`",
	'welcomeusergroup':
		u'`Welcome to {groupname}!`',
	'startfirstgroup':
		u"`Greetings new human, I don't know you yet, please send me a PM so I can scan you!`",
	'startgroup':
		u"`I've sent you a message to our private conversation, let's not spam this group!`",
	'startfromgroup':
		u"`Hello, if you're interested on trying out stuff, play around here, let's not spam {title}`",
	'premade':
		u"/destroyed\n"
		u"/nmeme\n"
		u"/ememe\n"
		u"/shrug\n"
		u"/savage\n"
		u"/lenny\n"
		u"/stare\n"
}

# Start bot

@bot.message_handler(commands=['start'])
def send_welcome(message):

	uid = str(message.from_user.id)
	cid = str(message.chat.id)

	if message.chat.type == 'private':
		if uid not in loadjson("userlist"):
			addUser(uid, message.from_user.first_name, "userlist")
			bot.send_message(uid, text_messages['startfirst'], parse_mode="Markdown")
		else:
			bot.send_message(uid, text_messages['start'], parse_mode="Markdown")
	elif message.chat.type == 'group' or message.chat.type == 'supergroup':
		if uid not in loadjson("userlist"):
			bot.reply_to(message, text_messages['startfirstgroup'], parse_mode="Markdown")
		else:
			bot.send_message(cid, text_messages['startgroup'], parse_mode="Markdown")
			bot.send_message(uid, text_messages['startfromgroup'].format(title = message.chat.title), parse_mode="Markdown")
	else:
		pass

# Help menu

@bot.message_handler(commands=['help'])
def send_help_reply(message):
	if intime(message):
		uid = str(message.from_user.id)
		cid = str(message.chat.id)
		if message.chat.type == 'private':
			bot.send_message(uid, text_messages['help'], parse_mode="Markdown")
		elif message.chat.type == 'group' or message.chat.type == 'supergroup':
			if uid not in loadjson("userlist"):
				bot.reply_to(message, text_messages['help_group_first'], parse_mode="Markdown")
			else:
				bot.send_message(uid, text_messages['help'].format(title = message.chat.title), parse_mode="Markdown")
				bot.reply_to(message, text_messages['help_group'], parse_mode="Markdown")
		else:
			pass	

# Ping user

@bot.message_handler(commands=['ping'])
def ping(message):
	if intime(message):
		uName = message.from_user.first_name
		lname = message.from_user.last_name
		usName = message.from_user.username
		if message.chat.type == 'private':
			uid = str(message.from_user.id)
			if lname != None:
				bot.reply_to(message, text_messages['ping'].format(name=uName, uname=usName, lname=lname, uid=uid), parse_mode="Markdown")
			else:
				lname = ''
				bot.reply_to(message, text_messages['ping'].format(name=uName, uname=usName, lname=lname, uid=uid), parse_mode="Markdown")

		elif message.chat.type == 'group' or message.chat.type == 'supergroup':
			uid = str(message.from_user.id)
			gid = str(message.chat.id).lstrip('-')
			gName = message.chat.title
			if lname != None:
				bot.reply_to(message, text_messages['pinggroup'].format(name=uName, uname=usName, lname=lname, uid=uid, gName=gName, gid=gid), parse_mode="Markdown")
			else:
				lname = ''
				bot.reply_to(message, text_messages['pinggroup'].format(name=uName, uname=usName, lname=lname, uid=uid, gName=gName, gid=gid), parse_mode="Markdown")
		else:
			pass

# Print to console the list of users registered 

@bot.message_handler(commands=['userlist'])
def user_list(message):
	cid = message.from_user.id
	if cid == adminid:
		print "\n" + str(len(loadjson("userlist"))) +" users: " 
		print loadjson("userlist")
		print "\n" + str(len(loadjson("fmuser"))) + " lastfm users: "
		print loadjson("fmuser")
		groups = ""
		for group in loadjson("grouplist").keys():
			groups += group + " "
		print "\n" + str(len(loadjson("grouplist"))) + " groups: "
		print groups
	else:
		bot.send_message(cid,'`Access Denied`', parse_mode="Markdown")

# Todo list

@bot.message_handler(commands=['todo'])
def todolist(message):
	if adminid == message.from_user.id:
		content = getContent(message)
		if content:
			if "-add" in content:
				todo = content[5:len(message.text)]
				number = str(datetime.datetime.now())
				addUser(number, todo, 'todo')
				bot.send_message(message.chat.id, "`Added successfully`", parse_mode="Markdown")
			elif "-del" in content:
				done = content[5:len(message.text)]
				print done
				if deljson(done, 'todo'):
					bot.send_message(message.chat.id, "`Task successfully deleted!`", parse_mode="Markdown")
				else:
					bot.send_message(message.chat.id, "`Couldn't remove the task, please make them match.`", parse_mode="Markdown")
			elif "-show" in content:
				features = loadjson('todo')
				wholelist = ""
				for todo in features:
					key = todo
					wholelist += "- " + features[key] + "\n"
				bot.send_message(message.chat.id, u"`> Things to do:\n{wholelist}`".format(wholelist=wholelist),parse_mode="Markdown")
			else:
				pass
	else:
		bot.send_message(cid, "`Access Denied.`", parse_mode="Markdown")

# Quiet group

@bot.message_handler(commands=['quiet'])
def quiet_group(message):
	if intime(message):
		cid = getCID(message)
		cid = str(cid)
		if message.chat.type == 'group' or message.chat.type == 'supergroup':
			action = getContent(message)
			gName = (message.chat.title)
			if action:
				if action == "-add":
					if str(cid) in loadjson("quietlist") or gName in loadjson("quietlist"):
						bot.reply_to(message, "`This group is already on the quiet list, if you desire to remove it, send /quiet -remove`", parse_mode="Markdown")
					else:
						addUser(cid, gName, "quietlist")
						bot.reply_to(message, "`This group has been added to the quiet list, I will now only answer when called and to commands.`", parse_mode="Markdown")
				elif action == "-remove":
					if str(cid) in loadjson("quietlist"):
						deljson(cid, "quietlist")
						bot.reply_to(message, "`This group has been removed from the quiet list, I will now randomly beep, boop, repeat and broadcast!`", parse_mode="Markdown")
					else:
						bot.reply_to(message, "`Couldnt find this group on the quiet list, if you desire to add it, send /quiet -add`", parse_mode="Markdown")
				else:
					bot.reply_to(message, "`Invalid input, only -add and -remove accepted.`", parse_mode="Markdown")
			else:
				bot.reply_to(message, "`> There are to options available:\n/quiet -add\n/quiet -remove\n\nI will stop randomly beeping, booping, repeating and broadcasting if you add this group to the quiet list`", parse_mode="Markdown")
		else:
			bot.reply_to(message, "`This option is only available for groups.`", parse_mode="Markdown")

# Broadcast message

@bot.message_handler(commands=['broadcast'])
def broadcast_group(message):
	if intime(message):
		uid = getUID(message)
		if uid == adminid:
			content = getContent(message)
			for group in loadjson("grouplist").keys():
				if str(group) not in loadjson("quietlist"):
					bot.send_message(group, "`{content}`".format(content=content), parse_mode="Markdown")
			bot.send_message(adminid,  "`{content}`".format(content=content) + "`\n\nBroadcasted`", parse_mode="Markdown")

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
			PREMADE MESSAGES
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

@bot.message_handler(commands=['premades'])
def prem(message):
	if intime(message):
		cid = getCID(message)
		bot.send_message(cid, text_messages['premade'])

# Destroyed

@bot.message_handler(func=lambda message: "/destroyed" in message.text.lower())
def prem_destr(message):
	if intime(message):
		cid = getCID(message)
		bot.send_message(cid, premades['destroy'], parse_mode="Markdown")

# Excelente meme

@bot.message_handler(commands=['ememe'])
def prem_ememe(message):
	if intime(message):
		cid = getCID(message)
		bot.send_message(cid, premades['ememe'], parse_mode="Markdown")

# Nice Meme

@bot.message_handler(commands=['nmeme'])
def prem_nmeme(message):
	if intime(message):
		cid = getCID(message)
		bot.send_message(cid, premades['nmeme'],parse_mode="Markdown")

# Top kek

@bot.message_handler(func=lambda message: "/top" in message.text.lower())
def top_kek(message):
	if intime(message):
		cid = getCID(message)
		bot.send_message(cid, random.choice(top_response), parse_mode="Markdown")

# Shrug

@bot.message_handler(func=lambda message: "/shrug" in message.text.lower())
def shrug(message):
	cid = getCID(message)
	if intime(message):
		cid = getCID(message)
		bot.send_message(cid, premades['shrug'], parse_mode="Markdown")

# Lenny

@bot.message_handler(func=lambda message: "/lenny" in message.text.lower())
def lenny(message):
	if intime(message):
		cid = getCID(message)
		bot.send_message(cid, premades['lenny'], parse_mode="Markdown")

# Stare

@bot.message_handler(func=lambda message: "/stare" in message.text.lower())
def lenny(message):
	if intime(message):
		cid = getCID(message)
		bot.send_message(cid, premades['stare'], parse_mode="Markdown")

# Savage

@bot.message_handler(func=lambda message: "/savage" in message.text.lower() or "/salvaje" in message.text.lower())
def savage_message(message):
	if intime(message):
		cid = getCID(message)
		message_send = ""
		rand = random.randrange(6, 20)
		i = 0
		while i < rand:
			message_send += random.choice(savage)
			i += 1
		bot.send_message(cid, message_send)

# Thanks

@bot.message_handler(commands=['thanks'])
def say_thanks(message):
	if intime(message):
		if message.from_user.id == adminid:
			try:
				rid = message.reply_to_message
				bot.reply_to(rid, "`We both thank you and love you!`", parse_mode="Markdown")
			except:
				pass
		else:
			pass

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
			REGULAR PLUGINS
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# Len

@bot.message_handler(commands=['len'])
def lenght(message):
	if intime(message):
		cid = getCID(message)
		content = getContent(message)
		if content != "-?" and content:
			no_spaces = str(len(content.replace(" ", "")))
			spaces = str(len(content))
			bot.send_message(cid, "`Your text is:\n"+ spaces + " characters long including spaces\n" + no_spaces +" characters long not including spaces.`", parse_mode="Markdown")
		elif content == "-?":
			bot.reply_to(message, "`Follow this command with a message and I will return its lenght`", parse_mode="Markdown")
		else:
			try:
				rid = message.reply_to_message
				content = rid.text
				no_spaces = str(len(content.replace(" ", "")))
				spaces = str(len(content))
				bot.send_message(cid, "`Your text is:\n"+ spaces + " characters long including spaces\n" + no_spaces +" characters long not including spaces.`", parse_mode="Markdown")
			except:
				pass

# Flip

@bot.message_handler(commands=['flip'])
def flip_coin(message):
	if intime(message):
		message = getContent(message)
		if message != "-?" and message:
			cid = getCID(message)
			coin = ['`Heads`', '`Tails`']
			bot.send_message(cid, random.choice(coin), parse_mode="Markdown")
		else:
			bot.reply_to(message, "`This command will flip a coin (virtually) and tell you its result`", parse_mode="Markdown")

# diceroll

@bot.message_handler(commands=['diceroll'])
def dice_roll(message):
	if intime(message):
		faces = getContent(message)
		cid = getCID(message)
		if faces != "-?" or not faces:
			if faces == "4" or faces == "d4":
				roll = random.randrange(1, 5, 1)
				bot.send_message(cid, "`" + str(roll) + "`", parse_mode="Markdown")
			elif faces == "6" or faces == "d6" or not faces:
				roll = random.randrange(1, 7, 1)
				bot.send_message(cid, "`" + str(roll) + "`", parse_mode="Markdown")
			elif faces == "8" or faces == "d8":
				roll = random.randrange(1, 9, 1)
				bot.send_message(cid, "`" + str(roll) + "`", parse_mode="Markdown")
			elif faces == "10" or faces == "d10":
				roll = random.randrange(1, 11, 1)
				bot.send_message(cid, "`" + str(roll) + "`", parse_mode="Markdown")
			elif faces == "12" or faces == "d12":
				roll = random.randrange(1, 13, 1)
				bot.send_message(cid, "`" + str(roll) + "`", parse_mode="Markdown")
			elif faces == "20" or faces == "d20":
				roll = random.randrange(1, 21, 1)
				bot.send_message(cid, "`" + str(roll) + "`", parse_mode="Markdown")
			else:
				roll = random.randrange(1, 7, 1)
				bot.send_message(cid, "`No valid dice detected, rolling a 6d:\n\n    " + str(roll) + "\n\n/diceroll -?`", parse_mode="Markdown")
		else:
			bot.reply_to(message, "`Valid dices:\nd4\nd6\nd10\nd12\nd20\n\n  /diceroll d20`", parse_mode="Markdown")

# Roll

@bot.message_handler(commands=['roll'])
def roll_number(message):
	if intime(message):
		cid = getCID(message)
		number = getContent(message)
		if number != "-?" and number:
			print type(number)
			try:
				if "-" in number:
					number = number.replace(" ", "")
					number = number.split("-")
					roll = random.randrange(int(number[0]), int(number[1])+1, 1)
					bot.send_message(cid, "`" + str(roll) + "`", parse_mode="Markdown")
				else:
					number = int(number)
					roll = random.randrange(int(number))
					bot.send_message(cid, "`" + str(roll) + "`", parse_mode="Markdown")
			except:
				bot.reply_to(message, "`Please enter an integer as option.`", parse_mode="Markdown")
		elif number == "-?":
			bot.reply_to(message, "`Send this command alone to get a random number from 1 to 100, send it with either a range or a number to set a new range`", parse_mode="Markdown")
		else:
			roll = random.randrange(100)
			bot.send_message(cid, "`" + str(roll) + "`", parse_mode="Markdown")

# Binary

@bot.message_handler(commands=['bin'])
def binarytranslate(message):
	if intime(message):
		content = getContent(message)
		cid = getCID(message)
		if content != "-?" and content:
			try:
				if content[0:3] == '-2b':
					result = text_to_bin(content[4:len(content)])
					result = "`{result}`".format(result=result)
				elif content[0:3] == '-2t':
					content = content[4:len(content)]
					result = bin_to_text(content)
					result = "`{result}`".format(result=result)
				else:
					result = "`Please enter a valid option\n\n> -2b to translate to binary.\n> -2t to translate to text.`"
				bot.send_message(cid, result, parse_mode="Markdown")
			except:
				bot.reply_to(message, "`Unexpected error, only ascii characters can be translated to binary, please check your text.`", parse_mode="Markdown")
		else:
			bot.reply_to(message, "`Use this command to translate from binary to text and from text to binary\n\n/bin -2t to translate from binary to text\n/bin 2b to translate from text to binary `", parse_mode="Markdown")

# Send Message

@bot.message_handler(commands=['message', 'sendmessage'])
def sendmessageto(message):
	if intime(message):
		uid = getUID(message)
		if uid == adminid:
			cid = re.findall(r'\w+[@RadRetroRobot]*\s+(\S+)\s+(.*)', message.text)
			try:
				content = cid[0][1]
				content = content.encode('utf-8')
				cid = cid[0][0]
				bot.send_message(cid, "`{cid}`".format(cid=content), parse_mode="Markdown")
			except:
				print "error"
				print cid
				print content

# Echo

@bot.message_handler(commands=['echo'])
def calc(message):
	if intime(message):
		cid = getCID(message)
		error = False
		msg = getContent(message)
		if msg:
			bot.send_message(cid, u"`{msg}`".format(msg=msg), parse_mode="Markdown")
		else:
			bot.reply_to(message, "`Follow this command with some text and I will repeat it`", parse_mode="Markdown")



"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

		HTML Fetchs

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# Is it down

@bot.message_handler(commands=['isdown'])
def isdown(message):
	if intime(message):
		cid = getCID(message)
		page = getContent(message)
		page = page.replace("http://", "").replace("https://", "")
		if page != "-?" and page:
			url = "http://downornotworking.com/" + page
			request = requests.get(url)
			if request.status_code == 200:
				soup = BeautifulSoup(request.text, "html.parser")
				down = soup.findAll('div', class_='col-md-8')
				down = down[1]
				if down.span.text.replace("\n", "").replace(" ", "") == "ok":
					lastping = "\n" + down.contents[-2].text.split(".")[-3]
					avgping = "\n" + down.contents[-2].text.split(".")[-2]
				else:
					lastping = ""
					avgping = ""
				down = down.span.text.replace("\n", "").replace(" ", "")
				down = down + lastping + avgping
				bot.send_message(cid, "`" + page + " is currently " + down + "`", parse_mode="Markdown")
			else:
				bot.reply_to(message, "`There has been an error, the number {error} to be specific.`".format(error=request.status_code), parse_mode="Markdown")
		else:
			bot.reply_to(message, "`Follow this command with an URL to know if its down for everyone or its just you`", parse_mode="Markdown")

# Calc

@bot.message_handler(commands=['calc', 'c'])
def calc(message):
	if intime(message):
		cid = getCID(message)
		uName = (message.from_user.first_name)
		error = False
		exp = getContent(message)
		if exp != "-?" and exp:
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
		else:
			bot.send_message(cid, "`Please enter your expression after the command to get the result`", parse_mode="Markdown")
		
# Google search

@bot.message_handler(commands=['g', 'google', 'gnsfw'])
def gsearch(message):
	if intime(message):
		cid = getCID(message)
		safeSearch = True
		command = getCommand(message)
		search = getContent(message)
		if command == 'gnsfw':
			safeSearch = False
		if search != "-?" and search:
			url = "https://ajax.googleapis.com/ajax/services/search/web?v=1.0&rsz=5"
			if safeSearch:
				url = url +  "&safe=active"
			url = url + "&q=" + search
			request = requests.get(url)
			if request.status_code == 200:
				data = request.json()
				if data['responseData'] != None:
					links = ""
					for link in data['responseData']['results']:
						url = treatLink(link['url'])
						title = treatTitle(link['titleNoFormatting'])
						links += u"`> `[{title}]({url})\n".format(url=url, title=title)
					if links:
						bot.reply_to(message,  u"`Results for: \"{query}\"\n`".format(query=search) + links, parse_mode="Markdown", disable_web_page_preview=True)
					else:
						bot.reply_to(message, "`Results not found, if you are trying to google something nsfw, try /gnsfw.`", parse_mode="Markdown")
				else:
					bot.reply_to(message, "`There has been an issue with Google, here's a message from them:\n\n{details}`".format(details=data['responseDetails']), parse_mode="Markdown")
			else:
				bot.send_message(cid, "`There has been an issue with your request, I'm really sorry.`")
		else:
			bot.send_message(cid, "`Follow this command with your search and I will show you some results of said search.`", parse_mode="Markdown")


# Google Images Search

@bot.message_handler(commands=['i', 'insfw', 'image'])
def isearch(message):
	if intime(message):
		try:
			google_img_key
		except:
			print "\n\n\t\tPlease setup google api key\n\n"
		cid = getCID(message)
		search = getContent(message)
		command = getCommand(message)
		if command == 'insfw':
			safeSearch = True
		else:
			safeSearch = False
		if search != "-?" and search:
			url = ("https://www.googleapis.com/customsearch/v1?&searchType=image&imgSize=xlarge&alt=json&num=8&start=1&key=" + google_img_key + "&cx=017597791379160176083:kooipmedh98&q=")
			url = url + search
			if not safeSearch:
				url = url + "&safe=high"
			request = requests.get(url)
			if request.status_code == 200:
				try:
					if not safeSearch:
						data = request.json()
						link = data['items'][random.randrange(0, 7)]['link']
						link = treatLink(link)
						bot.send_message(cid, u"[​]({link})".format(link=link), parse_mode="Markdown")
					else:
						data = request.json()
						link = data['items'][random.randrange(0, 7)]['link']
						link = treatLink(link)
						bot.send_message(cid, u"[​]({link})".format(link=link), parse_mode="Markdown")
				except:
					bot.reply_to(message, "`Oops! Something went wrong, if you are trying to google something nsfw, try /insfw.`", parse_mode="Markdown")
			elif request.status_code == 403:
				bot.reply_to(message, "`Sorry, the daily limit for images search has been reached, blame Google for this.`", parse_mode="Markdown")
			else:
				bot.reply_to(message, "`There has been an error, the number {error} to be specific.`".format(error=request.status_code), parse_mode="Markdown")
		else:
			bot.send_message(cid, "`Follow this command with your search and I will get you an image.`", parse_mode="Markdown")

# Urban Dictionary definitions

@bot.message_handler(commands=['ud'])
def ud(message):
	if intime(message):
		cid = getCID(message)
		isSearch = False
		search = getContent(message)
		if search != "-?" and search:
			url = "http://api.urbandictionary.com/v0/define?term=" + search
			request = requests.get(url)
			if request.status_code == 200:
				data = request.json()
				if data['result_type'] == 'exact':
					definition = data['list'][0]['definition']
					permalink = data['list'][0]['permalink']
					example = data['list'][0]['example']
					word = data['list'][0]['word']
					definition = definition.rstrip('].').lstrip('[')
					message_ub = u"\t`Urban Dictionary Definition`\n\n"u" \t\t`\t\t> {word}:`\n\n"u"`{definition}`\n\n\n"u"`Example:\n{example}`\n\n"u"`If you want more info on this, feel free to visit this link:` {permalink}".format(word=word, definition=definition, example=example, permalink=permalink)
					bot.send_message(cid, message_ub, parse_mode="Markdown", disable_web_page_preview=True)
				else:
					bot.send_message(cid, u"`No results found for {search}.`".format(search=search), parse_mode="Markdown")
			else:
				bot.send_message(cid, '`{error}`'.format(error=data.raise_for_status()), parse_mode="Markdown")
		else:
			bot.send_message(cid, "`Follow this command with your search and I will show you the definition of it.`", parse_mode="Markdown")

# Reddit

@bot.message_handler(commands=['r'])
def reddit(message):
	if intime(message):
		try:
			reddit_user
		except:
			print "\n\n\t\tPlease setup your reddit user\n\n"
		cid = getCID(message)
		isSub = False
		sub = message.text
		sub = getContent(message)
		if sub != "-?" and sub:
			if sub[0:2] != 'r/':
				sub = 'r/' + sub
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
			else:
				bot.reply_to(message, "`There has been an error, the number {error} to be specific.`".format(error=request.status_code), parse_mode="Markdown")
		else:
			bot.send_message(cid, "`Follow this command with r/ and the name of a subreddit to see the top 4 posts.`", parse_mode="Markdown")

# Reddit comment thing

@bot.message_handler(func=lambda message: "www.reddit.com/r/" in message.text and "/comments/" in message.text)
def reddit_selfpost(message):
	if intime(message):
		try:
			reddit_user
		except:
			print "\n\n\t\tPlease setup your reddit user\n\n"
		cid = getCID(message)
		sub = ""
		try:
			url = re.findall (r'(http[s]?://(?:www.reddit.com/r/+.*/comments/+\S*))+', str(message.text))
			url = url[0] + ".json"
			request = requests.get(url, headers = {'User-agent': reddit_user})
			data = request.json()
		
			if request.status_code == 200:
				try:
					selftext = data[0]['data']['children'][0]['data']['selftext']
					poster = data[0]['data']['children'][0]['data']['author']
					sub = data[0]['data']['children'][0]['data']['subreddit']
					title = data[0]['data']['children'][0]['data']['title']
					up = data[0]['data']['children'][0]['data']['ups']
					comments = data[0]['data']['children'][0]['data']['num_comments']
					if data[0]['data']['children'][0]['data']['over_18']:
						isNsfw = "nsfw"
					else:
						isNsfw = "sfw"

					if data[0]['data']['children'][0]['data']['is_self']:
						if len(selftext) <= 4999:
							self_post = u"`> post from /r/{sub} by {author}\n{title}:`\n\n {selftext}\n\n`<{nsfw}> | {up} upvotes | {comments} comments`"
							bot.send_message(cid, self_post.format(selftext=selftext, sub=sub, author=poster,title=title, nsfw= isNsfw, up=up, comments=comments), parse_mode="Markdown", disable_web_page_preview = True)
						else:
							self_post_long = u"`> post from /r/{sub} by {author}\n\n{title}:\n\nThe text from this post excedes my text message limit\n\n<{nsfw}> | {up} upvotes | {comments} comments`"
							bot.send_message(cid, self_post_long.format(selftext=selftext, sub=sub, author=poster,title=title, nsfw= isNsfw, up=up, comments=comments), parse_mode="Markdown", disable_web_page_preview = True)
					elif not data[0]['data']['children'][0]['data']['is_self']:
						not_self_post = u"`> post from /r/{sub} by {author}\n{title}:`\n\n`<{nsfw}> | {up} upvotes | {comments} comments`"
						bot.send_message(cid, not_self_post.format(sub=sub, author=poster,title=title, nsfw= isNsfw, up=up, comments=comments), parse_mode="Markdown", disable_web_page_preview = True)
					else:
						pass
				except:
					pass
			else:
				pass
		except:
			pass

# gfy auto gif

@bot.message_handler(func=lambda message: "gfycat.com" in message.text.lower())
def gfy(message):
	if intime(message):
		cid = getCID(message)
		try:
			bot.send_message(cid, getGfy(message.text))
		except:
			pass

# Last FM User Set

@bot.message_handler(commands=['fmuser'])
def fmuser(message):
	if intime(message):
		cid = unicode(message.chat.id)
		uid = unicode(message.from_user.id)
		hasUser = True
		fmUsers = loadjson("fmuser")
		user = getContent(message)
		if user and user != "-?":
			if uid not in fmUsers:
				addUser(uid, user, "fmuser")
				bot.send_message(cid, "`You've been registered into my data base as {username}.`".format(username=user), parse_mode="Markdown")
			elif uid in fmUsers:
				addUser(uid, user, "fmuser")
				bot.send_message(cid, "`Changing your username from: {olduser} to {username}.`".format(olduser=fmUsers[uid], username=user), parse_mode="Markdown")
		else:
			bot.reply_to(message, "`Follow this command with your last.fm username to be able to use now playing command.`", parse_mode="Markdown")

# Last FM Now playing

@bot.message_handler(commands=['np'])
def nowplaying(message):
	if intime(message):
		try:
			lastfm_key
		except:
			print "\n\n\t\tPlease setup lastfm api key\n\n"
		uid = unicode(message.from_user.id)
		fmUsers = loadjson("fmuser")
		isUser = False
		content = getContent(message)
		if uid in fmUsers:
			isUser = True
		else:
			bot.reply_to(message, "`Please set your username with /fmuser, preferably from PM.`", parse_mode="Markdown")
		
		if isUser and content != "-?":
			url = "http://ws.audioscrobbler.com/2.0/?method=user.getRecentTracks&format=json&user=" + fmUsers[uid] + "&api_key=" + lastfm_key + "&limit=1"
			request = requests.get(url)
			data = request.json() 
			if request.status_code == 200:
				try:
					artist = data['recenttracks']['track'][0]['artist']['#text']
					song = data['recenttracks']['track'][0]['name']
					album = data['recenttracks']['track'][0]['album']['#text']
					if '@attr' in data['recenttracks']['track'][0]:
						bot.reply_to(message, u"`> {user} is currently listening:\nsong: {song}\nartist: {artist}\nalbum: {album}\n\t\t\t\t\t\t\t\t♪   ♫   ♪   ♫`".format(user=message.from_user.first_name, song=song, artist=artist, album=album), parse_mode="Markdown")
					else:
						bot.reply_to(message, u"`> {user} listened to:\nsong: {song}\nartist: {artist}\nalbum: {album}\n\t\t\t\t\t\t\t\t♫   ♪   ♫   ♪`".format(user=message.from_user.first_name, song=song, artist=artist, album=album), parse_mode="Markdown")
				except:
					bot.reply_to(message, "`Theres has been an error, please verify that your username is valid`", parse_mode="Markdown")
			else:
				bot.reply_to(message, "`Theres has been an error, heres some info from lastfm: {error}`".format(error=data['message']), parse_mode="Markdown")
		else:
			bot.reply_to(message, "`Send this command after setting up your user with /fmuser to show what you are currently listening to`", parse_mode="Markdown")

# Last FM Top 5

@bot.message_handler(commands=['fmtop'])
def top_artist_fm(message):
	if intime(message):
		try:
			lastfm_key
		except:
			print "\n\n\t\tPlease setup lastfm api key\n\n"

		cid = unicode(message.chat.id)
		uid = unicode(message.from_user.id)
		fmUsers = loadjson("fmuser")
		isUser = False
		content = getContent(message)
		if uid in fmUsers:
			isUser = True
		else:
			bot.reply_to(message, "`Please set your username with /fmuser, preferably from PM.`", parse_mode="Markdown")
		if isUser and content != "-?":
			url = "http://ws.audioscrobbler.com/2.0/?method=user.getTopArtists&format=json&user=" + fmUsers[uid] + "&api_key=" + lastfm_key + "&period=7day&limit=5"
			request = requests.get(url)
			data = request.json()
			artists = ""
			if request.status_code == 200:
				try:
					if data['topartists']['@attr']['totalPages'] != "0":
						i = 0
						artists = ""
						for artist in data['topartists']['artist']:
							artist_name = unicode(artist['name'])
							playcount = unicode(artist['playcount'])
							artists += u"`> {artist} - {playcount}` \n".format(artist=artist_name, playcount=playcount)
							i += 1
						if i > 1:
							artist = "artist"
						else:
							aritst = "artists"
						bot.reply_to(message, u"`{name}'s last week Top {playcount} {artist} and its playcount:` \n".format(artist=artist, name=message.from_user.first_name, playcount=i) + artists, parse_mode="Markdown")
					else: 
						bot.reply_to(message, "`Theres has been an error, I found no information from your user.`", parse_mode="Markdown")
				except:
					bot.reply_to(message, "`Theres has been an error, I found no information from your user.`", parse_mode="Markdown")
			else:
				bot.reply_to(message, "`Theres has been an error, heres some info from lastfm: {error}`".format(error=data['message']), parse_mode="Markdown")
		else:
			bot.reply_to(message, "`Send this command after setting up your user with /fmuser to show your top 5 artists from last week`", parse_mode="Markdown")

# Last FM Top albums

@bot.message_handler(commands=['fmalbums'])
def top_album_fm(message):
	if intime(message):
		try:
			lastfm_key
		except:
			print "\n\n\t\tPlease setup lastfm api key\n\n"
		cid = unicode(message.chat.id)
		uid = unicode(message.from_user.id)
		fmUsers = loadjson("fmuser")
		isUser = False
		content = getContent(message)
		if uid in fmUsers:
			isUser = True
		else:
			bot.reply_to(message, "`Please set your username with /fmuser, preferably from PM.`", parse_mode="Markdown")
		if isUser and content != "-?":
			url = "http://ws.audioscrobbler.com/2.0/?method=user.getTopAlbums&format=json&user=" + fmUsers[uid] + "&api_key=" + lastfm_key + "&limit=5&period=7day"
			request = requests.get(url)
			data = request.json()
			artists = ""
			if request.status_code == 200:
				if data['topalbums']['@attr']['totalPages'] != "0":
					i = 0
					artists = ""
					for album in data['topalbums']['album']:
						album_name = unicode(album['name'])
						playcount = unicode(album['playcount'])
						artist_name = unicode(album['artist']['name'])
						artists += u"`> {artist} - {album} - {playcount}` \n".format(artist=artist_name, playcount=playcount, album=album_name)
						i += 1
					if i > 1:
						artist = "album"
					else:
						aritst = "albums"
					bot.reply_to(message, u"`{name}'s last week Top {playcount} {artist} and its playcount:` \n".format(artist=artist, name=message.from_user.first_name, playcount=i) + artists, parse_mode="Markdown")
				else: 
					bot.reply_to(message, "`Theres has been an error, I found no information from your user.`", parse_mode="Markdown")
			else:
				bot.reply_to(message, "`Theres has been an error, heres some info from lastfm: {error}`".format(error=data['message']))
		else:
			bot.reply_to(message, "`Send this command after setting up your user with /fmuser to show your top 5 album from last week`", parse_mode="Markdown")

# Last fm grid 

@bot.message_handler(commands=['fmgrid'])
def fm_grid(message):
	if intime(message):
		if getContent(message) != "-?" or not getContent(message):
			cid = getCID(message)
			options = getContent(message)
			uid = unicode(message.from_user.id)
			isUser = False
			fmUsers = loadjson("fmuser")
			validTypes = ["7days", "1month", "3month", "6month", "12month", "overall"]
			validSizes = ["3x3", "4x4", "5x5"]
			if uid in fmUsers:
				isUser = True
			else:
				bot.reply_to(message, "`Please set your username with /fmuser, preferably from PM.`", parse_mode="Markdown")
			if isUser:
				if options:
					options = re.findall(r'(.*)\s+(\d+x{1}\d+)', options)
					gridtype = options[0][0].replace(" ", "")
					gridtype = gridtype.replace("s", "")
					gridsize = options[0][1]
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
				url = "http://www.tapmusic.net/collage.php?type=" + gridtype + "&size=" + gridsize + "&user=" + fmUsers[uid]
				request = requests.get(url)
				soup = BeautifulSoup(request.text, "html.parser")
				if "Error" in soup.text:
					bot.reply_to(message, "`There has been an error, heres some info:`\n\n" + "`" + soup.text + "`", parse_mode="Markdown")
				else:
					bot.reply_to(message, url, parse_mode="Markdown")
		else:
			bot.reply_to(message, "`This command will return a grid with your last listened albums here are the options you can set\n\n /fmgrid <type> <size>\n\nTypes: 7 day, 1 month, 3 months, 6 months, 12 months, Overall.\nSize: 3x3, 4x4, 5x5\n\nBy default this command will give you a 3x3 grid from last week`", parse_mode="Markdown")


# Last FM

@bot.message_handler(commands=['lastfm'])
def last_commands(message):
	if intime(message):
		cid = getCID(message)
		bot.send_message(cid, "`Last FM related commands: \n\n  /fmuser <username> - sets your username for these commands\n  /fmtop - shows your top 5 artists from last week\n  /fmalbums - shows your top 5 albums from last week.\n  /np - shows what you are currently listening to\n  /fmgrid - shows a grid of your last week albums,\n  send /fmgrid -? for more options`", parse_mode="Markdown")

# Dota Update

@bot.message_handler(commands=['dotanews', 'dotanew', 'dnews', 'dnew'])
def dota_news(message):
	if intime(message):
		cid = getCID(message)
		content = getContent(message)
		url = "http://api.steampowered.com/ISteamNews/GetNewsForApp/v0002/?appid=570&count=3&maxlength=300&format=json"
		request = requests.get(url)
		data = request.json()
		if content != "?":
			if request.status_code == 200:
				title = data['appnews']['newsitems'][0]['title']
				content = data['appnews']['newsitems'][0]['contents']
				url = data['appnews']['newsitems'][0]['url']
				bot.send_message(cid, u'`> {title}\n\n{content}\n\n`'.format(title=title, content=content) + '[More info here]({url})'.format(url=url), parse_mode="Markdown", disable_web_page_preview=True)
			else:
				bot.reply_to(message, "`There has been an error, the number {error} to be specific.`".format(error=request.status_code), parse_mode="Markdown")
		else:
			bot.reply_to(message, "`Send this command alone and I will show you the last Dota 2 blog entry`", parse_mode="Markdown")

# Dota League info

@bot.message_handler(commands=['dotaleague', 'dleague', 'dtournament', 'dotatournament'])
def dota_league_info(message):
	if intime(message):
		try:
			dota_key
		except:
			print "\n\n\t\tPlease setup dota api key\n\n"
		cid = getCID(message)
		league_id = getContent(message)
		url = "http://api.steampowered.com/IDOTA2Match_570/GetLeagueListing/v1/?key=" + dota_key + "&format=JSON&language=en_us"
		leagues = getJson(url)
		if league_id and league_id != "-?":
			found = False
			for league in leagues['result']['leagues']:
				if str(league['leagueid']) == league_id:
					found = True
					name = league['name']
					description = league['description']
					league_url = league['tournament_url']
					league_url = treatLink(league_url)
					if league_url != "":
						league_url = "[Tournament Webpage]({league_url})".format(league_url=league_url)
					else:
						league_url = ""
					bot.send_message(cid, "`> {name}\n\n{description}\n`\n{league_url}".format(name=name, description=description, league_url=league_url), parse_mode="Markdown", disable_web_page_preview=True)
					break
			if not found:
				bot.reply_to(message, "`Couldnt find a league with that ID.`", parse_mode="Markdown")
		else:
			bot.reply_to(message, "`Follow this command with a Dota 2 league ID to get its basic info`", parse_mode="Markdown")


# Dota Live League Games

@bot.message_handler(commands=['dotalive', 'dlive'])
def dota_leagues(message):
	if intime(message):
		try:
			dota_key
		except:
			print "\n\n\t\tPlease setup dota api key\n\n"
		cid = getCID(message)
		content = getContent(message)
		url = "http://api.steampowered.com/IDOTA2Match_570/GetLiveLeagueGames/v1/?key=" + dota_key + "&format=JSON&language=en_us"
		request = requests.get(url)
		data = request.json()
		if request.status_code == 200:
			games = ""
			total = 10
			if "-full" == content:
				for game in data['result']['games']:
					try:
						radiant = game['radiant_team']['team_name']
						radiant_id = "(" + str(game['radiant_team']['team_id']) + ")"
					except:
						radiant = "Radiant Team"
						radiant_id = ""
					try:
						dire = game['dire_team']['team_name']
						dire_id = "(" + str(game['dire_team']['team_id']) + ")"
					except:
						dire = "Dire Team"
						dire_id = ""
					match_id = game['match_id']
					league_id = game[u'league_id']
					try:
						dire_score = game[u'scoreboard']['dire']['score']
					except:
						dire_score = 0
					dire_score = str(dire_score)
					try:
						radiant_score = game[u'scoreboard']['radiant']['score']
					except:
						radiant_score = 0
					radiant_score = str(radiant_score)
					radiant_total = "{radiant} {radiant_id} {radiant_score}".format(radiant=radiant, radiant_id=radiant_id, radiant_score=radiant_score)
					dire_total = "{dire_score} {dire} {dire_id}".format(dire_score=dire_score, dire_id=dire_id, dire=dire)
					games += "`> {radiant_total} - {dire_total} \n\t\t\t Match ID: {match_id} - League ID: {league_id}`\n".format(radiant_total=radiant_total, dire_total=dire_total, match_id=match_id, league_id=league_id)
				bot.send_message(cid, "`These are the Live League Games currently: `\n" + games, parse_mode="Markdown")
			elif content == "-?":
				bot.reply_to(message, "`Send this command alone to get 10 Dota 2 Live Tournament games, send it with -full after the command to get the full list.`", parse_mode="Markdown")
			else:
				for game in data['result']['games']:
					if total > 0:
						try:
							radiant = game['radiant_team']['team_name']
							radiant_id = "(" + str(game['radiant_team']['team_id']) + ")"
						except:
							print 
							radiant = "Radiant Team"
							radiant_id = ""
						try:
							dire = game['dire_team']['team_name']
							dire_id = "(" + str(game['dire_team']['team_id']) + ")"
						except:
							dire = "Dire Team"
							dire_id = ""
						match_id = game['match_id']
						league_id = game[u'league_id']
						try:
							dire_score = game[u'scoreboard']['dire']['score']
						except:
							dire_score = 0
						dire_score = str(dire_score)
						try:
							radiant_score = game[u'scoreboard']['radiant']['score']
						except:
							radiant_score = 0
						radiant_score = str(radiant_score)
						radiant_total = "{radiant} {radiant_id} {radiant_score}".format(radiant=radiant, radiant_id=radiant_id, radiant_score=radiant_score)
						dire_total = "{dire_score} {dire} {dire_id}".format(dire_score=dire_score, dire_id=dire_id, dire=dire)
						games += "`> {radiant_total} - {dire_total} \n\t\t\t Match ID: {match_id} - League ID: {league_id}`\n".format(radiant_total=radiant_total, dire_total=dire_total, match_id=match_id, league_id=league_id)
					total -= 1
				bot.send_message(cid, "`These are the Live League Games currently: `\n" + games + "`\n\nSend your commmand as /dlive -full to get the full list of content.`", parse_mode="Markdown")

		else:
			bot.reply_to(message, "`There has been an error, the number {error} to be specific.`".format(error=request.status_code), parse_mode="Markdown")

# Dota Live Details

@bot.message_handler(commands=['dotalivedetails', 'dldetails'])
def dota_league_detail(message):
	if intime(message):
		try:
			dota_key
		except:
			print "\n\n\t\tPlease setup dota api key\n\n"
		cid = getCID(message)
		url = "http://api.steampowered.com/IDOTA2Match_570/GetLiveLeagueGames/v1/?key=" + dota_key + "&format=JSON&language=en_us"
		hero_list = getJson("http://api.steampowered.com/IEconDOTA2_570/GetHeroes/v1/?key=" + dota_key + "&format=JSON&language=en_us")
		match_id = getContent(message)
		request = requests.get(url)
		data = request.json()
		if match_id and match_id != "-?":
			if request.status_code == 200:
				games = ""
				found = False
				for game in data['result']['games']:
					# FOUND THE GAME
					if str(game['match_id']) == match_id:
						found = True
						print "game found"
						match_id = game['match_id']
						spectators = game['spectators']
						league_id = game['league_id']
						duration = 0.0
						radiant_heroes = ""
						dire_heroes = ""
						dire = ""
						dire_players = ""
						radiant = ""
						radiant_players = ""
						# NAME RADIANT TEAM
						try:
							radiant = game['radiant_team']['team_name']
							radiant_id = "(" + str(game['radiant_team']['team_id']) + ")"
						except:
							radiant = "Radiant Team"
							radiant_id = ""
						# NAME DIRE TEAM
						try:
							dire = game['dire_team']['team_name']
							dire_id = "(" + str(game['dire_team']['team_id']) + ")"
						except:
							dire = "Dire Team"
							dire_id = ""	

						# IF THE GAME STARTED 
						if game['scoreboard']['duration'] > 0:
							duration = game['scoreboard']['duration']/60
							duration = str(int(duration)) + " minutes"
							radiant_score = game['scoreboard']['radiant']['score']
							dire_score = game['scoreboard']['dire']['score']
							rosh_timer = game['scoreboard']['roshan_respawn_timer']
							if rosh_timer == 0:
								rosh_timer_message = "\nRosh is up!"
							else:
								rosh_timer = rosh_timer/60.0
								rosh_timer = str(rosh_timer)[0:3]
								rosh_timer_message = "\nRosh timer: " + rosh_timer + " minutes."
							# RADIANT HEROES AND STATS
							for player in game['scoreboard']['radiant']['players']:
								for hero in hero_list['result']['heroes']:
									if player['hero_id'] == hero['id']:
										player_hero = hero['localized_name']
										break
								player_slot = player['player_slot']
								kills = player['kills']
								deaths = player['death']
								assists = player['assists']
								lh = player['last_hits']
								denies = player['denies']
								gpm = player['gold_per_min']
								xpm = player['xp_per_min']
								level = player['level']
								gold = player['gold']
								if deaths != 0:
									kda = float(kills+assists)/float(deaths)
									kda = str(kda)
									kda = kda[0:3]
								else:
									kda = "0"
								radiant_heroes += "> " + str(player_hero) +" " + str(level) + " " + str(kills) + "/" + str(deaths) + "/" + str(assists) + " " + kda + " " + str(gold) + " " + str(lh) + " " + str(denies) + " " + str(gpm) + " " + str(xpm) + "\n"							
							# DIRE HEROES AND STATS
							for player in game['scoreboard']['dire']['players']:
								for hero in hero_list['result']['heroes']:
									if player['hero_id'] == hero['id']:
										player_hero = hero['localized_name']
										break
								player_slot = player['player_slot']
								kills = player['kills']
								deaths = player['death']
								assists = player['assists']
								lh = player['last_hits']
								denies = player['denies']
								gpm = player['gold_per_min']
								xpm = player['xp_per_min']
								level = player['level']
								gold = player['gold']
								if deaths != 0:
									kda = float(kills+assists)/float(deaths)
									kda = str(kda)
									kda = kda[0:3]
								else:
									kda = "0"
								dire_heroes += "> " + str(player_hero) +" " + str(level) + " " + str(kills) + "/" + str(deaths) + "/" + str(assists) + " " + kda + " " + str(gold) + " " + str(lh) + " " + str(denies) + " " + str(gpm) + " " + str(xpm) + "\n"
							header = "|Hero|Level|K|D|A|KDA|Gold|LH|DN|GPM|XPM\n"
							divider = "\n"
							match = str(radiant_score) + "\n_" + radiant +"\n" + header + radiant_heroes + divider + str(dire_score) + "\n_" + dire  +"\n" + header + dire_heroes
							dotabuff = "http://www.dotabuff.com/matches/" + str(match_id)
							dotabuff = treatLink(dotabuff)
							player_name_error = False
							# PLAYERS WITH HEROES
							for player in game['players']:
								for hero in hero_list['result']['heroes']:
									if player['hero_id'] == hero['id']:
										player_hero = hero['localized_name']
										break
								player_name = player['name']
								if player['team'] == 0:
									try:
										radiant_players += "> " + player_name + " - " + player_hero + "\n"
									except:
										radiant_players += "> Radiant player " + player_hero + "\n"
										player_name_error = True
								elif player['team'] == 1:
									try:
										dire_players += "> " +  player_name + " - " + player_hero + "\n"
									except:
										dire_players += "> Radiant player " + player_hero + "\n"
										player_name_error = True
								else:
									pass
							total_players = "_" + radiant + " Players:\n" + radiant_players + "\n_" + dire + " Players:\n" + dire_players + "\n"
							if player_name_error:
								total_players = "_Radiant Players:\n" + radiant_players + "\n_Dire Players:\n" + dire_players + "\nI could not display some of these names correctly, sorry.\n"
							final_message = total_players + "\n" + "Time: " + duration + rosh_timer_message + "\nSpectators: " + str(spectators) + "\n\n" + match + "\n League ID: " + str(league_id)
							bot.send_message(cid, u"`{final_message}`".format(final_message=final_message), parse_mode="Markdown")
						else:
							bot.reply_to(message, "`This game is still on picking phase, lets wait until it starts!`", parse_mode="Markdown")
						break
				if not found:
					bot.reply_to(message, "`I could not find any game with that ID.\n\nMaybe the game is already finished, try using /dmatch`", parse_mode="Markdown")
		else:
			bot.reply_to(message, "`Follow this command with the ID of a live league game. \n\nUse /dotalive to see the list`", parse_mode="Markdown")

# Dota Live structures

@bot.message_handler(commands=['dotalivemap', 'dlmap'])
def dota_map(message):
	if intime(message):
		try:
			dota_key
		except:
			print "\n\n\t\tPlease setup dota api key\n\n"
		cid = getCID(message)
		content = getContent(message)
		if content and content != "-?":
			match_id = content[5:len(content)]
			url = "http://api.steampowered.com/IDOTA2Match_570/GetLiveLeagueGames/v1/?key=" + dota_key + "&format=JSON&language=en_us"
			hero_list = getJson("http://api.steampowered.com/IEconDOTA2_570/GetHeroes/v1/?key=" + dota_key + "&format=JSON&language=en_us")
			data = getJson(url)
			if validLink(url):
				games = ""
				found = False
				for game in data['result']['games']:
					# FOUND THE GAME
					if str(game['match_id']) == match_id:
						found = True
						dire_towers = dota_bin(game['scoreboard']['dire']['tower_state'])
						dire_rax = dota_bin(game['scoreboard']['dire']['barracks_state'])
						radiant_towers = dota_bin(game['scoreboard']['radiant']['tower_state'])
						radiant_rax = dota_bin(game['scoreboard']['radiant']['barracks_state'])
						duration = game['scoreboard']['duration']/60
						duration = str(int(duration))
						radiant_score = game['scoreboard']['radiant']['score']
						dire_score = game['scoreboard']['dire']['score']
						# NAME RADIANT TEAM
						try:
							radiant = game['radiant_team']['team_name']
							radiant_id = "(" + str(game['radiant_team']['team_id']) + ") "
						except:
							radiant = "Radiant Team"
							radiant_id = ""
						# NAME DIRE TEAM
						try:
							dire = game['dire_team']['team_name']
							dire_id = " (" + str(game['dire_team']['team_id']) + ")"
						except:
							dire = "Dire Team"
							dire_id = ""	
						d_towers = init_towers(dire_towers)
						d_rax = init_rax(dire_rax)
						r_towers = init_towers(dire_towers)
						r_rax = init_rax(dire_rax)
						try:
							if "-map" in content:
								dota_map = """---------------------------------------------\n|         ({dire_top_1})      ({dire_top_2})    ({dire_top_3})({dire_top_melee})             |\n|                            ({dire_top_ranged})  ({dire_ancient_top})(_A_)   |\n|                                   ({dire_ancient_bot})      |\n|    \       \              ({dire_mid_melee})              |\n|      \       \            ({dire_middle_3})({dire_mid_ranged})    ({dire_bottom_melee})({dire_bottom_ranged}) |\n|        \       \                      ({dire_bottom_3})  |\n|  ({radiant_top_1})     \       \    ({dire_middle_2})                  |\n|            \                           ({dire_bottom_2}) |\n|              \     ({dire_middle_1})                     |\n|                                            |\n|               ({radiant_middle_1})           \              |\n|  ({radiant_top_2})                 \        \            |\n|             ({radiant_middle_2})        \       \       ({dire_bottom_1}) |\n|  ({radiant_top_3})                     \       \         |\n| ({radiant_top_melee})({radiant_top_ranged})   ({radiant_middle_3})               \       \       |\n|        ({radiant_mid_ranged})({radiant_mid_melee})                              |\n|    ({radiant_ancient_top})                                     |\n| (_A_)({radiant_ancient_bot})  ({radiant_bottom_ranged})                              |\n|           ({radiant_bottom_melee})({radiant_bottom_3})    ({radiant_bottom_2})      ({radiant_bottom_1})           |\n----------------------------------------------\n""".format(dire_bottom_1=d_towers[10], dire_middle_1=d_towers[7], dire_top_1=d_towers[4], dire_bottom_2=d_towers[9], dire_middle_2=d_towers[6], dire_top_2=d_towers[3], dire_bottom_3=d_towers[8], dire_middle_3=d_towers[5], dire_top_3=d_towers[2], dire_bottom_ranged=r_rax[4], dire_bottom_melee=r_rax[5], dire_mid_ranged=r_rax[2], dire_mid_melee=r_rax[3], dire_top_melee=r_rax[1], dire_top_ranged=r_rax[0], dire_ancient_bot=d_towers[1], dire_ancient_top=d_towers[0], radiant_bottom_1=r_towers[10], radiant_middle_1=r_towers[7], radiant_top_1=r_towers[4], radiant_bottom_2=r_towers[9], radiant_middle_2=r_towers[6], radiant_top_2=r_towers[3], radiant_bottom_3=r_towers[8], radiant_middle_3=r_towers[5], radiant_top_3=r_towers[2], radiant_bottom_ranged=r_rax[4], radiant_bottom_melee=r_rax[5], radiant_mid_ranged=r_rax[2], radiant_mid_melee=r_rax[3], radiant_top_melee=r_rax[1], radiant_top_ranged=r_rax[0], radiant_ancient_bot=r_towers[1], radiant_ancient_top=r_towers[0])
								map_details = "\nT = Tower, m = Melee Rax, r = Ranged Rax, X = Structure destroyed"
								header = radiant + " " + str(radiant_id) + str(radiant_score) + "| " + str(duration) + " minutes" + " |" + str(dire_score) + " " + dire + str(dire_id) + "\n"
								final_message = header + dota_map + map_details
								bot.send_message(cid, "`{final_message}`".format(final_message=final_message), parse_mode="Markdown")

							elif "-lis" in content:
								dota_match = "\n_Radiant Structures:\nRax:\n  Top melee: {radiant_top_melee}\n  Top ranged: {radiant_top_ranged}\n  Mid melee: {radiant_mid_melee}\n  Mid ranged: {radiant_mid_ranged}\n  Bot melee: {radiant_bottom_melee}\n  Bot ranged: {radiant_bottom_ranged}\nAncient Towers:\n  Top Ancient Tower: {radiant_ancient_top}\n  Bot Ancient Tower: {radiant_ancient_bot}\nTop Towers:\n  Tier 1: {radiant_top_1}\n  Tier 2: {radiant_top_2}\n  Tier 3: {radiant_top_3}\nMid Towers:\n  Tier 1: {radiant_middle_1}\n  Tier 2: {radiant_middle_2}\n  Tier 3: {radiant_middle_3}\n Bottom Towers:\n Tier 1: {radiant_bottom_1}\n  Tier 2: {radiant_bottom_2}\n  Tier 3: {radiant_bottom_3}\n\n_Dire Structures:\nRax:\n  Top melee: {dire_top_melee}\n  Top ranged: {dire_top_ranged}\n  Mid melee: {dire_mid_melee}\n  Mid ranged: {dire_mid_melee}\n  Bot melee: {dire_bottom_melee}\n  Bot ranged: {dire_bottom_ranged}\nAncient Towers:\n  Top Ancient Tower: {dire_ancient_top}\n  Bot Ancient Tower: {dire_ancient_bot}\nTop Towers:\n  Tier 1: {dire_top_1}\n  Tier 2: {dire_top_2}\n  Tier 3: {dire_top_3}\nMid Towers:\n  Tier 1: {dire_middle_1}\n  Tier 2: {dire_middle_2}\n  Tier 3: {dire_middle_3}\n Bottom Towers:\n Tier 1: {dire_bottom_1}\n  Tier 2: {dire_bottom_2}\n  Tier 3: {dire_bottom_3}".format(dire_bottom_1=d_towers[10], dire_middle_1=d_towers[7], dire_top_1=d_towers[4], dire_bottom_2=d_towers[9], dire_middle_2=d_towers[6], dire_top_2=d_towers[3], dire_bottom_3=d_towers[8], dire_middle_3=d_towers[5], dire_top_3=d_towers[2], dire_bottom_ranged=r_rax[4], dire_bottom_melee=r_rax[5], dire_mid_ranged=r_rax[2], dire_mid_melee=r_rax[3], dire_top_melee=r_rax[1], dire_top_ranged=r_rax[0], dire_ancient_bot=d_towers[1], dire_ancient_top=d_towers[0], radiant_bottom_1=r_towers[10], radiant_middle_1=r_towers[7], radiant_top_1=r_towers[4], radiant_bottom_2=r_towers[9], radiant_middle_2=r_towers[6], radiant_top_2=r_towers[3], radiant_bottom_3=r_towers[8], radiant_middle_3=r_towers[5], radiant_top_3=r_towers[2], radiant_bottom_ranged=r_rax[4], radiant_bottom_melee=r_rax[5], radiant_mid_ranged=r_rax[2], radiant_mid_melee=r_rax[3], radiant_top_melee=r_rax[1], radiant_top_ranged=r_rax[0], radiant_ancient_bot=r_towers[1], radiant_ancient_top=r_towers[0])
								details = "\n\nT = Tower, m = Melee Rax, r = Ranged Rax, X = Structure destroyed"
								header = radiant + " " + str(radiant_id) + str(radiant_score) + "| " + str(duration) + " |" + str(dire_score) + " " + dire + str(dire_id) + "\n"
								final_message = header + dota_match + details
								bot.send_message(cid, "`{final_message}`".format(final_message=final_message), parse_mode="Markdown")
							else:
								bot.reply_to(message, "`Please enter a valid option:\n-map for a view of the map\n-lis to get a list of the structures (recommended for small screens)\n\n then follow the option with a live tournament ID\n\nEx: /dlmap -map <ID> `", parse_mode="Markdown")
						except IndexError:
							bot.reply_to(message, "`There has been an error, this game probably is over by now, check in a while or use /dotamatch`", parse_mode="Markdown")
			if not found:
				bot.reply_to(message, "`I could not find any game with that ID.\n\nMaybe the game is already finished, try using /dmatch`", parse_mode="Markdown")
		else:
			bot.reply_to(message, "`Follow this command with\n-map for a view of the map\n-lis to get a list of the structures (recommended for small screens)\n\n then follow the option with a live tournament ID\n\nEx: /dlmap -map <ID> `", parse_mode="Markdown")

# Dota Match ID

@bot.message_handler(commands=['dotamatch', 'dmatch'])
def dota_match(message):
	if intime(message):
		try:
			dota_key
		except:
			print "\n\n\t\tPlease setup dota api key\n\n"
		cid = getCID(message)
		match_id = getContent(message)
		if match_id and match_id != "-?":
			url ="http://api.steampowered.com/IDOTA2Match_570/GetMatchDetails/v1/?key=" + dota_key + "&format=JSON&language=en_us&match_id=" + match_id
			if validLink(url):
				game = getJson(url)
				game = game['result']
				hero_list = getJson("http://api.steampowered.com/IEconDOTA2_570/GetHeroes/v1/?key=" + dota_key + "&format=JSON&language=en_us")
				if 'players' in game:
					dire = ""
					radiant = ""
					for player in game['players']:
						for hero in hero_list['result']['heroes']:
							if player['hero_id'] == hero['id']:
								player_hero = hero['localized_name']
								break
						player_slot = player['player_slot']
						kills = player['kills']
						deaths = player['deaths']
						assists = player['assists']
						lh = player['last_hits']
						denies = player['denies']
						gpm = player['gold_per_min']
						xpm = player['xp_per_min']
						level = player['level']
						gold = player['gold']
						if deaths != 0:
							kda = float(kills+assists)/float(deaths)
							kda = str(kda)
							kda = kda[0:3]
						else:
							kds = 0
						if player_slot < 10:
							radiant += "> " + str(player_hero) +" " + str(level) + " " + str(kills) + "/" + str(deaths) + "/" + str(assists) + " " + kda + " " + str(gold) + " " + str(lh) + " " + str(denies) + " " + str(gpm) + " " + str(xpm) + "\n"
						else:
							dire += "> " + str(player_hero) +" " + str(level) + " " + str(kills) + "/" + str(deaths) + "/" + str(assists) + " " + kda + " " + str(gold) + " " + str(lh) + " " + str(denies) + " " + str(gpm) + " " + str(xpm) + "\n"
					header = "|Hero|Level|K|D|A|KDA|Gold|LH|DN|GPM|XPM\n"
					divider = "\n"
					match = "_Radiant Team\n" + header + radiant + divider + "_Dire team\n" + header + dire
					dotabuff = "http://www.dotabuff.com/matches/" + match_id
					dotabuff = treatLink(dotabuff)
					bot.send_message(cid, '`{match}`'.format(match=match) + '\n\t[Dota Buff Page]({dotabuff})'.format(dotabuff=dotabuff), parse_mode="Markdown", disable_web_page_preview=True)
				else:
					bot.reply_to(message, "`Match not found.\n\nRemember that it cant be a live match.`", parse_mode="Markdown")
			else:
				error = validLink(url)
				bot.reply_to(message, "`There has been an error, the number {error} to be specific.`".format(error=error), parse_mode="Markdown")
		else:
			bot.reply_to(message, "`Follow this command with a match ID and I will send the final scoreboard of the match, remember that it cant be a live match.`", parse_mode="Markdown")

# Dota Streams

@bot.message_handler(commands=['dotastreams', 'dstreams'])
def dota_streams(message):
	if intime(message):
		content = getContent(message)
		cid = getCID(message)
		if content != "-?":
			url = "http://www.gosugamers.net/dota2/streams"
			request = requests.get(url)
			soup = BeautifulSoup(request.text, "html.parser")
			streams = soup.findAll("a", class_="box-item-overlay news-overlay")
			streamlist = ""
			for stream in streams:
				channel = stream.find('label', class_="channel")
				channel = channel.string
				channel = channel.replace("\n","")
				streamurl = stream.attrs['href']
				streamurl = "http://www.gosugamers.net/" + streamurl
				streamlist += "`> `" + "[" + channel + "]" + "(" + streamurl + ")" + "\n"
			final_message = "`These are the available streams:`\n\n" + streamlist
			bot.send_message(cid, final_message, parse_mode="Markdown")
		else:
			bot.reply_to(message, "`Send this command alone and I will show you the list of streams currently available`", parse_mode="Markdown")


# Dota Commands

@bot.message_handler(commands=['dota'])
def dota_commands(message):
	if intime(message):
		cid = getCID(message)
		bot.send_message(cid, "`> Dota related commands: \n\n  /dotanews - Sends you the last dota new on the blog\n  /dmatch <Match ID> - Displays the info for a dota match\n  /dlive - Displays a list of up to 10 live tournament games\n  /dleague <League ID> - Displays the info of a League\n  /dldetails <MatchID> - displays live information from a tournament match\n  /dlmap <option> <MatchID> - displays live map information from a tournament match`", parse_mode="Markdown")

# Steam Commands

@bot.message_handler(commands=['steam'])
def steam_commands(message):
	if intime(message):
		cid = getCID(message)
		bot.send_message(cid, u'`> Steam related commands:\n\n  /steamid <game> - Returns the games ID\n  /steampage <ID> - Returns the games information\n  /steamdetails <ID> - Game details such as single player or multiplayer\n  /steamnews <ID> - Returns the last new from a game, it may contain weird formating.`\n\n`I will also auto detect steam store links and return the games information.`', parse_mode="Markdown")

# Get Steam News

@bot.message_handler(commands=['steamnews'])
def steam_news(message):
	if intime(message):
		cid = getCID(message)
		steamid = getContent(message)
		if steamid and steamid != "-?":
			url = "http://api.steampowered.com/ISteamNews/GetNewsForApp/v0002/?appid=" + steamid + "&count=3&maxlength=300&format=json"
			request = requests.get(url)
			data = request.json()
			if request.status_code == 200:
				title = data['appnews']['newsitems'][0]['title']
				content = data['appnews']['newsitems'][0]['contents']
				links = re.findall(r'<a[^>]*\shref="(.*?)"', content)
				for link in links:
					content = content.replace(link, "")
					content = content.replace('<', "")
					content = content.replace('>', "")
					content = content.replace('href=""', "")
				url = data['appnews']['newsitems'][0]['url']
				bot.send_message(cid, u'`> {title}\n\n{content}\n\n`'.format(title=title, content=content) + '[More info here]({url})'.format(url=url), parse_mode="Markdown", disable_web_page_preview=True)
			else:
				bot.reply_to(message, "`There has been an error, the number {error} to be specific.`".format(error=request.status_code), parse_mode="Markdown")
		else:
			bot.reply_to(message, "`Follow this command with the ID of a steam game and I will give you the last posted new, use /steamid if you dont know the ID of your game`",parse_mode="Markdown")

# Steam game ID

@bot.message_handler(commands=['steamid'])
def steam_id(message):
	if intime(message):
		try:
			dota_key
		except:
			print "\n\n\t\tPlease setup dota api key\n\n"
		name = getContent(message)
		if name and name != "-?":
			name = unicode(name)
			cid = getCID(message)
			url = "http://api.steampowered.com/ISteamApps/GetAppList/v2/?key=" + dota_key + "&format=JSON&language=en_us"
			request = requests.get(url)
			data = request.json()
			found = False
			if request.status_code == 200:
				for app in data['applist']['apps']:
					if app['name'].lower() == name.lower():
						appid = app['appid']
						url = "http://store.steampowered.com/app/" + unicode(appid) + "/"
						bot.send_message(cid, u"`{name}: {appid}\n\n/steampage <ID>\n/steamdetails <ID>\n/steamnews <ID>`".format(appid=appid, name=name) + u"\n\n[Store Link]("+url+")", parse_mode="Markdown", disable_web_page_preview=True)
						found = True
						break
				if not found:					
					bot.send_message(cid, "`I did not find {name} on steams app list`".format(name=name), parse_mode="Markdown")
			else:
				bot.reply_to(message, "`There has been an error, the number {error} to be specific.`".format(error=request.status_code), parse_mode="Markdown")
		else:
			bot.reply_to(message, "`Follow this command with the name of a steam game and I will give you its ID, useful to use along with\n\n/steamnews\n/steampage`", parse_mode="Markdown")

# Steam auto game page

@bot.message_handler(func=lambda message: "http://store.steampowered.com/app/" in message.text)
def steam_auto_page(message):
	if intime(message):
		cid = getCID(message)
		url = re.findall(r'(http[s]?://(?:store.steampowered.com/app+.*\S*))+', message.text)
		url = url[0]
		request = requests.get(url)
		if request.status_code == 200:
			try:
				data = request.text
				soup = BeautifulSoup(data, "html.parser")

				description = soup.findAll('div', class_='game_description_snippet')
				description = description[0].string
				description = description.replace("\t","")

				review_points = soup.findAll('span', class_='game_review_summary')
				review_points = review_points[0].string

				release_date = soup.findAll('span', class_='date')
				release_date = release_date[0].string

				price = soup.findAll('div', class_="game_purchase_price price")
				price = price[0].string
				price = price.replace("\t","")
				price = price.replace("\n","")

				img = soup.find('img', class_='game_header_image_full')['src']
				
				title = soup.findAll('div', class_='apphub_AppName')
				title = title[0].string
				invis = u"\u2063"
				try:
					image_prev = "[{invis}​​​​​​​​​]".format(invis=invis) + "({img})".format(img=img)
				except:
					image_prev = ""				
				bot.send_message(cid,"`> {title} - {price} \n\n {description}\n\nUser reviews: {reviews}\nRelease date: {release_date}`".format(title=title, price=price, description=description, reviews = review_points, release_date=release_date) + "[.]({image_prev})\n\n [More info]({url})".format(image_prev=img, url=url), parse_mode="Markdown")
			except:
				pass
		else:
			pass

# Steam Game page

@bot.message_handler(commands=['steampage'])
def steam_page(message):
	if intime(message):
		appid = getContent(message)
		cid = getCID(message)
		if appid and appid != "-?":
			url = "http://store.steampowered.com/app/" + appid + "/"
			request = requests.get(url)
			if request.status_code == 200:
				try:
					data = request.text
					soup = BeautifulSoup(data, "html.parser")
					description = soup.findAll('div', class_='game_description_snippet')
					description = description[0].string
					description = description.replace("\t","")
					review_points = soup.findAll('span', class_='game_review_summary')
					if review_points:
						review_points = review_points[0].string
					else:
						review_points = ""
					release_date = soup.findAll('span', class_='date')
					release_date = release_date[0].string
					price = soup.findAll('div', class_="game_purchase_price price")
					future_release = soup.findAll('div', class_="game_area_comingsoon game_area_bubble")
					if not price and not future_release:
						price = soup.findAll('div', class_="discount_final_price")
						price = price[0].string
						price = price.replace("\t","")
						price = price.replace("\n","")
						discounted = soup.findAll('div', class_="discount_original_price")
						discounted = discounted[0].string
						discounted = discounted.replace("\t","")
						discounted = discounted.replace("\n","")
						price = price + " discounted from " + discounted
					elif not price:
						price = soup.findAll('div', class_="game_area_comingsoon game_area_bubble")
						price = price[0].h1.string
						price = price.replace("\t", "").replace("\n", "")
					else:
						price = price[0].string
						price = price.replace("\t","")
						price = price.replace("\n","")
					img = soup.find('img', class_='game_header_image_full')['src']
					title = soup.findAll('div', class_='apphub_AppName')
					title = title[0].string
					bot.send_message(cid,u"`> {title} - {price} \n\n {description}\n\nUser reviews: {reviews}\nRelease date: {release_date}`".format(title=title, price=price, description=description, reviews = review_points, release_date=release_date) + u"[​]({image_prev})\n\n [More info]({url})".format(image_prev=img, url=url), parse_mode="Markdown")
				except:
					bot.send_message(cid, u"`Sorry, I did not find any game with that ID, please try again or look it up with /steamid`", parse_mode="Markdown")
			else:
				bot.reply_to(message, "`There has been an error, the number {error} to be specific.`".format(error=request.status_code), parse_mode="Markdown")

		else:
			bot.reply_to(message, "`Follow this command with the ID of a steam game and I will give you its basic information, use /steamid if you dont know the ID of your game.`", parse_mode="Markdown")
			
# Steam details

@bot.message_handler(commands=['steamdetails'])
def steam_details(message):
	if intime(message):
		appid = getContent(message)
		cid = getCID(message)
		if appid and appid != "-?":
			url = "http://store.steampowered.com/app/" + appid + "/"
			request = requests.get(url)
			if request.status_code == 200:
				data = request.text
				soup = BeautifulSoup(data, "html.parser")
				try: 
					details = soup.findAll('div', class_="block responsive_apppage_details_left")
					detlist = ""
					for detail in details[0].find_all('div'):
						if detail.text:
							detlist += "> " + detail.text + "\n"
					price = soup.findAll('div', class_="game_purchase_price price")
					future_release = soup.findAll('div', class_="game_area_comingsoon game_area_bubble")
					if not price and not future_release:
						price = soup.findAll('div', class_="discount_final_price")
						price = price[0].string
						price = price.replace("\t","")
						price = price.replace("\n","")
						discounted = soup.findAll('div', class_="discount_original_price")
						discounted = discounted[0].string
						discounted = discounted.replace("\t","")
						discounted = discounted.replace("\n","")
						price = price + " discounted from " + discounted
					elif not price:
						price = soup.findAll('div', class_="game_area_comingsoon game_area_bubble")
						price = price[0].h1.string
						price = price.replace("\t", "").replace("\n", "")
					else:
						price = price[0].string
						price = price.replace("\t","")
						price = price.replace("\n","")
					title = soup.findAll('div', class_='apphub_AppName')
					title = title[0].string

					bot.send_message(cid,u"`- {title} - {price}\n\n{detlist}`".format(title=title, price=price, detlist=detlist) + "\n\n[More info]({url})".format(url=url) , parse_mode="Markdown", disable_web_page_preview=True)
				except:
					bot.send_message(cid, "`Sorry, I did not find any game with that ID, please try again or look it up with /steamid`", parse_mode="Markdown")					
			else:
				bot.reply_to(message, "`There has been an error, the number {error} to be specific.`".format(error=request.status_code), parse_mode="Markdown")
		else:
			bot.reply_to(message, "`Follow this command with the ID of a steam game and I will give you its details, use /steamid if you dont know the ID of your game.`")

# Lyrics

@bot.message_handler(commands=['lyrics'])
def lyrics(message):
	if intime(message):
		cid = getCID(message)
		search = getContent(message)
		if search and search != "-?":
			search = re.findall(r'(.*) - {1}(.*)', search)
			try:
				artist = search[0][0]
				song = search[0][1]
				url = "http://lyrics.wikia.com/wiki/" + artist + ":" + song
				request = requests.get(url)
				data = request.text
				soup = BeautifulSoup(data, "html.parser")
				lyrics = soup.find('div', class_='lyricbox')
				lyrics = lyrics.contents
				lyric = ""
				listlen = len(lyrics)
				for line in lyrics[1:listlen-5]:
				 	if line.string != None:
				 		lyric += line.string
				 	else:
				 		lyric += "\n"
				if message.chat.type != "private":
					bot.send_message(cid, u"`> {artist} - {song}:\n\n{lyric}\n\nI suggest that you use this in private so we dont spam this group`".format(artist=artist, song=song, lyric=lyric), parse_mode="Markdown")
				else:
					bot.send_message(cid, u"`> {artist} - {song}\n\n{lyric}`".format(artist=artist, song=song, lyric=lyric), parse_mode="Markdown")
			except:
				bot.reply_to(message, "`Lyric not found, make sure the name of the song is well written and in the correct format\n\n<artist> - <song>.`", parse_mode="Markdown")
		else:
			bot.reply_to(message, "`Follow this message with <artist> - <song> and I will display the lyrics.\n\nI highly advice this to be used on private conversations instead of groups.`", parse_mode="Markdown")

# Weather

@bot.message_handler(commands=['weather'])
def weather_command(message):
	if intime(message):
		try:
			weather_api
		except:
			"\n\n\t\tPlease setup weather api key\n\n"
		city = getContent(message)
		cid = getCID(message)
		if city and city != "-?":
			try:

				city = city.replace(" ", "")
				url = "http://api.openweathermap.org/data/2.5/weather?appid=" + weather_api + "&q=" + city
				weather = getJson(url)
				city = weather['name']
				country = weather['sys']['country']

				weather_info = weather['weather'][0]['description']

				temp = weather['main']['temp']
				temp_cels = unicode(kelv2cels(temp)) + u" °C"
				temp = unicode(kelv2far(temp)) + u" °F"

				temp_min = weather['main']['temp_min']
				temp_min_cels = unicode(kelv2cels(temp_min)) + u" °C"
				temp_min = unicode(kelv2far(temp_min)) + u" °F"

				temp_max = weather['main']['temp_max']
				temp_max_cels = unicode(kelv2cels(temp_max)) + u" °C"
				temp_max = unicode(kelv2far(temp_max)) + u" °F"

				wind_speed = weather['wind']['speed']
				wind_speed = unicode(wind_speed) + u" meter/sec"

				humid = unicode(weather['main']['humidity']) + u"%"

				final_message = u"> Weather for " + city + ", " + country + ":\n\nWeather: " + weather_info.capitalize() + u"\n\nTemperature °F:\n   " + temp + "\n   Max: " + temp_max + "\n   Min: " + temp_min + u"\nTemperature °C: \n   " + temp_cels + "\n   Max: " + temp_max_cels + "\n   Min: " + temp_min_cels + "\n\n" + "Wind Speed: " + wind_speed
				bot.send_message(cid, u"`{final_message}`".format(final_message=final_message), parse_mode="Markdown" )
			except:
				bot.reply_to(message,"`There has been an error, please try again\n\nFollow this command with your city's:\n- Name\n- Geographic Coordinates - Lat=<lat> Lon=<lon>\n- ZIP code - zip=<zip code>,<country>\n\n/weather zip=94040,us`")
		else:
			bot.reply_to(message,"`Follow this command with your city's:\n- Name\n- Geographic Coordinates - Lat=<lat> Lon=<lon>\n- ZIP code - zip=<zip code>,<country>\n\n/weather zip=94040,us`")


# Mercadolibre

@bot.message_handler(commands=['ml', 'mercadolibre', 'ML','MercadoLibre'])
def mercadolibre(message):
	if intime(message):
		search = getContent(message)
		cid = getCID(message)
		try:
			if search and search != "-?":
				url = "https://api.mercadolibre.com/sites/MLV/search?q=" + search + "#json"
				data = getJson(url)
				query = data['query']
				listing = ""
				for result in data['results'][0:5]:
					if result['accepts_mercadopago']:
						mercadopago = "\n` MercadoPago`"
					else:
						mercadopago = ""
					cantidad = str(result['available_quantity'])
					if result['condition'] == 'new':
						condicion = "`Nuevo`"
					else:
						condicion = "`Usado`"
					perma = result['permalink']
					perma = treatLink(perma)
					vendidos = str(result['sold_quantity'])
					titulo = unicode(result['title'])
					state = result['seller_address']['state']['name']
					precio = str(result['price'])
					precio = " Bs. " + precio  
					listing += u"`> `" + "[" + titulo + "]" +"(" + perma + ")" + "`\n" + precio + "`\n  `" + state + " - `" + condicion + "\n  `Cant: " + cantidad + " | Vendidos: " + vendidos + "`" + mercadopago + "\n"
				final_message = u"`Top 5 resultados para "+ query + ": `\n" + listing
				bot.send_message(cid, final_message, parse_mode="Markdown")
			else:
				bot.reply_to(message, "`Spanish exclusive command\n\nBusqueda de articulos en MercadoLibre.com.ve`", parse_mode="Markdown")
		except:
			bot.reply_to(message, "Something went wront, please try again later.", parse_mode="Markdown")
		
# Dolar today

@bot.message_handler(commands=['dt', 'dolartoday', 'dolortoday'])
def dolar_today_message(message):
	if intime(message):
		cid = getCID(message)
		content = getContent(message)
		if content != "-?":
			url = "https://s3.amazonaws.com/dolartoday/data.json"
			request = requests.get(url)
			data = request.json()
			if request.status_code == 200:
				dolartoday_usd = data['USD']['dolartoday']
				implicito_usd = data['USD']['efectivo']
				simadi_usd = data['USD']['sicad2']
				dolartoday_eur = data['EUR']['dolartoday']
				implicito_eur = data['EUR']['efectivo']
				simadi_eur = data['EUR']['sicad2']
				date = data['_timestamp']['fecha']
				bot.send_message(cid, u"`$ Dolar Today, {date}\n > USD\nDolar Today: BsF. {dolartoday_usd}\nImplicito: BsF. {implicito_usd}\nSimadi: BsF. {simadi_usd}\n> EUR \nDolar Today: BsF. {dolartoday_eur}\nImplicito: BsF. {implicito_eur}\nSicad: BsF. {simadi_eur}`".format(date=date, dolartoday_usd=dolartoday_usd, implicito_usd=implicito_usd, simadi_usd=simadi_usd, dolartoday_eur=dolartoday_eur, implicito_eur=implicito_eur, simadi_eur=simadi_eur), parse_mode="Markdown")
			else:
				bot.reply_to(message, "`There has been an error, the number {error} to be specific.`".format(error=request.status_code), parse_mode="Markdown")
		else:
			bot.reply_to(message, "`Venezuela exclusive commmand\n\nInformacion basica desde dolartoday.`", parse_mode="Markdown")

# imdb

@bot.message_handler(commands=['imdb'])
def imdb_message(message):
	if intime(message):
		cid = getCID(message)
		title = getContent(message)
		if title and title != "-?":
			url = "http://www.omdbapi.com/?t="+ title
			request = requests.get(url)
			data = request.json()
			if request.status_code == 200:
				if data['Response'] == "True":
					movie_title = data['Title']
					movie_year = data['Year']
					movie_release = data['Released']
					movie_runtime = data['Runtime']
					movie_rate = data['imdbRating']
					movie_genre = data['Genre']
					movie_rated = data['Rated']
					movie_plot = data['Plot']
					movie_permalink = data['imdbID']
					movie_director = data['Director']
					movie_writer = data['Writer']
					movie_permalink = "http://www.imdb.com/title/" + movie_permalink + "/"
					movie_poster = data['Poster']
					movie_actors = data['Actors']
					message_imdb = u"`` ` >` [{title}]({link}) `({rated}) - [{year}]`\n\n    `★ {rate}/10\n{time} - {genre}`\n\n`{plot}`\n\n`Actors: {actors}`\n`Director: {director}`"

					bot.send_message(cid, u"[​]({poster})".format(poster=movie_poster) + message_imdb.format(rated=movie_rated, title=movie_title, link=movie_permalink, year=movie_year, rate=movie_rate, plot=movie_plot, genre=movie_genre, time=movie_runtime, writer=movie_writer, director=movie_director, actors=movie_actors), parse_mode="Markdown")
				elif "Response" in data:
					bot.reply_to(message, u"`There has been an error:\n> {error}`".format(error=data['Error']), parse_mode="Markdown")
			else:
				bot.reply_to(message, "`There has been an error, the number {error} to be specific.`".format(error=request.status_code), parse_mode="Markdown")
		else:
			bot.reply_to(message, "`Send this command along with the title of a movie to get its information.`",parse_mode="Markdown")

# Tweet

@bot.message_handler(commands=['tw'])
def tweetadm(message):
	tweet = getContent(message)
	try:
		api
	except:
		print "\n\n\t\tPlease setup your tweepy api key\n\n"
	if message.from_user.id == adminid:
		if len(tweet) <= 140:
			api.update_status(unicode(tweet))
			bot.send_message(adminid, "`Tweet sent.`", parse_mode="Markdown")
		else:
			bot.reply_to(message, "`Tweet is " + str(len(tweet) - 140) + " characters longer than accepted lenght`", parse_mode="Markdown")
	else:
		bot.reply_to(message, "`Access Denied.`", parse_mode="Markdown")

# auto tweet

@bot.message_handler(func=lambda message: "twitter.com" in message.text and "/status/" in message.text)
def tweepy_f(message):
	if intime(message):
		try:
			api
			tweets= ""
			tweet_id = re.findall(r'/status/+(\d*)', unicode(message.text))
			try:
				status = api.get_status(tweet_id[0])
				tweet = status.text
				favs = str(status.favorite_count)
				RTs = str(status.retweet_count)
				user = status.user.screen_name
				username = status.user.name
			except:
				pass
			try:
				try:
					quoted_tweet = status.quoted_status["text"]
					quoted_user = status.quoted_status["user"]["screen_name"]
					quoted_username = status.quoted_status["user"]["name"]
					bot.reply_to(message, u"`_______quoted tweet_______\n  > Tweet from {quoted_username}({quoted_user})`\n".format(quoted_username=quoted_username, quoted_user=quoted_user) + u"{quoted_tweet}".format(quoted_tweet=quoted_tweet) + "`\n_____end of quoted tweet_____`\n\n`RTs:{RTs} | Likes: {favs}\n`".format(RTs=RTs, favs=favs), parse_mode="Markdown")	
				except:
					bot.reply_to(message, u"`> Tweet from {username}(@{user}):`".format(user=user, username=username) + "\n`RTs:{RTs} | Likes: {favs}\n`".format(RTs=RTs, favs=favs), parse_mode="Markdown", disable_web_page_preview=True)
			except:
				pass
		except:
			print "\n\n\t\tPlease setup your tweepy api key\n\n"

# Cat api

@bot.message_handler(commands=['cat'])
def catapi(message):
	if intime(message):
		try:
			catapi_key
		except:
			print "\n\n\t\tPlease setup cat api key\n\n"
		content = getContent(message)
		if content != "-?":
			cid = getCID(message)
			url = "http://thecatapi.com/api/images/get?format=html&api_key=" + catapi_key
			request = requests.get(url)
			data = re.findall(r'<img[^>]*\ssrc="(.*?)"', request.text)
			data = treatLink(data[0])
			if request.status_code == 200:
				bot.send_message(cid, u'[​]({data})'.format(data=data), parse_mode="Markdown")
			else:
				bot.reply_to(message, "`There has been an error, the number {error} to be specific.`".format(error=request.status_code), parse_mode="Markdown")
		else:
			bot.reply_to(message, "`Send this command alone and I will send you a random cat picture.`", parse_mode="Markdown")

# Facts

@bot.message_handler(commands=['fact'])
def fact(message):
	if intime(message):
		cid = getCID(message)
		content = getContent(message)
		if content != "-?":
			request = requests.get("http://freehostedscripts.net/fq.php")
			if request.status_code == 200:
				data = request.text
				soup = BeautifulSoup(data, "html.parser")
				fact = re.findall(r'("{1}.*)+(Interesting Facts)', soup.get_text())
				fact = fact[0][0] + '"'
				fact = unicode(fact)
				try:
					bot.send_message(cid, u"`{fact}`".format(fact=fact), parse_mode="Markdown")
				except:
					bot.send_message(cid, u"`This in fact, is not a fact, something went wrong, please try again.`", parse_mode="Markdown")
			else:
				bot.reply_to(message, "`There has been an error, the number {error} to be specific.`".format(error=request.status_code), parse_mode="Markdown")
		else:
			bot.reply_to(message, "`Send this command alone and I will send you a random fact.`", parse_mode="Markdown")

# Wiki

@bot.message_handler(commands=['wiki'])
def wiki_plug(message):
	if intime(message):
		if getContent(message) and getContent(message) != "-?":
			cid = getCID(message)
			url = "https://en.wikipedia.org/wiki/" + getContent(message)
			request = requests.get(url)
			if request.status_code == 200:
				data = request.text
				soup = BeautifulSoup(data, "html.parser")
				info = ""
				for content in soup.p.contents:
					info += unicode(content.string)
				if info != "None":
					bot.send_message(cid, u"`Wikipedia Result\n\n \t> {Search} \n\n{info}\n`".format(info=info, Search=getContent(message)) + "\n[more detailed information]({link})".format(link=url.replace(" ", "_")), parse_mode="Markdown", disable_web_page_preview=True)
				else:
					bot.send_message(cid, u"`Wikipedia Result\n\n \t> {Search} \n\nSorry user, this wiki page is terribly formatted and my coder was tired, feel free to check the link below\n`".format(Search=getContent(message)) + "\n[more detailed information]({link})".format(link=url.replace(" ", "_")), parse_mode="Markdown", disable_web_page_preview=True)
			elif request.status_code == 404:
				bot.reply_to(message, "`Sorry, I could not find any result.`", parse_mode="Markdown")
			else:
				bot.reply_to(message, "`There has been an error, the number {error} to be specific.`".format(error=request.status_code), parse_mode="Markdown")
		else:
			bot.send_message(cid, "`Follow this command with your search, then I will print resumed info if the search finds results.`", parse_mode="Markdown")

# Cambridge Dict

@bot.message_handler(commands=['dict'])
def dictcam(message):
	if intime(message):
		word = getContent(message)
		cid = getCID(message)
		if word and word != "-?":
			url = "http://dictionary.cambridge.org/dictionary/english/" + word
			try:
				request = requests.get(url)
				data = request.text
				soup = BeautifulSoup(data, "html.parser")
				definitions = soup.find_all('span', class_='def-block')
				results = ""
				result_num = 0
				for definition in definitions[0:1]:
					result_num += 1
					defi = definition.find('span', class_='def')
					defi = defi.text
					examples_list = ""
					examples = definition.find_all('span', class_='examp')
					for example in examples:
						examples_list += "- " + example.text + "\n"
					gc = definition.find_all('span', class_='gc')
					gc_list = ""
					for component in gc:
						gc_list += component['title'] + "\n"
					results +=gc_list + "\n" + defi + "\n\n" + examples_list + "\n"
				pos = soup.find('span', class_='pos').text
				ipa = soup.find('span', class_='ipa').text
				word = soup.find('span', class_='hw').text

				link = treatLink(url)
				link = "\n[Cambridge word page]({link})".format(link=link)
				final_message = "> " + word + "  |  " + pos + "  /" + ipa + "/\n\n" + results

				bot.send_message(cid, u"`{final_message}`".format(final_message=final_message) + link, parse_mode="Markdown", disable_web_page_preview=True)
			except:
				bot.reply_to(message, "`Your search term did not match any definition.`",parse_mode="Markdown")

		else:
			bot.reply_to(message, "`Follow this command to get up to two definitions from the Cambridge Dictionary.`", parse_mode="Markdown")


"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
			AUTO MESSAGE RESPONSES
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# Good night 

@bot.message_handler(func=lambda message: 'good night' in message.text.lower() or 'buenas noches' in message.text.lower() or 'good night, rrr' in message.text.lower() )
def goodnight_message(message):
	if intime(message):
		cid = getCID(message)
		uid = getUID(message)
		uName = message.from_user.id		
		if uid == adminid:
			bot.send_message(cid, random.choice(good_night_admin), parse_mode="Markdown")
		else:
			bot.send_message(cid, random.choice(good_night), parse_mode="Markdown")

# Answer to beep

@bot.message_handler(func=lambda message: message.text.lower() == 'beep')
def boop(message):
	if intime(message):
		cid = getCID(message)
		bot.send_message(cid, '`Boop`', parse_mode="Markdown")

# Answer to boop

@bot.message_handler(func=lambda message: message.text.lower() == 'boop')
def boop(message):
	if intime(message):
		cid = getCID(message)
		bot.send_message(cid, '`Beep`', parse_mode="Markdown")

# Answer to bop

@bot.message_handler(func=lambda message: message.text.lower() == 'bop')
def bop(message):
	if intime(message):
		uid = getUID(message)
		cid = getCID(message)
		if uid == adminid:
			bot.send_message(cid, "`Stop it, you are embarrassing​ me`", parse_mode="Markdown")

# Answer to hi

@bot.message_handler(func=lambda message: message.text.lower() == 'hello, rad retro robot' or message.text.lower() == 'hello, rrr' or message.text.lower() == 'hi, rad retro robot' or message.text.lower() == 'hi, rrr' or  message.text.lower() == 'hello, radretrorobot' or  message.text.lower() == 'hi, radretrorobot')
def hello_messages(message):
	if intime(message):
		cid = getCID(message)
		bot.send_message(cid, random.choice(hello), parse_mode="Markdown")

# Love

@bot.message_handler(func=lambda message: message.text.lower() == 'i love you, rad retro robot' or message.text.lower() == 'i love you, radretrorobot' or message.text.lower() == 'i love you, rrr' or message.text.lower() == 'i love you rrr' or message.text.lower() == 'i love you, radretrorobot' or message.text.lower() == 'i love you rad retro robot')
def love_messages(message):
	if intime(message):
		cid = getCID(message)
		uid = getUID(message)
		uName = message.from_user.id
		if uid == adminid:
			bot.send_message(cid, random.choice(love_admin), parse_mode="Markdown")
		else:
			bot.send_message(cid, random.choice(love), parse_mode="Markdown")

# Shut up

@bot.message_handler(func=lambda message: message.text.lower() == 'shut up.' or message.text.lower() == 'shutup.')
def shutup(message):
	if message.from_user.id == adminid:
		bot.reply_to(message, "`No, fuck off.`", parse_mode="Markdown")


# Fuck you

@bot.message_handler(func=lambda message: message.text.lower() == "fuck you, rrr" or message.text.lower() == "fuck you, radretrorobot" or message.text.lower() == "fuck you, rad retro robot" or message.text.lower() == "fuck you rrr" or message.text.lower() == "fuck you radretrorobot" or message.text.lower() == "fuck you rad retro robot")
def fuckyou(message):
	if intime(message):
		cid = getCID(message)
		uid = getUID(message)
		bot.send_message(cid, random.choice(fuckyou_response), parse_mode="Markdown")

# Answer when mentioned

@bot.message_handler(func=lambda message: ('RRR' in message.text or 'radretrorobot' in message.text.lower() or 'rad retro robot' in message.text.lower()) and not ('/' in message.text.lower() or 'hi' in message.text.lower() or 'hello' in message.text.lower() or 'i love you' in message.text.lower()), content_types=['text'])
def mention(message):
	if intime(message):
		cid = getCID(message)
		if cid == adminid:
			bot.send_message(cid, random.choice(mentionadmin), parse_mode="Markdown")
		else:
			bot.send_message(cid, random.choice(mentioned), parse_mode="Markdown")


"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
						RANDOM REPEAT
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# Random repeats stuff
# Beeps and boops
# Always keep this on last

@bot.message_handler(func=lambda message: True, content_types=['text'])
def repeat(message):
	if intime(message):
		cid = getCID(message)
		gid = message.chat
		message_to_repeat = message.text
		if (random.randrange(1, repeatMax) == 1):
			try:
				if str(cid) not in loadjson("quietlist"):
					print "repeated"
					bot.send_message(cid, random.choice(repeat_message).format(message=message_to_repeat) , parse_mode="Markdown")
			except:
				pass

		if (random.randrange(1, beepMax) == 1):	
			try:
				if str(cid) not in loadjson("quietlist"):
					print "random beep sent"
					bot.send_message(cid, random.choice(beeps), parse_mode="Markdown")
			except:
				pass

# Welcome user

@bot.message_handler(content_types=['new_chat_participant'])
def welcomeuser(message):
	if intime(message):	
		cid = getCID(message)
		if message.new_chat_participant.id != botid:
			bot.send_message(cid, text_messages['welcomeusergroup'].format(groupname = message.chat.title), parse_mode="Markdown")
		elif message.new_chat_participant.id == botid:
			bot.send_message(cid, u"`Greetings humans, thanks for adding me to {groupname}, I hope we have fun together!\n\n`".format(groupname=message.chat.title) + "[You can join my channel to know about my updates!](https://telegram.me/RRRUpdates)", parse_mode="Markdown")
			if gid not in loadjson("grouplist"):
				addUser(gid, gName, "grouplist")


# Goodby user

@bot.message_handler(content_types=['left_chat_participant'])
def welcomeuser(message):
	if intime(message):	
		cid = getCID(message)
		bot.send_message(cid, "`Bye bye!`", parse_mode="Markdown")



print "Bot: running"
try:
	bot.polling()
except KeyboardInterrupt:
	pass
except:
	os.system("py RRR.py")