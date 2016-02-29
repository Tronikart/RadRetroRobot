#!/usr/bin/env python
# -*- coding: utf-8 -*-

from utils import *

print "Loading " + __name__ + "..."

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
