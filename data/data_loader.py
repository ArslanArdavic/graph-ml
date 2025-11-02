"""Loading Data. 

This script defines the DataLoader class.   

"""

class DataLoader:   
    """This class loads data.

    Loads data.

    Attributes:
        attr: None
    """ 
    def __init__(self, attr=None):
        print(f"Initializing instance: {str(self)}")
        self.attr = attr

    def __repr__(self):
        items = ((k, v) for k, v in vars(self).items() if not k.startswith('_'))
        body = ", ".join(f"{k}={v!r}" for k, v in sorted(items))
        return f"{type(self).__name__}({body})"              
    
    def __str__(self):
        return "DataLoader"