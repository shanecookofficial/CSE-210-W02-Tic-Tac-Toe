#This is the outline for the full game
from generate_board import generate_board
from generate_menu import generate_menu
from play_again_logic import play_again_logic
def main():

    
    #Menu
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

        if selection_1 != 3:
            generate_menu()
            selection_1 = int(input(f'Enter your selection: '))
            if selection_1 == 1:
                #This is where the game will be played for 2 people sharing a computer
                selection_1 = play_again_logic()
                pass
            elif selection_1 == 2:
                #This is where the game will be played for 1 person against an AI
                #generated through the random library
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