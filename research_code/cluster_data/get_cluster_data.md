# Easy access to the data on the cluster

- STEP 1: [SSH Connection requiered] copy the data from the cluster environment (Hadoop) to the local environment (/home/cleres)

  ```hadoop fs -get /datasets/twitter_internetarchive/2017/01/01/01/* /home/cleres```

- STEP 2: [in the terminal of your laptop - no SSH] Copy the data from your home folderon the cluster to your local machine

  ```scp -r -p cleres@iccluster028.iccluster.epfl.ch:/home/cleres/*.json.bz2 ./``` 

