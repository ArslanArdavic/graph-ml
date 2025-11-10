
from .architecture_builder import ArchitectureBuilder

class Director():
    """This class controls the builder.

    Defines methods to build specific architectures. 

    Attributes:
        builder: ArchitectureBuilder
    """
    def __init__(self):
        self.builder = ArchitectureBuilder()

    def __repr__(self):
        items = ((k, v) for k, v in vars(self).items() if not k.startswith('_'))
        body = ", ".join(f"{k}={v!r}" for k, v in sorted(items))
        return f"{type(self).__name__}({body})"              
    
    def __str__(self):
        return "ArchitectureBuilder"

    def construct_single_gcn(self, blueprint):
        """This function construct an Architecture with a sole GCN
        Args:  
            blueprint: Dictionary of GCN specifications.
        Returns:
            Architecture including one GCN
        """        
        self.builder.reset()
        return self.builder.build_arch_single_gcn(blueprint=blueprint)       
    
    def construct_single_mlp(self, blueprint):
        """This function constructs an Architecture with a sole MLP
        Args:  
            blueprint: Dictionary of MLP specifications.
        Returns:
            Architecture including one MLP
        """
        self.builder.reset()
        return self.builder.build_arch_single_mlp(blueprint=blueprint)
    
    def construct_gcn_with_head(self, blueprint_gcn, blueprint_mlp):
        """This function constructs an Architecture,
            with a GCN with an MLP on top. 

        Args:  
            blueprint_gcn: Dictionary of GCN specifications
            blueprint_mlp: Dictionary of MLP specifications.
        Returns:
            Architecture including GCN with MLP Head
        """
        self.builder.reset()
        return self.builder.build_arch_construct_gcn_with_head(blueprint_gcn, blueprint_mlp)
    
    def construct_gcn_preproject(self, blueprint_gcn, blueprint_mlp):
        """This function construct an Architecture,
            with a GCN with an MLP on top. 

        Args:  
            blueprint_gcn: Dictionary of GCN specifications
            blueprint_mlp: Dictionary of MLP specifications.
        Returns:
            Architecture including GCN with MLP pre-projection 
        """
        self.builder.reset()
        return self.builder.build_arch_construct_gcn_preproject(blueprint_gcn, blueprint_mlp)