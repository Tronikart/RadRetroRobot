#!/usr/bin/env python
# -*- coding: utf-8 -*-

from utils import *
import importdir

importdir.do('plugins', globals())

try:
	bot.send_message(adminid, "*Bot loaded and ready for action!*", parse_mode="Markdown")
except:
	pass


def poll(option):
	if option == "debug":
		print "Bot: debug mode"
		bot.polling(True)
	else:
		try:
			print "Bot: running"
			bot.polling(none_stop=False, interval=0)
		except KeyboardInterrupt:
			pass
		except:
			try:
				print "\nUnexpected error:", sys.exc_info()[0]
				print "\n\t"+unicode(sys.exc_info()[1]) + "\n"
				bot.send_message(adminid, "\n*Unexpected error:*\n" + "_" + unicode(sys.exc_info()[0]) + "\n    "+unicode(sys.exc_info()[1]) + "_\n", parse_mode="Markdown")
			except:
				bot.send_message(adminid, "\n*Unexpected error:*\n" + "_" + unicode(sys.exc_info()[0]) + "\n    "+unicode(sys.exc_info()[1]) + "_\n")
			os.system("python RRR.py")
		


poll("go")