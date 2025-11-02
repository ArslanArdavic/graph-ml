"""Implementation of ML pipeline. 

This script defines the Experiment class and creates an environment to train/evaluate/report models with monitorization.   

Typical usage example:

  exp = Experiment()
  result = exp.main()
"""
from data import DataLoader

class Experiment:   
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
    def __init__(self, attr=None):
        print(f"Initializing instance: {str(self)}")
        self.attr = attr

    def __repr__(self):
        items = ((k, v) for k, v in vars(self).items() if not k.startswith('_'))
        body = ", ".join(f"{k}={v!r}" for k, v in sorted(items))
        return f"{type(self).__name__}({body})"              
    
    def __str__(self):
        return "Experiment"
        
    def prepare_interaction(self):
        """ Function to instantiate parser, logger and Neptune run.

            Returns: 
                Argument parser 
                Logger 
                Neptune run
        """   
        parser, logger, neptune_run = None, None, None
        return parser, logger, neptune_run

    def construct_data_loaders(self):
        """ Function to retrive dataloaders for different splits or datasets.

            Returns: 
                Collection of dataloaders
        """  
        data_loaders = None
        DataLoader()
        return data_loaders

    def construct_framework_architecture(self):
        """ Function to create and connect components such as trainable models.

            Returns: 
                Framework consists of trainable and non-trainable modules
        """  
        framework = None
        return framework

    def construct_training_pipeline(self):
        """ Function to define objectives, optimizers, training loops and train/validation metrics over an existing framework. 

            Returns: 
                Trainable framework along with optimizer(s) to solve task(s) designated over dataset(s).   
        """
        training_pipeline = None
        return training_pipeline
    
    def execute_training(self):
        """ Function to train the system.

            Returns: 
                Trained framework.  
        """
        return 

    def construct_test_reporter(self):
        """ Function to test the system.

            Returns: 
                Report about the framework performance on multiple metrics.   
        """
        return 

    
    def main(self):
        """ Function to implement class functionalities in a single entry-point.

            Performs every action to construct an experiment environment.

            Args:
                arg: A defualt argument

            Returns: 
                Object instances involved in the environment. 
        """        
        parser, logger, neptune_run = self.prepare_interaction()
        data_loaders = self.construct_data_loaders()            # Collection of dataloaders for different splits or datasets.
        framework    = self.construct_framework_architecture()  # Trainable system.
        return

    
if __name__ == "__main__":
    exp = Experiment()
    exp.main()
