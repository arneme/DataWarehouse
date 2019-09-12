<<<<<<< HEAD
# Data Warehouse project

## Table of Contents

1. [Discuss the purpose of this database in the context of the startup, Sparkify, and their analytical goals](#discuss)
2. [Redshift as both staging and dimension table database](#redshift)
3. [How to run the scripts](#run)
4. [Notes](#notes)

## <a name="discuss"></a>Discuss the purpose of this database
The purpose of this database is to provide Sparkify the necessary tool to retrieve vital, business oriented, information about their service. Their current main focus is to be able to, easily and fast, to retrieve information about which songs users are listening to. They do have information about this stored in logfiles already but it is not easy to search or aggregate data from these logfiles. In this assignment we have been asked to transform data from the logfiles together with meta data about songs (also stored in files) into a database design that will allow Sparkify to meet their business need related to finding out which songs their users are listening to.

## <a name="run"></a>How to run the scripts
In order for the scripts to run successfully it is required that an apprpriate IAM user is created in order to be able to access and read from the S3 buckets containing log data and song data.

It is also necessary to setup the Redshift cluster used by the etl.py script in order for the script to run without errors.

### Create an IAM user using your AWS Console
Use your AWS Console to add a user that at least has S3 read rights.

### Setup a Redshift Cluster using your AWS Console
Use your AWS Console to setup a Redshift cluster.

### Add the IAM and Redshift setup to the config file
Copy the IAM ARN to the _dwh.cfg_ config file
Copy the Redshift cluster configuration (HOST, DB_NAME, DB_USER, DB_PASSWORD and DB_PORT) to the _dwh.cfg_ config file

### Run etl.py
_python3 etl.py_

## <a name="redshift"></a>Redshift as both staging and dimension table database
In this project we will use Redshift to hold both the staging tables and the dimension and fact tables. The staging tables are just mirroring the logfile and songfile content into two tables; *log_events_table* and *song_table*. From the staging tables we will use COPY statements to transfer the content from the staging tables to the selected dimension and fact tables.
=======
# Data Warehouse project
Documentation is TBD
>>>>>>> 02dbbc0d1613f0b8f6c7bfc59c2f19d92e080a4b
