#This code is to generate the tic-tac-toe board
def main():

    #choice = int(input(f'How large would you like your board to be?: '))

    #These variables on lines 8-16 are set so the board can initially be filled.
    #Logic will update them as the game is played
    _1 = 1
    _2 = 2
    _3 = 3
    _4 = 4
    _5 = 5
    _6 = 6
    _7 = 7
    _8 = 8
    _9 = 9
    generate_board(_1, _2, _3, _4, _5, _6, _7, _8, _9)

    pass

def generate_board(_1, _2, _3, _4, _5, _6, _7, _8, _9):
    print(f'[{_1}] [{_2}] [{_3}]\n[{_4}] [{_5}] [{_6}]\n[{_7}] [{_8}] [{_9}]')
    
    #This code below was an attempt to create an adjustable board size
    #for row in range(1, board_size+1):
        #for col in range(1, board_size+1):
            #print(board_size, end = '\t')
        #print()

if __name__ == '__main__':
    main()