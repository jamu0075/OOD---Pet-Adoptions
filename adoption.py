#!/usr/bin/env python
from os import system, name
import time

#Homepage for the program
def page_home():
    clear()
    print('Welcome to the Adoption Center! What would you like to do? \n[1]View Available Pets \n[2]Pet Drop-off \n[3]Admin Login \n[4]Quit')

    action = get_input(4, False)

    if action == 1:
        page_pets_home()
    elif action == 2:
        page_adoption()
    elif action == 3:
        page_admin()
    elif action == 4:
        return


#Admin Home page
def page_admin():
    clear()
    print('Admin Homepage')


#Pet viewing home page
def page_pets_home():
    clear()
    print('How would you like to view pets? \n[1]View All \n[2]Sorted View \n[3]Home')

    action = get_input(3, False)

    if action == 1:
        page_pets_all()
    elif action == 2:
        page_pets_sorted()
    elif action == 3:
        page_home()


#Page to add a pet to the directory
def page_pets_add():
    clear()
    print('Adoption Homepage')



#Page that displays all available pets
def page_pets_all():
    clear()
    print('ALL PETS LISTED HERE')
    print('\nWhat would you like to do? \n[1]Schedule a Visit \n[2]Adopt a Pet \n[3]Sorted View \n[4]Home')

    action = get_input(4, False)

    if action == 1:
        page_pets_visit()
    elif action == 2:
        page_pets_adopt()
    elif action == 3:
        page_pets_sorted()
    elif action == 4:
        page_home()


#Page of all available pets that meet some inputed criteria(Sorted by type of animal)
def page_pets_sorted():
    clear()
    print('How would you like to sort?\n')

    #Prints all types of pets currently available
    x=6
    for i in range(x):
        print('[{}]{}'.format(i+1, i+1))

    animal = get_input(x, False)

    clear()
    print('Currently Available [{}]\n'.format(animal))
    print('What would you like to do? \n[1]Schedule a Visit \n[2]Adopt a Pet \n[3]View Another Category \n[4]View All Pets \n[5]Home')

    action = get_input(5, False)

    if action == 1:
        page_pets_visit()
    elif action == 2:
        page_pets_adopt()
    elif action == 3:
        page_pets_sorted()
    elif action == 4:
        page_pets_all()
    elif action == 5:
        page_home()


#Page to adopt a pet - remove it from the list of available pets
def page_pets_adopt():
    print('Please enter the pet ID you wish to adopt visit. [0 to exit]')

    action = get_input(None, True)

    if action == 0:
        page_home()
    else:
        print('Thank you for adopting [{}], they can''t wait to see you!'.format(action))
        time.sleep(3)
        page_home()

#Page to schedule a visit
def page_pets_visit():
    print('Please enter the pet ID you wish to visit. [0 to exit]')

    action = get_input(None, True)

    if action == 0:
        page_home()
    else:
        print('Thank you for scheduling a visit with [{}], we''ll see you soon!'.format(action))
        time.sleep(3)
        page_home()


#Helper function that clears the screen
def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


#Helper function that gets user input. Limit is the upper limit allowed input(Number of user options)
#Visit is a boolen for the vist scheduling, will ensure entered ID is in directory of pets
def get_input(limit, check_ID):
    while True:
        try:
            action = int(input('\nInput: '))
        except:
            print('Please enter a number.')
            continue
        else:
            #Ensures the inputed ID is in the directory of pets
            if check_ID:
                if action == 0:
                    return action
                elif action not in pet_directory:
                    print('Please enter a valid pet ID.')
                    continue
                else:
                    return action

            #Handles all other user inputs
            elif action < 1 or action > limit:
                print('Please enter a valid number.')
                continue
            else:
                return action

pet_directory = [1, 2]
def main():
    while True:
        page_home()
        break

    print('Thanks for stopping by!')

if __name__== "__main__":
    main()
