#!/usr/bin/env python3
import time
import helper
from main import PetFactory
#================================================================================================================================================
#All the UI pages for the program. Pages handle the navigation between each page individually.

#Pet factory to create any new Pets
myFactory = PetFactory()

#Homepage for the program
def page_home(shelter):
    helper.clear()
    print('Welcome to the Adoption Center! What would you like to do? \n[1]View Pets \n[2]Pet Drop-off \n[3]Admin Login \n[4]Quit')

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

#Page to add a pet to the directory
def page_pet_dropoff(shelter):
    helper.clear()
    print('Please enter the requested information:')
    shelter.add_Pet(myFactory.createPet(shelter))
    print('Thank you for your submission!')
    time.sleep(3)
    page_home(shelter)

#Admin Home page
def page_admin():
    helper.clear()
    print('Admin Homepage')

#Pet viewing home page
def page_pets_home(shelter):
    helper.clear()
    print('How would you like to view pets? \n[1]View All \n[2]Sorted View \n[3]Home')

    limit = 3
    action = helper.get_next_page(limit)

    if action == 1:
        page_pets_all(shelter)
    elif action == 2:
        page_pets_sorted(shelter)
    elif action == 3:
        page_home(shelter)

#Page that displays all available pets
def page_pets_all(shelter):
    helper.clear()
    shelter.print_Pets()
    print('\nWhat would you like to do? \n[1]Schedule a Visit \n[2]Adopt a Pet \n[3]Sorted View \n[4]Home')

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

#Page of all available pets that meet some inputed criteria(Sorted by type of animal)
def page_pets_sorted(shelter):
    helper.clear()
    print('How would you like to sort?\n')

    #Prints all types of pets currently available
    limit = 0
    for animal in shelter.animal_types:
        limit = limit + 1
        print('[{}]{}'.format(limit, animal))

    animal = shelter.animal_types[helper.get_next_page(limit)-1]
    helper.clear()
    print('Currently Available {}s: \n'.format(animal))
    shelter.print_Pets_Sorted(animal)
    print('\nWhat would you like to do? \n[1]Schedule a Visit \n[2]Adopt a Pet \n[3]View Another Category \n[4]View All Pets \n[5]Home')

    limit = 5
    action = helper.get_next_page(limit)

    if action == 1:
        page_pets_visit(shelter)
    elif action == 2:
        page_pets_adopt(shelter)
    elif action == 3:
        page_pets_sorted(shelter)
    elif action == 4:
        page_pets_all(shelter)
    elif action == 5:
        page_home(shelter)

#Page to adopt a pet - remove it from the list of available pets
def page_pets_adopt(shelter):
    print('Please enter the pet ID you wish to adopt. [0 to exit]')

    id = helper.get_input_ID(shelter.pet_directory)

    if id == 0:
        page_home(shelter)
    else:
        print('Thank you for adopting [{}], they can''t wait to see you!'.format(id))
        shelter.update_Pet_Status(id, 'Adopted')
        time.sleep(3)
        page_home(shelter)

#Page to schedule a visit
def page_pets_visit(shelter):
    print('Please enter the pet ID you wish to visit. [0 to exit]')

    id = helper.get_input_ID(shelter.pet_directory)

    if id == 0:
        page_home(shelter)
    else:
        print('Thank you for scheduling a visit with [{}], we{}ll see you soon!'.format(id, "'"))
        shelter.update_Pet_Status(id, 'On Hold')
        time.sleep(3)
        page_home(shelter)
