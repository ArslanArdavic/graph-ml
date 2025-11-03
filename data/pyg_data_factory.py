# TODO: implement construct_data_loader(self)
"""Class to retrieve torch_geometric datasets.

This script defines the PyGDataFactory.

Typical usage example for full-batch single graph retrieval:

  data_factory = PyGDataFactory()
  data = data_factory.load_data()
"""
from torch_geometric import datasets

from . import AbstractDataFactory

class PyGDataFactory(AbstractDataFactory):
    """This class loads the benchmark datasets included in torch_geometric library. 
    
    Instantiates the dataset wrapper e.g. Planetoid
    Graph-level tasks and large single-graphs necessitate DataLoaders.

    Attributes:
        wrapper_name: PyG class name, e.g. Planetoid
        root:         Directory to save into
        name:         Name of the dataset, e.g. Cora
    """
    def __init__(self, wrapper_name=None, root=None, name=None):
        self.wrapper_name = wrapper_name
        self.root         = root
        self.name         = name

    def __repr__(self):
        items = ((k, v) for k, v in vars(self).items() if not k.startswith('_'))
        body = ", ".join(f"{k}={v!r}" for k, v in sorted(items))
        return f"{type(self).__name__}({body})"  
    
    def __str__(self):
        return "PyGDataFactory"
    
    def load_dataset(self):
        dataset = None
        cls = getattr(datasets)
        try:
            pass
        except:
            #not found
            pass
        return dataset
    
    def construct_data_loader(self):
        return super().construct_data_loader()