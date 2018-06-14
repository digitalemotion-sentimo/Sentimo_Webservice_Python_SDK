# AnalyzeOntheAir Module
from __future__ import absolute_import

from urllib import parse
from .sentimo_service import SentimoService
from .utils.utils import Utils

# def construct_aoa_data_array(content, title = None, data_type=None, user_id = None, screen_name=None, post_count= None, 
#                       post_time= None , msg_from= None, url=None, source = None):
#     
#     '''This is to construct the format of analysis data.
#     
#     :param content: analysis content to input
#     :type  content: str/[str] 
#     
#     :param title: title of the content
#     :type  title: str
#     
#     :param data_type: the type of input data 
#     :type  data_type: str
#     
#     :param user_id: the user_id of the input information 
#     :type  user_id: str
#     
#     :param screen_name: the display of user name in webstie
#     :type  screen_name: str
#     
#     :param post_count: the total count number of target user's post
#     :type  post_count: str
#     
#     :param post_time: the post time of input data
#     :type  post_time: str
#     
#     :param msg_from: the origin source of input data if the content is not originated
#     :type  msg_from: str
#     
#     :param url: the base url to retrive the information
#     :type  url: str
#     
#     :param source: the source of soical platform
#     :type  source: str
#     
#     example: /sentimo_developer_cloud/examples/AnalyzeOvertheAir.py
#     
#     '''
#     
#     params = []
#     
#     for i in content:
#         param = construct_aoa_data(i, title, data_type, user_id, screen_name, post_count, post_time, msg_from, url, source)
#         params.append(param)
#     
#     in_json = json.dumps(params, separators = (',',':'))
# 
#     return str(in_json)
# 
# def construct_aoa_data(content, title = None, data_type=None, user_id = None, screen_name=None, post_count= None, 
#                       post_time= None , msg_from= None, url=None, source = None):
#     
#     if(title == None):
#             title = 'default'
#     if(data_type == None):
#         data_type = 'String'
#     if(source == None):
#         source = 'default'
#     if(user_id ==None):
#         user_id = 'default'
#     if(screen_name== None):
#         screen_name = 'default'
#     if(post_count == None):
#         post_count = '0'
#     if(msg_from == None):
#         msg_from = 'default'    
#     if(url == None):
#         url= 'default'
#     if(post_time == None):
#         post_time = time.strftime('%Y-%m-%dT%H:%M:%S.000Z',time.localtime(time.time()))
#     
#     param = {'title' : title,
#               'type' : data_type , 
#               'user_id' : user_id,
#               'source': source,
#               'screen_name': screen_name,
#               'userjoindate' : 0,
#               'postcount' : post_count,
#               'post_time' : post_time,
#               'post_id': "default",
#               'content' : content,
#               'reply_to_post_id': "-",
#               'reply_to_uid': "-",
#               'msg_from': msg_from,
#               'likes' : 0,
#               'url' : url}
#                   
#     return param
   
   
class AnalyzeOnTheFly(SentimoService):
    '''
    This call allows for immediate analysis of data sent in the request body, 
    returning results of the general sentiment analysis if the sentiment module is called, 
    and the fine-grained emotion analysis if the sentimo module is called.   
    '''
    
    def __init__(self, url = None, token = None, timeout = 30):
        '''
        Construct a new client for the AnalyzeOvertheAir service.
        
        :param url: The base url to use when contacting the web service 
                (e.g. "https://sentimoplus.net/sentimo-webservice/rest")
        
        :param token: the PID token used to authenticate with the service.
        
        :param timeout: the timeout duration if the service doens't response
        
        '''
        
        SentimoService.__init__(self, url = url, token = token, timeout = timeout)
        
    
    def analyze_sentimo_on_the_fly(self, content, target=None, domain= None):
        
        '''General Sentiment Analysis over the air
        
        :param content: opinion(s) string/strings array to be analyzed
        :type content: str/[str], required = true
        
        :param domain: Analysis domain
        :type domain: str or format(domain1,domain2,...), required = false.
                    The maximum support domains are 5


        :return: A 'dict' containing the result response
        
        example: /sentimo_developer_cloud/examples/AnalyzeOntheFly.py
        '''
        
        if(isinstance(content, list) == 1):
            if(len(content) > 5 or len(content) < 1):
                return BaseException
        else:
            content = [content]
        
        
        function_endpoint = ''
        if(target !=None and target!= ''):
            function_endpoint = parse.quote(target)
        
        if(domain != None and domain != ''):
            function_endpoint += ('?domain=' + parse.quote(domain))

        data = Utils.construct_aoa_data_array(content = content)
        response = self._api_request(method = 'POST',  path= '/aoa/sentimo/analyze' + function_endpoint, data = data)
        
        return response.json()
    
    def analyze_sentiment_on_the_fly(self, dataset, target=None, domain= None):
        
        '''Fine-grained Emotion Analysis over the air
        
        :param content: opinion(s) string/strings array to be analyzed
        :type content: str/[str], required = true
        
        :param domain: Analysis domain
        :type domain: str or format(domain1,domain2,...), required = false.
                    The maximum support domains are 5


        :return: A 'dict' containing the result response
        
        example: /sentimo_developer_cloud/examples/AnalyzeOntheFly.py
        '''
        
        if(isinstance(dataset, list) == 1):
            if(len(dataset) > 5 or len(dataset) < 1):
                return BaseException
        else:
            content = [dataset]
        
        function_endpoint = ''
        if(target !=None and target!= ''):
            function_endpoint = parse.quote(target)
        
        if(domain != None and domain != ''):
            function_endpoint += ('?domain=' + parse.quote(domain))

        data = Utils.construct_aoa_data_array(content = content)
        response = self._api_request(method = 'POST',  path= '/aoa/sentiment/analyze' + function_endpoint, data = data)
        
        return response.json()
    
    def analyze_sentimo_full_dataset_on_the_fly(self, data, targets = None, domain = None):
        
        '''Interface wrapper of <aoa> function of sentiment analytics on air
        
        :param content: opinion(s) full dataset/full dataset array to be analyzed
        :type content: str, required = true
        
        :param domain: Analysis domain
        :type domain: str or format(domain1,domain2,...), required = false.
                    The maximum support domains are 5


        :return: A 'dict' containing the result response
        
        example: /sentimo_developer_cloud/examples/AnalyzeOntheFly.py
        '''
        
        if(isinstance(data, list) == 1):
            if(len(data) > 5 or len(data) < 1):
                return BaseException
            
        function_endpoint = ''
        if(targets !=None and targets!= ''):
            function_endpoint = parse.quote(targets)
            
        if(domain != None):
            function_endpoint = '?domain=' + parse.quote(domain)
         
        response = self._api_request(method = 'POST', path = '/aoa/sentimo/analyze'+ function_endpoint, data = data)
         
        return response.json()
    
    def analyze_sentiment_full_dataset_on_the_fly(self, content, targets=None, domain = None):      
        '''Interface wrapper of <aoa> function of sentiment analytics on air
        
        :param content: opinion(s) full dataset/full dataset array to be analyzed
        :type content: str, required = true
        
        :param domain: Analysis domain
        :type domain: str or format(domain1,domain2,...), required = false.
                    The maximum support domains are 5


        :return: A 'dict' containing the result response
        
        example: /sentimo_developer_cloud/examples/AnalyzeOntheFly.py
        
        '''
        
        if(isinstance(content, list) == 1):
            if(len(content) > 5 or len(content) < 1):
                return BaseException
            
        function_endpoint = ''
        if(targets !=None and targets!= ''):
            function_endpoint = parse.quote(targets)
        if(domain != None):
            function_endpoint = '?domain=' + parse.quote(domain)
         
        response = self._api_request(method = 'POST', path = '/aoa/sentiment/analyze'+ function_endpoint, data = content)
         
        return response.json()
    
    def _construct_raw_dataset(self, content, title = None, data_type=None, user_id = None, screen_name=None, post_count= None, 
                      post_time= None , msg_from= None, url=None, source = None):
        '''A function is to convert string data to AOA input dataset
        
        :param content: analysis content to input
        :type  content: str/[str] 
        
        :param title: title of the content
        :type  title: str
        
        :param data_type: the type of input data 
        :type  data_type: str
        
        :param user_id: the user_id of the input information 
        :type  user_id: str
        
        :param screen_name: the display of user name in webstie
        :type  screen_name: str
        
        :param post_count: the total count number of target user's post
        :type  post_count: str
        
        :param post_time: the post time of input data
        :type  post_time: str
        
        :param msg_from: the origin source of input data if the content is not originated
        :type  msg_from: str
        
        :param url: the base url to retrive the information
        :type  url: str
        
        :param source: the source of soical platform
        :type  source: str
        
        :return: An array containing AOA input 'dict' data
        
        example: /sentimo_developer_cloud/examples/AnalyzeOntheFly.py
        '''        
        
                    
        if(isinstance(content, list) == 1):
            if(len(content) > 5 or len(content) < 1):
                return BaseException
        else:
            content = [content]
 
        
        return Utils.construct_aoa_data_array(content, title,data_type, user_id, screen_name , post_count, post_time, msg_from, url, source )
        
    
    