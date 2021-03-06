#!/usr/bin/env python3

import pages
import animals
import helper

#================================================================================================================================================
class PetFactory:
    """Factory Design Pattern that Creates Pet objects based on user inputted data

            Return Type: Pet
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

    def acceptPet(shelter):
        """Move a Pet from the drop off directory and add to the pet directory

                Args:
                    shelter(Shelter): shelter currently being managed
        """
        print('Please enter the ID of the Pet you wish to accept.')
        id = helper.get_input_ID(shelter.pet_drop_directory)
        shelter.add_Pet(shelter.get_Pet(id, shelter.pet_drop_directory), shelter.pet_directory)
        shelter.remove_Pet(id, shelter.pet_drop_directory)
        print('Pet {} has been accepted to the pet directory.'.format(id))
        time.sleep(3)
        return

    def declinePet(shelter):
        """Remove a Pet from the drop off directory

                Args:
                    shelter(Shelter): shelter currently being managed
        """
        print('Please enter the ID of the Pet you wish to decline.')
        id = helper.get_input_ID(shelter.pet_drop_directory)
        shelter.remove_Pet(id, shelter.pet_drop_directory)
        print('Pet {} has been declined.'.format(id))
        time.sleep(3)
        return

#================================================================================================================================================
class Customer:
    """An object that can update a Pet's status or dropoff a Pet
    """

    def petDropoff(shelter):
        """Add a Pet to the Shelter's drop off directory for admin approval

                Args:
                    shelter(Shelter): current shelter being managed
        """
        helper.clear()
        print('Please enter the requested information:')
        shelter.add_Pet(myFactory.createPet(shelter), shelter.pet_drop_directory)
        print('Thank you for your submission!')
        time.sleep(3)
        return

    def petAdopt(shelter):
        """Adopt a pet(Set status to Adopted). User inputs Pet ID to update

                Args:
                    shelter(Shelter): current shelter being managed
        """
        print('Please enter the pet ID you wish to adopt. [0 to exit]')

        id = helper.get_input_ID(shelter.pet_directory)

        if id == 0:
            return(0)
        else:
            print('Thank you for adopting {}, they can''t wait to see you!'.format((shelter.get_Pet(id, shelter.pet_directory)).name))
            shelter.update_Pet_Status(id, 'Adopted')
            time.sleep(3)
            return

    def petVisit(shelter):
        """Schedule a visit with a Pet(Set status to On-Hold). User inputs Pet ID to update

                Args:
                    shelter(Shelter): current shelter being managed
        """
        print('Please enter the pet ID you wish to visit. [0 to exit]')

        id = helper.get_input_ID(shelter.pet_directory)

        if id == 0:
            return(0)
        else:
            print('Thank you for scheduling a visit with {}, we{}ll see you soon!'.format((shelter.get_Pet(id, shelter.pet_directory)).name, "'"))
            shelter.update_Pet_Status(id, 'On Hold')
            time.sleep(3)
            return
            
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

    def add_Pet(self, pet, directory):
        """Append a Pet to the Shelter's Pet Directory

            Args:
                pet(Pet): Pet object to add to the shelter
                directory(list): Directory you wish to add a pet to
        """
        directory.append(pet)

    def remove_Pet(self, id, directory):
        """Remove a pet from a directory

            Args:
                id(int): The id of the pet you wish to remove
                directory(list): The directory you wish to remove the pet from
        """
        for i, pet in enumerate(directory):
            if pet.id == id:
                del directory[i]
                break


    def get_Pet(self, ID, directory):
        """Get a Pet with the unique ID

            Args:
                ID(int): unique ID of a Pet object
                directory(list): the directory you wish to retrieve a Pet from
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
    shelter.add_Pet(animals.Dog('German Shepard', 'Fido', 'M', 5, 40, shelter.get_ID(), True), shelter.pet_directory)

    shelter.increment_ID()
    shelter.add_Pet(animals.Dog('Golden Retriever', 'Goldy', 'F', 6, 53, shelter.get_ID(), True), shelter.pet_directory)
    shelter.update_Pet_Status(2, 'Adopted')

    shelter.increment_ID()
    shelter.add_Pet(animals.Cat('Mixed', 'Fluffy', 'F', 8, 5, shelter.get_ID(), 'Indoors'), shelter.pet_directory)

    shelter.increment_ID()
    shelter.add_Pet(animals.Bird('Parrot', 'Chirps', 'M', 3, 1.3, shelter.get_ID(), 'Both'), shelter.pet_directory)

    shelter.increment_ID()
    shelter.add_Pet(animals.Cat('Spinx', 'Mushu', 'F', 2, 6, shelter.get_ID(), 'Indoors'), shelter.pet_directory)
    shelter.update_Pet_Status(5, 'On-Hold')

    shelter.increment_ID()
    shelter.add_Pet(animals.Reptile('Bearded Dragon', 'Toasty', 'Unknown', 4, 2.6, shelter.get_ID(), 92), shelter.pet_directory)

    shelter.increment_ID()
    shelter.add_Pet(animals.Rabbit('Unknown', 'Hops', 'F', 1, 3, shelter.get_ID()), shelter.pet_directory)

    shelter.increment_ID()
    shelter.add_Pet(animals.Dog('Unknown', 'Ruff', 'M', 3, 30, shelter.get_ID(), False), shelter.pet_drop_directory)

    shelter.increment_ID()
    shelter.add_Pet(animals.Bird('Parrot', 'Squeks', 'F', 2, 2, shelter.get_ID(), 'Caged'), shelter.pet_directory)
    shelter.update_Pet_Status(9, 'On-Hold')

    shelter.admin_directory.append(Admin('Jacob', 1))

#================================================================================================================================================

def main():
    myShelter = Shelter()
    defaultShelter(myShelter)
    pages.page_home(myShelter)
    print('Thanks for stopping by!')

if __name__== "__main__":
    main()
