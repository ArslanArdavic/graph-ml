"""Base Experiment class

This script defines the Experiment class.   

Typical usage example:

  exp = Experiment()
  result = exp.main()
"""

import os
import argparse
import logging

from neptune.integrations.python_logger import NeptuneHandler
import neptune

from . import AbstractExperiment

class Experiment(AbstractExperiment):   
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
                Arguments parsed 
                Logger 
                Neptune run
        """   
        # Parse command-line arguments
        parser = argparse.ArgumentParser()
        parser.add_argument("--remote", type=bool, default=False)
        parser.add_argument("--monitor", type=bool, default=False)
        args = parser.parse_args()

        # Set up logging
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.INFO)

        # Initialize Neptune run, add handler and cmd args
        run = None
        if args.monitor:
            run = neptune.init_run(
                project="ALLab-Boun/graph-ml",
                api_token="eyJhcGlfYWRkcmVzcyI6Imh0dHBzOi8vYXBwLm5lcHR1bmUuYWkiLCJhcGlfdXJsIjoiaHR0cHM6Ly9hcHAubmVwdHVuZS5haSIsImFwaV9rZXkiOiJjYjlhZjMxMS1mZjgyLTQ4Y2YtYmY5ZC1mMjVjOWU2YmI4YWMifQ==",
                name="Simple Experiment",
                description="Simple Experiment",
                tags=["Experiment"],
            )

            # Set default logging information
            logger.addHandler(NeptuneHandler(run=run))
            run["cmd-args"] = args
            
            if args.remote:
                # Make sure these are non-empty strings
                job_id = os.environ.get("SLURM_ARRAY_JOB_ID") or os.environ.get("SLURM_JOB_ID") or "UNKNOWN"
                stdout_path = os.environ.get("SLURM_STDOUT_PATH") or f"slurm/log/greeting_{job_id}.out"
                stderr_path = os.environ.get("SLURM_STDERR_PATH") or f"slurm/log/greeting_{job_id}.err"

                # Log as a small namespace/dict (shows in metadata even if values are empty strings)
                run["slurm"] = {
                    "job_id": job_id,
                    "stdout_path": stdout_path,
                    "stderr_path": stderr_path,
                }

        logger.info(f"Initialized instance: {repr(self)}")
        
        return args, logger, run
    
    def construct_data_loaders(self):
        """ Function to retrive dataloaders for different splits or datasets.

            Returns: 
                Collection of dataloaders
        """  
        data_loaders = None
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
                arg: A default argument

            Returns: 
                Object instances involved in the environment. 
        """        
        args, logger, neptune_run = self.prepare_interaction()
        data_loaders = self.construct_data_loaders()            # Collection of dataloaders for different splits or datasets.
        framework    = self.construct_framework_architecture()  # Trainable system.
        return

if __name__ == "__main__":
  exp = Experiment()
  result = exp.main()