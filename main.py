#!/usr/bin/env python3
import pages
import animals
import helper

#================================================================================================================================================
#Factory that creates Pets
class PetFactory:
    def createPet(self, shelter):

        #Gets all required info from user
        pet_info = helper.get_input_pet(shelter.animal_types)

        #Create appropriate Pet class, increment ID before creating pet to get a unique ID
        if pet_info[0].lower() == 'dog':
            shelter.increment_ID()
            return(animals.Dog(pet_info[1], pet_info[2], pet_info[3], pet_info[4], pet_info[5], shelter.get_ID(), pet_info[6]))

        elif pet_info[0].lower() == 'cat':
            shelter.increment_ID()
            return(animals.Cat(pet_info[1], pet_info[2], pet_info[3], pet_info[4], pet_info[5], shelter.get_ID(), pet_info[6]))

        elif pet_info[0].lower() == 'bird':
            shelter.increment_ID()
            return(animals.Bird(pet_info[1], pet_info[2], pet_info[3], pet_info[4], pet_info[5], shelter.get_ID(), pet_info[6]))

        elif pet_info[0].lower() == 'reptile':
            shelter.increment_ID()
            return(animals.Reptile(pet_info[1], pet_info[2], pet_info[3], pet_info[4], pet_info[5], shelter.get_ID(), pet_info[6]))

        elif pet_info[0].lower() == 'rabbit':
            shelter.increment_ID()
            return(animals.Rabbit(pet_info[1], pet_info[2], pet_info[3], pet_info[4], pet_info[5], shelter.get_ID()))

#================================================================================================================================================
#Shelter that manages Pets
class Shelter:
    def __init__(self):
        self.animal_types = ['dog', 'cat', 'bird', 'rabbit', 'reptile']
        self.pet_directory = []
        self.id_counter = 0

    def get_ID(self):
        return self.id_counter

    def print_Pets(self):
        for pet in self.pet_directory:
            helper.print_pet(pet)

    def print_Pets_Sorted(self, animal):
        for pet in self.pet_directory:
            if pet.animal.lower() == animal:
                helper.print_pet(pet)

    def increment_ID(self):
        self.id_counter = self.id_counter + 1

    def add_Pet(self, pet):
        self.pet_directory.append(pet)

    #def remove_Pet(self, id):
    #    if any(id == pet.id for pet in self.pet_directory):
    #        self.pet_directory.remove(pet)

#================================================================================================================================================
#Method that creates Pets for a default test shelter
def defaultShelter(shelter):
    shelter.increment_ID()
    shelter.add_Pet(animals.Dog('German Shepard', 'Fido', 'M', 5, 40, shelter.get_ID(), 'Y'))

    shelter.increment_ID()
    shelter.add_Pet(animals.Cat('Mixed', 'Fluffy', 'F', 8, 5, shelter.get_ID(), 'Indoors'))

    shelter.increment_ID()
    shelter.add_Pet(animals.Bird('Parrot', 'Chirps', 'M', 3, 1.3, shelter.get_ID(), 'Both'))

    shelter.increment_ID()
    shelter.add_Pet(animals.Reptile('Bearded Dragon', 'Toasty', 'Unknown', 4, 2.6, shelter.get_ID(), 92))

    shelter.increment_ID()
    shelter.add_Pet(animals.Rabbit('Unknown', 'Hops', 'F', 1, 3, shelter.get_ID()))

#================================================================================================================================================

def main():
    myShelter = Shelter()
    defaultShelter(myShelter)
    pages.page_home(myShelter)
    print('Thanks for stopping by!')

if __name__== "__main__":
    main()
