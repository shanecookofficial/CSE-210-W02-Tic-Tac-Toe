#This code is to generate the tic-tac-toe board
def main():

    #choice = int(input(f'How large would you like your board to be?: '))

    generate_board()

    pass

def generate_board():

    print('[1] [2] [3]\n[4] [5] [6]\n[7] [8] [9]')

    #This code below was an attempt to create an adjustable board size
    #for row in range(1, board_size+1):
        #for col in range(1, board_size+1):
            #print(board_size, end = '\t')
        #print()

if __name__ == '__main__':
    main()