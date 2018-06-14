# coding: utf-8
# sentimo_service.py
import sys
import platform
import requests
import logging

from requests.exceptions import HTTPError

from requests.structures import CaseInsensitiveDict

import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

PY2 = sys.version_info[0] == 2
DEFAULT_SENTIMO_URL = ""

logger = logging.getLogger(__name__)

if PY2:
#     text_type = unicode
#     string_types = (str, unicode)
    text_type= ''
else:
    text_type = str
    string_types = (str,)


def _remove_null_values(dictionary):
    """A function to remove 'null' value"""
    if isinstance(dictionary, dict):
        return dict([(k, v) for k, v in dictionary.items() if v is not None])
    return dictionary


class SentimoService(object):
    """The Sentimo Service"""
    
    def __init__(self, url, token, timeout = 30):   
        """Construct a new client for Sentimo Service
        :param url URL path of service
        :param token certified PID of target service 
        :param timeout HTTP timeout value
        """
        
        self.url = url
        self.token = token
        self.timeout = timeout
        
        user_agent_string = 'sentimo-webservice-python-sdk-' ##+ __VERSION__ #SDK Version
        user_agent_string += ' ' + platform.system()  #OS
        user_agent_string += ' ' + platform.release() #OS version
        user_agent_string += ' ' + platform.python_version() # Python version
        
        self.user_agent_header = {'user-agent' : user_agent_string}
        
        
    def _api_request(self, method, path, headers = None, params = None, data = None, **kwargs):
        kwargs.setdefault('timeout', self.timeout)
        
        url = self.url + path
        
        input_headers = _remove_null_values(headers) if headers else {}
        headers = CaseInsensitiveDict(self.user_agent_header)
        headers['accept'] = 'application/json'
        headers.update(input_headers)
        headers.update({'content-type' : 'application/json'})
        headers.update({'pid' : self.token})
        
        # Remove keys with None values
        params = _remove_null_values(params)
        data = _remove_null_values(data)
        
        if sys.version_info >= (3, 0) and isinstance(data, str):
            data = data.encode('utf-8')
        
#         res = {}
#         try:
        res = requests.request(method = method, url = url, headers = headers, params = params, data=data,   **kwargs, verify =False)
#         except:
#             res = requests.json()['']
#             return  
        
        http_error_msg = ''
        
        if 200 <=res.status_code <= 299:
            if res.status_code == 204:
                return None
        else: 
            if 400 <= res.status_code < 600:
                reason = res.reason
                try:
                    reason = res.json()['message']
                except:
                    pass
                http_error_msg = 'HTTPError: %s %s' % (res.status_code, reason)
                
            if http_error_msg:
                raise HTTPError(http_error_msg, response = res)
            
        return res        
        