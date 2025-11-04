"""Base ArchitectureBuilder class

This script defines the class to construct components and connect them.

Typical usage example:
    builder = ArchitectureBuilder()

"""
from overrides import override

from . import AbstractArchitectureBuilder, Architecture
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
    def create_component(self, blueprint):
        """ This function instantiates an GCN or MLP object.
            Adds the object to the architecture.

            Args:
                blueprint: Dictionary for component specification, "model_type" is required.
                          e.g. {"model_type": "GCN", "in_dim": 512, "hidden_dims": [1028,1028], "out_dim": 256, "bias": True}
            Returns:
                Object created
        """
        if type(blueprint) != dict:
            raise TypeError(f"Argument to blueprint should be of type dict. Given type {type(blueprint)} is incorrect.")

        model_type =  blueprint.get("model_type") 

        if model_type not in ["GCN", "MLP"] or model_type == None:
            raise ValueError(f"Given model_type : {model_type} is not supported.")
        else:
            in_dim, hidden_dims, out_dim, bias = blueprint.get("in_dim"), blueprint.get("hidden_dims"), blueprint.get("out_dim"), blueprint.get("bias")
            if model_type=="GCN":
                component = GCN(in_dim=in_dim, hidden_dims=hidden_dims, out_dim=out_dim, bias=bias)
            elif model_type=="MLP":
                component = MLP(in_dim=in_dim, hidden_dims=hidden_dims, out_dim=out_dim, bias=bias)

        self.arch.add_component(component)

        return component
    
    @override
    def connect_components(self):
        return