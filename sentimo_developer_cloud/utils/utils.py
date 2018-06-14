import time
import json

class Utils(object):

    @staticmethod
    def construct_aoa_data_array(content, title = None, data_type=None, user_id = None, screen_name=None, post_count= None, 
                          post_time= None , msg_from= None, url=None, source = None):
        
        '''This is to construct the format of analysis data.
        
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
        
        example: /sentimo_developer_cloud/examples/AnalyzeOvertheAir.py
        
        '''
        
        params = []
        
        for i in content:
            param = Utils.construct_aoa_data(i, title, data_type, user_id, screen_name, post_count, post_time, msg_from, url, source)
            params.append(param)
        
        in_json = json.dumps(params, separators = (',',':'))
    
        return str(in_json)
    
    @staticmethod
    def construct_aoa_data(content, title = None, data_type=None, user_id = None, screen_name=None, post_count= None, 
                          post_time= None , msg_from= None, url=None, source = None):
        
        if(title == None):
                title = 'default'
        if(data_type == None):
            data_type = 'String'
        if(source == None):
            source = 'default'
        if(user_id ==None):
            user_id = 'default'
        if(screen_name== None):
            screen_name = 'default'
        if(post_count == None):
            post_count = '0'
        if(msg_from == None):
            msg_from = 'default'    
        if(url == None):
            url= 'default'
        if(post_time == None):
            post_time = time.strftime('%Y-%m-%dT%H:%M:%S.000Z',time.localtime(time.time()))
        
        param = {'title' : title,
                  'type' : data_type , 
                  'user_id' : user_id,
                  'source': source,
                  'screen_name': screen_name,
                  'userjoindate' : 0,
                  'postcount' : post_count,
                  'post_time' : post_time,
                  'post_id': "default",
                  'content' : content,
                  'reply_to_post_id': "-",
                  'reply_to_uid': "-",
                  'msg_from': msg_from,
                  'likes' : 0,
                  'url' : url}
                      
        return param
    
    @staticmethod    
    def construct_upload_data(content, post_id=None, source=None, user_id=None, post_time=None):
        """ A function to construct upload data set
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
        """
        
        params =[]
        
        for i in content:
        
            if(post_id == None):
                post_id = 'default'
            if(source == None):
                source = 'default'
            if(user_id ==None):
                user_id = 'default'
            if(post_time == None):
                post_time = time.strftime('%Y-%m-%d-%H:%M:%S',time.localtime(time.time()))
            
            param = {'post_id': post_id, 
                      'source': source, 
                      'user_id' : user_id, 
                      'post_time': post_time, 
                      'content': i}
            params.append(param)
        
        data = {'data' : params}
        dataStr = str(data)
      
        return dataStr
    
    @staticmethod
    def construct_dictionary_data(category_code, sentiment_word):
        
        params = [];