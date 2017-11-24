from utils import *

print ('loading ' + __name__)

def action(bot, update, args):
	try:
		soup = makesoup("http://whenisthenextsteamsale.com/")
		info = soup.find('input', id="hdnNextSale")['value']
		json_acceptable_string = info.replace("'", "\"")
		info = json.loads(json_acceptable_string)
		date = info['StartDate']
		try:
			dateone = datetime.strptime(date, "%d-%m-%Y").strftime('%A ')
		except ValueError:
			dateone = datetime.strptime(date, "%Y-%m-%dT%H:%M:%S").strftime('%A ')
		try:
			datetwo = datetime.strptime(date, "%d-%m-%Y").strftime('%d')
		except ValueError:
			datetwo = datetime.strptime(date, "%Y-%m-%dT%H:%M:%S").strftime('%d')
		if datetwo == "1":
			datetwo += "st"
		elif datetwo == "2":
			datetwo += "nd"
		elif datetwo == "3":
			datetwo += "rd"
		else:
			datetwo += "th"
		try:
			datethree = datetime.strptime(date, "%d-%m-%Y").strftime(', %B %Y')
		except ValueError:
			datethree = datetime.strptime(date, "%Y-%m-%dT%H:%M:%S").strftime(', %B %Y')

		datelong = dateone + datetwo + datethree
		try:
			dateunix = time.mktime(datetime.strptime(date, "%d-%m-%Y").timetuple())
		except ValueError:
			dateunix = time.mktime(datetime.strptime(date, "%Y-%m-%dT%H:%M:%S").timetuple())

		now = time.time()
		remaining = dateunix - now
		if remaining > 604800:
			howlong = remaining/60/60/24/7
			howlongdays = remaining/60/60/24
			howlong = str(int(howlong)) + " week(s) (" + str(int(howlongdays)) + " days)"
		elif remaining > 86400:
			howlong = remaining/60/60/24
			howlong = str(int(howlong)) + " day(s)"
		elif (remaining/60/60)-4 > 0:
			howlong = remaining/60/60
			howlongminut = (remaining-int(howlong)*60*60)/60
			howlong = str(int(howlong)-4) + " hour(s) " + str(int(howlongminut)) + " minute(s)"
		else:
			howlong = "Right now!"
		confirmed = u"Confirmed: \u2705" if info['IsConfirmed'] else u"Confirmed: \u274C"
		name = info['Name']
		final = u"`When is the next Steam Sale:\n\nWhich one? " + name + "\nWhen? " + datelong + "\n" + confirmed + "\nHow long until then? " + howlong + "\n\n`[more info](http://whenisthenextsteamsale.com/)"
		update.message.reply_text(final, parse_mode="Markdown", disable_web_page_preview=True, reply_to_message_id=update.message.message_id)
	except:
		update.message.reply_text("`Theres has been an error, please try again later.`", parse_mode="Markdown", reply_to_message_id=update.message.message_id)

info = {	'triggers'	:	('steamsales', 'ss', 'whenisthenextsteamsale'),
			'name'		:	'Steam Sales',
			'help'		: 	"Will give you information about the next possible Steam Sale",
			'example'	:	'',
			'active'	: 	True,
			'admin'		: 	False,
			'arguments' :	""}