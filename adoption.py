#!/usr/bin/env python3
from os import system, name
import time
import animals

#================================================================================================================================================
#All the UI pages for the program
#Handles all the navigation within each page individually

#Homepage for the program
def page_home():
    clear()
    print('Welcome to the Adoption Center! What would you like to do? \n[1]View Available Pets \n[2]Pet Drop-off \n[3]Admin Login \n[4]Quit')

    action = get_input(4, False)

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
    clear()
    print('Please enter the requested information:')
    createPet()
    print('Thank you for your submission!')
    time.sleep(3)
    page_home()

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

#Page that displays all available pets
def page_pets_all():
    clear()
    print('ALL PETS LISTED HERE')
    myShelter.print_Pets()
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
    print('Please enter the pet ID you wish to adopt. [0 to exit]')

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
        print('Thank you for scheduling a visit with [{}], we{}ll see you soon!'.format(action, "'"))
        time.sleep(3)
        page_home()

#===================================================================================================================================
#Helper Functions

#Clears the screen
def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

#Handles inputed information regarding page navigation and pet adoption/visits
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
                elif action not in myShelter.pet_directory:
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

#Helper function that handles inputed information regarding pet information
def get_input_pets():
    while True:
        animal = input('\nAnimal type(Dog, Cat, Bird, Rabbit, Reptile): ')
        if animal.lower() not in myShelter.animal_types:
            print('I''m sorry but we are not accepting that type of animal at this time.')
            continue
        else:
            break

    animal_species = input('\nAnimal Breed/Species: ')
    name = input('\nName: ')

    while True:
        gender = input('\nGender(M/F/Unknown): ')
        if gender.lower() not in ['m', 'f', 'unknown']:
            print('Please enter a valid gender.')
            continue
        else:
            break

    while True:
        try:
            age = int(input('\nAge: '))
        except:
            print('Please enter a number.')
            continue
        else:
            if age < 0:
                print('Please enter a valid age.')
                continue
            break

    while True:
        try:
            weight = float(input('\nWeight: '))
        except:
            print('Please enter a number.')
            continue
        else:
            if weight <= 0:
                print('Please enter a valid weight.')
                continue
            break

    return(animal, animal_species, name, gender, age, weight)

#Prints all info on a given pet
def print_Pet(pet):
    if type(pet) == animals.Dog:
        print('ID: {} | Animal: {} | Species: {} | Name: {} | Gender: {} | Age: {} | Weight: {} | House Trained: {} | Status: {}'.format(pet.get_ID(), pet.get_Animal(), pet.get_Species(), pet.get_Name(), pet.get_Gender(), pet.get_Age(), pet.get_Weight(), pet.get_IsTrained(), pet.get_Status()))

    elif type(pet) == animals.Cat:
        print('ID: {} | Animal: {} | Species: {} | Name: {} | Gender: {} | Age: {} | Weight: {} | Lifestyle: {} | Status: {}'.format(pet.get_ID(), pet.get_Animal(), pet.get_Species(), pet.get_Name(), pet.get_Gender(), pet.get_Age(), pet.get_Weight(), pet.get_Lifestyle(), pet.get_Status()))

#============================================================================================================================

#The Factory
def createPet():

    #Gets info that is required for all pets
    pet_info = get_input_pets()

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
            print_Pet(pet)

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
