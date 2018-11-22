.. Pet Adoptions documentation master file, created by
   sphinx-quickstart on Wed Nov 21 14:03:54 2018.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

******************************************
Welcome to Pet Adoptions's documentation!
******************************************

.. contents:: Table of Contents
   :depth: 3

Main Classes
============
Classes that are core to the functionality of the program.

Shelter
-------
A class that keeps track of all the animals within a shelter. Holds a list of accepted animal types along with a list of Pet objects to manage. The ID counter provides a unique ID for all new Pets.

*class* main. **Shelter**
    **add_Pet(Pet)**
        Append a Pet to the Shelter's Pet Directory

            Args:
                pet(Pet): Pet object to add to the shelter
    **get_ID()**
        Returns current ID counter: int
    **increment_ID()**
        Increment the ID to provide a unique ID
    **print_Pets()**
        Prints all pets in the Pet Directory using helper.print_pet()
    **print_Pets_Sorted(animal)**
        Print all Pets that are an inputted animal type.

            Args:
                animal(str): animal type to sort by
    **update_Pet_Status(ID, status)**
        Update a Pet's status

            Args:
                ID(int): Pet ID to update
                status(str): new status for Pet

Factory
-------
A class that creates Pet objects based off user inputted information

*class* main. **PetFactory**
   **createPet()**
       Factory Design Pattern that Creates the appropriate Pet object based on the animal type

Animal Classes
===============
All animal classes use the following interface:

.. currentmodule:: animals

Pet Interface
-------------
.. autoclass:: PetInterface
   :members:

Dog
---
.. autoclass:: Dog
   :members:

Cat
---
.. autoclass:: Cat
   :members:

Bird
----
.. autoclass:: Bird
   :members:

Reptile
-------
.. autoclass:: Reptile
   :members:

Rabbit
------
.. autoclass:: Rabbit
   :members:

-----------------------------------------------------------------

Helper Functions
=================
Helper functions that makeup the program functionality

.. currentmodule:: helper

.. automodule:: helper
   :members:

-----------------------------------------------------------------

Application Pages
=================
All the UI pages for the program. Pages handle the navigation between each page individually. **All pages require a Shelter object arg to manage**

.. automodule:: pages
   :members:
