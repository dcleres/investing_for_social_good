# Easy access to the data on the cluster

- **STEP 1**: SSH coonection to the cluster : 
  ```ssh cleres@iccluster028.iccluster.epfl.ch```

- **STEP 2**: Upload your script on the server [outside from ssh]: 

  ```scp -r -p FILE cleres@iccluster028.iccluster.epfl.ch:/home/cleres/```
  INFO: This is uploading the code to the local environment on the server. 

- **STEP 3**: Run your script on the cluster [in SSH Connection]: 

  ```python ON_CLUSTER_retrieve_data_hours```

- ```spark-submit --master yarn --deploy-mode cluster --driver-memory 4G --num-executors 5 --executor-memory 4G --executor-cores 5 fetch_data_from_server.py
  spark-submit --master yarn --deploy-mode cluster --driver-memory 4G --num-executors 5 --executor-memory 4G --executor-cores 5 ON_CLUSTER_retrieve_data_hours
  ```

  - INFO: The script is basically doing this [SSH Connection requiered] : copy the data from the cluster environment (Hadoop) to the local environment (/home/cleres)

  ```hadoop fs -get /datasets/twitter_internetarchive/2017/01/01/01/* /home/cleres```

- **STEP 4**: [in the terminal of your laptop - no SSH] Copy the data from your home folderon the cluster to your local machine

  ```scp -r -p cleres@iccluster028.iccluster.epfl.ch:/home/cleres/*.json.bz2 ./``` 

- NOTE: Setup-up an automatic SSH connection to the server without passord 
  ```ssh-copy-id id@server```if you already set-up and SSH id at some point otherwise you need to create an id with : 

  ```
  ssh-keygen -t rsa -b 2048
  Generating public/private rsa key pair.
  Enter file in which to save the key (/home/username/.ssh/id_rsa): 
  Enter passphrase (empty for no passphrase): 
  Enter same passphrase again: 
  Your identification has been saved in /home/username/.ssh/id_rsa.
  Your public key has been saved in /home/username/.ssh/id_rsa.pub.
  ```

