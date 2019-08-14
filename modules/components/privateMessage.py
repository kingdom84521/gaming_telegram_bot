import configparser
from telegram import Updater
from telegram.ext import CommandHandler

# Self Module Import
import gameDetailsControlTools as gdctools

# Get token
config = configparser.ConfigParser()
config.read( "config.ini" )

token = config["TELEGRAM"]["ACCESS_TOKEN"]

updater = Updater( token )

def make_message( playerNumber, identity ):
    textForm = "您是編號 {} 的玩家, 您的身份是 \"{}\"".format( playerNumber, identity )

    return textForm

def send_message( bot, update ):
    game_id = update.message.text.split(" ")[ 1 ]
    game = gdctools.get_game_details( game_id )
    # playersIdList = []
    if game == None:
        update.message.reply_text( "This id of game is not in list." )
        return
    for i in range( len( game["players"] ) ):
        bot.send_message( game["players"][ i ][ "id" ], make_message( i, ? ) )
    

    