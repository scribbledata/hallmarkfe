import sys 
import pytest 
import hallmarkfe 

def test_processor(): 
    """
    Test the processor class 
    """

    proc = hallmarkfe.FEProcessor(conf={
        'name': 'hello',
        'owner': 'Brian'
    }) 

    
def test_state():
    """
    Test state access 
    """
    state = hallmarkfe.FEAtomicState()

    # 
    state.set_feature('hello', 'value')
    assert 'hello' in state.state['features']


def test_data():
    """
    Test data storage 
    """
    state = hallmarkfe.FEAtomicState()

    # Value could be any time 
    state.set_data('hello', 'value')
    assert 'hello' in state.state['data'] 

    state.set_data('hello', [
        {
            '1': 2,
            '2': 1 
        }
    ])

    assert 'hello' in state.state['data']
        
    d = state.get_data('hello') 
    assert isinstance(d, list) 
