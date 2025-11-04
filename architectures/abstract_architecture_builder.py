"""Construction of Architecture

This script defines the AbstractArchitectureBuilder class, a template to build/connect trainable components.    

"""
from abc import ABC, abstractmethod

class AbstractArchitectureBuilder(ABC):
    """This class builds the system architecture.
    
    Creates trainable/non-trainable components.
    Connects components.

    """ 

    @abstractmethod
    def create_component(self, blueprint):
        """ Function to create a component
            Args:
                blueprint: Dictionary of elements describing the component
            Returns: 
                Trainable or non-trainable object
        """  
        return
    
    @abstractmethod
    def connect_components(self):
        """ Function to connect multiple components

        """  
        return
    
