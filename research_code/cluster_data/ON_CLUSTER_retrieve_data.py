
# coding: utf-8
### RUN THIS IN THE CLUSTER ENVIRONMENT IN THE LOCAL FOLDER
#to run this file : in the cluster environment : python ON_CLUSTER_retrieve_data

import os
import re

#strats at one since the is no day 0 in a month
for j in range(1, 32):
    if j < 10 :
        day = '0' + str(j)
    else:
        day = str(j)

    os.system('mkdir /home/cleres/' + day)

    for i in range(24):
        if i < 10 :
            hour = '0' + str(i)
        else:
            hour = str(i)

        #create a directory on the local home folder of the cluster
        os.system('mkdir /home/cleres/' + day + '/' + hour)

        #fetcheds the data from the cluster and saves it in the folder created jsut before which is local on the cluster
        os.system('hadoop fs -get /datasets/twitter_internetarchive/2017/01/'+ day +'/' + hour + '/* /home/cleres/' + day + '/' + hour)
