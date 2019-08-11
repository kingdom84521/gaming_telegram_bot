import random, os, configparser, logging, threadin

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
logging.basicConfig(format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s',level = logging.INFO)

#Get token
config = configparser.ConfigParser()
config.read( "config.ini" )
token = config["TELEGRAM"]["ACCESS_TOKEN"]
    
###遊戲結束###
def winer(x):
    if x == 'spy':
        updater.message.reply_text('間諜獲勝！')
    if x == 'c'
        updater.message.reply_text('平民獲勝！')
    if x == 'cw':
        updater.message.reply_text('平民與白板獲勝！')

###檢查有沒有說過話###
def check_id(bot,update):
    t = 1
    for i in range(len(players_role)):
        if players_role[i]['id'] == update.message.from_user.id:
            speack[i] = 1
            break

    for i in range(len(speak)):
        if speack[i] == 0:
            t = 0
            break
    if t == 1:
        updater.message.reply_text('TIME UP!回合結束！/n'.format(run))
        vote(bot,update)
        speack = [0 for i in range(len(players_role))]
        run += 1
    civilian = 0
    spy = 0
    whiteboard = 0                                                  
    for i in range(len(players_role)):
        if players_role[i]['role'] == '平民':
            civilian += 1
        if players_role[i]['role'] == '間諜':
            spy += 1
        if players_role[i]['role'] == '白板':
            whiteboard += 1
    if civilian == 0 and whiteboard == 0:
        def winer('spy') 
    if spy == 0 and civilian == 0:
        def winer('c')
    if spy == 0:
        def winer('cw')

###分配角色###
def change_rote(gameDetails,players_id):
    -
    #角色數目生成
    for i in range(gameDetails['identity']['civilian']):
        role.append('平民')
    for i in range(gameDetails['identity']['spy']):
        role.append('間諜')
    for i in range(gameDetails['identity']['whiteboard']):
        role.append('白板')
    
    #作出角色and順序分配
    role,players_role=[ ] , [ ]
    role = random.shuffle(role)#身分打亂
    for i in range(len(players_id)):#分配身分
        players_role.append({"id":players_id[i],'role':role[i]})

    #呼叫 私訊()###############
    send_private_message(players_role)''''''
    
    return players_role


########遊戲開始########
gameDetails = gameDetails()#遊戲定義
players_id = []#取id
run = 0#回合數
if i in range(len(gameDetails][players])):
    players_id.append(list(gameDetails[players][i].keys())[0])#list(a[0].keys())[0]

players_name = []#取name
if i in range(len(gameDetails][players])):
    players_name.append(list(gameDetails[players][i].keys())[1])

for i in range(len(players_id)):
    alive.append(i)

players_role = change_role(gameDetails,players_id)#角色設定



updater = Updater(token)#reading bot data
updater.message.reply_text('現在是第 {} 回合 ！/n大家請開始序述自己的角色'.format(run))
check_temp = [0 for i in range(len(players_role))]#是否說過話

updater.dispatcher.add_handler(MessageHandler((Filters.text, check_id)'''設爲已說話'''
                           
updater.start_polling()
updater.idel()

