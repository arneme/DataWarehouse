# Data Warehouse project

## Table of Contents

1. [Discuss the purpose of this database in the context of the startup, Sparkify, and their analytical goals](#discuss)
2. [Redshift as both staging and dimension table database](#redshift)
3. [How to run the scripts](#run)
4. [Notes](#notes)

## <a name="discuss"></a>Discuss the purpose of this database
The purpose of this database is to provide Sparkify the necessary tool to retrieve vital, business oriented, information about their service. Their current main focus is to be able to, easily and fast, to retrieve information about which songs users are listening to. They do have information about this stored in logfiles already but it is not easy to search or aggregate data from these logfiles. In this assignment we have been asked to transform data from the logfiles together with meta data about songs (also stored in files) into a database design that will allow Sparkify to meet their business need related to finding out which songs their users are listening to.

The purpose of using Redshift is to allow for scalability and fast answers to (business analytics oriented) queries.

## <a name="run"></a>How to run the scripts
The script can be runned in several ways. I have been running it inside a JupyterLab setup (Anaconda) on my own laptop. It is also possible to run the etl.py script directly in python3.

### Setup a Redshift Cluster using your AWS Console
It is  necessary to setup the Redshift cluster used by the etl.py script before running the script in order for the script to run without errors. This can be done either in the AWS Console or programatically. I did it in the AWS Console using the Quick Deploy option. It is also important to edit the default security group (that quick launch adds to the cluster) to allow access from the IP address the etl.py script is run on.

When creating the Redshift cluster I attached a role that allows the Redshift cluster to access S3 (read). This is necessary in order for the COPY SQL statements to work.

### Add the IAM and Redshift setup to the config file
Copy the Redshift role ARN to the _dwh.cfg_ config file
Copy the Redshift cluster configuration you specify when creating the Redshift cluster using Quick Launch (HOST, DB_NAME, DB_USER, DB_PASSWORD and DB_PORT) to the _dwh.cfg_ config file. Note that the HOST name will not be available until the cluster is up and running.

### Run etl.py standalone
The Python 3 installation must have psycopg2 packages installed (pip3 install psycopg2-binary)
Run:<br/><br/>
_python3 etl.py_

If you want to drop existing tables you can run the script like this:<br/><br/>
_python3 etl.py --drop 1_

If you intend to run it under Anaconda Jupyter Lab you will need to install the psycopg2 for your Anaconda installation (conda install -c anaconda psycopg)

## <a name="redshift"></a>Redshift as both staging and dimension table database
In this project we will use Redshift to hold both the staging tables and the dimension and fact tables. The staging tables are just mirroring the logfile and songfile content into two tables; *log_events_table* and *song_table*. From the staging tables we will use COPY statements to transfer the content from the staging tables to the selected dimension and fact tables.

The staging tables has been defined with all fields without "NOT NULL". This is to make sure that all staging data is copied from S3 and that errors does not occur during copying into the staging tables.


