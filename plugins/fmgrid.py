#!/usr/bin/env python
# -*- coding: utf-8 -*-

from utils import *

print "Loading " + __name__ + "..."

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
			try:
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
					print url
					soup = makesoup(url)
					if "Error" in soup.text:
						bot.reply_to(message, "`There has been an error, heres some info:`\n\n" + "`" + soup.text + "`", parse_mode="Markdown")
					else:
						bot.reply_to(message, url)
			except:
				bot.reply_to(message, "`Something went wrong, sorry try again later.`", parse_mode="Markdown")
		else:
			bot.reply_to(message, "`This command will return a grid with your last listened albums here are the options you can set\n\n /fmgrid <type> <size>\n\nTypes: 7 day, 1 month, 3 months, 6 months, 12 months, Overall.\nSize: 3x3, 4x4, 5x5\n\nBy default this command will give you a 3x3 grid from last week`", parse_mode="Markdown")
