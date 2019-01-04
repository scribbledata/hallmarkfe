from .base import *
from .utils import * 

def parse(dct):
    """
    Create Hallmark specification object 
    """
    cls = SpecRegistry.find_handler_for_dict(dct)
    obj = cls() 
    obj.load(dct)
    return obj 

def unregister(cls):
    SpecRegistry.unregister(cls)

def register(cls):
    SpecRegistry.register(cls)
