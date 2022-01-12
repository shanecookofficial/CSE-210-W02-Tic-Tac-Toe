#This program is for the logic of the game, how a win or a tie is determined
def main():

    test_list = ['O','X','O','X','O','O','X','O','X']
    end = game_logic(test_list)
    print(end)

    pass

def game_logic(list):
    #These first 3 cover left to right win combinations for player 1
    if list[0] == 'X' and list[1] == 'X' and list [2] == 'X':
        return 'Player 1 has won!'
    elif list[3] == 'X' and list[4] == 'X' and list [5] == 'X':
        return 'Player 1 has won!'
    elif list[6] == 'X' and list[7] == 'X' and list [8] == 'X':
        return 'Player 1 has won!'
    #These two cover diagonal win combinations for player 1
    elif list[0] == 'X' and list[4] == 'X' and list [8] == 'X':
        return 'Player 1 has won!'
    elif list[2] == 'X' and list[4] == 'X' and list [6] == 'X':
        return 'Player 1 has won!'
    #These three cover top to bottom win combinations for player 1
    elif list[0] == 'X' and list[3] == 'X' and list [6] == 'X':
        return 'Player 1 has won!'
    elif list[1] == 'X' and list[4] == 'X' and list [7] == 'X':
        return 'Player 1 has won!'
    elif list[2] == 'X' and list[5] == 'X' and list [8] == 'X':
        return 'Player 1 has won!'

    #These first 3 cover left to right win combinations for player 2
    elif list[0] == 'O' and list[1] == 'O' and list [2] == 'O':
        return 'Player 2 has won!'
    elif list[3] == 'O' and list[4] == 'O' and list [5] == 'O':
        return 'Player 2 has won!'
    elif list[6] == 'O' and list[7] == 'O' and list [8] == 'O':
        return 'Player 2 has won!'
    #These two cover diagonal win combinations for player 2
    elif list[0] == 'O' and list[4] == 'O' and list [8] == 'O':
        return 'Player 2 has won!'
    elif list[2] == 'O' and list[4] == 'O' and list [6] == 'O':
        return 'Player 2 has won!'
    #These three cover top to bottom win combinations for player 2
    elif list[0] == 'O' and list[3] == 'O' and list [6] == 'O':
        return 'Player 2 has won!'
    elif list[1] == 'O' and list[4] == 'O' and list [7] == 'O':
        return 'Player 2 has won!'
    elif list[2] == 'O' and list[5] == 'O' and list [8] == 'O':
        return 'Player 2 has won!'
    #This last set of logic checks if all of the spaces in the list have been filled
    #And if a win has not been achieved, it prints out tie game
    elif list[0] == 'X' or 'O' and list[1] == 'X' or 'O' and list[2] == 'X' or 'O' and list[3] == 'X' or 'O' and list[4] == 'X' or 'O' and list[5] == 'X' or 'O' and list[6] == 'X' or 'O' and list[7] == 'X' or 'O' and list[8] == 'X' or 'O':
        return 'Tie game!'
    
    pass

def end_game_loop():

    end  = game_logic
    if end == 'Player 1 has won!' or end == 'Player 2 has won!' or end == 'Tie game!':
        end = True
        return end
    else:
        end = False
        return end

if __name__ == '__main__':
    main()