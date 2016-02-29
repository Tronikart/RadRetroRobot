#!/usr/bin/env python
# -*- coding: utf-8 -*-

from utils import *

print "Loading " + __name__ + "..."

# Todo list

@bot.message_handler(commands=['todo'])
def todolist(message):
	if intime(message):
		content = getContent(message)
		cid = getCID(message)
		uid = getUID(message)
		uName = (message.from_user.first_name)
		if content and content != "-?":
			if "-add" == content[0:4]:
				todo = content[5:len(content)]
				setTodoList(uid, todo, "add")
				bot.send_message(cid, "`" + unicode(todo) + " added successfully`", parse_mode="Markdown")
			elif "-del" == content[0:4]:
				done = content[5:len(content)]
				if delTodoList(uid, done):
					bot.send_message(cid, "`Task successfully deleted!`", parse_mode="Markdown")
	 			else:
	 				bot.send_message(cid, "`Couldn't remove the task, please make them match.`", parse_mode="Markdown")
	 		elif "-show" == content[0:5]:
	 			todo = getTodoList(uid)
	 			whole = ""
	 			for s in todo:
	 				whole += unicode(s) + "\n"
	 			if whole:
 					bot.send_message(cid, u"`> Things for " +  uName + u" to do:\n{whole}`".format(whole=whole),parse_mode="Markdown")
 				else:
 					bot.send_message(cid, u"`Your todo list is empty, you did it all!`",parse_mode="Markdown")
	 		else:
	 			bot.reply_to(message, "`Follow this command with the following:\n\n  > '-add' to add an item to the list\n  > '-show' to show your list\n  > '-del' to delete an item from your list\n\nExample:\n  /todo -add Be rad`", parse_mode="Markdown")
	 	else:
 			bot.reply_to(message, "`Follow this command with the following:\n\n  > '-add' to add an item to the list\n  > '-show' to show your list\n  > '-del' to delete an item from your list\n\nExample:\n  /todo -add Be rad`", parse_mode="Markdown")
