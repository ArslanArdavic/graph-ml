"""Base Experiment class

This script defines the Experiment class.   

Typical usage example:

  exp = Experiment()
  result = exp.main()
"""

import os
import argparse
import logging
from overrides import override

from neptune.integrations.python_logger import NeptuneHandler
import neptune

from . import AbstractExperiment
from data import PlanetoidDataFactory

class Experiment(AbstractExperiment):   
    """This class creates experiment environment.

    Instantiates neptune logging.
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
    
    @override
    def prepare_interaction(self):
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
    
    @override
    def retrieve_data(self):
        data_factory = PlanetoidDataFactory(name="Cora")
        dataset      = data_factory.load_dataset()
        data         = dataset[0]
        self.logger.info(f"Loaded the dataset: {dataset}")
        return data

    @override
    def construct_framework_architecture(self):
        """ Function to create and connect components such as trainable models.

            Returns: 
                System consists of trainable and non-trainable modules
        """  
        framework = None
        return framework

    @override
    def construct_training_pipeline(self):
        training_pipeline = None
        return training_pipeline
    
    @override
    def execute_training(self):
        return 

    @override
    def construct_test_reporter(self):
        return 
    
    @override
    def main(self):     
        self.args, self.logger, self.neptune_run = self.prepare_interaction()
        data         = self.retrieve_data()                     # Collection of dataloaders/datasets
        framework    = self.construct_framework_architecture()  # Trainable system.
        return

if __name__ == "__main__":
  exp = Experiment()
  result = exp.main()