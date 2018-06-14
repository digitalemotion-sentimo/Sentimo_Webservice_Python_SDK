from __future__ import print_function
from sentimo_developer_cloud.secured_upload import SecuredUpload
from sentimo_developer_cloud.get_sentiments import GetSentiments
import json
import time

#Import default configuration value from './config.json'
with open('./../config.json') as json_cfg_file:
    cfg = json.load(json_cfg_file)

platform_url = cfg['url']
pid = cfg['token']
timeout = cfg['timeout']

#Initial the service
up = SecuredUpload(
    url = platform_url,
    token = pid,
    timeout = timeout)

rr = GetSentiments(
    url = platform_url,
    token = pid)

###########Test-for-sentence-update######################
sample_string = ['Singapore is a fine place.']


def upload_sentence_data():
    response = up.upload_data(sample_string)
    data_ids = json.dumps(response['data_ids']).strip('[').strip(']').replace(' ','')
    print(response)

    time.sleep(12)

    response = rr.retrieve_sentiment(data_ids)
    print(response)
      
    response = rr.retrieve_sentimo(data_ids)
    print(response)



###########Test-for-data-set-update######################
sample_set = up._construct_upload_dataset(sample_string, 'Airtest', 'network', 'ihpc', '2018-03-23')

def upload_dataset():
    response = up.upload_full_dataset(sample_set)
    data_ids = json.dumps(response['data_ids']).strip('[').strip(']').replace(' ','')
    print(response)
    
    time.sleep(12)
     
    response = rr.retrieve_sentiment(data_ids)
    print(response)
       
    response = rr.retrieve_sentimo(data_ids)
    print(response)

#Run the upload data case
upload_dataset()
