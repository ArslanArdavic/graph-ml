"""Base ArchitectureBuilder class

This script defines the class to construct components and connect them.

Typical usage example:
    builder = ArchitectureBuilder()

"""
from overrides import override

from .abstract_architecture_builder import AbstractArchitectureBuilder 
from .architecture import Architecture
from models import GCN, MLP

class ArchitectureBuilder(AbstractArchitectureBuilder):
    """This class builds up a complex of components.

    Creates an Architecture class

    Attributes:
        arch: Architecture object

    """
    def __init__(self):
        self.arch = Architecture()

    def __repr__(self):
        items = ((k, v) for k, v in vars(self).items() if not k.startswith('_'))
        body = ", ".join(f"{k}={v!r}" for k, v in sorted(items))
        return f"{type(self).__name__}({body})"              
    
    def __str__(self):
        return "ArchitectureBuilder"
    
    @override
    def reset(self):
        self.arch = Architecture()
        return
    
    @override
    def get_result(self):
        return self.arch
    
    def build_gcn(self, blueprint):
        """ This function creates a GCN object.
            Adds the object to the architecture.

            Args:
                blueprint: Dictionary of GCN specifications.
                          e.g. {"in_dim": 512, "hidden_dims": [1028,1028], "out_dim": 256, "bias": True}
            Returns:
                Object created
        """ 
        if type(blueprint) != dict:
            raise TypeError(f"Argument to blueprint should be of type dict. Given type {type(blueprint)} is incorrect.")

        in_dim, hidden_dims, out_dim, bias = blueprint.get("in_dim"), blueprint.get("hidden_dims"), blueprint.get("out_dim"), blueprint.get("bias")
        component = GCN(in_dim=in_dim, hidden_dims=hidden_dims, out_dim=out_dim, bias=bias)
        self.arch.add_component(component=component)
        return component

    def build_mlp(self, blueprint):
        """ This function creates an MLP object.
            Adds the object to the architecture.

            Args:
                blueprint: Dictionary of MLP specifications.
                          e.g. {"in_dim": 512, "hidden_dims": [1028,1028], "out_dim": 256, "bias": True}
            Returns:
                Object created
        """ 
        if type(blueprint) != dict:
            raise TypeError(f"Argument to blueprint should be of type dict. Given type {type(blueprint)} is incorrect.")

        in_dim, hidden_dims, out_dim, bias = blueprint.get("in_dim"), blueprint.get("hidden_dims"), blueprint.get("out_dim"), blueprint.get("bias")
        component = MLP(in_dim=in_dim, hidden_dims=hidden_dims, out_dim=out_dim, bias=bias)
        self.arch.add_component(component=component)
        return component
