from __future__ import print_function
from sentimo_developer_cloud.get_sentiments import GetSentiments
import json;

#Import DataFrame library to process the JSON data
import pandas as pd
from pandas.io.json import json_normalize

#Import default configuration value from './config.json'
with open('./../config.json') as json_cfg_file:
    cfg = json.load(json_cfg_file)

platform_url = cfg['url']
pid = cfg['token']
timeout = cfg['timeout']

#Initial the service
rr = GetSentiments(
    url = platform_url,
    token = pid,
    timeout = timeout)

#Set an initial data_id
data_ids = 165996

#Example Case 1:
def retrieve_general_sentiment_from_dataid():
    response = rr.retrieve_sentiment(data_ids)
    print(response)
    #Process the response as DataFrame format
    analyseData = response['results'][0]['data'][0]
    df = json_normalize(analyseData);
    print(df);


#Example Case 2:
def  retrieve_general_sentiment_set_from_dataid():
    response = rr.retrieve_sentiment_set(data_ids,num=50)
    print(response)
    
    #Process the response as DataFrame format
    analyseData = response['results'][0]['data']
    df = pd.DataFrame.from_dict(json_normalize(analyseData), orient = 'columns')
    print(df.to_string());

def retrieve_fine_grained_emotion_from_dataid():
    response = rr.retrieve_sentimo(data_ids)
    print(response)
    #Process the response as DataFrame format
    analyseData = response['results'][0]['data'][0]['objects']
    analyseScores = response['results'][0]['data'][0]['objects'][0]['scores']
    print(json_normalize(analyseData).to_string());
    print(json_normalize(analyseScores).to_string());

def retrieve_fine_grained_emotion_set_from_dataid():
    response = rr.retrieve_sentimo_set(data_ids,num=40)
    print(response)
    #Process the response as DataFrame format
    analyseData = response['results'][0]['data']
    df = pd.DataFrame.from_dict(json_normalize(analyseData), orient = 'columns')
    print(df.to_string());
    
    
#Run the test case    
retrieve_general_sentiment_from_dataid()
retrieve_general_sentiment_set_from_dataid()
retrieve_fine_grained_emotion_from_dataid()
retrieve_fine_grained_emotion_set_from_dataid()


