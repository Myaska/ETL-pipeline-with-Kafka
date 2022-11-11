import extraction as ex
import yaml
import loading as ld
import transformation as tf

with open('params.yml') as f:
    params = yaml.safe_load(f)
    
postgres_table_name = params['postgres_table_name']
path = params['path']
dbname = params['dbname']
user = params['user']
password = params['password']
load_to_postgres = params['load_to_postgres']   

db, collection = ex.mongo_connection(params['mongo_client'], params['db_name'])
tf.quality_control(db)
tf.save_clean_data(collection)

conn, cursor = ld.postgres_connection(dbname, user, password)
ld.create_table(postgres_table_name, conn, cursor)
ld.put_data_to_db(conn, cursor, load_to_postgres)
