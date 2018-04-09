# !usr/bin/env python
# encoding:utf-8
"""
@project = awesome-python3-webapp
@file = handlers
@author = EastonLiu
@time = 2018/4/8 14:45
@Description:

"""

import asyncio
import re
import time
from www.coroweb import get, post
from www.models import User,Blog
import apis



@get('/')
async def index(request):
    summary = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.'
    blogs = [
        Blog(id='1', name='Test Blog', summary=summary, created_at=time.time() - 120),
        Blog(id='2', name='Something New', summary=summary, created_at=time.time() - 3600),
        Blog(id='3', name='Learn Swift', summary=summary, created_at=time.time() - 7200)
    ]
    return {
        '__template__': 'blogs.html',
        'blogs': blogs
    }


@get('/api/users')
async def aip_get_users():
    users = await User.findall(orderBy='created_at desc')
    for u in users:
        u.passwd = '******'
    return dict(users=users)


_RE_EMAIL = re.compile(r'^[a-z0-9\.\_\-]+\@[a-z0-9\_\-]+(\.[a-z0-9\_\-]+){1,4}$')
_RE_SHA1 = re.compile(r'^[0-9a-f]{40}$')
@post('/api/users')
def api_register_user(*, email, name, passwd):
    if not name or not name.strip():
        raise
