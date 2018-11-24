#!/usr/bin/env python3
import time
import helper
from main import PetFactory
#================================================================================================================================================

#Pet factory to create any new Pets
myFactory = PetFactory()


def page_home(shelter):
    """Homepage for the program
    """
    helper.clear()
    print('Welcome to the Adoption Center! What would you like to do? \n[1]View All Available Pets \n[2]Pet Drop-off \n[3]Admin Login \n[4]Quit')

    limit = 4
    action = helper.get_next_page(limit)

    if action == 1:
        page_pets_home(shelter)
    elif action == 2:
        page_pet_dropoff(shelter)
    elif action == 3:
        page_admin()
    elif action == 4:
        return


def page_pet_dropoff(shelter):
    """Page to add pets to the Shelter's Pet Directory
    """
    helper.clear()
    print('Please enter the requested information:')
    shelter.add_Pet(myFactory.createPet(shelter))
    print('Thank you for your submission!')
    time.sleep(3)
    page_home(shelter)


def page_admin():
    """Admin Homepage
    """
    helper.clear()
    print('Admin Homepage')


def page_pets_home(shelter):
    """Main Pet viewing page. Get user input for preferred viewing style
    """
    helper.clear()
    print('How would you like to view pets? \n[1]View All Available Pets \n[2]Sort Available Pets \n[3]Home')

    limit = 3
    action = helper.get_next_page(limit)

    if action == 1:
        page_pets_available(shelter)
    elif action == 2:
        page_pets_sorted(shelter)
    elif action == 3:
        page_home(shelter)


def page_pets_all(shelter):
    """Page to display all pets in Shelter's Pet Directory
    """
    helper.clear()
    shelter.print_Pets()
    print('\nWhat would you like to do? \n[1]Schedule a Visit \n[2]Adopt a Pet \n[3]Sort Available Pets \n[4]Home')

    limit = 4
    action = helper.get_next_page(limit)

    if action == 1:
        page_pets_visit(shelter)
    elif action == 2:
        page_pets_adopt(shelter)
    elif action == 3:
        page_pets_sorted(shelter)
    elif action == 4:
        page_home(shelter)


def page_pets_available(shelter):
    """Page to display all available(Not Adopted and not On-Hold) pets in the Shelter's Pet Directory
    """
    helper.clear()
    shelter.print_Pets_Available()
    print('\nWhat would you like to do? \n[1]Schedule a Visit \n[2]Adopt a Pet \n[3]Sort Available Pets \n[4]Home')

    limit = 4
    action = helper.get_next_page(limit)

    if action == 1:
        page_pets_visit(shelter)
    elif action == 2:
        page_pets_adopt(shelter)
    elif action == 3:
        page_pets_sorted(shelter)
    elif action == 4:
        page_home(shelter)


def page_pets_sorted(shelter):
    """Page to display Pets that meet a user inputed criteria(Animal Type)
    """
    helper.clear()
    print('How would you like to sort?\n')

    limit = 0
    for animal in shelter.animal_types:
        limit = limit + 1
        print('[{}]{}'.format(limit, animal))

    animal = shelter.animal_types[helper.get_next_page(limit)-1]
    helper.clear()
    print('Currently Available {}s: \n'.format(animal))
    shelter.print_Pets_Sorted(animal)
    print('\nWhat would you like to do? \n[1]Schedule a Visit \n[2]Adopt a Pet \n[3]View Another Category \n[4]View All Available Pets \n[5]Home')

    limit = 5
    action = helper.get_next_page(limit)

    if action == 1:
        page_pets_visit(shelter)
    elif action == 2:
        page_pets_adopt(shelter)
    elif action == 3:
        page_pets_sorted(shelter)
    elif action == 4:
        page_pets_available(shelter)
    elif action == 5:
        page_home(shelter)


def page_pets_adopt(shelter):
    """Page to adopt a pet - update the status. User inputs Pet ID to update
    """
    print('Please enter the pet ID you wish to adopt. [0 to exit]')

    id = helper.get_input_ID(shelter.pet_directory)

    if id == 0:
        page_home(shelter)
    else:
        print('Thank you for adopting {}, they can''t wait to see you!'.format((shelter.get_Pet(id)).name))
        shelter.update_Pet_Status(id, 'Adopted')
        time.sleep(3)
        page_home(shelter)


def page_pets_visit(shelter):
    """Page to schedule a visit with a Pet - update the status. User inputs Pet ID to update
    """
    print('Please enter the pet ID you wish to visit. [0 to exit]')

    id = helper.get_input_ID(shelter.pet_directory)

    if id == 0:
        page_home(shelter)
    else:
        print('Thank you for scheduling a visit with {}, we{}ll see you soon!'.format((shelter.get_Pet(id)).name, "'"))
        shelter.update_Pet_Status(id, 'On Hold')
        time.sleep(3)
        page_home(shelter)
