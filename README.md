# graph-ml
Machine Learning On Graphs

    .
    ├── exec                            # Executable files
    │   ├── greeting.py 
    ├── data                            # Data-related classes 
    │   ├── __init__.py            
    │   ├── abstract_data_factory.py            # Interface for a data factory 
    │   ├── pyg_data_factory.py                 # Class for torch_geometric.datasets
    │   ├── planetoid_data_factory.py           # Class for torch_geometric Planetoid 
    ├── experiments                     # Setups for ML tasks
    │   ├── abstract_experiment.py              # Interface for an experiment
    │   ├── experiment.py                       # Basic experiment example
    ├── slurm                           # Slurm scripts & logs
    │   ├── experiment.sh                       # Run experiment
    │   ├── greeting.sh
    ├── tests                           # Tests for classes 
    │   ├── planetoid_data_factory_test.py      
    └── README.md
<br>

greeting.py is an hello world program that creates a Neptune run for the [project](https://app.neptune.ai/o/ALLab-Boun/org/graph-ml/runs/table?viewId=standard-view), connects python logger to the run, logs cmd arguments and slurm output file names.

### Working from remote server
Submit slurm scripts when pwd is the root directory.

### Tests
Locate to root an run the tests as modules e.g.
`python -m tests.planetoid_data_factory_text`

### TODO
- Implement the generic class PyGDataFactory  
- PlanetoidDataFactory should create DataLoader 