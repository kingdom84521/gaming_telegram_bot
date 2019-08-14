from telegram import InlineKeyboardButton, InlineKeyboardMarkup

def generate_keyboard_pack( dataList: list ):
    '''
    Parameter "dataList" should be a list formatted like below:
    [
        [ 
            { "text": text_for_button_1_in_row_1, "callback_data": callback_data_for_button_1_in_row_1 },
            { "text": text_for_button_2_in_row_1, "callback_data": callback_data_for_button_2_in_row_1 },
            { "text": text_for_button_3_in_row_1, "callback_data": callback_data_for_button_3_in_row_1 },
            ...
        ],
        [
            { "text": text_for_button_1_in_row_2, "callback_data": callback_data_for_button_1_in_row_2 },
            { "text": text_for_button_2_in_row_2, "callback_data": callback_data_for_button_2_in_row_2 },
            { "text": text_for_button_3_in_row_2, "callback_data": callback_data_for_button_3_in_row_2 },
        ],
        ...
    ]
    mention: numbers of buttons in every row can be different

    This function will return a dictionary formatted like below:
    { keyboard: keyboard_value, reply_markup: reply_markup_value }
    '''
    returnPackage = { "keyboard": None, "reply_markup": None }
    reply_markup = None
    keyboard = []
    for i in range( len( dataList ) ):
        temp = []
        for j in range( len( dataList[ i ] ) ):
                temp.append( InlineKeyboardButton( dataList[ i ][ j ][ "text" ], dataList[ i ][ j ][ "callback_data" ] ) )
        keyboard.append( temp )
    
    reply_markup = InlineKeyboardMarkup( keyboard )
    
    returnPackage[ "keyboard" ] = keyboard
    returnPackage[ "reply_markup" ] = reply_markup

    return returnPackage

    
                


    