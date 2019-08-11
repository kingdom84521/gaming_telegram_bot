from collections import Counter
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
from telegram import InlineKeyboardMarkup, InlineKeyboardButton
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')




def vote_func(bot,update):  
    global x
    keyboard=list()
    for i in range(2):                          
        keyboard.append(list())
        for j in range(1,6):
                if not (j+i*5) in alive:
                        continue
                else:
                        keyboard[i].append(InlineKeyboardButton('{}號'.format(j+i*5),callback_data='{}'.format(j+i*5)))
    
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('請選擇要投票的對象:',reply_markup=reply_markup)

def Poll_option(bot, update):
    Num = update.callback_query
    player_list.append(int(Num.data))
    print(player_list,number)
    if len(player_list) == number:
        word_count = Counter(player_list)
        count = word_count.most_common(1)       #回傳[(元素,幾次)]
        x = count[0][0]
        kill_func(x,bot,update)

        
def kill_func(x,bot,update):
    print(x)
    alive.remove(x)
    reply_message = '{}號被殺死了QQ '.format(x)
    bot.sendMessage(update.callback_query.message.chat.id,reply_message)
    global player_list
    player_list=list()

def Game_countine(bot, update):
    pass

alive = [1,2,3,4,5,6,7,8,9,10]
player_list= []
keyboard = list()
number=5
updater = Updater('827032992:AAHMDGLAIyVc5VAKjcxmg0vMKws1mZha2Ww')

updater.dispatcher.add_handler(CommandHandler('vote', vote_func))
updater.dispatcher.add_handler(CallbackQueryHandler(Poll_option))

updater.start_polling()
updater.idle()