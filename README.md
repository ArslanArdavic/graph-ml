# graph-ml
Machine Learning On Graphs

    .
    ├── exec                    # Executable files
    │   ├── greeting.py 
    ├── slurm                   # Slurm scripts & logs
    │   ├── greeting.sh
    │   ├── logs
    ├── experiments             # Setups for ML tasks
    │   ├── experiment.py
    │   ├── experiment_abstract.py
    └── README.md
<br>

Submit slurm scripts when pwd is the root directory.

greeting.py is an hello world program that creates a Neptune run for the [project](https://app.neptune.ai/o/ALLab-Boun/org/graph-ml/runs/table?viewId=standard-view), connects python logger to the run, logs cmd arguments and slurm output file names.