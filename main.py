import extraction as ex
import yaml

def main(params):
    file_name = params['file_name']
    path = params['path']
    bootstrap_servers = params['bootstrap_servers']
    mongo_client = params['mongo_client']
    comNum = params['comNum']
    db_name = params['db_name']
    
    hour = params['hour']
    minute = params['minute']
    sec = params['sec']
    volt = params['volt']
    curr = params['curr']
    
    run_time = hour*3600 + minute*60 + sec
    

    ser = ex.port_connection(comNum)
    ex.set_curr_and_volt(curr, volt, ser)
    ex.set_timer(hour, minute, sec, ser)

    topic_vol, topic_cur = ex.create_topic(bootstrap_servers)
    consumer_vol, consumer_cur, producer_vol, producer_cur = ex.kafka_connection(topic_vol, topic_cur)
    db, collection = ex.mongo_connection(mongo_client, db_name)
    ex.data_collect(collection, run_time, file_name, path, ser, consumer_vol, consumer_cur, producer_vol, producer_cur)
    
if __name__ == __main__:
    with open('params.yml') as f:
        params = yaml.safe_load(f)
    
    main(params)
