
# coding: utf-8

# # Connect to the clusters 

# ### STEPS: 
# - connect to VPN and type in the terminal :  *ssh cleres@iccluster028.iccluster.epfl.ch*
# - see the list of datasets: hadoop fs -ls /datasets
# 

# ## TWITTER dataset
# What do we need to do : 
# - The data is on the cluster in the datasets folder 
# - Pandas is perfect for data analysis and manipulation, while Spark can do the heavy job. The ideal workflow is to write your aggregation task in Spark, save the reduced dataset in JSON format and then load it on your laptop with Pandas.
# - How can I access local files in the cluster, I try to access
# user/greffe/data/mapping_country_codes.csv
# with 
# spark.read.csv("/home/greffe/data/mapping_country_codes.csv", header=True)
# but get the following error:
# pyspark.sql.utils.AnalysisException: u'Path does not exist: hdfs://iccluster028.iccluster.epfl.ch:8020/user/greffe/data/mapping_country_codes.csv;'
# EDIT: I understood the problem
# 1) we have to put the files on hdfs "hadoop fs -put file"
# 2) we access those at "hdfs:///user/USERNAME/FILE" from spark (edited)
# 
# - put the py file on the cluster : scp -r -p FILE YOURNAME@iccluster028.iccluster.epfl.ch:/home/YOURNAME/FILE
# 
# - download those output from the cluster right? how could we download the output from the cluster? you have to transfering from the hdfs to your local file system with hadoop and then to use scp to get it locally (if you use files in the py script, they have to be on the hdfs by the way)
# 
# - spark-submit --master yarn --deploy-mode cluster --driver-memory 4G --num-executors 5 --executor-memory 4G --executor-cores 5 some_script.py script_arg1 script_arg2
# - OUR VERSION: spark-submit --master yarn --deploy-mode cluster --driver-memory 4G --num-executors 5 --executor-memory 4G --executor-cores 5 fetch_data_from_server.py
# 

# In[ ]:


#from pyspark.sql import SparkSession
#from pyspark.sql import SQLContext # if needed'''


import os
import re

from pyspark.sql import *
from pyspark.sql.functions import unix_timestamp, udf, to_date
from pyspark.sql.types import ArrayType, StringType, IntegerType
from datetime import datetime

spark = SparkSession.builder.getOrCreate()
spark.conf.set('spark.sql.session.timeZone', 'UTC')
sc = spark.sparkContext


CLUSTER_DATA_DIR = '/datasets/twitter_internetarchive/2017/01/01/01/'
MY_DATA_DIR = '/user/cleres/data/'

extension = '.json.bz2'
for i in range(60):
    if i < 10 :
        name = '0' + str(i)
    else:
        name = str(i)

    posts_df = spark.read.json(CLUSTER_DATA_DIR + name + extension)
    posts_df.write.parquet(MY_DATA_DIR + name + '.parquet', mode = "overwrite")

'''
name = '00.json.bz2'

posts_df = spark.read.json(CLUSTER_DATA_DIR + name)
posts_df.write.parquet('dc.parquet', mode = "overwrite")
'''

    os.system('hdfs dfs -copyToLocal ' + MY_DATA_DIR + name + '.parquet ./') #save the files to local so that we can download it

#MY_DATA_DIR + name[0:2]
