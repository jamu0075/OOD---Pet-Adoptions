#!/usr/bin/env python3
from abc import ABC, abstractmethod

class PetInterface(ABC):

    @abstractmethod
    def get_Animal(self):
        pass

    @abstractmethod
    def get_Species(self):
        pass

    @abstractmethod
    def get_Name(self):
        pass

    @abstractmethod
    def get_Gender(self):
        pass

    @abstractmethod
    def get_Age(self):
        pass

    @abstractmethod
    def get_Weight(self):
        pass

    @abstractmethod
    def get_ID(self):
        pass

    @abstractmethod
    def get_Status(self):
        pass

class Dog(PetInterface):

    def __init__(self, species, name, gender, age, weight, id, isTrained):
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
        return self.isTrained

class Cat(PetInterface):

    def __init__(self, species, name, gender, age, weight, id, lifestyle):
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
        return self.lifestyle

class Bird(PetInterface):

    def __init__(self, species, name, gender, age, weight, id, lifestyle):

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
        return self.lifestyle
