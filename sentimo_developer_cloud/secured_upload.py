# coding: utf-8
# secured_upload.py
from __future__ import absolute_import

# from urllib import parse
# import time
from .sentimo_service import SentimoService
from .utils.utils import Utils

# def construct_upload_data(content, post_id=None, source=None, user_id=None, post_time=None):
#     """ A function to construct upload data set
#     :param content: the input data that need to upload
#     :type  content: str/[str]
#     
#     :param post_id: the post_id on the input data
#     :type  post_id: str
#     
#     :param source: the source of input data
#     :type  source: str
#     
#     :param user_id: the user_id that shown on webpage of input data
#     :type  user_id: str
#     
#     :param post_time: the post time of the input data
#     :type  post_time: str
#     """
#     
#     params =[]
#     
#     for i in content:
#     
#         if(post_id == None):
#             post_id = 'default'
#         if(source == None):
#             source = 'default'
#         if(user_id ==None):
#             user_id = 'default'
#         if(post_time == None):
#             post_time = time.strftime('%Y-%m-%d-%H:%M:%S',time.localtime(time.time()))
#         
#         param = {'post_id': post_id, 
#                   'source': source, 
#                   'user_id' : user_id, 
#                   'post_time': post_time, 
#                   'content': i}
#         params.append(param)
#     
#     data = {'data' : params}
#     dataStr = str(data)
#   
#     return dataStr

class SecuredUpload(SentimoService):
    '''
    The Secured Upload class
    '''
    
    def __init__(self, url = None, token = None, timeout = 30 ):      
        """
        Construct a new client for the AnalyzeOvertheAir service.
                
        :param url: The base url to use when contacting the web service 
                (e.g. "https://sentimoplus.net/sentimo-webservice/rest")
        
        :param token: the PID token used to authenticate with the service.
        
        :param timeout: the timeout duration if the service doens't response
        
        example: /sentimo_developer_cloud/examples/SecuredUpload.py
        """
        
        SentimoService.__init__(self, url = url, token = token, timeout = timeout)
        
        
    def upload_data(self, content):    
        """ Interface wrapper of <upload> function of secured upload
        
        :param content: contents to be uploaded 
        :type  content: str
    
        :return: A 'dict' containing the result response
        
        example: /sentimo_developer_cloud/examples/SecuredUpload.py
        """
        
        if(len(content) > 5):
            return BaseException
        else:
            if(len(content) < 1):
                return BaseException
        
        data = Utils.construct_upload_data(content)
        api_endpoint = '/upload'
        response = self._api_request('POST', api_endpoint ,data = data)
        return response.json()
    
    def upload_full_dataset(self, data):
         
        """ Interface wrapper of <upload> function of secured upload
         
        :param data: full data set content of data to be uploaded 
        :type  data: str
     
        :return: A 'dict' containing the result response
         
        example: /sentimo_developer_cloud/examples/SecuredUpload.py
        """
         
        api_endpoint = '/upload'
        response = self._api_request('POST', api_endpoint ,data = data)
        return response.json()
#         
#     
#     
#     def retrieve_sentiment(self, id, domain=None ):
#         
#         """ Interface wrapper of <sentiment> function of retrieving sentiment data
#         
#         :param domain: target analysis domain
#         :type  domain: String
#         
#         :param id: target result id
#         :type  id: Str/[Str]
#         
#         :param domain: the domain information for the analysis data
#         :type  domain: str
#         
#         :return: A 'dict' containing the result response
#                 
#         example: /sentimo_developer_cloud/examples/SecuredUpload.py
#         
#         """
#         if(isinstance(id, str) == False):
#             id = str(id)
#         api_endpoint = '/ar/sentiment/' + parse.quote(id)
#         
#         if(domain != None): 
#             api_endpoint = '/ar/sentiment/' + parse.quote(domain) + '/' + parse.quote(id)
#         r  = self._api_request('GET', api_endpoint)
#         return r.json()
#     
#     
#     def retrieve_sentiment_set(self, id, domain=None, num=None ):
#         
#         """ Interface wrapper of <sentiment> function of retrieving sentiment data
#         
#         :param domain: target analysis domain
#         :type  domain: String
#         
#         :param id: target result id
#         :type  id: Str/[Str]
#         
#         :param domain: the domain information for the analysis data
#         :type  domain: str
#         
#         :return: A 'dict' containing the result response
#                 
#         example: /sentimo_developer_cloud/examples/SecuredUpload.py
#         
#         """
#         if(isinstance(id, str) == True):
#             if ',' in id:
#                 print('server only accept one id')
#                 return None
#         else:
#             id = str(id)
#             
#         api_endpoint = '/ar/sentiment/start/' + id
#         
#         if(domain != None): 
#             api_endpoint = '/ar/sentiment/' + parse.quote(domain) + '/start/' + id
#         
#         if(num != None):
#             if(isinstance(num, str) == False):
#                 num = str(num)
#             api_endpoint += ('?max=' + num)   
#         
#         r  = self._api_request('GET', api_endpoint)
#         return r.json()
#     
# 
#     def retrieve_sentimo_set(self, id, domain = None, num = None ):
#         
#         """ Interface wrapper of <sentiment> function of retrieving sentiment data
#         
#         :param domain: target analysis domain
#         :type domain: String
#         
#         :param id: target result id
#         :type id: String/[String]
#         
#         :param domain: the domain information for the analysis data
#         :type  domain: str
# 
#         :return: A 'dict' containing the result response
#                 
#         example: /sentimo_developer_cloud/examples/SecuredUpload.py
#         
#         """
#         
#         if(isinstance(id, str) == True):
#             if ',' in id:
#                 print('server only accept one id')
#                 return None
#         else:
#             id = str(id)
#             
#         api_endpoint = '/ar/sentimo/start/' + id
#         
#         if(domain != None): 
#             api_endpoint = '/ar/sentimo/' + parse.quote(domain) + '/start/' + id
#             
#         if(num!= None):
#             if(isinstance(num, str) == False):
#                 num = str(num)
#             api_endpoint += ('?max=' + num )
#         r  = self._api_request('GET', api_endpoint)
#         return r.json()
#     
#     def retrieve_sentimo(self, id, domain = None ):
#         
#         """ Interface wrapper of <sentiment> function of retrieving sentiment data
#         
#         :param domain: target analysis domain
#         :type domain: String
#         
#         :param id: target result id
#         :type id: String/[String]
#         
#         :param domain: the domain information for the analysis data
#         :type  domain: str
# 
#         :return: A 'dict' containing the result response
#                 
#         example: /sentimo_developer_cloud/examples/SecuredUpload.py
#         
#         """
#         if(isinstance(id, str) == False):
#             id = str(id)
#         api_endpoint = '/ar/sentimo/' + parse.quote(id)
#         
#         if(domain != None): 
#             api_endpoint = '/ar/sentimo/' + parse.quote(domain) + '/' + parse.quote(id)
#         r  = self._api_request('GET', api_endpoint)
#         return r.json()
    
    
    def _construct_upload_dataset(self, content, post_id=None, source=None, user_id=None, post_time=None): 
        """
        :param content: the input data that need to upload
        :type  content: str/[str]
        
        :param post_id: the post_id on the input data
        :type  post_id: str
        
        :param source: the source of input data
        :type  source: str
        
        :param user_id: the user_id that shown on webpage of input data
        :type  user_id: str
        
        :param post_time: the post time of the input data
        :type  post_time: str
        
        :return: An array containing upload input 'dict' data
        
        example: /sentimo_developer_cloud/examples/SecuredUpload.py
        """ 
        return Utils.construct_upload_data(content, post_id, source, user_id, post_time) 
        