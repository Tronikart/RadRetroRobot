#!/usr/bin/env python
# -*- coding: utf-8 -*-

from utils import *

print "Loading " + __name__ + "..."

# Timezone

@bot.message_handler(commands=['time'])
def timezone(message):
	if intime(message):
		cid = getCID(message)
		city = getContent(message)
		if city and city != "-?":
			now = time.mktime(datetime.now().timetuple())
			coord_url = "https://maps.googleapis.com/maps/api/geocode/json?address=" + city + "&key=" + google_time_key
			bot.send_chat_action(cid, "find_location")
			coord_request = requests.get(coord_url)
			coord = coord_request.json()
			if coord_request.status_code == 200:
				if coord['status'] != "ZERO_RESULTS":
					try:
						coord = coord['results'][0]
						city_name = coord['address_components'][0]['long_name']
						try:
							country_name = coord['address_components'][3]['short_name']
						except:
							country_name = city_name
							city_name = ""
						lat = coord['geometry']['location']['lat']
						lon = coord['geometry']['location']['lng']
						time_url = "https://maps.googleapis.com/maps/api/timezone/json?location=" + str(lat) + "," + str(lon) + "&timestamp=" + str(now) + "&key=" + google_time_key
						time_request = requests.get(time_url)
						time_json = time_request.json()
						dstOffset = time_json['dstOffset']
						rawOffset = time_json['rawOffset']
						timezone = time_json['timeZoneId']
						timezoneName = time_json['timeZoneName']
						# This is your local timezone
						time_offset = 16200
						time_total = now + dstOffset + rawOffset + time_offset
						time_total = unix2date(time_total)
						time_total = time_total.split(',')
						hours = from24to12(time_total[0])
						day = time_total[1]
						month = time_total[2]
						if city_name:
							final_message = "`" + city_name + ", " + country_name + "\n\n" + hours + "\n" + day + ", " + month + "\n\nTimezone: " + timezone + ", " + timezoneName + "`"
						else:
							final_message = "`" + country_name + "\n\n" + hours + "\n" + day + ", " + month + "\n\nTimezone: " + timezone + ", " + timezoneName + "`"
						bot.send_message(cid, final_message, parse_mode="Markdown")
					except:
						bot.reply_to(message, "`Sorry something went wrong, try later or with another city`", parse_mode="Markdown")
				else:
					bot.reply_to(message, "`I couldnt find anything, please try again.`", parse_mode="Markdown")
			else:
				bot.reply_to(message, "`There has been an error, the number {error} to be specific.`".format(error=request.status_code), parse_mode="Markdown")
		else:
			bot.reply_to(message, "`Follow this command with a city name and I will show you its timezone information\n\nExample:\n   /time Caracas`", parse_mode="Markdown")
