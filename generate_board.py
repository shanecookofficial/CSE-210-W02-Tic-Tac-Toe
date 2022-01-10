#This code is to generate the tic-tac-toe board
def main():

    tile_1 = 1
    tile_2 = 2
    tile_3 = 3
    tile_4 = 4
    tile_5 = 5
    tile_6 = 6
    tile_7 = 7
    tile_8 = 8
    tile_9 = 9
    
    generate_board(tile_1,tile_2,tile_3,tile_4,tile_5,tile_6,tile_7,tile_8,tile_9)
    pass

def generate_board(_1,_2,_3,_4,_5,_6,_7,_8,_9):

    print(f'[{_1}] [{_2}] [{_3}]\n[{_4}] [{_5}] [{_6}]\n[{_7}] [{_8}] [{_9}]')



if __name__ == '__main__':
    main()