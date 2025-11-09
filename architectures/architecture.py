"""Minimal container class

This script defines various architectures.  

"""
import torch.nn as nn

class Architecture(nn.Module):
    def __init__(self):
        super().__init__()
        self.components = [] 

    def __repr__(self):
        items = ((k, v) for k, v in vars(self).items() if not k.startswith('_'))
        body = ", ".join(f"{k}={v!r}" for k, v in sorted(items))
        return f"{type(self).__name__}({body})"              
    
    def __str__(self):
        return "Architecture"
    
    def add_component(self, component):
        self.components.append(component)
