#!/usr/bin/env python
# -*- coding: utf-8 -*-

from utils import *

print "Loading " + __name__ + "..."

# Weather

@bot.message_handler(commands=['weather'])
def weather_command(message):
	if intime(message):
		city = getContent(message)
		cid = getCID(message)
		if city and city != "-?":
			try:
				city = city.replace(" ", "")
				bot.send_chat_action(cid, "find_location")
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
				final_message = u"> Weather for " + city + ", " + country + ":\n\nWeather: " + weather_info.capitalize() + u"\n\nTemperature °F:\n   " + temp + "\n   Max: " + temp_max + "\n   Min: " + temp_min + u"\nTemperature °C: \n   " + temp_cels + "\n   Max: " + temp_max_cels + "\n   Min: " + temp_min_cels + "\n\n" + "Wind Speed: " + wind_speed
				bot.send_message(cid, u"`{final_message}`".format(final_message=final_message), parse_mode="Markdown" )
			except:
				bot.reply_to(message,"`There has been an error, please try again\n\nFollow this command with your city's:\n- Name\n- Geographic Coordinates - Lat=<lat> Lon=<lon>\n- ZIP code - zip=<zip code>,<country>\n\n/weather zip=94040,us`")
		else:
			bot.reply_to(message,"`Follow this command with one of these:\n- Name\n- Geographic Coordinates - Lat=<lat> Lon=<lon>\n- ZIP code - zip=<zip code>,<country>\n\n\n\nExample:\n  /weather zip=94040,us`",parse_mode="Markdown")
