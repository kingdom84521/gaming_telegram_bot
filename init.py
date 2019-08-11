from telegram.ext import CallbackQueryHandler,Updater,CommandHandler,MessageHandler,Filters
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
import logging
import random,os,pprint
import gameDetailsControlTools as gdctools
import json


logging.basicConfig(level=logging.DEBUG,
                   format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

packageForm = { 
                "id": None,
                "identity": {
                                "civilian": None,
                                "spy": None,
                                "whiteboard": None
                            },
                "players": []
              }

def init_(bot,update):
    keyboard = [[InlineKeyboardButton(" 3", callback_data='person3'),
                 InlineKeyboardButton(" 4", callback_data='person4'),
                 InlineKeyboardButton(" 5", callback_data='person5'),
                 InlineKeyboardButton(" 6", callback_data='person6')],
                 [InlineKeyboardButton(" 7", callback_data='person7'),
                 InlineKeyboardButton(" 8", callback_data='person8'),
                 InlineKeyboardButton(" 9", callback_data='person9'),
                 InlineKeyboardButton("10", callback_data='person10')]]
    #print(update)
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Please choose how many user:',reply_markup=reply_markup)

keyboard4 = [[InlineKeyboardButton("Join",callback_data='join')]]
    

keyboard2 = [[InlineKeyboardButton(" 0", callback_data='spy0'),
              InlineKeyboardButton(" 1", callback_data='spy1'),
              InlineKeyboardButton(" 2", callback_data='spy2')]]

keyboard3 = [[InlineKeyboardButton(" 0", callback_data='board0'),
              InlineKeyboardButton(" 1", callback_data='board1'),
              InlineKeyboardButton(" 2", callback_data='board2')]]

number=0
spy=0
whiteboard=0
ordinary=0

def button(bot,update):
    query = update.callback_query
    #print(update)
    if query.data[0:6] == "person" :
        global number
        number=int(query.data[6:])
        query.edit_message_reply_markup()
        reply_markup = InlineKeyboardMarkup(keyboard2)
        bot.sendMessage(update.callback_query.message["chat"]["id"],'Please choose how many spy:',reply_markup=reply_markup)
    elif query.data[0:3] == "spy" :
        global spy
        spy=int(query.data[3])
        query.edit_message_reply_markup()
        reply_markup = InlineKeyboardMarkup(keyboard3)
        bot.sendMessage(update.callback_query.message["chat"]["id"],'Please choose how many whiteboard:',reply_markup=reply_markup)
    elif query.data[0:3] == "boa" :
        global whiteboard
        whiteboard=int(query.data[5])
        global ordinary
        ordinary=number-spy-whiteboard
        query.edit_message_reply_markup()
        reply_markup = InlineKeyboardMarkup(keyboard4)
        bot.sendMessage(update.callback_query.message["chat"]["id"],'Please choose join to join the game',reply_markup=reply_markup)
    elif query.data[0:4] == "join":
        players.append({"id":update.callback_query.message.chat.id,"name":update.callback_query.message.chat.username})
        print( len( players ), end=" " )
        print( number )
        if len(players) == number:
            query.edit_message_reply_markup()
            with open( "runningGames.json", "r" ) as file_io:
                data = json.loads( file_io.read() )
                lastId = None
                if "id" not in data[ -1 ].keys():
                    lastId = -1
                else:
                    lastId = data[ -1 ][ "id" ]
                global packageForm
                packageForm["id"] = lastId + 1
                packageForm["identity"]["civilian"] = ordinary
                packageForm["identity"]["spy"] = spy
                packageForm["identity"]["whiteboard"] = whiteboard
                packageForm["players"] = players
                print( packageForm )
                gdctools.update_game_details( packageForm )
                file_io.close()

    

def help(bot,update):
    update.message.reply_text("Use /init to start initializing a new game.")
    

def init(bot,update):
    update.message.reply_text('please enter how many user')



players=list()


updater = Updater('847398333:AAEz5T0w6qDlFPxRZvRZ8Di6FtT2M8knxVY')

updater.dispatcher.add_handler(CommandHandler("init",init_))
updater.dispatcher.add_handler(CallbackQueryHandler(button))

# print( len( players ), end=" " )
# print( number )


updater.start_polling()

updater.idle()
