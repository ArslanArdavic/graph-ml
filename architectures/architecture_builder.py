"""Base ArchitectureBuilder class

This script defines the class to construct components and connect them.

Typical usage example:
    builder = ArchitectureBuilder()

"""
from overrides import override

from .abstract_architecture_builder import AbstractArchitectureBuilder 
from .architecture import Architecture, SingleGCN, SingleMLP, GCNHeaded, GCNPreproject
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
        return component

    def build_mlp(self, blueprint):
        """ This function creates an MLP object.
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
        return component
    
    def build_arch_single_gcn(self, blueprint):
        """Instantiates an SingleGCN architecture
            Args:
                blueprint: GCN specs
            Returns: 
                SingleGCN architecture object       
        """
        self.arch = SingleGCN()
        gcn = self.build_gcn(blueprint=blueprint)
        self.arch.update_component(name="GCN", component=gcn)
        return self.arch
    
    def build_arch_single_mlp(self, blueprint):
        """Instantiates an SingleMLP architecture
            Args:
                blueprint: MLP specs
            Returns: 
                SingleMLP architecture object       
        """
        self.arch = SingleMLP()
        mlp = self.build_mlp(blueprint=blueprint)
        self.arch.update_component(name="MLP", component=mlp)
        return self.arch
    
    def build_arch_construct_gcn_with_head(self, blueprint_gcn, blueprint_mlp):
        """Instantiates a GCNHeaded architecture
            Args:
                blueprint_gcn: GCN specs
                blueprint_mlp: MLP specs
            Returns: 
                GCNHeaded architecture object       
        """
        self.arch = GCNHeaded()
        if blueprint_gcn.get("out_dim") != blueprint_mlp.get("in_dim"):
            raise ValueError(f"GCN logit dimension does not match with MLP input dimension.")
        
        gcn = self.build_gcn(blueprint=blueprint_gcn)
        mlp = self.build_mlp(blueprint=blueprint_mlp)
        self.arch.update_component(name="GCN", component=gcn)
        self.arch.update_component(name="MLP", component=mlp)
        return self.arch
    
    def build_arch_construct_gcn_preproject(self, blueprint_gcn, blueprint_mlp):
        """Instantiates a GCNPreproject architecture
            Args:
                blueprint_gcn: GCN specs
                blueprint_mlp: MLP specs
            Returns: 
                GCNPreproject architecture object       
        """
        self.arch = GCNPreproject()
        if blueprint_gcn.get("in_dim") != blueprint_mlp.get("out_dim"):
            raise ValueError(f"MLP logit dimension does not match with GCN input dimension.")
        
        gcn = self.build_gcn(blueprint=blueprint_gcn)
        mlp = self.build_mlp(blueprint=blueprint_mlp)
        self.arch.update_component(name="GCN", component=gcn)
        self.arch.update_component(name="MLP", component=mlp)
        return self.arch
    
    
