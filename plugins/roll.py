from utils import *

print ('loading ' + __name__)

def roll(dice):
	endResult = {}
	result = 0
	#################
	# It is a string
	#################
	if type(dice) == str:
		numberDice = int(dice.split('d')[0])
		modifier = 0 if len(dice.split('+')) < 2 else int(dice.split('+')[1])
		##############
		# Its xDy form
		###############
		if len(dice.split('d')) == 2:
			dieNumber = int(dice.split('d')[1]) if modifier == 0 else int(dice.split('+')[0].split('d')[1])
			###################
			# Only one die roll
			###################
			if numberDice == 1:
				endResult['multipleResult'] = False
				result = random.randrange(numberDice, dieNumber + 1)
				endResult['dice'] = str(result)
			###################
			# Several Die Roll
			###################
			else:
				endResult['multipleResult'] = True
				endResult['dice'] = ""
				# Avoiding negative numbers
				# i = numberDice if numberDice > 0 else -numberDice
				# i += 1
				i = 0
				result = 0
				# Going through all the dice rolls, at the end, delete the extra ' + ' and break
				while(True):
					if i < numberDice:
						aux = random.randrange(1, dieNumber + 1)
						result += aux
						if i == numberDice:
							pass
						else:
							endResult['dice'] += str(aux) + " + "
						i += 1
					else:
						endResult['dice'] = endResult['dice'][:len(endResult['dice'])-3]
						break
		##################
		# Its xDyDyDy form
		##################
		else:
			endResult['multipleResult'] = True
			dieNumber = int(dice.split('d')[1]) if modifier == 0 else int(dice.split('+')[0].split('d')[1])
			###################
			# Only one die roll
			###################
			if numberDice == 1:
				#endResult['multipleResult'] = True
				auxResult = random.randrange(numberDice, dieNumber + 1)
				#endResult['dice'] = str(auxResult)
			###################
			# Several Die Roll
			###################
			else:
				endResult['multipleResult'] = True
				endResult['dice'] = ""
				#i = numberDice if numberDice > 0 else -numberDice
				#i += 1
				i = 0
				auxResult = 0
				while(True):
					if i < numberDice:
						i += 1
						aux = random.randrange(1, dieNumber + 1)
						auxResult += aux
					else:
						break
			# Recursively handling more than one dice roll
			recur = roll(str(auxResult) + dice[3:].split('+')[0])
			endResult['dice'] = ""
			if recur['error'] == False:
				result += recur['total']
				endResult['dice'] += recur['dice']
			else:
				endResult['error'] = True
		# Useful flags for printing info
		# Crit, fail, the dice that were added, if there was any error
		endResult['crit'] = True if result == dieNumber else False
		endResult['fail'] = True if result == 1 else False
		endResult['total'] = result + modifier
		endResult['dice'] = endResult['dice'] + " + (" + str(modifier) + ")" if modifier > 0 else endResult['dice']
		endResult['error'] = False
	elif type(dice) == int:
		modifier = 0
		endResult['total'] = random.randrange(1, dice+1)
		endResult['error'] = False
		endResult['multipleResult'] = False
	else:
		endResult['error'] = True
	if endResult['error']:
		pass
	else:
		endResult['multipleResult'] = True if modifier > 0 else endResult['multipleResult']
	return endResult

def action(bot, update, args):
	cid = getCID(update)
	number = ' '.join(args)
	if number:
		if number != '-?' and not len(number.split('d')) == 1:
			rolledDice = roll(str(number))
			if rolledDice['error']:
				update.message.reply_text("`Send this command alone to roll a d20, send it along with dice to roll them`", parse_mode="Markdown", reply_to_message_id=update.message.message_id)
			else:
				Message = ""
				if rolledDice['multipleResult']:
					Message += "Rolling " + number + ":\n" + rolledDice['dice'] + "\n" + str(rolledDice['total'])
				else:
					Message += "Rolling " + number + ":\n" + str(rolledDice['total'])
				if rolledDice['crit'] and not rolledDice['fail']:
					Message += "\nCRIT!!"
				elif rolledDice['fail'] and not rolledDice['crit']:
					Message += "\nCritical Failure!"
				elif rolledDice['fail'] and rolledDice['crit']:
					Message += "\nYou rolled a d1, what did you expect?"
				update.message.reply_text("`" + Message + "`", parse_mode="Markdown", reply_to_message_id=update.message.message_id)
		elif len(number.split('d')) == 1:
			update.message.reply_text("`Rolling 1d" + number + ":\n" + str(random.randrange(int(number))+1) + "`", parse_mode="Markdown", reply_to_message_id=update.message.message_id)
		else:
			pass
	else:
		update.message.reply_text("`Rolling 1d20:\n" + str(random.randrange(21)) + "`", parse_mode="Markdown", reply_to_message_id=update.message.message_id)


info = {	'triggers'	: 	'roll',
			'name'		:	'Roll',
			'help'		: 	"Send this command alone to roll a d20, send it along with dice to roll them.",
			'example'	:	'/roll 1d8',
			'active'	: 	True,
			'admin'		: 	False,
			'arguments' :	"[<number of dice>d<number of faces>]"}