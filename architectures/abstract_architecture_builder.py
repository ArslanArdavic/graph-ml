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
    def reset(self):
        """ Function to create an empty architecture
            Returns: 
                Initial Architecture object
        """  
        return
    
    @abstractmethod
    def get_result(self):
        """ Function to get latest architecture configuration.
            Returns:
                Architecture object
        """  
        return
    
