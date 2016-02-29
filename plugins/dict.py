#!/usr/bin/env python
# -*- coding: utf-8 -*-

from utils import *

print "Loading " + __name__ + "..."

# Cambridge Dict

@bot.message_handler(commands=['dict'])
def dictcam(message):
	if intime(message):
		word = getContent(message)
		cid = getCID(message)
		if word and word != "-?":
			url = "http://dictionary.cambridge.org/dictionary/english/" + word.lower()
			try:
				soup = makesoup(url)
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
			bot.reply_to(message, "`Follow this command to get up to two definitions from the Cambridge Dictionary.\n\nExample:\n  /dict Rad`", parse_mode="Markdown")

