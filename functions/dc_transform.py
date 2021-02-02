# %%writefile /dev/notebook/dc_transform.py
# %load /dev/notebook/dc_transform.py
def dc_transform (db = 'ufrn_wait',dc = 'turmas', key_types={}):
    dbc = db+'/'+dc
    dc_data = dc_join.dict[dbc]['data']
    
    for key in dc_data:
        for key_type in key_types:
            print(key, key_type)
            if key.startswith(key_type):
                key_fcn,key_data,key_args = key_types[key_type];
                for arg in key_args:
                    key_fcn_args = { **{ key_data : dc_data[key] } , **arg }
                    dc_data[key] = key_fcn( **key_fcn_args )
                break
    dc_join.dict[dbc]['key_types'] = key_types
