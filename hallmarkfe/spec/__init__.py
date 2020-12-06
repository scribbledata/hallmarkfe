<<<<<<< HEAD
from .base import *
from .utils import * 

def parse(dct):
    """
    Create Hallmark specification object 
    """
    cls = SpecRegistry.find_handler_for_dict(dct)
=======
"""
Specification Interface 
------------------------

"""

from .base import *
from .exceptions import *

from . import exceptions, base 

__all__ = ['parse_generic', 'register', 'unregister'] + \
          base.__all__ + \
          exceptions.__all__

def parse_generic(arg):
    """
    Create Hallmark specification object 
   
    :param object arg: Specification (a dictionary) or file location (a string)

    """
    dct, cls = SpecRegistry.find_handler_generic(arg)
>>>>>>> 9c2e4ba7a27d033f201f4f7493648ed2b26341f3
    obj = cls() 
    obj.load(dct)
    return obj 

<<<<<<< HEAD
def unregister(cls):
    SpecRegistry.unregister(cls)

def register(cls):
    SpecRegistry.register(cls)
=======
def register(cls):
    """
    Register specification handler

    :param class cls: Handler class
    """    
    SpecRegistry.register(cls)

def unregister(cls):
    """
    Unregister specification handler

    :param class cls: Handler class
    """
    SpecRegistry.unregister(cls)

def schema_list():
    """
    Get a list of available schemas 
    """
    return SpecRegistry.schema_list()
    

def schema_list():
    """
    Get a list of available schemas 
    """
    return SpecRegistry.schema_list()
    
def schema_get(schema):
    """
    Get a list of available schemas 
    """
    return SpecRegistry.schema_get(schema) 
    
>>>>>>> 9c2e4ba7a27d033f201f4f7493648ed2b26341f3
