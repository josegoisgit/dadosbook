# %load /dev/notebook/dc_join.py
def dc_join(db='ufrn_wait',dc='turmas',num=[],**kwargs):

    import re

    if not hasattr(dc_join,'dict'):
        dc_join.dict = {}
    if not 'key_types' in kwargs:
        key_types = {}
    if not 'ignore_index' in kwargs:
        ignore_index = True

    db_folder_fcn = lambda db,dc : '/data/%s' % (db)
    db_folder     = db_folder_fcn(db,dc)

    db_folders = os.listdir(db_folder)
    
    dc_folders = [
        db_folder+'/'+folder
        for folder in db_folders
        if re.findall(dc,folder)
    ]
    
    dc_files = [
        dc_folder+'/'+dc_file
        for dc_folder in dc_folders
        for dc_file in os.listdir(dc_folder)
    ]
    
    csv_files = [
        dc_file
        for dc_file in dc_files
        if dc_file.endswith('.csv')
    ]

    dc_data = pd.concat([pd.read_csv(csv,sep=';') for csv in csv_files], ignore_index=ignore_index)
    
    dc_data = dc_data[~dc_data.duplicated()]
    
    dc = re.sub('[^\w]','',dc)
    dbc = db+'/'+dc
    
    dc_join.dict[dbc] = {'folder':dc_folders, 'csv_files': csv_files, 'db':db, 'dc':dc, 'data':dc_data}

    dc_transform(db = db, dc = dc, key_types=key_types)

    return dc_data
