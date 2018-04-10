# !usr/bin/env python
# encoding:utf-8
"""
@project = awesome-python3-webapp
@file = config_default
@author = EastonLiu
@time = 2018/4/8 11:09
@Description:

"""

configs = {
    'debug': True,
    'db': {
        'host': '172.21.13.65',
        'port': 3306,
        'user': 'root',
        'password': 'coship',
        'db': 'awesome'
    },
    'session': {
        'secret': 'Awesome'

    }
}
