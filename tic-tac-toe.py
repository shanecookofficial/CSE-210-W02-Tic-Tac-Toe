#This is the outline for the full game
from generate_board import generate_board
from generate_menu import generate_menu
def main():

    
    #Menu
    selection_1 = 0
    while selection_1 != 3:
        if selection_1 != 3:
            generate_menu()
            selection_1 = int(input(f'Enter your selection: '))
            if selection_1 == 1:
                #This is where the game will be played for 2 people sharing a computer
                pass
            elif selection_1 == 2:
                #This is where the game will be played for 1 person against an AI
                #generated through the random library
                pass
            elif selection_1 == 3:
                pass
            else:
                print(f'\nThat selection is incorrect, please type the correct number.\n')
    
    
    print(f'\nThank you for playing my Tic-Tac-Toe Game!')

        
        
        
    


    pass

if __name__ == '__main__':
    main()