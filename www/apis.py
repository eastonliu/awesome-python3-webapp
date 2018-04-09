# !usr/bin/env python
# encoding:utf-8
"""
@project = awesome-python3-webapp
@file = apis
@author = EastonLiu
@time = 2018/4/8 10:32
@Description:

"""


class APIError(Exception):
    def __init__(self, error, data='', message=''):
        super().__init__(message)
        self.error = error
        self.data = data
        self.message = message


class APIValuelError(APIError):
    def __init__(self, field, message=''):
        super().__init__('value:invalid', field, message)


class APIResourceNotFoundError(APIError):
    def __init__(self, field, message):
        super().__init__('value:notfound', field, message)


class APIPermissionError(APIError):
    def __init__(self, message):
        super().__init__('permission:forbidden', 'permission', message)