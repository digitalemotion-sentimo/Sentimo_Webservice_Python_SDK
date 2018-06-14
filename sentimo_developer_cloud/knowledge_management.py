from __future__ import absolute_import

from urllib import parse
from .sentimo_service import SentimoService
import json

class KnowledgeManagement(SentimoService):
    '''
    The Knowledge Management class
    ''' 
    def __init__(self, url = None, token = None, timeout = 30):
        """
        Construct a new client for the KnowldegeManagement service.
                
        :param url: The base url to use when contacting the web service 
                (e.g. "https://sentimoplus.net/sentimo-webservice/rest")
        
        :param token: the PID token used to authenticate with the service.
        
        :param timeout: the timeout duration if the service doens't response
        
        example: /sentimo_developer_cloud/examples/SecuredUpload.py
        """
        SentimoService.__init__(self, url = url, token = token, timeout = timeout)
        
    def add_dictionary(self, dataset, domain = None):
        
        '''Interface wrapper of <km> function of dictionary management
        
        :param dataset: opinion(s) full dataset/full dataset array to be analyzed
        :type JSON Array, required = true
              :param category_code, required = true
              :type str
                  (possible values: Negate, Positive, Negative, Anxiety, Anger, Sadness, Satisfaction, Happiness, Excitement)
              :param sentimo_word, required = true
              :type str
        
        :param domain: Analysis domain
        :type str


        :return: A 'dict' containing the result response
        
        example: /sentimo_developer_cloud/examples/KnowledgeManagement.py
        '''
        
        function_endpoint = '/km/dict/add'
        
        if(domain != None):
            function_endpoint = '?domain=' + parse.quote(domain)
            
        in_json = json.dumps(dataset, separators = (',',':'))   
        
        response = self._api_request(method = 'POST', path = function_endpoint, data = str(in_json))
        
        return response.json()
        
    def update_dictionary(self, dataset, domain = None):
        
        '''Interface wrapper of <km> function of dictionary management
        
        :param dataset: opinion(s) full dataset/full dataset array to be analyzed
        :type JSON Array, required = true
              :param id Target Id in database, required = true
              :type str
              :param category_code, required = true
              :type str
                  (possible values: Negate, Positive, Negative, Anxiety, Anger, Sadness, Satisfaction, Happiness, Excitement)
              :param sentimo_word, required = true
              :type str
        
        :param domain: Analysis domain
        :type str


        :return: A 'dict' containing the result response
        
        example: /sentimo_developer_cloud/examples/KnowledgeManagement.py
        '''
        
        function_endpoint = '/km/dict/update'
        
        if(domain != None):
            function_endpoint = '?domain=' + parse.quote(domain)

        in_json = json.dumps(dataset, separators = (',',':'))
        
#         response = self._api_request('POST', path = function_endpoint, data = str(in_json))
        response = self._api_request('POST', path = function_endpoint, data = in_json)
        
        return response.json()
    
    def delete_dictionary(self, dataIds):
        
        '''Interface wrapper of <km> function of dictionary management
        
        :param dataId: Target ID in database
        :type str

        :return: A 'dict' containing the result response
        
        example: /sentimo_developer_cloud/examples/KnowledgeManagement.py
        '''
        
        function_endpoint = ''
        
        if(type(dataIds) != type([])):
            return BaseException
        else:
            if(len(dataIds)>0):
                for id in dataIds:
                    function_endpoint += ('Ids=' + str(id) + '&')
            else:
                return BaseException
    
        function_endpoint = '/km/dict/delete?' + function_endpoint[0:-1]
        
        response = self._api_request(method = 'POST', path = function_endpoint)
        
        return response.json()
        
        
    def get_dictionary_item(self, dataId):
        '''Interface wrapper of <km> function of dictionary management
        
        :param dataId: Target ID in database
        :type str

        :return: A 'dict' containing the result response
        
        example: /sentimo_developer_cloud/examples/KnowledgeManagement.py
        '''
                
        function_endpoint = '/km/dict/get?id=' + parse.quote(str(dataId))
        
        response = self._api_request(method ='GET', path = function_endpoint)
        
        return response.json()
        
        
    def get_dictionary_list(self, domain =None):
        '''Interface wrapper of <km> function of dictionary management
        
        :param domain: Analysis domain
        :type str


        :return: A 'dict' containing the result response
        
        example: /sentimo_developer_cloud/examples/KnowledgeManagement.py
        '''
                
        function_endpoint = '/km/dict/list'
        
        if(domain != None):
            function_endpoint += '?domain=' + parse.quote(domain)
            
        response = self._api_request(method = 'GET', path = function_endpoint)
        
        return response.json()