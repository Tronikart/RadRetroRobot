# RadRetroRobot

Multifunctional Telegram Bot RadRetroRobot.

Running publicly as [@RadRetroRobot](http://telegram.me/radretrorobot).

licensed under the GNU General Public License. 
 
## How to setup
Clone this repository.

Setup your Telegram bot key and all the respective keys on config.json.

Install [python-telegram-bot](https://python-telegram-bot.org) API Wrapper and the required dependencies.

Run RRR.py using Python 3.X.

## Required dependencies

`python -m pip install tweepy`

`python -m pip install BeautifulSoup`

`python -m pip install wikipedia`

## Config.json

Which of these keys are needed for what plugins.

| Key | Plugins they rely on | Where to get your key | 
| :-- | :------------------- | :-------------------: |
|**bot**|The whole functionality of the bot | [Bot Father](t.me/BotFather)|
|**weather**| `weather` plugin.|[OpenWeatherMap](https://openweathermap.org/price)|
|**reddit**| Reddit `r` plugin and `autoReddit`. | Not as much of a key, its just your [reddit](www.reddit.com) username|
|**lastfm**|Every lastfm command, such as `np`, `fmalbums` and `fmtop`, `fmgrid` will work without this. | [last.fm](https://www.last.fm/api) |
|**bing**|This is used in the `steamid` command to improve the speed of the search.| [Bing Web Search API](https://azure.microsoft.com/en-us/services/cognitive-services/bing-web-search-api/) |
|**steam**| Almost every Steam command, even `steamid` will use this in case the bing search doesnt return any results, `steamdetails` and `steamnews`, `steamsales`, `autoSteam` and `steampage` will work without this. | [Steam Web API](https://steamcommunity.com/dev/apikey)| 
|**tweepy**|This will be needed for any Twitter related plugin, such as `tw` and `autoTweet`.|[Twitter API](https://apps.twitter.com/)|

If you dont want to include one of these, you should also change the plugin's active state to `False` in order to avoid future issues.

## Plugins

Running /help will return a basic list of the currently active plugins.

Following /help with a plugin will give a more detailed overview of said plugin, this can be done with severals at a time by separating them with space.

### This bot will also auto detect:

 **Youtube links** - post the name of the channel with a link, duration of the video, the amount of views and subscribers.

 **Subreddit post links** - post its text content in case its a text post, otherwise it will try to send the picture or link as a gif, sending the link as a last resort.
 
 **Tweet links** - post its basic information with the full text of the tweet, if the tweet has a quoted tweet, will post the quoted tweet.
 
 **Steam Store links** - post its basic information as if the user used /steampage.
 
 **Gfycat links** - return the .mp4 as a document (this means as a gif) if the file is not too large for telegram, otherwise it will try to send a smaller version.
 
 **Imgur gif and gifv links** - return the .mp4 version as a document (this means as a gif).
 
 **Good night messages** - with special messages for admin.
 
 **Fuck you messages**
 
 **Beep, Boop**
 
 **When mentioned** - either Rad Retro Robot or RRR.
 
 **Hi**
 
 **Love** - with special messages for admin.
 
 **Bop** - Only from admin.
 
## Making a new plugin

The structure of a plugin is really simple, you need to setup a few things in order to make it work.

### Import utils

First you have to from utils.py, so you get every function and module loaded up.

`from utils import *`

### Print out the loading process

This step is optional, every plugin does this and its a nice way to keep everything organized.

`print ('loading ' + __name__)`

### Define the main action of the plugin

This is the function thats going to be called when the command is called, you need to define this function as action, otherwise it wont work, you will include args even if you dont plan to pass anything through.

```
def action(bot, update, args):
    ...
```
Inside this function you can do whatever you want, `update` will have your `message` object and `args` will be a list with everything after the command, so if you need some options after the command or the content of the message, this is a nice and easy way to get those.

### Write the info dictionary

This step is really important, as it will determine how the `help` plugin handles commands and how the command will be triggered.

The structure is pretty straight forward.

| Key        | Value           | Data Type |  
| ------------- |:-------------|:--:|
| **triggers**      | This is what your command will need to be activated, you can either set this as a single string or a tuple with all the possible ways to trigger this command. |`String` or `Tuple` |
| **name**          | This is the name that will show up in the help information.      | `String` |
| **example**       | If your command could use an example to clarify some things, add the example's text in here, no need to write anything else other than the text itself.      | `String` |
| **active**        | This will be used right at launch to load the plugins.      | `Boolean` | 
| **admin**			 | If you have exclusive commands, this will keep them out of user's help list but will still show for you.      | `Boolean` |
| **arguments**     | Include here, if any, the arguments required to use the command, this will be displayed on the help information, the rule they follow is `<>` for required arguments, `[]` for optional arguments. | `String` |

And with this, your plugin up and running!

## Disclaimer

This program is provided "as is" without warranty of any kind.



