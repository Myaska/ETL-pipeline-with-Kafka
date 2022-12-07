# ETL pipeline with Kafka
<img width="916" alt="Screen Shot 2022-11-11 at 2 45 05 PM" src="https://user-images.githubusercontent.com/72933965/201428156-ae1347cb-4fbb-481c-bcc9-de40936a7113.png">

### Before run this app you should:
  - download and install Apache Kafka (https://kafka.apache.org/)
  - go to the kafka-folder in CLI:
      - `cd 'derectory kafka-folder'`
  - run the following commands in CLI: 
      - `bin/zookeeper-server-start.sh config/zookeeper.properties`
      - `bin/kafka-server-start.sh config/server.properties`
  - create a DataBase in PostgresSQL where you want to load data

### Change parameters in params.yml:
  - file_name : choose the file name 
  - path : put the path to the folder with all this files in your computer

#### MongoDB
  - bootstrap_servers : localhost:9092
  - mongo_client : change `<user_name>` and `<password>` on yours
  - db_name : choose the database name in MongoDB
  - comNum : check the port number in your device
  - set up duration of experiment, current and voltage

#### PostgresSQL
  - dbname : choose the database name in PostgresSLQ
  - user : set up your username
  - password : set up your password
  - postgres_table_name : choose the table name
  - load_to_postgres : choose the file name where clean data will be saved
  
### To run the app execute the following commands:
  - tested in Python 3.9.12
  - pip install -r requirements.txt
  - sh run_app.sh

