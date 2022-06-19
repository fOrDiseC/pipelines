import pandas as pd
import os
path_to_file=os.environ.get('Path_to_file')
pd.__version__
titanic = pd.read_csv(path_to_file)
ship_sex = titanic['Sex']
titanic['unsex']=ship_sex
print(titanic)
print('completed')