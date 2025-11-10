"""Minimal container class

This script defines various architectures.  

"""
import torch.nn as nn

class Architecture(nn.Module):
    def __init__(self):
        super().__init__()
        self.module_dict = nn.ModuleDict()         
    
    def __str__(self):
        return "Architecture"
    
    def update_component(self, name, component):
        self.module_dict.update({name:component})

class SingleGCN(Architecture):
    def forward(self, x, edge_index, edge_weight=None):
        return self.module_dict["GCN"].forward(x, edge_index, edge_weight)
    
class SingleMLP(Architecture):
    def forward(self, x):
        return self.module_dict["MLP"].forward(x)
    
class GCNHeaded(Architecture):
    def forward(self, x, edge_index, edge_weight=None):
        x = self.module_dict["GCN"].forward(x, edge_index, edge_weight)
        return self.module_dict["MLP"].forward(x)
    
class GCNPreproject(Architecture):
    def forward(self, x, edge_index, edge_weight=None):
        x = self.module_dict["MLP"].forward(x)
        return self.module_dict["GCN"].forward(x, edge_index, edge_weight)