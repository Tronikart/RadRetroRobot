#!/usr/bin/env python
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests
import json
import random




with open('comics.json') as f:
		comiclist = json.load(f)

def getCH():
	lastch = comiclist['explosm']
	ch = random.randint(15, int(lastch))
	url = "http://explosm.net/comics/" + unicode(ch) + "/"
	request = requests.get(url)
	data = request.text
	soup = BeautifulSoup(data, "html.parser")
	comic = soup.find('img', id="main-comic")['src']
	comic = "http:" + comic
	return u"[​](" + comic + ") [Cyanide & Happiness](" + url + ")"

def getxkcd():
	lastxkcd = comiclist['xkcd']
	xkcd = random.randint(1, int(lastxkcd))
	url = "http://xkcd.com/" + unicode(xkcd) + "/info.0.json"
	request = requests.get(url)
	url = "http://xkcd.com/" + unicode(xkcd) + "/"
	data = request.json()
	comic = data['img']
	title = data['safe_title']
	alt_text = data['alt']
	return u"[​](" + comic + ") [" + title + "]("+ url + ")\n\n`" + alt_text + "`"

def getmrlove():
	lastmrlove = comiclist['mrlove']
	mrlove = random.randint(1, int(lastmrlove))
	url = "http://www.mrlovenstein.com/comic/" + unicode(mrlove)
	request = requests.get(url)
	data = request.text
	soup = BeautifulSoup(data, "html.parser")
	comic = soup.find('img', id="comic_main_image")
	title = comic['alt']
	if not title:
		title = "Mr Lovenstein"
	comic = "http://www.mrlovenstein.com/" + comic['src']
	return u"[​](" + comic + ") [" + title + "]("+ url + ")"

def getla():	
	la = random.randint(2014, 2016)
	url = "http://www.loadingartist.com/archives/?archive_year=" + str(la)
	request = requests.get(url)
	data = request.text
	soup = BeautifulSoup(data, "html.parser")
	comics = soup.findAll('div', class_="archive-thumbs")
	comicurl = soup.findAll('a', class_="normal")
	comicurl = random.choice(comicurl)['href']
	url = comicurl
	request = requests.get(url)
	data = request.text
	soup = BeautifulSoup(data, "html.parser")
	comic = soup.findAll('div', class_='comic')
	comic = comic[1].a.img['src']
	title = soup.find('title').string
	return u"[​](" + comic + ") [" + title + "]("+ url + ")"

def gethab():
	url = "http://theawkwardyeti.com/chapter/heart-and-brain-2/"
	request = requests.get(url)
	data = request.text
	soup = BeautifulSoup(data, "html.parser")
	comics = soup.findAll('p', class_="comic-thumbnail-in-archive")
	comic = random.choice(comics)
	title = comic.img['alt']
	url = comic.a['href']
	comic = comic.img['src']
	return u"[​](" + comic + ") [" + title + "]("+ url + ")"

def getay():
	url = "http://theawkwardyeti.com/chapter/awkward-yeti-comics/"
	request = requests.get(url)
	data = request.text
	soup = BeautifulSoup(data, "html.parser")
	comics = soup.findAll('p', class_="comic-thumbnail-in-archive")
	comic = random.choice(comics)
	title = comic.img['alt']
	url = comic.a['href']
	comic = comic.img['src']
	return u"[​](" + comic + ") [" + title + "]("+ url + ")"

def getnn():
	nnmax = comiclist['NN']	
	nn = random.randint(4, int(nnmax))
	url = "http://www.nerfnow.com/comic/" + str(nn)
	request = requests.get(url)
	data = request.text
	soup = BeautifulSoup(data, "html.parser")
	comic = soup.find('div', id="comic").img['src']
	title = soup.find('div', id="comic").img['alt']
	return u"[​](" + comic + ") [" + title + "]("+ url + ")"

def getpieco():
	url = "http://piecomic.tumblr.com"
	request = requests.get(url)
	data = request.text
	soup = BeautifulSoup(data, "html.parser")
	comics = soup.findAll('div', class_='photo post')
	comic = random.choice(comics).a.img['src']
	return u"[​](" + comic + ") [" + "piecomic" + "]("+ url + ")"

def getjoan():
	url = "http://elblogdejoancornella.blogspot.com/"
	request = requests.get(url)
	data = request.text
	soup = BeautifulSoup(data, "html.parser")
	comics = soup.find('div', class_='blog-posts hfeed')
	comics = comics.findAll('img')
	allcomics = []
	found = True
	while found:
		comic = random.choice(comics)['src']
		if comic.split('.')[-1] == "jpg":
			comic = comic.replace("s400", "s1600")
			break
		else:
			pass
	return u"[​](" + comic + ") [" + "Joan Cornella "+ "]("+ url + ")"

def getefc():
	efcmax = comiclist['EFC']
	efc = random.randint(10, int(efcmax))
	url = "http://extrafabulouscomics.com/comic/" + str(efc)
	request = requests.get(url)
	data = request.text
	soup = BeautifulSoup(data, "html.parser")
	comic = soup.find('div', id='comic').img['src']
	return u"[​](" + comic + ") [" + " Extra Fabulous Comics "+ "]("+ url + ")"

def getpdl():
	url = "http://poorlydrawnlines.com/archive/"
	request = requests.get(url)
	data = request.text
	soup = BeautifulSoup(data, "html.parser")
	comics = soup.find('div', class_="content page")
	comics = comics.findAll('li')
	comic = random.choice(comics)
	url = comic.a['href']
	request = requests.get(url)
	data = request.text
	soup = BeautifulSoup(data, "html.parser")
	comic = soup.find('div', class_='post')
	comic = comic.img['src']
	title = soup.find('title').string
	return u"[​](" + comic + ") [" + title + "]("+ url + ")"

def getoptipess():
	op = random.randint(2008, 2016)
	url = "http://www.optipess.com/archive/?archive_year=" + unicode(op)
	request = requests.get(url)
	data = request.text
	soup = BeautifulSoup(data, "html.parser")
	comics = soup.findAll('table', class_="month-table")
	comicurl = comics[0].findAll('td', class_="archive-title")
	comicurl = random.choice(comicurl).a['href']
	url = comicurl
	request = requests.get(url)
	data = request.text
	soup = BeautifulSoup(data, "html.parser")
	comic = soup.find('div', class_='comicpane').img['src']
	title = soup.find('title').string
	return u"[​](" + comic + ") [" + title +  "]("+ url + ")"



def randomcomic():
	return random.choice(comics)()

comics= [
		getCH,
		getCH,
		getxkcd,
		getxkcd,
		getmrlove,
		getmrlove,
		getla,
		getla,
		gethab,
		getay,
		getnn,
		getnn,
		getpieco,
		getjoan,
		getefc,
		getefc,
		getpdl,
		getpdl,
		getoptipess,
		getoptipess
]
