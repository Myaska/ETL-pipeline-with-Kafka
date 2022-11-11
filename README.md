# ETL pipeline with Kafka
<img width="923" alt="Screen Shot 2022-11-11 at 2 23 58 PM" src="https://user-images.githubusercontent.com/72933965/201425697-900b572d-7962-4bfd-8ed2-e1e0c0fb680a.png">

### Befor run this up you should:
- download and install Apache Kafka (https://kafka.apache.org/)
- go to the kafka-folder and run the following commands:
  bin/zookeeper-server-start.sh config/zookeeper.properties
  bin/kafka-server-start.sh config/server.properties
- create a DataBase in PostgresSQL where you want to load data

### Change parameters in params.yml:
- file_name : choose the file name 
- path : put the path to the folder with all this files in your computer

#### MongoDB
- bootstrap_servers : localhost:9092
- mongo_client : mongodb+srv://<user_name>:<password>@cluster0.uplpgvn.mongodb.net/?retryWrites=true&w=majority 
  change <user_name>:<password> on yours
- db_name : choose the database name in MongoDB

- comNum : /dev/tty.usbserial-506J19110
- set up duration of experiment, current and voltage

#### PostgresSQL
- dbname : choose the database name in PostgresSLQ
- user : set up your username
- password : set up your password
- postgres_table_name : choose the table name
- load_to_postgres : choose the file name where clean data will be saved

