#This is the outline for the full game
from generate_board_visual import generate_board_visual
from generate_menu import generate_menu
from play_again_logic import play_again_logic
from game_logic import game_logic_check
def main():

    
    #Pre-set variable so the menu loop will begin
    selection_1 = 0
    while selection_1 != 3:
        #Pre-set tile variables
        tile_1 = 1
        tile_2 = 2
        tile_3 = 3
        tile_4 = 4
        tile_5 = 5
        tile_6 = 6
        tile_7 = 7
        tile_8 = 8
        tile_9 = 9
        #Pre-set variable to end the game when winner is declared or there is a tie
        end = False
        #Pre-set list to hold the board information
        board = [tile_1,tile_2,tile_3,tile_4,tile_5,tile_6,tile_7,tile_8,tile_9]
        #Pre-set variable so player 1 always starts first
        player_num = 1
        

        if selection_1 != 3:
            generate_menu()
            selection_1 = int(input(f'Enter your selection: '))
            if selection_1 == 1:
                #This is a while loop to perpetuate the game until a winner is declared
                while end == False:
                    if end == False:
                        if player_num == 1:
                            generate_board_visual(tile_1,tile_2,tile_3,tile_4,tile_5,tile_6,tile_7,tile_8,tile_9)
                            tile_logic = False
                            while tile_logic == False:
                                tile_choice = int(input(f'Enter the number of the tile you want to select: '))
                                if tile_choice == 1:
                                    if tile_1 == 'X' or tile_1 == 'O':
                                        print(f'That tile has already been chosen, please select another!')
                                        tile_logic = False
                                    else:
                                        board[0] = 'X'
                                        tile_1 = 'X'
                                        tile_logic = True
                                        end = game_logic_check(board)
                                        player_num = 2
                                        
                                elif tile_choice == 2:
                                    if tile_2 == 'X' or tile_2 == 'O':
                                        print(f'That tile has already been chosen, please select another!')
                                        tile_logic = False
                                    else:
                                        board[1] = 'X'
                                        tile_2 = 'X'
                                        tile_logic = True
                                        end = game_logic_check(board)
                                        player_num = 2
                                elif tile_choice == 3:
                                    if tile_3 == 'X' or tile_3 == 'O':
                                        print(f'That tile has already been chosen, please select another!')
                                        tile_logic = False
                                    else:
                                        board[2] = 'X'
                                        tile_3 = 'X'
                                        tile_logic = True
                                        end = game_logic_check(board)
                                        player_num = 2
                                elif tile_choice == 4:
                                    if tile_4 == 'X' or tile_4 == 'O':
                                        print(f'That tile has already been chosen, please select another!')
                                        tile_logic = False
                                    else:
                                        board[3] = 'X'
                                        tile_4 = 'X'
                                        tile_logic = True
                                        end = game_logic_check(board)
                                        player_num = 2
                                elif tile_choice == 5:
                                    if tile_5 == 'X' or tile_5 == 'O':
                                        print(f'That tile has already been chosen, please select another!')
                                        tile_logic = False
                                    else:
                                        board[4] = 'X'
                                        tile_5 = 'X'
                                        tile_logic = True
                                        end = game_logic_check(board)
                                        player_num = 2
                                elif tile_choice == 6:
                                    if tile_6 == 'X' or tile_6 == 'O':
                                        print(f'That tile has already been chosen, please select another!')
                                        tile_logic = False
                                    else:
                                        board[5] = 'X'
                                        tile_6 = 'X'
                                        tile_logic = True
                                        end = game_logic_check(board)
                                        player_num = 2
                                elif tile_choice == 7:
                                    if tile_7 == 'X' or tile_7 == 'O':
                                        print(f'That tile has already been chosen, please select another!')
                                        tile_logic = False
                                    else:
                                        board[6] = 'X'
                                        tile_7 = 'X'
                                        tile_logic = True
                                        end = game_logic_check(board)
                                        player_num = 2
                                elif tile_choice == 8:
                                    if tile_8 == 'X' or tile_8 == 'O':
                                        print(f'That tile has already been chosen, please select another!')
                                        tile_logic = False
                                    else:
                                        board[7] = 'X'
                                        tile_8 = 'X'
                                        tile_logic = True
                                        end = game_logic_check(board)
                                        player_num = 2
                                elif tile_choice == 9:
                                    if tile_9 == 'X' or tile_9 == 'O':
                                        print(f'That tile has already been chosen, please select another!')
                                        tile_logic = False
                                    else:
                                        board[8] = 'X'
                                        tile_9 = 'X'
                                        tile_logic = True
                                        end = game_logic_check(board)
                                        player_num = 2
                        
                        elif player_num == 2:
                            generate_board_visual(tile_1,tile_2,tile_3,tile_4,tile_5,tile_6,tile_7,tile_8,tile_9)
                            tile_logic = False
                            while tile_logic == False:
                                tile_choice = int(input(f'Enter the number of the tile you want to select: '))
                                if tile_choice == 1:
                                    if tile_1 == 'X' or tile_1 == 'O':
                                        print(f'That tile has already been chosen, please select another!')
                                        tile_logic = False
                                    else:
                                        board[0] = 'O'
                                        tile_1 = '0'
                                        tile_logic = True
                                        end = game_logic_check(board)
                                        player_num = 1
                                elif tile_choice == 2:
                                    if tile_2 == 'X' or tile_2 == 'O':
                                        print(f'That tile has already been chosen, please select another!')
                                        tile_logic = False
                                    else:
                                        board[1] = 'O'
                                        tile_2 = '0'
                                        tile_logic = True
                                        end = game_logic_check(board)
                                        player_num = 1
                                elif tile_choice == 3:
                                    if tile_3 == 'X' or tile_3 == 'O':
                                        print(f'That tile has already been chosen, please select another!')
                                        tile_logic = False
                                    else:
                                        board[2] = 'O'
                                        tile_3 = '0'
                                        tile_logic = True
                                        end = game_logic_check(board)
                                        player_num = 1
                                elif tile_choice == 4:
                                    if tile_4 == 'X' or tile_4 == 'O':
                                        print(f'That tile has already been chosen, please select another!')
                                        tile_logic = False
                                    else:
                                        board[3] = 'O'
                                        tile_4 = '0'
                                        tile_logic = True
                                        end = game_logic_check(board)
                                        player_num = 1
                                elif tile_choice == 5:
                                    if tile_5 == 'X' or tile_5 == 'O':
                                        print(f'That tile has already been chosen, please select another!')
                                        tile_logic = False
                                    else:
                                        board[4] = 'O'
                                        tile_5 = '0'
                                        tile_logic = True
                                        end = game_logic_check(board)
                                        player_num = 1
                                elif tile_choice == 6:
                                    if tile_6 == 'X' or tile_6 == 'O':
                                        print(f'That tile has already been chosen, please select another!')
                                        tile_logic = False
                                    else:
                                        board[5] = 'O'
                                        tile_6 = '0'
                                        tile_logic = True
                                        end = game_logic_check(board)
                                        player_num = 1
                                elif tile_choice == 7:
                                    if tile_7 == 'X' or tile_7 == 'O':
                                        print(f'That tile has already been chosen, please select another!')
                                        tile_logic = False
                                    else:
                                        board[6] = 'O'
                                        tile_7 = '0'
                                        tile_logic = True
                                        end = game_logic_check(board)
                                        player_num = 1
                                elif tile_choice == 8:
                                    if tile_8 == 'X' or tile_8 == 'O':
                                        print(f'That tile has already been chosen, please select another!')
                                        tile_logic = False
                                    else:
                                        board[7] = 'O'
                                        tile_8 = '0'
                                        tile_logic = True
                                        end = game_logic_check(board)
                                        player_num = 1
                                elif tile_choice == 9:
                                    if tile_9 == 'X' or tile_9 == 'O':
                                        print(f'That tile has already been chosen, please select another!')
                                        tile_logic = False
                                    else:
                                        board[8] = 'O'
                                        tile_9 = '0'
                                        tile_logic = True
                                        end = game_logic_check(board)
                                        player_num = 1
                        
                #This is where the game will be played for 2 people sharing a computer
                selection_1 = play_again_logic()
                pass
            elif selection_1 == 2:
                #This is where the game will be played for 1 person against an AI
                #generated through the random library
                print(f'THIS PORTION IS STILL UNDER CONSTRUCTION')
                selection_1 = play_again_logic()
                pass
            elif selection_1 == 3:
                pass
            else:
                print(f'\nThat selection is incorrect, please type the correct number.\n')
    
    
    print(f'\nThank you for playing my Tic-Tac-Toe Game!')

        
        
        
    


    pass

if __name__ == '__main__':
    main()