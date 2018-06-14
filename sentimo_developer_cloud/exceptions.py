# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function, unicode_literals

from requests.exceptions import HTTPError

class TaskNotFoundError(HTTPError):
    """Task is not found"""
    
class TaskError(HTTPError):
    """Task analysis error"""
    
class TimeoutError(Exception):
    """Analysis timeout error"""

class SizeExcessError(Exception):
    """Analysis Size Excess error"""