import os 
import sys 
import json 
import random 
import pytest 
import pandas as pd 
import hallmarkfe 

thisdir = os.path.abspath(os.path.dirname(__file__))

def toseconds(s):
    # s = 0:03:11
    s = s.split(":")
    return (int(s[0]) * 3600) + (int(s[1]) * 60) + (int(s[2].split(".")[0]))
    

def load_calls():

    calllog = os.path.join(thisdir, 'fixtures','call_log.csv') 
    df1 = pd.read_csv(calllog)
    df1.loc[:, 'Duration'] = df1.Duration.apply(toseconds)
    df2 = df1.copy()
    df2.loc[:,'CallDate'] = "2010-12-26"
    df = pd.concat([df1, df2]) 
    
    return df

class SimpleProcessor(hallmarkfe.HMFEProcessor):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.level_tags = {
            1: ['a', 'b', 'c'],
            2: ['p', 'q', 'r'] 
        }
        
    def process(self, state, level):

        calls = state.get_data('calls') 
        tags = self.level_tags.get(level, [])
        for t in tags:
            fname = '{}_{}_{}'.format(self.name, level, t)
            fval = len(calls) 
            state.set_feature(fname, fval) 
        
    
def test_complex_annotation():
    """
    Test state access 
    """

    mgr = hallmarkfe.HMFEManager({
        'sequence': ['simple1'] 
    })
    myproc = SimpleProcessor(conf={
        'name': 'simple1',
        'owner': 'Dilloy',
        'manager': 'Manager'       
    })
    mgr.add_processor('simple1', myproc) 

    df = load_calls() 

    uniques = df['In'].nunique() 
    def summarize(rows):
        rows = rows.to_dict('records')

        state = hallmarkfe.HMFEAtomicState()
        state.set_data('calls', rows) 

        # Now collect all the tags 
        mgr.process(state) 

        features = state.get_all_features()

        # Now return the 
        return pd.Series(features)
    
    df = df.groupby(["In"]).apply(summarize)
    df = df.reset_index()
    assert df.shape[0] == uniques
    assert len(df.columns) == 7 
    
# Data 
# In,Out,Direction,CallDate,CallTime,DOW,Duration,TowerID,TowerLat,TowerLon
# 7622433748,3207621566,Incoming,2010-12-25,07:16:24.736813,Sat,0:02:41.741499,0db53dd3-eb9c-4344-abc5-c2d74ebc3eec,32.731611,-96.709417
# 

class SimpleRuleProcessor1(hallmarkfe.HMFERuleBasedProcessor,
                          hallmarkfe.MetricHandlerMixin):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.metric_handlers = {
            'total': lambda args, rows: self.toolz_sum('Duration', rows),
            'dates': lambda args, rows: self.toolz_count('CallDate', rows),
        }
        
        self.rules = [
            {
                'name': 'calls',
                'description': 'Large duration calls',
                'notes': 'Includes only those that are longer than 2 mins',
                'operators': [
                    {
                        'level': 1,
                        'handler': 'table_apply_rule',
                        'params': {
                            'table': 'calls',
                            'rule': {
                                'column': 'Duration',
                                'match': 'GT',
                                'values': 60
                            },
                            'metrics': [
                                {
                                    'name': 'total',
                                    'handler': 'total',
                                    'args': {
                                        'feature': "%(owner)s__%(level)s__%(rule_name)s__xx__%(suffix)s",
                                    }
                                },
                                {
                                    'name': 'dates',
                                    'handler': 'dates',
                                    'args': {
                                        'suffix': 'days',
                                    }
                                }
                            ]
                        }
                    }
                ]
            }
        ]
        
class SimpleRuleProcessor2(hallmarkfe.HMFERuleBasedProcessor,
                          hallmarkfe.MetricHandlerMixin):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.metric_handlers = {
            'total_match': lambda args, rows: self.toolz_sum(args['match'], rows),
            'avg_match': lambda args, rows: self.toolz_avg(args['match'], rows),
            'avg2x': lambda args, rows: 2*self.toolz_sum(args['col'], rows),
            'first_day': lambda args, rows: self.toolz_min('CallDate', rows),
            'last_day': lambda args, rows: self.toolz_max('CallDate', rows),
            'dates': lambda args, rows: self.toolz_count('CallDate', rows),
        }
        self.rules = [
            {
                'name': 'calls',
                'description': 'Large duration calls',
                'notes': 'Includes only those that are longer than 2 mins',
                'operators': [
                    {                
                        'level': 1,
                        'handler': 'table_apply_rule',
                        'params': {
                            'table': 'memberdates',
                            'match': '.*__xx__total', 
                            'metrics': [
                                {
                                    'name': 'total', 
                                    'handler': 'total_match',
                                    'args': {
                                        'feature': '%(match)s'
                                    }
                                },
                                {
                                    'name': 'avg', 
                                    'handler': 'avg_match',
                                }
                            ]
                        }
                    },
                    {                
                        'level': 1,
                        'handler': 'table_apply_rule',
                        'params': {
                            'table': 'memberdates',
                            'metrics': [
                                {
                                    'name': 'dates', 
                                    'handler': 'dates',
                                },
                                {
                                    'name': 'first_day', 
                                    'handler': 'first_day',
                                    'args': {
                                        'suffix': 'firstday' 
                                    }
                                },
                                {
                                    'name': 'last_day', 
                                    'handler': 'last_day',
                                    'args': {
                                        'suffix': 'lastday' 
                                    }
                                },                                
                            ]
                        }
                    },
                    {                
                        'level': 2,
                        'handler': 'table_apply_rule',
                        'params': {
                            'table': '__computed__',
                            'metrics': [
                                {
                                    'name': 'avg2x', 
                                    'handler': 'avg2x',
                                    'args': {
                                        'col': 'marketing__1__calls__xx__avg'
                                    }
                                },
                            ]
                        }
                    }                    
                ]
            }
        ]
            
    def generate_feature_name(self, args):
        """
        Generate feature name...
        """
        name = args['name']
        
        if name == 'avg':
            feature_name = args['match'] 
            feature = feature_name.replace("_total","_avg") 
        else: 
            # Otherwise use the default 
            feature = super().generate_feature_name(args) 

        return feature 


def test_complex_annotation2():
    """
    Test state access 
    """

    mgr1 = hallmarkfe.HMFEManager({
        'sequence': ['complex1'] 
    })

    myproc1 = SimpleRuleProcessor1(conf={
        'name': 'complex1',
        'owner': 'marketing',
        'manager': 'manager'
    })

    mgr1.add_processor('complex1', myproc1) 

    mgr2 = hallmarkfe.HMFEManager({
        'sequence': ['complex2'] 
    })
    myproc2 = SimpleRuleProcessor2(conf={
        'name': 'complex2',
        'owner': 'marketing',
        'manager': 'manager'
    })
    mgr2.add_processor('complex2', myproc2) 

    df = load_calls()     

    # Level 1  
    uniques = df['In'].nunique() 
    def summarize(rows):
        rows = rows.to_dict('records')

        state = hallmarkfe.HMFEAtomicState()
        state.set_data('calls', rows) 

        # Now collect all the tags 
        mgr1.process(state) 

        features = state.get_all_features()

        # Now return the 
        return pd.Series(features)
    
    df1 = df.groupby(["In", "CallDate"]).apply(summarize)
    df1 = df1.reset_index()


    verifydf = df[df['Duration'] > 60]
    print("Sup = {}".format(df1.columns))
    assert df1['marketing__1__calls__xx__total'].sum() == verifydf['Duration'].sum()     
    assert df1['In'].nunique() == uniques 
    assert len(df1.columns) == 4

    #print("DF1")
    #print(df1.head())

    #=> 
    
    def summarize2(rows):
        rows = rows.to_dict('records')

        state = hallmarkfe.HMFEAtomicState()
        state.set_data('memberdates', rows) 

        # Now collect all the tags 
        mgr2.process(state) 

        features = state.get_all_features()

        # Now return the 
        return pd.Series(features)
    
    df2 = df1.groupby(["In"]).apply(summarize2)
    df2 = df2.reset_index()

    print("DF2")
    print(df2.head())
    assert df1['marketing__1__calls__xx__total'].sum() == df2['marketing__1__calls__xx__total'].sum()
    assert df1['In'].nunique() == df2['In'].nunique() 
