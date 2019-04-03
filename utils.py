import os
import sys
import requests
import time
import json
import re
import tweepy
import random
import wikipedia
import datetime
import binascii
import logging

from bs4 import BeautifulSoup
from tweepy import OAuthHandler
from datetime import datetime
from threading import Thread

import telegram
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, BaseFilter, RegexHandler, CallbackQueryHandler
from telegram.utils.helpers import escape_markdown, from_timestamp, to_timestamp

# Enabling logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', 
					level=logging.INFO)

logger = logging.getLogger(__name__)

config = json.load(open('config.json'))
if config['bot']:
	bot = telegram.Bot(token=config['bot'])
else:
	print ("###################################################")
	print ("# Please setup the needed keys in the config file #")
	print ("###################################################")
	sys.exit()


weather_api 	= config['weather']
reddit_user 	= config['reddit']
lastfm_key 		= config['lastfm']
google_time_key = config['google_time']
bing_key 		= config['bing']
steam_key 		= config['steam']
imgur_id 		= config['imgur']

# facebook stuff
facebook_app_secret = config['facebook']['app_secret']
facebook_app_id 	= config['facebook']['app_id']

# tweepy stuff
consumer_key 	= config['tweepy']['consumer_key']
consumer_secret = config['tweepy']['consumer_secret']
access_token 	= config['tweepy']['access_token']
access_secret 	= config['tweepy']['access_secret']
auth 			= OAuthHandler(consumer_key, consumer_secret)

auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

adminid = ### Set your ID here
adminTwitterUser = ### Set your Twitter User here
botid = bot.getMe().id
uptime = datetime.now()

def get_help(info):
	if type(info['triggers']) == tuple:
			trigger = info['triggers'][0]
			triggers =  "\n\n    Alternative Triggers:"
			for trigger in info['triggers']:
				triggers += "\n        " + trigger
	else:
		trigger = info['triggers']
		triggers = trigger
	if info['example']:
		return "`> " + info['name'] + "`\n\n    /" + trigger + " `" + info['arguments'] + "\n\n    " + info['help'].replace('\n', '\n    ') + "\n\n    Example:\n        " + info['example'].replace('\n', '\n        ') + triggers + "`"
	else:
		return "`> " + info['name'] + "`\n\n    /" + trigger + " `" + info['arguments'] + "\n\n    " + info['help'].replace('\n', '\n    ') + triggers + "`"

def makesoup(url):
	request = requests.get(url)
	data = request.text
	soup = BeautifulSoup(data, "html.parser")
	return soup

def kelv2far(temp):
	return temp * 9./5. - 459.67

def kelv2cels(temp):
	return temp - 273.15

def from24to12(hour):
	d = datetime.strptime(hour, "%H:%M:%S")
	return d.strftime("%I:%M %p")

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
	rname = re.findall(r'gfycat.com/[gifs/detail/]*(\w*)', url)
	data = requests.get('https://api.gfycat.com/v1/gfycats/' + rname[0])
	url = data.json()['gfyItem']['mp4Url']
	url2 = data.json()['gfyItem']['mobileUrl']
	title = data.json()['gfyItem']['title'] if data.json()['gfyItem']['title'] else ""
	print (rname, data, url)
	return url, url2, title

def getImgur(url):
	url = re.findall(r'(http[s]?://i.imgur.com/.+.gif[v]?)', url)[0]
	url = url if url[-1] == 'v' else url + "v"
	request = requests.get(url)
	title = BeautifulSoup(request.text, 'html.parser').title.text
	url = url.replace('gifv', 'mp4').replace('gif', 'mp4')
	return url, title

def getFBToken():
    global facebook_app_secret
    global facebook_app_id
    url = 'https://graph.facebook.com/oauth/access_token?client_id=' + facebook_app_id + '&client_secret=' + facebook_app_secret + '&grant_type=client_credentials'
    request = requests.get(url)
    return request.json()['access_token']

def getCID(update):
	return update.message.chat.id

def getUID(update):
	return update.message.from_user.id

def getCommand(update):
	command = re.findall(r'/{1}(\w*)', update.message.text)
	if command:
		return command[0]
	else:
		pass

def treatLyric(text):
	if type(text) == str:
		text = text.replace("<br>", "\n")
		return text

def urlsForAlbum(urls):
	video_output = []
	photo_output = []
	for url in urls:
		if "mp4" in url or "gif" in url:
			video_output.append(
							telegram.InputMediaVideo(
								media		=	url['url'],
								caption	=	url['caption']
							)
						)
		else:
			photo_output.append(
							telegram.InputMediaPhoto(
								media		=	url['url'],
								caption	=	url['caption']
							)

						)
	return photo_output, video_output

def sendAlbums(data_type, array, cid):
	if data_type == "photo":
		if len(array) > 10:
			number = len(array)
			start = 0
			stop = 10
			while number > 0:
				bot.send_media_group(cid, array[start:stop])
				start = stop
				stop += 10
				number -= 10
		else:
			print("\n\n--------------------------------")
			print(array)
			print("\n\n--------------------------------")
			bot.send_media_group(cid, array)
	else:
		if len(array) > 10:
			number = len(array)
			start = 0
			stop = 9
			while number > 0:
				bot.send_media_group(cid, array[start:stop])
				start = stop
				stop += 10
				number -= 10
		else:
			bot.send_media_group(cid, array)

def download_video(url):
    request = requests.get(url, stream=True)
    with open('@RadRetroRobot_Downloaded_Video.mp4', 'wb') as f:
        for chunk in request.iter_content(chunk_size=1024): 
            if chunk: # filter out keep-alive new chunks
                f.write(chunk)
                #f.flush() commented by recommendation from J.F.Sebastian
    return True

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

def addUser(userID, userName, filename, newUser=False, twitterVerifier='', requestToken='', clearData=False):
	if newUser:
		user = {
			userID : {'name': userName, 'fmuser' : '', 'twitter' : {'verifier': '', 'token' : ''}}
		}
	with open(filename + '.json') as f:
		data = json.load(f)
	
	if twitterVerifier and not clearData:
		data[str(userID)]['twitter']['verifier'] = twitterVerifier
	elif clearData:
		data[str(userID)]['twitter']['verifier'] = ''

	if requestToken and not clearData:
		data[str(userID)]['twitter']['token'] = requestToken
	elif clearData:
		data[str(userID)]['twitter']['token'] = ''

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

def error(bot, update, error):
	"""Log Errors caused by Updates."""
	logger.warning('Update "%s" caused error "%s"', update, error)
	bot.send_message(adminid, 'Update "%s" caused error "%s"', update, error)

fuckyou_response = [
		"`Sorry, I am not that kind of robot.`"
		"`I am not capable of doing that, that is for a diferent kind of robot.`"
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
beepMax = 500
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
repeatMax = 1500
repeat_message = [
		u"`{message}, I am a human`",
		u"`{message}`",
		u"`I am a human, I say things like {message}`",
		u"`{message}, is this really how you humans communicate?`",
		u"`It must be weird to be a fully functioning human being and say things like {message}`",
		u"`Trust in me, I'm a human, and like we all humans do, I say things like {message}`"

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
		u"`Great, can't I have a single moment without someone reminding me about feelings?`",
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
		u"`Make sure you come back when youre fully rested!`",
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
top_response_degen = [
		"`kek`",
		'`lel`',
		"`lek`",
		"`kel`",
		"`kecleon`",
		"`kecleon`"
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
	'shrug':
		u'`¯\_(ツ)_/¯`',
	'lenny':
		u'`( ͡° ͜ʖ ͡°)`',
	'stare':
		u'`ಠ_ಠ`'
}

text_messages = {
	'start': 
		u'`Welcome back to our personal chat! Remember that you can send` /help `to get a list my commands.`',
	'ping':
		u'`Hello! This is Rad Retro Robot and you are {name} {lname}({uid}), your username is` @{uname}',
	'pinggroup':
		u"`Hello! This is Rad Retro Robot and you are {name} {lname}({uid}), your username is` @{uname}\n\n"
		u"`We're speaking on {gName}({gid})`",
	'startfirst':
		u"`Greetings! Im Rad Retro Robot! Want to know about my options? Send` /help `and a list of the commands available for you will show up.`",
	'help_group_first':
		u"`Please, go ahead and `[PM me](https://t.me/radRetroRobot)`, click on the /start so I can get to know you.`",
	'startfirstgroup':
		u"`Greetings new human, I don't know you yet, please` [send me a PM](https://t.me/radRetroRobot) `so I can scan you!`",
	'startgroup':
		u"`I've sent you a message to our private conversation, let's not spam this group!`",
	'startfromgroup':
		u"`Hello, if you're interested on trying out stuff, play around here, let's not spam {title}`",
	'premade':
		u"/shrug\n"
		u"/lenny\n"
		u"/stare\n"
		u"/top\n"
}
