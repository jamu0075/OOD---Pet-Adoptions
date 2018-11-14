#!/usr/bin/env python3
import pages
import animals
import helper

#============================================================================================================================

#The Factory returns a pet
def createPet(shelter):

    #Gets info that is required for all pets
    pet_info = helper.get_input_pet(shelter.animal_types)

    #Get info that is specific to each animal
    if pet_info[0].lower() == 'dog':

        isTrained = get_info_dog(pet_info[2])

        #Increment ID counter before creating pet to get unique ID
        shelter.increment_ID()
        return(animals.Dog(pet_info[1], pet_info[2], pet_info[3], pet_info[4], pet_info[5], shelter.get_id(), isTrained))

    elif pet_info[0].lower() == 'cat':
        lifestyle = get_info_cat(pet_info[2])
        shelter.increment_ID()
        return(animals.Cat(pet_info[1], pet_info[2], pet_info[3], pet_info[4], pet_info[5], shelter.get_id(), lifestyle))

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

    def add_Pet(self, pet):
        self.pet_directory.append(pet)

    #def remove_Pet(self, id):
    #    if any(id == pet.id for pet in self.pet_directory):
    #        self.pet_directory.remove(pet)

#========================================================================================================================================
#Testing

#myShelter.increment_ID()
#myDog = animals.Dog('German Shepard', 'Fido', 'M', 5, 40, myShelter.get_id(), 'Y')
#myShelter.pet_directory.append(myDog)

#myShelter.increment_ID()
#myCat = animals.Cat('Mixed', 'Fluffy', 'F', 8, 5, myShelter.get_id(), 'Inside')
#myShelter.pet_directory.append(myCat)

#myShelter.print_Pets()

#=======================================================================================================================================
def main():
    myShelter = Shelter()
    pages.page_home(myShelter)
    print('Thanks for stopping by!')

if __name__== "__main__":
    main()
