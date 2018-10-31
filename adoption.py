#!/usr/bin/env python

#Homepage for the program
def page_home():
    print('\nWelcome to the Adoption Center! What would you like to do? \n[1]View Available Pets \n[2]Pet Drop-off \n[3]Admin Login \n[4]Quit \n')

    #Ensure the user inputs an int between the valid values(1-4)
    while True:
        try:
            action = int(input('Input: '))
        except:
            print('Please enter a number\n')
            continue
        else:
            if action < 1 or action > 4:
                print('Please enter a valid number.\n')
                continue
            else:
                break

    print('Input recieved')
    if action == 1:
        print('Action 1 Revieved')
        page_pets()
    elif action == 2:
        print('Action 2 Revieved')
        pass
    elif action == 3:
        print('Action 3 Revieved')
        pass
    elif action == 4:
        print('Quiting')
        return


#Pet viewing page
def page_pets():
    print('Pets Homepage')


def main():
    while True:
        page_home()
        break

    print('Thanks for stopping by!')

if __name__== "__main__":
    main()
