#!/usr/bin/python3

from abc import ABC

class Animal(ABC):
    """Abstract base class representing an animal."""

    def sound(self):
        """Abstract method to be implemented by subclasses.
        
        Returns:
            str: The sound made by the animal.
        """
        pass

class Dog(Animal):
    """Class representing a dog."""

    def sound(self):
        """Returns the sound made by a dog.
        
        Returns:
            str: The sound "Bark".
        """
        return "Bark"

class Cat(Animal):
    """Class representing a cat."""

    def sound(self):
        """Returns the sound made by a cat.
        
        Returns:
            str: The sound "Meow".
        """
        return "Meow"
