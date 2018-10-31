#!/usr/bin/env python
from os import system, name

#Homepage for the program
def page_home():
    clear()
    print('Welcome to the Adoption Center! What would you like to do? \n[1]View Available Pets \n[2]Pet Drop-off \n[3]Admin Login \n[4]Quit \n')

    action = get_input(4)

    if action == 1:
        page_pets_home()
    elif action == 2:
        page_adoption()
    elif action == 3:
        page_admin()
    elif action == 4:
        return


#Pet viewing home page
def page_pets_home():
    clear()
    print('How would you like to view pets? \n[1]View All \n[2]Sorted View \n[3]Home \n')

    action = get_input(3)

    if action == 1:
        page_pets_all()
    elif action == 2:
        page_pets_sorted()
    elif action == 3:
        page_home()


#Adoption Home page
def page_adoption():
    clear()
    print('Adoption Homepage')


#Admin Home page
def page_admin():
    clear()
    print('Admin Homepage')


#Page of all available pets
def page_pets_all():
    clear()
    print('ALL PETS LISTED HERE')
    print('\nWhat would you like to do? \n[1]Schedule a Visit \n[2]Adopt a Pet \n[3]Sorted View \n[4]Home')

    action = get_input(4)

#Page of all available pets that meet some inputed criteria
def page_pets_sorted():
    clear()
    print('Pets Sorted Page')



#Helper function that clears the screen
def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


#Helper function that gets user input. Limit is the upper limit allowed input(Number of user options)
def get_input(limit):
    while True:
        try:
            action = int(input('Input: '))
        except:
            print('Please enter a number\n')
            continue
        else:
            if action < 1 or action > limit:
                print('Please enter a valid number.\n')
                continue
            else:
                return action

def main():
    while True:
        page_home()
        break

    print('Thanks for stopping by!')

if __name__== "__main__":
    main()
