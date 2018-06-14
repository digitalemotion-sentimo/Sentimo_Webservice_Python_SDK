from __future__ import print_function
from sentimo_developer_cloud.knowledge_management import KnowledgeManagement
import json

#Import DataFrame library to process the JSON data
# from pandas.io.json import json_normalize
# import pandas as pd

#Import default configuration value from './config.json'
with open('./../config.json') as json_cfg_file:
    cfg = json.load(json_cfg_file)
    
platform_url = cfg['url']
pid = cfg['token']
timeout = cfg['timeout']

#Initial the service
service = KnowledgeManagement(
    url = platform_url,
    token = pid,
    timeout=timeout)

print('############# start test : ##############')

####### Add item in dictionary #############
sample = [{"category_code": "Negate", "sentimo_word":"cool ah."}]
res = service.add_dictionary(sample)
print(res)

########## Update item in dictionary ##########
[{"id": "0", "category_code": "Negate", "sentimo_word": "string"}]
sample = [{"id": "0", "category_code": "Negate", "sentimo_word":"cool ah."}]
res = service.update_dictionary(sample)
print(res)

####### search dictionary list ##########
res = service.get_dictionary_list("general,healthcare,travel")
print(res)

####### search dictionary list ##########
res = service.get_dictionary_list("general")
print(res)

########## search dictionary item ########
dataId = '176544'
res = service.get_dictionary_item(dataId)
print(res)

####### Delete dictionary data ##########
#assume Id is 176544
dataIds = [176544]
res = service.delete_dictionary(dataIds)
print(res)


