# TODO: Implement construct_data_loader() if graph will be partitioned into batches.
"""Class to retrieve Planetoid datasets.

This script defines the PlanetoidDataFactory that overrides PyGDataFactory.

Typical usage example for full-batch single graph retrieval:

  data_factory = PlanetoidDataFactory(name="Cora")
  dataset      = data_factory.load_dataset()
  data         = dataset[0]
"""
from overrides import override
from torch_geometric.datasets import Planetoid

from . import PyGDataFactory

class PlanetoidDataFactory(PyGDataFactory):
    def __init__(self, wrapper_name="Planetoid", root="./outputs/data/", name=None):
        super().__init__(wrapper_name, root, name)

    @override 
    def load_dataset(self):
        if self.name not in ["Cora", "CiteSeer", "PubMed"]:
            raise ValueError(f"Planetoid does not accept name={self.name}.")
        dataset = Planetoid(root=self.root, name=self.name)
        return dataset

    @override 
    def construct_data_loader(self):
        return