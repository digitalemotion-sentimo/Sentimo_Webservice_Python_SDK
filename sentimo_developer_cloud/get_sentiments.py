# coding: utf-8
# retrieve_data.py
from __future__ import absolute_import

from urllib import parse
from .sentimo_service import SentimoService

class GetSentiments(SentimoService):
    '''
    The Get Result class
    '''    
    def __init__(self, url = None, token = None, timeout = 30 ):
        
        """
        Construct a new client for the GetSentiments service.
                
        :param url: The base url to use when contacting the web service 
                (e.g. "https://sentimoplus.net/sentimo-webservice/rest")
        
        :param token: the PID token used to authenticate with the service.
        
        :param timeout: the timeout duration if the service doens't response
        
        example: /sentimo_developer_cloud/examples/SecuredUpload.py
        """
        
        SentimoService.__init__(self, url = url, token = token, timeout = timeout)
        


    def retrieve_sentiment(self, dataIds, domain=None ):
        
        """ In this method, users can indicate the Data IDs of the data to retrieve the analysis results. 
        Data IDs need not be in sequence. Users can also indicate their domain of interest in the request.
        
        :param dataIds: target result dataIds
        :type  dataIds: Str/[Str]
        
        :param domain: the domain information for the analysis data
        :type  domain: str
        
        :return: A 'dict' containing the result response
                
        example: /sentimo_developer_cloud/examples/SecuredUpload.py
        
        """
        if(isinstance(dataIds, str) == False):
            dataIds = str(dataIds)
        api_endpoint = '/ar/sentiment/' + parse.quote(dataIds)
        
        if(domain != None): 
            api_endpoint = '/ar/sentiment/' + parse.quote(domain) + '/' + parse.quote(dataIds)
        r  = self._api_request('GET', api_endpoint)
        return r.json()
    
    
    def retrieve_sentiment_set(self, dataId, domain=None, num=None ):
        """ This method returns the analysis results of a series of Data IDs in sequence. 
        Users can specify the starting Data ID and specify the number of data records they 
        want analysed. Users can also indicate their domain of interest in the request and
        the maximum number of return records. The default size of records returned is 20
        if the max parameter is omited.The maximum size of records cannot exceed 100. 
        
        :param domain: target analysis domain
        :type  domain: String
        
        :param id: target result ID/ target result IDs list
        :type  id: Str/[Str]
        
        :param domain: the domain information for the analysis data
        :type  domain: str
        
        :return: A 'dict' containing the result response
                
        example: /sentimo_developer_cloud/examples/SecuredUpload.py
        
        """
        if(isinstance(dataId, str) == True):
            if ',' in dataId:
                print('server only accept one id')
                return None
        else:
            dataId = str(dataId)
            
        api_endpoint = '/ar/sentiment/start/' + dataId
        
        if(domain != None): 
            api_endpoint = '/ar/sentiment/' + parse.quote(domain) + '/start/' + dataId
        
        if(num != None):
            if(isinstance(num, str) == False):
                num = str(num)
            api_endpoint += ('?max=' + num)   
        
        r  = self._api_request('GET', api_endpoint)
        return r.json()
    

    '''Fine-grained Emotion Analysis'''
    def retrieve_sentimo(self, dataIds, domain = None ):
        """ In this method, users can indicate the Data IDs of the data to retrieve the analysis results. 
        Data IDs need not be in sequence.  Users can also indicate their domain of interest in the request.
        
        :param domain: target analysis domain
        :type domain: String
        
        :param dataIds: target result id
        :type dataIds: String/[String]
        
        :param domain: the domain information for the analysis data
        :type  domain: str

        :return: A 'dict' containing the result response
                
        example: /sentimo_developer_cloud/examples/SecuredUpload.py
        
        """
        if(isinstance(dataIds, str) == False):
            dataIds = str(dataIds)
        api_endpoint = '/ar/sentimo/' + parse.quote(dataIds)
        
        if(domain != None): 
            api_endpoint = '/ar/sentimo/' + parse.quote(domain) + '/' + parse.quote(dataIds)
        r  = self._api_request('GET', api_endpoint)
        return r.json()
    

    def retrieve_sentimo_set(self, dataId, domain = None, num = None ):
        """ This methods returns the analysis results of a series of Data IDs in sequence. 
        Users can specify the starting Data ID and specify the number of data records they wish to retrieve, 
        and the maximum number of records to return. The default size for records returned is 20, 
        if the max parameter is omitted. The maximum size of records cannot exceed 100.
        
        :param domain: target analysis domain
        :type domain: String
        
        :param dataId: target result id
        :type dataId: String/[String]
        
        :param domain: the domain information for the analysis data
        :type  domain: str

        :return: A 'dict' containing the result response
                
        example: /sentimo_developer_cloud/examples/SecuredUpload.py
        
        """
        
        if(isinstance(dataId, str) == True):
            if ',' in id:
                print('server only accept one id')
                return None
        else:
            dataId = str(dataId)
            
        api_endpoint = '/ar/sentimo/start/' + dataId
        
        if(domain != None): 
            api_endpoint = '/ar/sentimo/' + parse.quote(domain) + '/start/' + dataId
            
        if(num!= None):
            if(isinstance(num, str) == False):
                num = str(num)
            api_endpoint += ('?max=' + num )
        r  = self._api_request('GET', api_endpoint)
        return r.json()
    
