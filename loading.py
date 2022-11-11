import psycopg2
import yaml

with open('params.yml') as f:
    params = yaml.safe_load(f)
 
postgres_table_name = params['postgres_table_name']
path = params['path']
dbname = params['dbname']
user = params['user']
password = params['password']
load_to_postgres = params['load_to_postgres']

def postgres_connection(dbname, user, password):
    conn = psycopg2.connect("dbname={0} user={1} password={2}".format(dbname, user, password))
    cursor = conn.cursor()
    
    return conn, cursor

    
def create_table(postgres_table_name, conn, cursor):

    sql ='''
            _id CHAR(45),
            file_name CHAR(20),
            date DATE,
            time INT,
            current FLOAT,
            voltage FLOAT
                            '''
        
    cursor.execute("CREATE TABLE IF NOT EXISTS %s(%s)"%(postgres_table_name, sql))
    conn.commit()

def put_data_to_db(conn, cursor, load_to_postgres):
    
    with open(path + load_to_postgres + '.csv', 'r+') as f:
        cursor.copy_expert("COPY electroplating_data FROM STDIN WITH CSV HEADER DELIMITER ','", f)
        conn.commit()
        conn.close()

  
    
    
    