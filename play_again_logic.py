#This is for the logic to determine whether the user would like to play again

def main():

    play_again_logic()
    pass

def play_again_logic():
    selection_1 = 0
    status = False
    while status != True:
        answer = input(f'Would you like to play again?(Y/N): ')
        answer = answer.upper()
        if answer == 'Y':
            status = True
            return selection_1
        elif answer == 'N':
            status = True
            selection_1 = 3
            return selection_1
        else:
            print(f'\nThat input is incorrect, please try again.\n')
    pass

if __name__ == '__main__':
    main()