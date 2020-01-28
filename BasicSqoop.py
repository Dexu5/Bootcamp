/mnt/data1/jobs/p800s1/sqoop/sqoop.py ## Location where the sqoop job is stored
--source_jdbc_connection_string jdbc:oracle:thin:@//xgrain-q-clt:1521/GRAINQ_PRI ## Source Location
--source_user DBO ## Source Username
--hdfs_target_path /shared_workspace/gbs/training_feb_2018/g559942/ ## Target path of HDFS
--hdfs_path_to_password_file /shared_workspace/gbs/training_feb_2018/g559942/.UGSdbo ## Password file stored in HDFS
--source_table DBO.TEMIS_CHARACTERISTIC ## Source Table 
--auto_create_target_table ## Auto create the table structure based on source table
--target_database wksp_gbs_training_feb_2018 ## Target DB name
--target_table_name sqoop_test ## Target Table name
--delete_target_dir ## Delete the directory before adding
