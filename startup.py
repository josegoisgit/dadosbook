import os
import pandas as pd
db = 'ufrn_wait'
db_folder = '/home/josegois/data/' + db
dc_folders = os.listdir(db_folder)
exec(open('./functions/dc_join.py').read())
exec(open('./functions/dc_transform.py').read())
#exec(open('./functions/dc_dict_merge.py').read())
exec(open('./functions/dc_join.py').read())
exec(open('./functions/dc_transform.py').read())
#exec(open('./functions/dc_dict_merge.py').read())
