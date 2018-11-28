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
        page_admin(shelter)
    elif action == 4:
        return


def page_admin(shelter):
    """Select an Admin to sign in as, pass shelter and admin into the admin home page
    """
    helper.clear()
    print('Who are you signing in as?\n')

    limit = 0
    for admin in shelter.admin_directory:
        limit = limit + 1
        print('[{}]{}'.format(limit, admin.name))

    admin = shelter.admin_directory[helper.get_next_page(limit) - 1]
    page_admin_home(shelter, admin)


def page_admin_home(shelter, admin):
    """The admin homepage where the user selects what operation they wish to perform
    """
    helper.clear()
    print('[Admin] What would you like to do? \n[1]View All Pets \n[2]View Drop-Off Requests \n[3]Add Pet \n[4]Edit Pet \n[5]Home')

    limit = 5
    action = helper.get_next_page(limit)

    if action == 1:
        page_admin_all_pets(shelter, admin)
    elif action == 2:
        page_admin_dropoffs(shelter, admin)
    elif action == 3:
        page_admin_add_pet(shelter, admin)
    elif action == 4:
        pass
    elif action == 5:
        page_home(shelter)


def page_admin_all_pets(shelter, admin):
    """Print all pets in the shelter including those not available. Keep track of records
    """
    shelter.print_Pets()
    print('[Admin] What would you like to do? \n[1]View Drop-Off Requests \n[2]Add Pet \n[3]Edit Pet \n[4]Home')

    limit = 4
    action = helper.get_next_page(limit)

    if action == 1:
        page_admin_dropoffs(shelter, admin)
    elif action == 2:
        page_admin_add_pet(shelter, admin)
    elif action == 3:
        pass
    elif action == 4:
        page_admin_home(shelter, admin)


def page_admin_dropoffs(shelter, admin):
    """Page for admins to accept/decline pet drop off requests
    """
    for pet in shelter.pet_drop_directory:
        helper.print_pet(pet)

    print('\n[Admin] What would you like to do? \n[1]Accept Pet \n[2]Decline Pet \n[3]Admin Home')

    limit = 3
    action = helper.get_next_page(limit)

    if action == 1:
        page_admin_accept(shelter, admin)
    elif action == 2:
        page_admin_decline(shelter, admin)
    elif action == 3:
        page_admin_home(shelter, admin)


def page_admin_accept(shelter, admin):
    """Page to move a Pet from the drop off directory and add to the pet directory
    """
    print('Please enter the ID of the Pet you wish to accept.')
    id = helper.get_input_ID(shelter.pet_drop_directory)
    shelter.add_Pet(shelter.get_Pet(id, shelter.pet_drop_directory), shelter.pet_directory)
    shelter.remove_Pet(id, shelter.pet_drop_directory)
    print('Pet {} has been accepted to the pet directory.'.format(id))
    time.sleep(3)
    page_admin_home(shelter, admin)


def page_admin_decline(shelter, admin):
    """Page to remove a pet from the drop off directory
    """
    print('Please enter the ID of the Pet you wish to decline.')
    id = helper.get_input_ID(shelter.pet_drop_directory)
    shelter.remove_Pet(id, shelter.pet_drop_directory)
    print('Pet {} has been declined.'.format(id))
    time.sleep(3)
    page_admin_home(shelter, admin)


def page_admin_add_pet(shelter, admin):
    """Admin can add a Pet directly to the Shelter's Pet Directory
    """
    helper.clear()
    print('[Admin] Please enter the requested information:')
    shelter.add_Pet(myFactory.createPet(shelter), shelter.pet_directory)
    print('Thank you for your submission!')
    time.sleep(3)
    page_admin_home(shelter, admin)


def page_pet_dropoff(shelter):
    """Page to add pets to the Shelter's drop off directory for admin approval
    """
    helper.clear()
    print('Please enter the requested information:')
    shelter.add_Pet(myFactory.createPet(shelter), shelter.pet_drop_directory)
    print('Thank you for your submission!')
    time.sleep(3)
    page_home(shelter)


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
        print('Thank you for adopting {}, they can''t wait to see you!'.format((shelter.get_Pet(id, shelter.pet_directory)).name))
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
        print('Thank you for scheduling a visit with {}, we{}ll see you soon!'.format((shelter.get_Pet(id, shelter.pet_directory)).name, "'"))
        shelter.update_Pet_Status(id, 'On Hold')
        time.sleep(3)
        page_home(shelter)
