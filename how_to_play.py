#This program is purely so I don't have extra lines of code where I don't have to in the main program
def main():

    how_to_play()

    pass

def how_to_play():
    line_1 = 'HOW TO PLAY'
    length_line_1 = len(line_1)
    print(line_1)
    print('-'*length_line_1)
    line_2 = 'Tic-Tac-Toe is a game for two players.'
    line_3 = 'The first person is X and the second'
    line_4 = 'is O. The goal of the game is to get'
    line_5 = '3 of your symbols in a row before your'
    line_6 = 'opponent. The person with X always goes'
    line_7 = 'first. When you are ready to begin,'
    line_8 = 'press 1 in the main menu. The game will'
    line_9 = 'alternate between Player 1 and Player 2'
    line_10 = 'so pay attention. Good luck!'
    print(line_2)
    print(line_3)
    print(line_4)
    print(line_5)
    print(line_6)
    print(line_7)
    print(line_8)
    print(line_9)
    print(line_10)
    print('-'*length_line_1)

if __name__ == '__main__':
    main()