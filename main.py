#!/usr/bin/env python3

import pages
import animals
import helper

#================================================================================================================================================
class PetFactory:
    """Factory Design Pattern that Creates Pet objects based on user inputted data
    """
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
class Admin:
    """An object that has access to admin capabilities like updating Pet information or accepting/declining new pet drop-offs
    """

    def __init__(self, name,  ID):
        self.id = ID
        self.name = name

    def accept_pet(self, shelter, pet):
        shelter.pet_directory.append(pet)
#================================================================================================================================================
class Shelter:
    """An object that keeps track of all the animals within a shelter. Holds a list of accepted animal types
        along with a list of Pet objects to manage. The ID counter provides a unique ID for all new Pets. The
        admin directory keeps track of all admin ID's that are in the shelter. The pet_drop directory keeps track
        of all drop-off requests to be evaluated by an admin.
    """
    def __init__(self):
        self.animal_types = ['dog', 'cat', 'bird', 'rabbit', 'reptile']
        self.pet_directory = []
        self.pet_drop_directory = []
        self.admin_directory = []
        self.id_counter = 0

    def get_ID(self):
        """Returns current ID counter: int
        """
        return self.id_counter

    def print_Pets(self):
        """Prints all pets in the Pet Directory using helper.print_pet()
        """
        for pet in self.pet_directory:
            helper.print_pet(pet)

    def print_Pets_Available(self):
        """Print all pets in the Pet Directory that have a status of 'Available' using helper.print_pet()
        """
        for pet in self.pet_directory:
            if pet.status == 'Available':
                helper.print_pet(pet)

    def print_Pets_Sorted(self, animal):
        """Print all Pets that are an inputted animal type.

            Args:
                animal(str): animal type to sort by
        """
        for pet in self.pet_directory:
            if pet.animal.lower() == animal:
                helper.print_pet(pet)

    def increment_ID(self):
        """Increment the ID to provide a unique ID
        """
        self.id_counter = self.id_counter + 1

    def add_Pet(self, pet):
        """Append a Pet to the Shelter's Pet Directory

            Args:
                pet(Pet): Pet object to add to the shelter
        """
        self.pet_directory.append(pet)

    def drop_off(self, pet):
        """Append a Pet to the Shelter's drop off directory

            Args:
                pet(Pet): Pet object requesting to be added
        """
        self.pet_drop_directory.append(pet)

    def get_Pet(self, ID, directory):
        """Get a Pet with the unique ID

            Args:
                ID(int): unique ID of a Pet object
            Return Type: Pet
        """
        for pet in directory:
            if pet.id == ID:
                return pet

    def update_Pet_Status(self, ID, status):
        """Update a Pet's status

            Args:
                ID(int): Pet ID to update
                status(str): new status for Pet
        """
        for pet in self.pet_directory:
            if pet.id == ID:
                pet.status = status
                break

#================================================================================================================================================
#Method that creates Pets for a default test shelter
def defaultShelter(shelter):
    """This is a default Shelter for the purposes of a demo
    """

    shelter.increment_ID()
    shelter.add_Pet(animals.Dog('German Shepard', 'Fido', 'M', 5, 40, shelter.get_ID(), True))

    shelter.increment_ID()
    shelter.add_Pet(animals.Dog('Golden Retriever', 'Goldy', 'F', 6, 53, shelter.get_ID(), True))
    shelter.update_Pet_Status(2, 'Adopted')

    shelter.increment_ID()
    shelter.add_Pet(animals.Cat('Mixed', 'Fluffy', 'F', 8, 5, shelter.get_ID(), 'Indoors'))

    shelter.increment_ID()
    shelter.add_Pet(animals.Bird('Parrot', 'Chirps', 'M', 3, 1.3, shelter.get_ID(), 'Both'))

    shelter.increment_ID()
    shelter.add_Pet(animals.Cat('Spinx', 'Mushu', 'F', 2, 6, shelter.get_ID(), 'Indoors'))
    shelter.update_Pet_Status(5, 'On-Hold')

    shelter.increment_ID()
    shelter.add_Pet(animals.Reptile('Bearded Dragon', 'Toasty', 'Unknown', 4, 2.6, shelter.get_ID(), 92))

    shelter.increment_ID()
    shelter.add_Pet(animals.Rabbit('Unknown', 'Hops', 'F', 1, 3, shelter.get_ID()))


    shelter.admin_directory.append(Admin('Jacob', 1))

#================================================================================================================================================

def main():
    myShelter = Shelter()
    defaultShelter(myShelter)
    pages.page_home(myShelter)
    print('Thanks for stopping by!')

if __name__== "__main__":
    main()
