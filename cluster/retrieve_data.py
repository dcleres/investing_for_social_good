
# coding: utf-8

# In[ ]:
### RUN THIS IN THE CLUSTER FOLDER OF GITHUB

import os
import re

MY_DATA_DIR = '/user/cleres/data/'
extension = '.json.bz2'

for i in range(60):
    if i < 10 :
        name = '0' + str(i)
    else:
        name = str(i)
        
    os.system('scp -r -p cleres@iccluster028.iccluster.epfl.ch:/home/cleres/' + name + '.parquet ./')
