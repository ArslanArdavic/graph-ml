"""Minimal container class

This script defines the Architecture class to  

"""

class Architecture():
    def __init__(self):
        self.components = None 

    def __repr__(self):
        items = ((k, v) for k, v in vars(self).items() if not k.startswith('_'))
        body = ", ".join(f"{k}={v!r}" for k, v in sorted(items))
        return f"{type(self).__name__}({body})"              
    
    def __str__(self):
        return "Architecture"
    
    def add_component(self,component):
        return
