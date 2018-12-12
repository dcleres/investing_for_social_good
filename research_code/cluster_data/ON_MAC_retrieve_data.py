
# coding: utf-8

# In[ ]:
### RUN THIS IN THE THE CLUSTER_DATA FOLDER ON THE LOCAL MACHINE

import os
import re
import pandas as pd
from os import listdir
from os.path import isfile, join


for k in range(1, 13):
    if k < 10 :
        month = '0' + str(k)
    else:
        month = str(k)
    
    os.system('mkdir ' + month)

    #strats at one since the is no day 0 in a month
    for j in range(1, 32):
        if j < 10 :
            day = '0' + str(j)
        else:
            day = str(j)

        os.system('mkdir ' + month + '/' + day)

        for i in range(24):
            if i < 10 :
                hour = '0' + str(i)
            else:
                hour = str(i)

            #create a directory on the local home folder of the cluster
            os.system('mkdir ' + month + '/' + day + '/' + hour)
            
            #fetcheds the data from the cluster and saves it in the folder created jsut before which is local on the cluster
            os.system('scp -r -p cleres@iccluster028.iccluster.epfl.ch:/home/cleres/' + month + '/' + day + '/' + hour + '/*.json.bz2 ./' + month + '/' + day + '/' + hour)


            #keep only the english tweets
            mypath = './' + month + '/' + day + '/' + hour + '/'

            for f in listdir(mypath):
                df = pd.read_json(mypath + f, lines=True)
                df = df[df.lang=='en']
                df = df.reset_index()
                
                print('SAVING TO :' , mypath + f)
                df.to_json(mypath + f, compression='bz2')
