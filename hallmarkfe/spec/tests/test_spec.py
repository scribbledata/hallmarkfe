import os
import sys
<<<<<<< HEAD
import json 
=======
import json
>>>>>>> 9c2e4ba7a27d033f201f4f7493648ed2b26341f3
import pytest

import hallmarkfe

<<<<<<< HEAD
clue = True
=======
thisdir = os.path.dirname(os.path.realpath(__file__))
>>>>>>> 9c2e4ba7a27d033f201f4f7493648ed2b26341f3

@pytest.fixture
def testdata(request):

    # => Load the test data...
<<<<<<< HEAD
    filename = request.param    
    if filename is None: 
=======
    filename = request.param
    if filename is None:
>>>>>>> 9c2e4ba7a27d033f201f4f7493648ed2b26341f3
        testdata = {}
    else:
        if not os.path.isabs(filename):
            filename = os.path.join(os.path.dirname(__file__), filename)
        testdata = json.load(open(filename))

<<<<<<< HEAD
    return testdata 
=======
    return testdata
>>>>>>> 9c2e4ba7a27d033f201f4f7493648ed2b26341f3

@pytest.fixture()
def user_incomplete():

    # => Gets automatically registered
    class Alpha(hallmarkfe.spec.SpecBase):
        schema = "user:default:v1"
<<<<<<< HEAD
            
=======

        def initialize(self):
            self.required.extend([
                'id',
                'entity',
                'granularity',
                'uri',
                'tags',
                'options',
                'dataStores',
            ])

    yield Alpha

    # Cleanup the function
    hallmarkfe.spec.unregister(Alpha)

@pytest.fixture()
def user_json_list():

    # => Gets automatically registered
    class Alpha(hallmarkfe.spec.SpecBase):
        schema = "user:default:v1"
        schema_list = ["user:default:v1"]

>>>>>>> 9c2e4ba7a27d033f201f4f7493648ed2b26341f3
        def initialize(self):
            self.required.extend([
                'id',
                'entity',
                'granularity',
                'uri',
                'tags',
                'options',
                'dataStores',
            ])

<<<<<<< HEAD
    yield Alpha 

    # Cleanup the function 
    hallmarkfe.spec.unregister(Alpha)     
=======
    yield Alpha

    # Cleanup the function
    hallmarkfe.spec.unregister(Alpha)
>>>>>>> 9c2e4ba7a27d033f201f4f7493648ed2b26341f3

@pytest.fixture()
def user_extra_cols():

    # => Gets automatically registered
    class Alpha(hallmarkfe.spec.SpecBase):
        schema = "user:default:v1"
<<<<<<< HEAD
            
=======

>>>>>>> 9c2e4ba7a27d033f201f4f7493648ed2b26341f3
        def initialize(self):
            self.required.extend([
                'id',
                'entity',
                'granularity',
                'uri',
                'tags',
                'options',
                'dataStores',
                'kilo'
            ])

<<<<<<< HEAD
    yield Alpha 

    # Cleanup the function 
    hallmarkfe.spec.unregister(Alpha)     
    
@pytest.mark.parametrize('testdata',
                         [
                             'fixtures/user.json',
=======
    yield Alpha

    # Cleanup the function
    hallmarkfe.spec.unregister(Alpha)


def test_schema_list():
    """
    Test schema list
    """
    speclist = hallmarkfe.spec.schema_list()
    assert isinstance(speclist, list)
    assert len(speclist) > 0

@pytest.mark.parametrize('schemaval',[
    '', [], None, 25, {}, [{}]
])
def test_schema_get_invalid(schemaval):
    """
    Test schema get invalid schema
    """

    with pytest.raises(hallmarkfe.spec.SpecInvalidSchema) as exc:
        handler = hallmarkfe.spec.schema_get(schemaval)
    
@pytest.mark.parametrize('schemaval',[
    'random'
])
def test_schema_get_invalid(schemaval):
    """
    Test schema get invalid schema
    """

    with pytest.raises(hallmarkfe.spec.SpecNoHandler) as exc:
        handler = hallmarkfe.spec.schema_get(schemaval)

def test_schema_get_valid():
    """
    Test schema get invalid schema
    """
    handler = hallmarkfe.spec.schema_get('global:default:v1')
    assert handler == hallmarkfe.SpecBase

@pytest.mark.parametrize('spec',
                         [
                             None, "", {}, [], [{}], object ,
                             { 'ehllo' : 11},
                             [{ 'ehllo' : 11}],
                         ])
def test_parse_invalid(spec):
    """
    Test schema get invalid schema
    """

    with pytest.raises(hallmarkfe.SpecInvalidSpecification) as exc:
        handler = hallmarkfe.parse_generic(spec)
        
@pytest.mark.parametrize('spec',
                         [os.path.join(thisdir,'fixtures/hello.html')])
def test_parse_invalid_file(spec):
    """
    Test schema get invalid schema
    """

    with pytest.raises(hallmarkfe.SpecInvalidSpecification) as exc:
        handler = hallmarkfe.parse_generic(spec)        


@pytest.mark.parametrize('testdata',
                         [
                             os.path.join(thisdir,'fixtures/user.json'),
>>>>>>> 9c2e4ba7a27d033f201f4f7493648ed2b26341f3
                         ],
                         indirect=True)
def test_user_nohandler(testdata):
    """
<<<<<<< HEAD
    Test complex spec 
    """
    with pytest.raises(hallmarkfe.spec.SpecNoHandler) as exc:    
        obj = hallmarkfe.spec.parse(testdata)

@pytest.mark.parametrize('testdata',
                         [
                             'fixtures/user.json',
=======
    Test complex spec
    """
    with pytest.raises(hallmarkfe.spec.SpecNoHandler) as exc:
        obj = hallmarkfe.spec.parse_generic(testdata)

@pytest.mark.parametrize('testdata',
                         [
                             os.path.join(thisdir,'fixtures/user.json'),
>>>>>>> 9c2e4ba7a27d033f201f4f7493648ed2b26341f3
                         ],
                         indirect=True)
def test_user_incomplete_handler(testdata, user_incomplete):
    """
<<<<<<< HEAD
    Test complex spec 
    """
    # This should go through 
    obj = hallmarkfe.spec.parse(testdata)
=======
    Test complex spec
    """
    # This should go through
    obj = hallmarkfe.spec.parse_generic(testdata)
>>>>>>> 9c2e4ba7a27d033f201f4f7493648ed2b26341f3

@pytest.mark.parametrize('testdata',
                         [
                             'fixtures/user.json',
                         ],
                         indirect=True)
def test_user_invalid_spec(testdata, user_extra_cols):
    """
<<<<<<< HEAD
    Test complex spec 
    """
    # This should go through 
    with pytest.raises(hallmarkfe.spec.SpecInvalidSpecification) as exc:
        obj = hallmarkfe.spec.parse(testdata)
    
        
    
#                             'fixtures/storage.json',
#                             'fixtures/entity.json'
=======
    Test complex spec
    """
    # This should go through
    with pytest.raises(hallmarkfe.spec.SpecInvalidSpecification) as exc:
        obj = hallmarkfe.spec.parse_generic(testdata)



#                             'fixtures/storage.json',
#                             'fixtures/entity.json'
@pytest.mark.parametrize('testdata',
                         [
                             os.path.join(thisdir,'fixtures/user_list.json'),
                         ],
                         indirect=True)
def test_user_json_list(testdata, user_json_list):
    """
    Test complex spec with list of dicts
    """
    # This should pass
    obj = hallmarkfe.spec.parse_generic(testdata)

@pytest.mark.parametrize('testdata',
                         [
                             os.path.join(thisdir,'fixtures/user.yaml'),
                             os.path.join(thisdir,'fixtures/user.yml'),
                         ],
                         indirect=False)
def test_user_yaml_list(testdata, user_json_list):
    """
    Test complex spec with list of dicts
    """
    # This should pass
    obj = hallmarkfe.spec.parse_generic(testdata)

@pytest.mark.parametrize('testdata',
                         [
                             os.path.join(thisdir,'fixtures/user_list.json')
                         ],
                         indirect=False)
def test_user_json_file(testdata, user_json_list):
    """
    Test complex spec with list of dicts
    """
    # This should pass
    obj = hallmarkfe.spec.parse_generic(testdata)

@pytest.mark.parametrize('testdata',
                         [
                             os.path.join(thisdir,'fixtures')
                         ],
                         indirect=False)
def test_SpecManager(testdata, user_json_list):
    """
    Test complex spec with list of dicts
    """
    # This should pass
    obj = hallmarkfe.SpecManagerBase()
    obj.load(testdata)


##################################################
# Subclasses
##################################################
@pytest.mark.parametrize('schemaval',[
    None, 1, {}, [], "", [""]
])
def test_subclass_invalid(schemaval):
    """
    Test subclass definition
    """

    with pytest.raises(hallmarkfe.spec.SpecInvalidSchema) as exc:
        class TestSubclass(hallmarkfe.SpecBase):
            schema = schemaval

@pytest.mark.parametrize('schemaval',[
    "hello", ["hello"]
])
def test_subclass_valid(schemaval):
    """
    Test subclass definition
    """

    class TestSubclass(hallmarkfe.SpecBase):
        schema = schemaval

def test_dump():
    """
    Test dump
    """

    class TestSubclass(hallmarkfe.SpecBase):
        schema = "hello"

    hallmarkfe.register(TestSubclass)

    testdata = {
        'schema': 'hello',
        'name': 'kilo',
        'description': "Test kilo",
        'owner': 'hello@hello.com'
    }
    handler = hallmarkfe.parse_generic(testdata)

    assert len(handler.dump()) > 0
    assert len(handler.prettyprint()) > 0
>>>>>>> 9c2e4ba7a27d033f201f4f7493648ed2b26341f3
