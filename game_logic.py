#This program is for the logic of the game, how a win or a tie is determined
def main():

    pass

def game_logic_check(list):
    #These first 3 cover left to right win combinations for player 1
    if list[0] == 'X' and list[1] == 'X' and list [2] == 'X':
        end = True
        return end
    elif list[3] == 'X' and list[4] == 'X' and list [5] == 'X':
        end = True
        return end
    elif list[6] == 'X' and list[7] == 'X' and list [8] == 'X':
        end = True
        return end
    #These two cover diagonal win combinations for player 1
    elif list[0] == 'X' and list[4] == 'X' and list [8] == 'X':
        end = True
        return end
    elif list[2] == 'X' and list[4] == 'X' and list [6] == 'X':
        end = True
        return end
    #These three cover top to bottom win combinations for player 1
    elif list[0] == 'X' and list[3] == 'X' and list [6] == 'X':
        end = True
        return end
    elif list[1] == 'X' and list[4] == 'X' and list [7] == 'X':
        end = True
        return end
    elif list[2] == 'X' and list[5] == 'X' and list [8] == 'X':
        end = True
        return end
    #These first 3 cover left to right win combinations for player 2
    elif list[0] == 'O' and list[1] == 'O' and list [2] == 'O':
        end = True
        return end
    elif list[3] == 'O' and list[4] == 'O' and list [5] == 'O':
        outcome ='Player 2 has won!'
        return outcome
    elif list[6] == 'O' and list[7] == 'O' and list [8] == 'O':
        end = True
        return end
    #These two cover diagonal win combinations for player 2
    elif list[0] == 'O' and list[4] == 'O' and list [8] == 'O':
        end = True
        return end
    elif list[2] == 'O' and list[4] == 'O' and list [6] == 'O':
        end = True
        return end
    #These three cover top to bottom win combinations for player 2
    elif list[0] == 'O' and list[3] == 'O' and list [6] == 'O':
        end = True
        return end
    elif list[1] == 'O' and list[4] == 'O' and list [7] == 'O':
        end = True
        return end
    elif list[2] == 'O' and list[5] == 'O' and list [8] == 'O':
        end = True
        return end
    #This last set of logic checks if all of the spaces in the list have been filled
    #And if a win has not been achieved, it prints out tie game
    elif (list[0] == 'X' or list[0] == 'O') and (list[1] == 'X' or list[1] == 'O') and (list[2] == 'X' or list[2] == 'O') and (list[3] == 'X' or list[3] == 'O') and (list[4] == 'X' or list[4] == 'O') and (list[5] == 'X' or list[5] == 'O') and (list[6] == 'X' or list[6] == 'O') and (list[7] == 'X' or list[7] == 'O') and (list[8] == 'X' or list[8] == 'O'):
        end = True
        return end
    else:
        end = False
        return end
    
    pass



if __name__ == '__main__':
    main()