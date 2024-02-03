def take_limited_input(Tuple,Message = '', Error_Message = ''):
    Output = input(Message)
    while Output not in Tuple:
        Output = input(Error_Message)

    return Output

def player_names(P_No, Forbidden):
    Forbidden_Str = '\' or \''.join(Forbidden)
    Player_Name = tr_upper(input(f'Enter a capital letter except \'{Forbidden_Str}\' to represent player {P_No}:'))

    while Player_Name in Forbidden or Player_Name.isalpha() == False:
        Player_Name = tr_upper(input(f'The input was not a letter or it was a forbidden letter. Please enter a capital letter except \'{Forbidden_Str}\' to represent player {P_No}:'))

    return Player_Name

def tr_upper(letter):
    if letter.islower():
        if letter != 'i':
            letter = letter.upper()
        else:
            letter = 'İ'

    return letter

def print_table(Game_Mode, Dictionary):
    match Game_Mode:
        case 3:
            print(f'    A   B   C\n  -------------\n1 | {Dictionary['1A']} | {Dictionary['1B']} | {Dictionary['1C']} | 1\n  -------------\n2 | {Dictionary['2A']} | {Dictionary['2B']} | {Dictionary['2C']} | 2\n  -------------\n3 | {Dictionary['3A']} | {Dictionary['3B']} | {Dictionary['3C']} | 3\n  -------------\n    A   B   C')
        case 5:
            print(f'    A   B   C   D   E\n  ---------------------\n1 | {Dictionary['1A']} | {Dictionary['1B']} | {Dictionary['1C']} | {Dictionary['1D']} | {Dictionary['1E']} | 1\n  ---------------------\n2 | {Dictionary['2A']} | {Dictionary['2B']} | {Dictionary['2C']} | {Dictionary['2D']} | {Dictionary['2E']} | 2\n  ---------------------\n3 | {Dictionary['3A']} | {Dictionary['3B']} | {Dictionary['3C']} | {Dictionary['3D']} | {Dictionary['3E']} | 3\n  ---------------------\n4 | {Dictionary['4A']} | {Dictionary['4B']} | {Dictionary['4C']} | {Dictionary['4D']} | {Dictionary['4E']} | 4\n  ---------------------\n5 | {Dictionary['5A']} | {Dictionary['5B']} | {Dictionary['5C']} | {Dictionary['5D']} | {Dictionary['5E']} | 5\n  ---------------------\n    A   B   C   D   E')
        case 7:
            print(f'    A   B   C   D   E   F   G\n  -----------------------------\n1 | {Dictionary['1A']} | {Dictionary['1B']} | {Dictionary['1C']} | {Dictionary['1D']} | {Dictionary['1E']} | {Dictionary['1F']} | {Dictionary['1G']} | 1\n  ----------------------------\n2 | {Dictionary['2A']} | {Dictionary['2B']} | {Dictionary['2C']} | {Dictionary['2D']} | {Dictionary['2E']} | {Dictionary['2F']} | {Dictionary['2G']} | 2\n  -----------------------------\n3 | {Dictionary['3A']} | {Dictionary['3B']} | {Dictionary['3C']} | {Dictionary['3D']} | {Dictionary['3E']} | {Dictionary['3F']} | {Dictionary['3G']} | 3\n  -----------------------------\n4 | {Dictionary['4A']} | {Dictionary['4B']} | {Dictionary['4C']} | {Dictionary['4D']} | {Dictionary['4E']} | {Dictionary['4F']} | {Dictionary['4G']} | 4\n  -----------------------------\n5 | {Dictionary['5A']} | {Dictionary['5B']} | {Dictionary['5C']} | {Dictionary['5D']} | {Dictionary['5E']} | {Dictionary['5F']} | {Dictionary['5G']} | 5\n  -----------------------------\n6 | {Dictionary['6A']} | {Dictionary['6B']} | {Dictionary['6C']} | {Dictionary['6D']} | {Dictionary['6E']} | {Dictionary['6F']} | {Dictionary['6G']} | 6\n  -----------------------------\n7 | {Dictionary['7A']} | {Dictionary['7B']} | {Dictionary['7C']} | {Dictionary['7D']} | {Dictionary['7E']} | {Dictionary['7F']} | {Dictionary['7G']} | 7\n  -----------------------------\n    A   B   C   D   E   F   G')

def create_dict(Game_Mode):
    Dictionary = {}
    match Game_Mode:
            case 3:
                for i in ('A','B','C'):
                    for j in range(1,4):
                        Key = str(j)+i
                        Dictionary[Key] = ' '            
            case 5:
                for i in ('A','B','C','D','E'):
                    for j in range(1,6):
                        Key = str(j)+i
                        Dictionary[Key] = ' '
            case 7:
                for i in ('A','B','C','D','E','F','G'):
                    for j in range(1,8):
                        Key = str(j)+i
                        Dictionary[Key] = ' '

    return Dictionary

def move(Player, Pos_Of_Player, Blocked_Tiles, Tiles, column_numbers = {'A':1, 'B':2, 'C':3, 'D':4, 'E':5, 'F':6, 'G':7}, columns_dict = {0:'@', 1:'A', 2:'B', 3:'C', 4:'D', 5:'E', 6:'F', 7:'G', 8:'@', 9:'@'}):
    Row_Of_Player = int(Pos_Of_Player[0])
    Column_Of_Player = Pos_Of_Player[1]
    Column_Number_Of_Player = column_numbers[Column_Of_Player]
    Neighbour_Columns = [columns_dict[i] for i in range(Column_Number_Of_Player-1, Column_Number_Of_Player+2)]
    Neighbour_Tiles = [str(i)+j for i in range(Row_Of_Player-1,Row_Of_Player+2) for j in Neighbour_Columns]
    Neighbour_Tiles = [i for i in Neighbour_Tiles if i in Tiles]
    Moveable_Tiles = [tiles for tiles in Neighbour_Tiles if tiles not in Blocked_Tiles]

    if Moveable_Tiles != []:
        Unsuccessful_Trials = []
        Message = 'Enter the direction for \''+Player+'\' you want to go (N,S,W,E,NE,NW,SE,SW):'
        Direction = take_limited_input(('w','W','e','E','n','N','s','S','ne','NE','nE','Ne','nw','NW','nW','Nw','se','SE','sE','Se','sw','SW','sW','Sw'), Message, 'The input you entered is not in the list. Please enter a direction from the list (N,S,W,E,NE,NW,SE,SW):').upper()
        Try_To_Move = True
        while Try_To_Move == True:  
            if Direction.find('W') != -1:
                Target_Column = columns_dict[Column_Number_Of_Player-1]
            elif Direction.find('E') != -1:
                Target_Column = columns_dict[Column_Number_Of_Player+1]
            else:
                Target_Column = columns_dict[Column_Number_Of_Player]

            if Direction.find('N') != -1:
                Target_Row = Row_Of_Player - 1
            elif Direction.find('S') != -1:
                Target_Row = Row_Of_Player + 1
            else:
                Target_Row = Row_Of_Player

            Target_Tile = str(Target_Row)+Target_Column

            Try_To_Move = False
            if Target_Tile not in Moveable_Tiles:
                Unsuccessful_Trials += [Direction]
                Direction = take_limited_input(('w','W','e','E','n','N','s','S','ne','NE','nE','Ne','nw','NW','nW','Nw','se','SE','sE','Se','sw','SW','sW','Sw'),'The direction you chosed is immoveable please reenter the direction you want to go (N,S,W,E,NE,NW,SE,SW):', 'The input you entered is not in the list. Please enter a moveable direction from the list (N,S,W,E,NE,NW,SE,SW):').upper()
                if Direction in Unsuccessful_Trials:
                    Direction = take_limited_input(('w','W','e','E','n','N','s','S','ne','NE','nE','Ne','nw','NW','nW','Nw','se','SE','sE','Se','sw','SW','sW','Sw'),'You already tried this direction. It is immoveable please enter another direction to go (N,S,W,E,NE,NW,SE,SW):', 'The input you entered is not in the list. Please enter a moveable direction from the list that you didn\'t tried before (N,S,W,E,NE,NW,SE,SW):').upper()
                Try_To_Move = True
            else:
                Blocked_Tiles.remove(Pos_Of_Player)
                Pos_Of_Player = Target_Tile
                Blocked_Tiles.append(Pos_Of_Player)
        Resume = True
    else:
        Resume = False

    return Pos_Of_Player, Blocked_Tiles, Resume

def place_stone(Player, Dictionary, Tiles, Blocked_Tiles):
    Message = 'Player \''+Player+'\' please enter the tile you want to place the small stone (ex: 3A):'
    Empty_Tiles = [i for i in Tiles if i not in Blocked_Tiles]
    Empty_Tiles += [i[0]+i[1].lower() for i in Empty_Tiles]
    Placed_Stone = take_limited_input(Empty_Tiles, Message, 'This tile does not exist or filled. Please enter another tile (ex: 3A):').upper()
    Blocked_Tiles.append(Placed_Stone)
    Dictionary[Placed_Stone] = 'O'

    return Dictionary, Blocked_Tiles

def menu():
    Forbidden = ['O']
    P_1 = player_names(1,Forbidden)
    Forbidden.append(P_1)
    P_2 = player_names(2,Forbidden)

    print('MENU \n1) 3x3 \n2) 5x5 \n3) 7x7')
    Game_Mode_Tuple = ('1','2','3')
    Game_Mode = take_limited_input(Game_Mode_Tuple,'Select a game mode fromde list above (1, 2, 3):', 'The input you entered is not in the list. Please enter a number from the list (1, 2, 3):')
    
    return P_1,P_2,Game_Mode


def main():
    columns_dict = {1:'A', 2:'B', 3:'C', 4:'D', 5:'E', 6:'F', 7:'G'}
    Play = True

    while Play == True:
        P_1, P_2, Game_Mode = menu()
        Game_Mode_Dict = {'1':3, '2':5, '3':7}
        Game_Mode = Game_Mode_Dict[Game_Mode]
        Mid_Colmn = columns_dict[(Game_Mode+1)/2]
        Tiles = [str(row)+columns_dict[i] for row in range(1,Game_Mode+1) for i in range(1,Game_Mode+1)]

        Dictionary = create_dict(Game_Mode)
        Pos_Of_P1 = str(Game_Mode)+Mid_Colmn
        Pos_Of_P2 = '1'+Mid_Colmn
        Dictionary[Pos_Of_P1] = P_1
        Dictionary[Pos_Of_P2] = P_2
        print_table(Game_Mode, Dictionary)
        Blocked_Tiles = [Pos_Of_P1, Pos_Of_P2]

        Resume = True
        while Resume == True:
            Dictionary[Pos_Of_P1] = ' '
            Pos_Of_P1, Blocked_Tiles, Resume = move(P_1, Pos_Of_P1, Blocked_Tiles, Tiles)
            if Resume == False:
                Player_Won = P_2
            else:
                Dictionary[Pos_Of_P1] = P_1
                print_table(Game_Mode, Dictionary)

                Dictionary, Blocked_Tiles = place_stone(P_1, Dictionary, Tiles, Blocked_Tiles)
                print_table(Game_Mode, Dictionary)

                Dictionary[Pos_Of_P2] = ' '
                Pos_Of_P2, Blocked_Tiles, Resume = move(P_2, Pos_Of_P2, Blocked_Tiles, Tiles)
                if Resume == False:
                    Player_Won = P_1
                else:
                    Dictionary[Pos_Of_P2] = P_2
                    print_table(Game_Mode, Dictionary)

                    Dictionary, Blocked_Tiles = place_stone(P_2, Dictionary, Tiles, Blocked_Tiles)
                    print_table(Game_Mode, Dictionary)

        print(f'Player {Player_Won} has won the game!')
        Yes_No_Tuple = ('y','Y','n','N')
        Again = take_limited_input(Yes_No_Tuple,'Do you want to play again (y,Y,n,N)?', 'The input you entered is not in the list. Please enter a letter from the list (y,Y,n,N)?')
        if Again == 'n' or Again == 'N':
            print('Thank you for playing :)')
            Play = False


if __name__ == "__main__":
    main()
