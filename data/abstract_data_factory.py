"""Interface for a data retrieving class. 

This script defines the AbstractDataFactory.

"""

from abc import ABC, abstractmethod

class AbstractDataFactory(ABC):
    """This class provides an interface for DataFactory classes.

    Retrieves data for training.
    """
    @abstractmethod
    def load_dataset(self):
        """ Function to retrieve the data itself.

            Returns: 
                Data object instance
        """ 
        return 
    
    @abstractmethod
    def construct_data_loader(self):
        """ Function to construct the dataloader.

            Returns: 
                DataLoader object instance 
        """ 
        return