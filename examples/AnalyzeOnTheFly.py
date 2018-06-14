from __future__ import print_function
from sentimo_developer_cloud.analyze_on_the_fly import AnalyzeOnTheFly
import json;

#Import DataFrame library to process the JSON data
from pandas.io.json import json_normalize
import pandas as pd

#Import default configuration value from './config.json'
with open('./../config.json') as json_cfg_file:
    cfg = json.load(json_cfg_file)

platform_url = cfg['url']
pid = cfg['token']
timeout = cfg['timeout']

#Initial the service
aoa = AnalyzeOnTheFly(
    url = platform_url,
    token = pid,
    timeout=timeout)

print('############# start test : ##############')

sample_string = 'Singapore is a fine place.' 
##### one sentence case #####
def analyze_general_sentiment_from_sentence():
    sentiment_response = aoa.analyze_sentiment_on_the_fly(sample_string)
    print(sentiment_response) 
    data = eval(sentiment_response['result'])
    df = json_normalize(data[0]['objects']);
    print(df);
    

def analyze_fine_grained_emotion_from_sentence():
    emotion_response = aoa.analyze_sentimo_on_the_fly(sample_string) 
    print(emotion_response) 
    data = eval(emotion_response['result']) 
    scores = json_normalize(data[0]['objects'][0]['scores'])
    print(scores.to_string())
  
##### sentences set case ######
sample_strings = ['Singapore is a fine place.', 'Today is good weather.']
sample_set = aoa._construct_raw_dataset(sample_strings)
print(sample_set)

def analyze_general_sentiment_from_sentence_set():
    sentiment_response = aoa.analyze_sentiment_full_dataset_on_the_fly(sample_set)
    print(sentiment_response)
    data = eval(sentiment_response['result'])
    df = json_normalize(data)
    print(df.to_string())

def analyze_fine_grained_emotion_from_sentence_set():
    emotion_response = aoa.analyze_sentimo_full_dataset_on_the_fly(sample_set)
    print(emotion_response)
    data = eval(emotion_response['result'])
    df = json_normalize(data)
    print(df.to_string())
    
    
analyze_general_sentiment_from_sentence()
analyze_fine_grained_emotion_from_sentence()
analyze_general_sentiment_from_sentence_set()
analyze_fine_grained_emotion_from_sentence_set()