import serial
import time
from pykafka import KafkaClient
from pymongo import MongoClient

def port_connection(comNum):
    ser = serial.Serial(comNum, 57600)
    ser.flush()
    ser.write("*idn?\n".encode())
    print(ser.readline())
    
    return ser

def set_curr_and_volt(curr, volt, ser):
    ser.write("SYS:BEEP OFF\n".encode())
    ser.write("SOUR:CURR {curr}\n".format(curr = curr).encode())
    ser.write("SOUR:VOLT {volt}\n".format(volt = volt).encode())

def set_timer(hour, minute, sec, ser):
    ser.write("TIMER:ON\n".encode())
    ser.write("TIMER:HOUR {hour}\n".format(hour = hour).encode())
    ser.write("TIMER:MIN {minute}\n".format(minute = minute).encode())
    ser.write("TIMER:SEC {sec}\n".format(sec = sec).encode())
    ser.write("OUT ON\n".encode())

def set_limits(lim_volt, lim_curr, ser):
    ser.write("OUT:LIM:VOLT 23\n".encode())
    ser.write("OUT:LIM:CURR 0.300\n".encode())

def memory_rec(mem_slot, m_volt, m_curr, ser):
    ser.write("MEM 0\n".encode())
    ser.write("MEM:VSET 10.000\n".encode())
    ser.write("MEM:ISET 0.200\n".encode())
    ser.write("MEM:SAV\n".encode())
   
def mongo_connection(mongo_client, db_name):
    client = MongoClient(mongo_client)
    db = client.test_database
    db = client[db_name]
    collection = db.test_collection
    collection = db[db_name]
    
    return db, collection 

def create_topic(bootstrap_servers):
    client = KafkaClient(hosts = bootstrap_servers)
    
    topic_vol = client.topics[b'volt']
    topic_cur = client.topics[b'curr']
    
    return topic_vol, topic_cur

def kafka_connection(topic_vol, topic_cur):
    
    consumer_vol = topic_vol.get_simple_consumer()
    consumer_cur = topic_cur.get_simple_consumer()
    
    producer_vol = topic_vol.get_sync_producer()
    producer_cur = topic_cur.get_sync_producer()    
    
    return consumer_vol, consumer_cur, producer_vol, producer_cur

def data_collect(collection, run_time, file_name, path, ser, consumer_vol, consumer_cur, producer_vol, producer_cur):
      
    for i in range(run_time):
        ser.write("MEAS:VOLT?\n".encode())
        voltage = ser.readline().decode("utf-8").strip()
        encoded_voltage = voltage.encode("utf-8")

        ser.write("MEAS:CURR?\n".encode())
        current = ser.readline().decode("utf-8").strip()
        encoded_current = current.encode("utf-8")
        
        producer_vol.produce(encoded_voltage)
        read_vol = consumer_vol.consume()
        msg_vol = float(read_vol.value.decode("utf-8").strip())
   
        producer_cur.produce(encoded_current)
        read_cur = consumer_cur.consume()
        msg_cur = float(read_cur.value.decode("utf-8").strip())       
        #time.sleep(1) 

        data = {'file_name' : file_name,
                'date': time.ctime(),
                'time' : i,
                'current' : msg_cur, 
                'voltage' : msg_vol}
        print(data)
        collection.insert_one(data)

            
    print('Experiment was compleated')
    ser.close()
    
    #return current, voltage, time

