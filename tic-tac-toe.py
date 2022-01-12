#This is the outline for the full game
from generate_board_visual import generate_board_visual
from generate_menu import generate_menu
from play_again_logic import play_again_logic
from game_logic import game_logic, end_game_loop
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
                                        tile_1 = 'X'
                                        game_logic(board)
                                        end = end_game_loop()
                                        tile_logic = True
                                        player_num = 2
                                elif tile_choice == 2:
                                    if tile_2 == 'X' or tile_2 == 'O':
                                        print(f'That tile has already been chosen, please select another!')
                                        tile_logic = False
                                    else:
                                        tile_2 = 'X'
                                        game_logic(board)
                                        end = end_game_loop()
                                        tile_logic = True
                                        player_num = 2
                                elif tile_choice == 3:
                                    if tile_3 == 'X' or tile_3 == 'O':
                                        print(f'That tile has already been chosen, please select another!')
                                        tile_logic = False
                                    else:
                                        tile_3 = 'X'
                                        game_logic(board)
                                        end = end_game_loop()
                                        tile_logic = True
                                        player_num = 2
                                elif tile_choice == 4:
                                    if tile_4 == 'X' or tile_4 == 'O':
                                        print(f'That tile has already been chosen, please select another!')
                                        tile_logic = False
                                    else:
                                        tile_4 = 'X'
                                        game_logic(board)
                                        end = end_game_loop()
                                        tile_logic = True
                                        player_num = 2
                                elif tile_choice == 5:
                                    if tile_5 == 'X' or tile_5 == 'O':
                                        print(f'That tile has already been chosen, please select another!')
                                        tile_logic = False
                                    else:
                                        tile_5 = 'X'
                                        game_logic(board)
                                        end = end_game_loop()
                                        tile_logic = True
                                        player_num = 2
                                elif tile_choice == 6:
                                    if tile_6 == 'X' or tile_6 == 'O':
                                        print(f'That tile has already been chosen, please select another!')
                                        tile_logic = False
                                    else:
                                        tile_6 = 'X'
                                        game_logic(board)
                                        end = end_game_loop()
                                        tile_logic = True
                                        player_num = 2
                                elif tile_choice == 7:
                                    if tile_7 == 'X' or tile_7 == 'O':
                                        print(f'That tile has already been chosen, please select another!')
                                        tile_logic = False
                                    else:
                                        tile_7 = 'X'
                                        game_logic(board)
                                        end = end_game_loop()
                                        tile_logic = True
                                        player_num = 2
                                elif tile_choice == 8:
                                    if tile_8 == 'X' or tile_8 == 'O':
                                        print(f'That tile has already been chosen, please select another!')
                                        tile_logic = False
                                    else:
                                        tile_8 = 'X'
                                        game_logic(board)
                                        end = end_game_loop()
                                        tile_logic = True
                                        player_num = 2
                                elif tile_choice == 9:
                                    if tile_9 == 'X' or tile_9 == 'O':
                                        print(f'That tile has already been chosen, please select another!')
                                        tile_logic = False
                                    else:
                                        tile_9 = 'X'
                                        game_logic(board)
                                        end = end_game_loop()
                                        tile_logic = True
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
                                        tile_1 = 'O'
                                        game_logic(board)
                                        end = end_game_loop()
                                        tile_logic = True
                                        player_num = 1
                                elif tile_choice == 2:
                                    if tile_2 == 'X' or tile_2 == 'O':
                                        print(f'That tile has already been chosen, please select another!')
                                        tile_logic = False
                                    else:
                                        tile_2 = 'O'
                                        game_logic(board)
                                        end = end_game_loop()
                                        tile_logic = True
                                        player_num = 1
                                elif tile_choice == 3:
                                    if tile_3 == 'X' or tile_3 == 'O':
                                        print(f'That tile has already been chosen, please select another!')
                                        tile_logic = False
                                    else:
                                        tile_3 = 'O'
                                        game_logic(board)
                                        end = end_game_loop()
                                        tile_logic = True
                                        player_num = 1
                                elif tile_choice == 4:
                                    if tile_4 == 'X' or tile_4 == 'O':
                                        print(f'That tile has already been chosen, please select another!')
                                        tile_logic = False
                                    else:
                                        tile_4 = 'O'
                                        game_logic(board)
                                        end = end_game_loop()
                                        tile_logic = True
                                        player_num = 1
                                elif tile_choice == 5:
                                    if tile_5 == 'X' or tile_5 == 'O':
                                        print(f'That tile has already been chosen, please select another!')
                                        tile_logic = False
                                    else:
                                        tile_5 = 'O'
                                        game_logic(board)
                                        end = end_game_loop()
                                        tile_logic = True
                                        player_num = 1
                                elif tile_choice == 6:
                                    if tile_6 == 'X' or tile_6 == 'O':
                                        print(f'That tile has already been chosen, please select another!')
                                        tile_logic = False
                                    else:
                                        tile_6 = 'O'
                                        game_logic(board)
                                        end = end_game_loop()
                                        tile_logic = True
                                        player_num = 1
                                elif tile_choice == 7:
                                    if tile_7 == 'X' or tile_7 == 'O':
                                        print(f'That tile has already been chosen, please select another!')
                                        tile_logic = False
                                    else:
                                        tile_7 = 'O'
                                        game_logic(board)
                                        end = end_game_loop()
                                        tile_logic = True
                                        player_num = 1
                                elif tile_choice == 8:
                                    if tile_8 == 'X' or tile_8 == 'O':
                                        print(f'That tile has already been chosen, please select another!')
                                        tile_logic = False
                                    else:
                                        tile_8 = 'O'
                                        game_logic(board)
                                        end = end_game_loop()
                                        tile_logic = True
                                        player_num = 1
                                elif tile_choice == 9:
                                    if tile_9 == 'X' or tile_9 == 'O':
                                        print(f'That tile has already been chosen, please select another!')
                                        tile_logic = False
                                    else:
                                        tile_9 = 'O'
                                        game_logic(board)
                                        end = end_game_loop()
                                        tile_logic = True
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