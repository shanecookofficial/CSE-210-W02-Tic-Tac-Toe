#This code is for the logic of the game
def main():

    logic('X','X','X')

    pass

def logic(_1, _2, _3, _4, _5, _6, _7, _8, _9):

    if _1 and _2 and _3 == 'X':
        print(f'Player 1 wins!')
    elif _4 and _5 and _6 == 'X':
        print(f'Player 1 wins!')
    elif _7 and _8 and _9 == 'X':
        print(f'Player 1 wins!')
    elif _1 and _4 and _7 == 'X':
        print(f'Player 1 wins!')
    elif _2 and _5 and _8 =='X':
        print(f'Player 1 wins!')
    elif _3 and _6 and _9 == 'X':
        print(f'Player 1 wins!')
    elif _1 and _5 and _9 == 'X':
        print(f'Player 1 wins!')
    elif _3 and _5 and _7 == 'X':
        print(f'Player 1 wins!')
    elif _1 and _2 and _3 == 'Y':
        print(f'Player 2 wins!')
    elif _4 and _5 and _6 == 'Y':
        print(f'Player 2 wins!')
    elif _7 and _8 and _9 == 'Y':
        print(f'Player 2 wins!')
    elif _1 and _4 and _7 == 'Y':
        print(f'Player 2 wins!')
    elif _2 and _5 and _8 == 'Y':
        print(f'Player 2 wins!')
    elif _3 and _6 and _9 == 'Y':
        print(f'Player 2 wins!')
    elif _1 and _5 and _9 == 'Y':
        print(f'Player 2 wins!')
    elif _3 and _5 and _7 == 'Y':
        print(f'Player 2 wins!')
    elif (_1 and _2 and _3 and _4 and _5 and _6 and _7 and _8 and _9) == 'X' or 'Y':
        print(f'Tie game!')

if __name__ == '__main__':
    main()