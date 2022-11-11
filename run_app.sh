#!/bin/sh

echo  "set cron job for download data from mongodb every minute"
echo  "upload clean data to PostgresSQL"

crontab -e 
* * * * * python3 /tmp/ETL-pipeline-with-Kafka/dependency.py

echo  "starting python app"
python3 /tmp/ETL-pipeline-with-Kafka/main.py

echo "finished"