#!/usr/bin/env python3
from os import system, name
import animals

#Helper Functions
#================================================================================================================================================
def clear():
    """Clears the screen.
    """
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

#================================================================================================================================================
def get_next_page(limit):
    """Get next page from user input. Ensure the input is within the appropriate range.

        Args:
            limit(int): Max number of user options
    """
    while True:
        try:
            action = int(input('\nInput: '))
        except:
            print('Please enter a number.')
            continue
        else:
            if action < 1 or action > limit:
                print('Please enter a valid number.')
                continue
            else:
                return action

#================================================================================================================================================
def get_input_ID(pet_directory):
    """ Get a Pet's ID from the user. Ensure the ID is in the Shelter's Pet Directory. 0 Exits.

        Args:
            pet_directory(list of Pet): All Pet objects currently in Shelter
    """
    while True:
        try:
            id = int(input('\nInput: '))
        except:
            print('Please enter a number.')
            continue
        else:
            if id == 0:
                return id
            elif any(id == pet.id for pet in pet_directory):
                return id
            else:
                print('Please enter a valid pet ID.')
                continue

#================================================================================================================================================
def get_input_pet(accepted_animals):
    """Collects all required info for a new Pet from user.

        Args:
            accepted_animals(list of str): All animal types accepted by Shelter

        Return Type: list
    """
    animal = get_input_animal(accepted_animals)
    animal_species = input('\nAnimal Breed/Species: ')
    name = input('\nName: ')
    gender = get_input_gender()
    age = get_input_age()
    weight = get_input_weight()

    if animal.lower() == 'dog':
        isTrained = get_input_dog(name)
        return(animal, animal_species, name, gender, age, weight, isTrained)
    elif animal.lower() == 'cat':
        lifestyle = get_input_cat(name)
        return(animal, animal_species, name, gender, age, weight, lifestyle)
    elif animal.lower() == 'bird':
        lifestyle = get_input_bird(name)
        return(animal, animal_species, name, gender, age, weight, lifestyle)
    elif animal.lower() == 'reptile':
        temperature = get_input_reptile(name)
        return(animal, animal_species, name, gender, age, weight, temperature)
    else:
        return(animal, animal_species, name, gender, age, weight)


def get_input_animal(accepted_animals):
    """Collect animal type from user. Compare input with accepted_animals

        Args:
            accepted_animals(list of str): All animal types accepted by Shelter

        Return Type: str
    """
    while True:
        animal = input('\nAnimal type(Dog, Cat, Bird, Rabbit, Reptile): ')
        if animal.lower() not in accepted_animals:
            print('I''m sorry but we are not accepting that type of animal at this time.')
            continue
        else:
            return animal


def get_input_gender():
    """Collect animal gender from user.

        Return Type: str
    """
    while True:
        gender = input('\nGender(M/F/Unknown): ')
        if gender.lower() not in ['m', 'f', 'unknown']:
            print('Please enter a valid gender.')
            continue
        else:
            return gender


def get_input_age():
    """Collect age from user.

        Return Type: int
    """
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
            return age


def get_input_weight():
    """Collect weight from user.

        Return Type: int
    """
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
            return weight


def get_input_dog(pet_name):
    """Collect unique Dog info(House trained status) from user.

        Return Type: bool
    """
    while True:
        isTrained = input('\nIs {} house trained? [Y][N]: '.format(pet_name))
        if isTrained.lower() not in ['y', 'n', 'yes', 'no']:
            print('Please enter yes or no.')
            continue
        else:
            if isTrained.lower() in ['y', 'yes']:
                return True
            else:
                return False

#Get unique cat info from user
def get_input_cat(pet_name):
    """Collect unique Cat info(lifestyle) from user.

        Return Type: str
    """
    while True:
        lifestyle = input('\nDoes {} live [indoors], [outdoors], or [both]? '.format(pet_name))
        if lifestyle.lower() not in ['indoors', 'outdoors', 'both']:
            print('Please enter indoors, outdoors, or both.')
            continue
        else:
            return lifestyle

#Get unique bird info from user
def get_input_bird(pet_name):
    """Collect unique Bird info(lifestyle) from user.

        Return Type: str
    """
    while True:
        lifestyle = input('\nDoes {} live [caged], [uncaged], or [both] '.format(pet_name))
        if lifestyle.lower() not in ['caged', 'uncaged', 'both']:
            print('Please enter caged, uncaged, or both.')
            continue
        else:
            return lifestyle


def get_input_reptile(pet_name):
    """Collect unique Reptile info(temperature) from user.

        Return Type: int
    """
    while True:
        try:
            temperature = float(input('\nWhat temperature does {} live in? '.format(pet_name)))
        except:
            print('Please enter a number.')
            continue
        else:
            return temperature

#================================================================================================================================================
def print_pet(pet):
    """Print all info on a Pet.

        Args:
            pet(Pet): The Pet you want to be printed
    """
    if type(pet) == animals.Dog:
        print('ID: {} | Animal: {} | Species: {} | Name: {} | Gender: {} | Age: {} | Weight: {} | House Trained: {} | Status: {}'.format(pet.get_ID(), pet.get_Animal(), pet.get_Species(), pet.get_Name(), pet.get_Gender(), pet.get_Age(), pet.get_Weight(), pet.get_IsTrained(), pet.get_Status()))

    elif type(pet) == animals.Cat:
        print('ID: {} | Animal: {} | Species: {} | Name: {} | Gender: {} | Age: {} | Weight: {} | Indoor/Outdoor: {} | Status: {}'.format(pet.get_ID(), pet.get_Animal(), pet.get_Species(), pet.get_Name(), pet.get_Gender(), pet.get_Age(), pet.get_Weight(), pet.get_Lifestyle(), pet.get_Status()))

    elif type(pet) == animals.Bird:
        print('ID: {} | Animal: {} | Species: {} | Name: {} | Gender: {} | Age: {} | Weight: {} | Caged/Uncaged: {} | Status: {}'.format(pet.get_ID(), pet.get_Animal(), pet.get_Species(), pet.get_Name(), pet.get_Gender(), pet.get_Age(), pet.get_Weight(), pet.get_Lifestyle(), pet.get_Status()))

    elif type(pet) == animals.Reptile:
        print('ID: {} | Animal: {} | Species: {} | Name: {} | Gender: {} | Age: {} | Weight: {} | Temperature: {} | Status: {}'.format(pet.get_ID(), pet.get_Animal(), pet.get_Species(), pet.get_Name(), pet.get_Gender(), pet.get_Age(), pet.get_Weight(), pet.get_Temperature(), pet.get_Status()))

    elif type(pet) == animals.Rabbit:
        print('ID: {} | Animal: {} | Species: {} | Name: {} | Gender: {} | Age: {} | Weight: {} | Status: {}'.format(pet.get_ID(), pet.get_Animal(), pet.get_Species(), pet.get_Name(), pet.get_Gender(), pet.get_Age(), pet.get_Weight(), pet.get_Status()))
