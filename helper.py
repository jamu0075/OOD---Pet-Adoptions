#!/usr/bin/env python3
from os import system, name
import animals

#Helper Functions

#Clears the screen
def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def get_next_page(limit):
    while True:
        try:
            action = int(input('\nInput: '))
        except:
            print('Please enter a number.')
            continue
        else:
            #Ensure input is within the limit
            if action < 1 or action > limit:
                print('Please enter a valid number.')
                continue
            else:
                return action

def get_input_ID(pet_directory):
    while True:
        try:
            id = int(input('\nInput: '))
        except:
            print('Please enter a number.')
            continue
        else:
            #Ensures the inputed ID is in the directory of pets
            if id == 0:
                return id
            elif any(id == pet.id for pet in pet_directory):
                return id
            else:
                print('Please enter a valid pet ID.')
                continue

#Gets all info required for pets in the shelter
def get_input_pet(accepted_animals):
    while True:
        animal = input('\nAnimal type(Dog, Cat, Bird, Rabbit, Reptile): ')
        if animal.lower() not in accepted_animals:
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

    #Get required unique info and return
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

#Get unique dog info from user
def get_input_dog(pet_name):
    while True:
        isTrained = input('\nIs {} house trained? [Y][N]: '.format(pet_name))
        if isTrained.lower() not in ['y', 'n', 'yes', 'no']:
            print('Please enter yes or no.')
            continue
        else:
            return isTrained

#Get unique cat info from user
def get_input_cat(pet_name):
    while True:
        lifestyle = input('\nDoes {} live [indoors], [outdoors], or [both]? '.format(pet_name))
        if lifestyle.lower() not in ['indoors', 'outdoors', 'both']:
            print('Please enter indoors, outdoors, or both.')
            continue
        else:
            return lifestyle

#Get unique bird info from user
def get_input_bird(pet_name):
    while True:
        lifestyle = input('\nDoes {} live [caged], [uncaged], or [both] '.format(pet_name))
        if lifestyle.lower() not in ['caged', 'uncaged', 'both']:
            print('Please enter caged, uncaged, or both.')
            continue
        else:
            return lifestyle

#Get unique reptile info from user
def get_input_reptile(pet_name):
    while True:
        try:
            temperature = float(input('\nWhat temperature does {} live in? '.format(pet_name)))
        except:
            print('Please enter a number.')
            continue
        else:
            return temperature

#Prints all info on a given pet
def print_pet(pet):
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
