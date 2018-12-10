
# coding: utf-8

# In[ ]:
### RUN THIS IN THE THE CLUSTER_DATA FOLDER ON THE LOCAL MACHINE

import os
import re

#strats at one since the is no day 0 in a month
for j in range(1, 32):
    if j < 10 :
        day = '0' + str(j)
    else:
        day = str(j)

    os.system('mkdir ' + day)

    for i in range(24):
        if i < 10 :
            hour = '0' + str(i)
        else:
            hour = str(i)

        #create a directory on the local home folder of the cluster
        os.system('mkdir ' + day + '/' + hour)
        
        #fetcheds the data from the cluster and saves it in the folder created jsut before which is local on the cluster
        os.system('scp -r -p cleres@iccluster028.iccluster.epfl.ch:/home/cleres/' + day + '/' + hour + '/*.json.bz2 ./' + day + '/' + hour)
