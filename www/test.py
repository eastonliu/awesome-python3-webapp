# !usr/bin/env python3
# -*- coding:utf-8 -*- 
"""
@project = awesome-python3-webapp
@file = test
@author = Easton Liu
@time = 2018/4/5 22:14
@Description: 

"""

import asyncio
from www import orm
from www.models import User


loop = asyncio.get_event_loop()
async def test():
    await orm.create_pool(loop=loop, host='172.21.13.65', user='root', password='coship', db='awesome')
    u = User(name='lmj', email='123@qq.com', passwd='12345678', image='about:blank')
    await u.save()


loop.run_until_complete(test())
loop.close()
