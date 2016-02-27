# RadRetroRobot

Multifunctional Telegram Bot RadRetroRobot

Running publicly as [@RadRetroRobot](http://telegram.me/radretrorobot)

licensed under the GNU General Public License. 
 
## How to setup
Download this repository

Setup your Telegram api key and all the respective keys on RRR.py

Install [eternoir](https://github.com/eternnoir/pyTelegramBotAPI/) Telegram bot api

Run RRR.py using python 2.7

## Required dependencies

tweepy

sortedcontainers 

BeautifulSoup

## Plugins

|Plugin | Brief explanation|
:-------------| -------------
|/help|Displays the basic help menu|
|/ping|Returns back a message with basic user info|
|/premades|Returns a list of commands of premades messages|
|/echo \<text\>|Returns the text|
|/ud \<query\>|Returns the first definition from Urban Dictionary|
|/calc \<query\>|Returns the result of the math expresion|
|/g \<query\>|Returns 5 results from google of said query|
|/gnsfw \<query\>|Same as /g but with SafeSearch off|
|/i \<query\>|Returns a random image from the search|
|/insfw \<query\>|Same as /i but with SafeSearch off|
|/lastfm|Returns a list of lastfm commmands|
|/fmuser \<user\>|Sets a new lastfm user|
|/np|Returns what you're listening to if you have a lastfm user set|
|/fmtop|Returns a top 5 from last weeks artist if you have a lastfm user set|
|/fmalbums|Returns a top 5 from last weeks albums if you have a lastfm user set|
|/fmgrid \<type\> \<size\>|Returns a grid with album covers, by default will return last week 3x3|
|/ml \<query\>|Returns results from www.mercadolibre.com.ve|
|/r \<sub\>|Returns the top 6 links from a subreddit|
|/fact|Returns a random fact|
|/roll [max\|range]|Returns by default a random number up to 100 if no range or max is given|
|/flip|Flips a (virtual) coin|
|/len \<query\>|Returns the lenght of the text|
|/quiet \<option\>|Adds or removes the group to the quiet list, turning off RRR's random beeps and bops|
|/steam|Returns a list of steam commands|
|/steamid \<game\>|Returns the steam id of a game|
|/steampage \<id\>|Returns basic information of a game|
|/steamdetails \<id\>|Returns details such as Single-player, Steam Trading Cards, etc|
|/steamnews \<id\>|Returns the last entry on the games blog|
|/dota|Returns a list of dota 2 commands|
|/dotanews|Returns the last entry on the Dota 2 blog|
|/dlive [option]|Returns a list of 10 games from live tournaments by default|
|/dleague \<leagueID\>|Returns information from a specific league|
|/dldetails \<matchID\>|Returns live info from a tournament match|
|/dlmap \<option\> \<matchID\>|Returns live info from the map of a live tournament match|
|/dmatch \<matchID\>|Returns the info from a finished match|
|/dstreams|Returns a list of Dota 2 live streams|
|/cat|Returns a random cat pic or gif|
|/wiki \<query\>|Returns information from wikipedia (WIP, might show some bugs)|
|/isdown \<url\>|Returns the status from a page, if up will also return ping|
|/bin \<option\> \<text\>|Translates from or to binary|
|/lyrics \<artist\> - \<song\>|Returns the lyrics for a given song|
|/diceroll [faces]|By default will roll a 6d|
|/top|kek|
|/todo \<-add\|-del\|-show\> \<text\>|Adds, deletes or shows content from the todo list|
|/comics [page]|Returns a random comic from the list|
|/weather \<city\>|Returns the information of the weather from that city|
|/time \<city\>|Returns the time from that city|
|/updatecomics|[ADMIN TOOL] Updates the comic list to the lastests|
|/tw \<tweet\>|[ADMIN TOOL] Will tweet from the account associated to tweepy|
|/message \<chatid\> \<text\>|[ADMIN TOOL] Sends a message to the chat|
|/broadcast \<message\>|[ADMIN TOOL] Broadcasts a message to all the registered groups that are not in the quiet list|

    You can follow any command with -? to get info and examples

#This bot will also auto detect:

 **Subreddit post links** - post its text content in case its a text post or its basic information if its not a text post
 
 **Tweet links** - post its basic information, if the tweet has a quoted tweet, will post the quoted tweet
 
 **Steam Store links** - post its basic information as if the user used /steampage
 
 **Gfycat links** - return the .gif if the gif can show the preview on Telegram
 
 **Good night messages** - with special messages for admin
 
 **Fuck you messages**
 
 **Beep, Boop**
 
 **When mentioned** - either Rad Retro Robot or RRR
 
 **Hi**
 
 **Love** - with special messages for admin
 
 **Shutup.** or **shut up.** - Only from admin
 
 **Bop** - Only from admin
 

## Disclaimer

This program is provided "as is" without warranty of any kind


