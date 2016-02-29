#!/usr/bin/env python
# -*- coding: utf-8 -*-

from utils import *

print "Loading " + __name__ + "..."

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

#	Destroyed

@bot.message_handler(func=lambda message: "/destroyed" in message.text.lower())
def prem_destr(message):
	if intime(message):
		cid = getCID(message)
		try:
			rid = message.reply_to_message
			bot.reply_to(rid, premade['destroy'], parse_mode="Markdown")
		except:	
			bot.send_message(cid, premades['destroy'], parse_mode="Markdown")

# Top kek

@bot.message_handler(func=lambda message: "/top" in message.text.lower())
def top_kek(message):
	if intime(message):
		cid = getCID(message)
		if not cid == degeneratesgroup:
			try:
				rid = message.reply_to_message
				bot.reply_to(rid, random.choice(top_response), parse_mode="Markdown")
			except:
				bot.send_message(cid, random.choice(top_response), parse_mode="Markdown")
		else:
			try:
				rid = message.reply_to_message
				bot.reply_to(rid, random.choice(top_response_degen), parse_mode="Markdown")
			except:
				bot.send_message(cid, random.choice(top_response_degen), parse_mode="Markdown")

# Shrug

@bot.message_handler(func=lambda message: "/shrug" in message.text.lower())
def shrug(message):
	cid = getCID(message)
	if intime(message):
		if not cid == degeneratesgroup:
			cid = getCID(message)
			try:
				rid = message.reply_to_message
				bot.reply_to(rid, premades['shrug'], parse_mode="Markdown")
			except:
				bot.send_message(cid, premades['shrug'], parse_mode="Markdown")

# Lenny

@bot.message_handler(func=lambda message: "/lenny" in message.text.lower())
def lenny(message):
	if intime(message):
		cid = getCID(message)
		try:
			rid = message.reply_to_message
			bot.reply_to(rid, premades['lenny'], parse_mode="Markdown")
		except:
			bot.send_message(cid, premades['lenny'], parse_mode="Markdown")

# Stare

@bot.message_handler(func=lambda message: "/stare" in message.text.lower())
def lenny(message):
	if intime(message):
		cid = getCID(message)
		try:
			rid = message.reply_to_message
			bot.reply_to(rid, premades['stare'], parse_mode="Markdown")
		except:
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
		try:
			rid = message.reply_to_message
			bot.reply_to(rid, message_send)
		except:
			bot.send_message(cid, message_send)

# Welcome user

@bot.message_handler(content_types=['new_chat_participant'])
def welcomeuser(message):
	if intime(message):	
		cid = getCID(message)
		if message.new_chat_participant.id != botid:
			bot.send_message(cid, text_messages['welcomeusergroup'].format(groupname = message.chat.title), parse_mode="Markdown")
		elif message.new_chat_participant.id == botid:
			bot.send_message(cid, u"`Greetings humans, thanks for adding me to {groupname}, I hope we have fun together!\n\n`".format(groupname=message.chat.title) + "[You can join my channel to know about my updates!](https://telegram.me/RRRUpdates)", parse_mode="Markdown")
			gid = str(message.chat.id)
			if gid not in loadjson("grouplist"):
				gName = (message.chat.title)
				addUser(gid, gName, "grouplist")

# Goodby user

@bot.message_handler(content_types=['left_chat_participant'])
def welcomeuser(message):
	if intime(message):	
		cid = getCID(message)
		bot.send_message(cid, "`Bye bye!`", parse_mode="Markdown")
		
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