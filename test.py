import configparser
from telegram.ext import CommandHandler, Updater

def test( bot, update ):
    update.message.reply_text( "bot: {}\n\n".format( bot ) )
    update.message.reply_text( "update: {}".format( update ) )

config = configparser.ConfigParser()
config.read("config.ini")
updater = Updater( config["TELEGRAM"]["ACCESS_TOKEN"] )

updater.dispatcher.add_handler( CommandHandler( "test", test ) )
updater.start_polling()
updater.idle()
