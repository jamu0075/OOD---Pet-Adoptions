#!/usr/bin/env python3

from abc import ABC, abstractmethod

class PetInterface(ABC):

    @abstractmethod
    def get_Animal(self):
        """Return the animal's type: str
        """
        pass

    @abstractmethod
    def get_Species(self):
        """Return the animal's species: str
        """
        pass

    @abstractmethod
    def get_Name(self):
        """Return the animal's name: str
        """
        pass

    @abstractmethod
    def get_Gender(self):
        """Return the animal's gender: str(M/F)
        """
        pass

    @abstractmethod
    def get_Age(self):
        """Return the animal's age: int
        """
        pass

    @abstractmethod
    def get_Weight(self):
        """Return the animal's weight: float
        """
        pass

    @abstractmethod
    def get_ID(self):
        """Return the animal's ID: int
        """
        pass

    @abstractmethod
    def get_Status(self):
        """Return the animal's status: str(Available, On-Hold, or Adopted)
        """
        pass

    @abstractmethod
    def update_status(self, status):
        """Updates the animal's status.

        Args:
            status: str(Available, On-Hold, or Adopted)
        """
        pass

class Dog(PetInterface):

    def __init__(self, species, name, gender, age, weight, id, isTrained):
        """Information required to initialize a Dog. Initialize animal to 'Dog' and status to 'Available'

            Args:
                species(str): Breed of Dog\n
                name(str): Name of Dog\n
                gender(str): Gender of Dog(M/F)\n
                age(int): Age of Dog\n
                weight(float): Weight of Dog\n
                id(int): Unique animal ID of Dog\n
                isTrained(bool): Whether or not the Dog is house trained(True/False)
        """
        self.animal = 'Dog'
        self.species = species
        self.name = name
        self.gender = gender
        self.age = age
        self.weight = weight
        self.isTrained = isTrained
        self.status = 'Available'
        self.id = id

    def get_Animal(self):
        return self.animal

    def get_Name(self):
        return self.name

    def get_Species(self):
        return self.species

    def get_Age(self):
        return self.age

    def get_Weight(self):
        return self.weight

    def get_Gender(self):
        return self.gender

    def get_ID(self):
        return self.id

    def get_Status(self):
        return self.status

    def get_IsTrained(self):
        """Return the animal's house trained status: bool
        """
        return self.isTrained

    def update_status(self, status):
        self.status = status

class Cat(PetInterface):

    def __init__(self, species, name, gender, age, weight, id, lifestyle):
        """Information required to initialize a Cat. Initialize animal to 'Cat' and status to 'Available'

            Args:
                species: Breed of Cat\n
                name: Name of Cat\n
                gender: Gender of Cat\n
                age: Age of Cat\n
                weight: Weight of Cat\n
                id: Unique animal ID of Cat\n
                lifestyle: Whether the Cat lives indoors, outdoors, or both
        """
        self.animal = 'Cat'
        self.species = species
        self.name = name
        self.gender = gender
        self.age = age
        self.weight = weight
        self.lifestyle = lifestyle
        self.status = 'Available'
        self.id = id

    def get_Animal(self):
        return self.animal

    def get_Name(self):
        return self.name

    def get_Species(self):
        return self.species

    def get_Age(self):
        return self.age

    def get_Weight(self):
        return self.weight

    def get_Gender(self):
        return self.gender

    def get_ID(self):
        return self.id

    def get_Status(self):
        return self.status

    def get_Lifestyle(self):
        """Return the animal's preferred lifestyle(indoors, outdoors, or both)
        """
        return self.lifestyle

    def update_status(self, status):
        self.status = status

class Bird(PetInterface):

    def __init__(self, species, name, gender, age, weight, id, lifestyle):
        """Information required to initialize a Bird. Initialize animal to 'Bird' and status to 'Available'

            Args:
                species: Species of Bird\n
                name: Name of Bird\n
                gender: Gender of Bird\n
                age: Age of Bird\n
                weight: Weight of Bird\n
                id: Unique animal ID of Bird\n
                lifestyle: Whether the Bird lives caged, uncaged, or both
        """
        self.animal = 'Bird'
        self.species = species
        self.name = name
        self.gender = gender
        self.age = age
        self.weight = weight
        self.lifestyle = lifestyle
        self.status = 'Available'
        self.id = id

    def get_Animal(self):
        return self.animal

    def get_Name(self):
        return self.name

    def get_Species(self):
        return self.species

    def get_Age(self):
        return self.age

    def get_Weight(self):
        return self.weight

    def get_Gender(self):
        return self.gender

    def get_ID(self):
        return self.id

    def get_Status(self):
        return self.status

    def get_Lifestyle(self):
        """Return the animal's preferred lifestyle(caged, uncaged, or both)
        """
        return self.lifestyle

    def update_status(self, status):
        self.status = status

class Reptile(PetInterface):

    def __init__(self, species, name, gender, age, weight, id, temperature):
        """Information required to initialize a Reptile. Initialize animal to 'Reptile' and status to 'Available'

            Args:
                species: Species of Reptile\n
                name: Name of Reptile\n
                gender: Gender of Reptile\n
                age: Age of Reptile\n
                weight: Weight of Reptile\n
                id: Unique animal ID of Reptile\n
                temperature: The Reptile's preferred temperature
        """
        self.animal = 'Reptile'
        self.species = species
        self.name = name
        self.gender = gender
        self.age = age
        self.weight = weight
        self.temperature = temperature
        self.status = 'Available'
        self.id = id

    def get_Animal(self):
        return self.animal

    def get_Name(self):
        return self.name

    def get_Species(self):
        return self.species

    def get_Age(self):
        return self.age

    def get_Weight(self):
        return self.weight

    def get_Gender(self):
        return self.gender

    def get_ID(self):
        return self.id

    def get_Status(self):
        return self.status

    def get_Temperature(self):
        """Return the animal's preferred temperature
        """
        return self.temperature

    def update_status(self, status):
        self.status = status

class Rabbit(PetInterface):

    def __init__(self, species, name, gender, age, weight, id):
        """Information required to initialize a Rabbit. Initialize animal to 'Dog' and status to 'Available'

            Args:
                species: Breed of Rabbit\n
                name: Name of Rabbit\n
                gender: Gender of Rabbit\n
                age: Age of Rabbit\n
                weight: Weight of Rabbit\n
                id: Unique animal ID of Rabbit\n
        """
        self.animal = 'Rabbit'
        self.species = species
        self.name = name
        self.gender = gender
        self.age = age
        self.weight = weight
        self.status = 'Available'
        self.id = id

    def get_Animal(self):
        return self.animal

    def get_Name(self):
        return self.name

    def get_Species(self):
        return self.species

    def get_Age(self):
        return self.age

    def get_Weight(self):
        return self.weight

    def get_Gender(self):
        return self.gender

    def get_ID(self):
        return self.id

    def get_Status(self):
        return self.status

    def update_status(self, status):
        self.status = status
