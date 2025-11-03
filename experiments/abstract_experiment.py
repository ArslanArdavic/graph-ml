"""Implementation of ML pipeline. 

This script defines the abstract Experiment class and creates an environment to train/evaluate/report models with monitorization.   

"""
from abc import ABC, abstractmethod

class AbstractExperiment(ABC):   
    """This class creates experiment environment.

    Prepares logging.
    Loads data.
    Connects trainable and non-trainable modules to construct the system architecture.
    Prepares training pipeline.
    Performs training.
    Reports the test results.

    Attributes:
        attr: None
    """ 

    @abstractmethod
    def prepare_interaction(self):
        """ Function to instantiate parser, logger and Neptune run.

            Returns: 
                Arguments parsed 
                Logger 
                Neptune run
        """   
        args, logger, run = None, None, None    
        return args, logger, run
    
    @abstractmethod
    def retrieve_data(self):
        """ Function to retrive dataloaders or the raw data for different splits or datasets.

            Returns: 
                Collection of dataloaders/datasets
        """  
        return

    @abstractmethod
    def construct_framework_architecture(self):
        """ Function to create and connect components such as trainable models.

            Returns: 
                Framework consists of trainable and non-trainable modules
        """  
        framework = None
        return framework

    @abstractmethod
    def construct_training_pipeline(self):
        """ Function to define objectives, optimizers, training loops and train/validation metrics over an existing framework. 

            Returns: 
                Trainable framework along with optimizer(s) to solve task(s) designated over dataset(s).   
        """
        training_pipeline = None
        return training_pipeline
    
    @abstractmethod
    def execute_training(self):
        """ Function to train the system.

            Returns: 
                Trained framework.  
        """
        return 

    @abstractmethod
    def construct_test_reporter(self):
        """ Function to test the system.

            Returns: 
                Report about the framework performance on multiple metrics.   
        """
        return 
    
    @abstractmethod
    def main(self):
        """ Function to implement class functionalities in a single entry-point.

            Performs every action to construct an experiment environment.

            Args:
                arg: A default argument

            Returns: 
                Object instances involved in the environment. 
        """        
        args, logger, neptune_run = self.prepare_interaction()
        data         = self.retrieve_data()                     # Collection of dataloaders/datasets
        framework    = self.construct_framework_architecture()  # Trainable system.
        return

