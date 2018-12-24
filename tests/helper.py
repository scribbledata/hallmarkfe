import logging
import  hallmarkfe.supernova  as hallmarkfe

logger = logging.getLogger()

mgr1 = None 

class SimpleRuleProcessor1(hallmarkfe.FERuleBasedProcessor,
                          hallmarkfe.MetricHandlerMixin):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.metric_handlers = {
            'total': lambda args, rows: self.toolz_sum('DurationSeconds', rows),
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
                                'column': 'DurationSeconds',
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
        
def get_mgr1(): 
    global mgr1
    if mgr1 is not None:
        return mgr1

    logger.debug("Creating a new mgr")
    
    mgr1 = hallmarkfe.FEManager({
        'processors': ['complex1'] 
    })

    myproc1 = SimpleRuleProcessor1(conf={
        'name': 'complex1',
        'owner': 'marketing' 
    })

    mgr1.add_processor('complex1', myproc1) 
    return mgr1

    
def reducefunc(g):

    mgr1 = get_mgr1() 
    
    key = g[0]
    rows = g[1]
    rows = list(rows)

    # logger.error("One row: " + str(rows[0])) 
    
    state = hallmarkfe.FEAtomicState()
    state.set_feature('In', key) 
    state.set_data('calls', rows) 
    
    # Now collect all the tags 
    mgr1.process(state) 
    
    features = state.get_all_features()

    return features 
