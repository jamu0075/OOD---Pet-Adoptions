#!/usr/bin/env python3
import time
import animals
import helper

#================================================================================================================================================
#All the UI pages for the program
#Handles all the navigation within each page individually

#Homepage for the program
def page_home():
    helper.clear()
    print('Welcome to the Adoption Center! What would you like to do? \n[1]View Available Pets \n[2]Pet Drop-off \n[3]Admin Login \n[4]Quit')

    limit = 4
    action = helper.get_next_page(limit)

    if action == 1:
        page_pets_home()
    elif action == 2:
        page_pets_adopt_request()
    elif action == 3:
        page_admin()
    elif action == 4:
        return

#Page to add a pet to the directory
def page_pets_adopt_request():
    helper.clear()
    print('Please enter the requested information:')
    createPet()
    print('Thank you for your submission!')
    time.sleep(3)
    page_home()

#Admin Home page
def page_admin():
    helper.clear()
    print('Admin Homepage')

#Pet viewing home page
def page_pets_home():
    helper.clear()
    print('How would you like to view pets? \n[1]View All \n[2]Sorted View \n[3]Home')

    limit = 3
    action = helper.get_next_page(limit)

    if action == 1:
        page_pets_all()
    elif action == 2:
        page_pets_sorted()
    elif action == 3:
        page_home()

#Page that displays all available pets
def page_pets_all():
    helper.clear()
    print('ALL PETS LISTED HERE')
    myShelter.print_Pets()
    print('\nWhat would you like to do? \n[1]Schedule a Visit \n[2]Adopt a Pet \n[3]Sorted View \n[4]Home')

    limit = 4
    action = helper.get_next_page(limit)

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
    helper.clear()
    print('How would you like to sort?\n')

    #Prints all types of pets currently available
    limit = 0
    for animal in myShelter.animal_types:
        limit = limit + 1
        print('[{}]{}'.format(limit, animal))

    animal = helper.get_next_page(limit)

    helper.clear()
    print('Currently Available [{}]\n'.format(myShelter.animal_types[animal-1]))
    print('What would you like to do? \n[1]Schedule a Visit \n[2]Adopt a Pet \n[3]View Another Category \n[4]View All Pets \n[5]Home')

    limit = 5
    action = helper.get_next_page(limit)

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
    print('Please enter the pet ID you wish to adopt. [0 to exit]')

    action = helper.get_input_ID(myShelter.pet_directory)

    if action == 0:
        page_home()
    else:
        print('Thank you for adopting [{}], they can''t wait to see you!'.format(action))
        time.sleep(3)
        page_home()

#Page to schedule a visit
def page_pets_visit():
    print('Please enter the pet ID you wish to visit. [0 to exit]')

    action = helper.get_input_ID(myShelter.pet_directory)

    if action == 0:
        page_home()
    else:
        print('Thank you for scheduling a visit with [{}], we{}ll see you soon!'.format(action, "'"))
        time.sleep(3)
        page_home()

#============================================================================================================================

#The Factory
def createPet():

    #Gets info that is required for all pets
    pet_info = helper.get_input_pet(myShelter.animal_types)

    #Get info that is specific to each animal
    if pet_info[0].lower() == 'dog':

        isTrained = get_info_dog(pet_info[2])

        #Increment ID counter before creating pet to get unique ID
        myShelter.increment_ID()
        myShelter.pet_directory.append(animals.Dog(pet_info[1], pet_info[2], pet_info[3], pet_info[4], pet_info[5], myShelter.get_id(), isTrained))

    elif pet_info[0].lower() == 'cat':
        lifestyle = get_info_cat(pet_info[2])
        myShelter.increment_ID()
        myShelter.pet_directory.append(animals.Cat(pet_info[1], pet_info[2], pet_info[3], pet_info[4], pet_info[5], myShelter.get_id(), lifestyle))

def get_info_dog(pet_name):
    while True:
        isTrained = input('\nIs {} house trained? [Y][N]: '.format(pet_name))
        if isTrained.lower() not in ['y', 'n', 'yes', 'no']:
            print('Please enter yes or no.')
            continue
        else:
            return isTrained

def get_info_cat(pet_name):
    while True:
        lifestyle = input('\nDoes {} enjoy being [indoors], [outdoors], or [both]? '.format(pet_name))
        if lifestyle.lower() not in ['indoors', 'outdoors', 'both']:
            print('Please enter indoors, outdoors, or both.')
            continue
        else:
            return lifestyle
#=========================================================================================================

class Shelter:
    def __init__(self):
        self.animal_types = ['dog', 'cat', 'bird', 'rabbit', 'reptile']
        self.pet_directory = []
        self.id_counter = 0

    def get_id(self):
        return self.id_counter

    def print_Pets(self):
        for pet in self.pet_directory:
            helper.print_pet(pet)

    def increment_ID(self):
        self.id_counter = self.id_counter + 1

#========================================================================================================================================
#Testing

myShelter = Shelter()

myShelter.increment_ID()
myDog = animals.Dog('German Shepard', 'Fido', 'M', 5, 40, myShelter.get_id(), 'Y')
myShelter.pet_directory.append(myDog)

myShelter.increment_ID()
myCat = animals.Cat('Mixed', 'Fluffy', 'F', 8, 5, myShelter.get_id(), 'Inside')
myShelter.pet_directory.append(myCat)

myShelter.print_Pets()

#=======================================================================================================================================
def main():

    while True:
        page_home()
        break

    print('Thanks for stopping by!')

if __name__== "__main__":
    main()
