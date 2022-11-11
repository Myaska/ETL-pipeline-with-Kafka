import extraction as ex
import yaml
import pandas as pd
import loading as ld


with open('params.yml') as f:
    params = yaml.safe_load(f)
    
def quality_control(db):
    
    db[params['db_name']].delete_many({'current':{ "$lt" : 0.01}})
    db[params['db_name']].delete_many({'voltage':{ "$gt" : 21.0}})
    

def save_clean_data(collection):
    for_clean_data = []
    for post in collection.find():     
        if post.get('time') %2 == 0:
            for_clean_data.append(post)
            clean_data = pd.DataFrame(for_clean_data)
            clean_data.to_csv(params['load_to_postgres'] + '.csv', index=False)

