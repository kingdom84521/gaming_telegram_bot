import json

def get_game_details( id ):
    data = None
    with open( "runningGames.json", "r" ) as game_details:
        data = json.load( game_details )
        game_details.close()
    for i in range( len( data ) ):
        if ( data[ i ]["id"] == id ):
            return data[ i ]
    return None
def update_game_details( new_data: dict ):
    old_file = open( "runningGames.json", "r" )
    old_data = json.loads( old_file.read() )
    old_file.close()

    with open( "runningGames.json", "w" ) as old_game_details:
        old_data.append( new_data )
        for i in range( 0, len( old_data ) - 1 ):
            for j in range( 0, len( old_data ) - 1 - i ):
                if old_data[ j ]["id"] > old_data[ j + 1 ]["id"]:
                    old_data[ j ], old_data[ j + 1 ] = old_data[ j + 1 ], old_data[ j ]
            
        new_game_details = json.dumps( old_data )
        old_game_details.write( new_game_details )
        old_game_details.close()
    
    return True

