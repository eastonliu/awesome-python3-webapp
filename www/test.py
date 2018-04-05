# !usr/bin/env python3
# -*- coding:utf-8 -*- 
"""
@project = awesome-python3-webapp
@file = test
@author = Easton Liu
@time = 2018/4/5 22:14
@Description: 

"""

from www import orm
from www.models import User, Blog, Comment


def test():
    orm.create_pool(user='root', password='coship', database='awesome')
    u = User(name='lmj', email='123@qq.com', passwd='12345678', image='about:blank')
    u.save()

