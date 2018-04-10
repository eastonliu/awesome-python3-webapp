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
import hashlib
import logging
import json
from www.coroweb import get, post
from www.models import User,Blog
from www.apis import APIValuelError, APIResourceNotFoundError,APIError
from www.models import next_id
from aiohttp import web
from www.config import configs



COOKIE_NAME = 'awesession'
_COOKIE_KEY = configs.session.secret


def user2cookie(user, max_age):
    expires = str(int(time.time()+max_age))
    s = '%s-%s-%s-%s' % (user.id, user.passwd, expires, _COOKIE_KEY)
    L = [user.id, expires, hashlib.sha1(s.encode('utf-8')).hexdigest()]
    return '-'.join(L)

async def cookie2user(cookie_str):
    if not cookie_str:
        return None
    try:
        L = cookie_str.split('-')
        if len(L) != 3:
            return None
        uid, expires, sha1 = L
        if int(expires) < time.time():
            return None
        user = await User.find(uid)
        if user is None:
            return None
        s = '%s-%s-%s-%s' % (uid, user.passwd, expires, _COOKIE_KEY)
        if sha1 != hashlib.sha1(s.encode('utf-8')).hexdigest():
            logging.info('invalid sha1.')
            return None
        user.passwd = '******'
        return user
    except Exception as e:
        logging.exception(e)
        return None




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
        'blogs': blogs,
        '__user__': request.__user__
    }


@get('/register')
async def register():
    return {
        '__template__': 'register.html'
    }

@get('/signin')
async def signin():
    return {
        '__template__': 'signin.html'

    }

@post('/api/authenticate')
async def authenticate(*, email, passwd):
    if not email:
        raise APIValuelError('email', 'Invalid email.')
    if not passwd:
        raise APIValuelError('passwd', 'Invalid passwd.')
    users = await User.findall('email=?', [email])
    if len(users) == 0:
        raise APIValuelError('email', 'email not exit.')
    user = users[0]
    sha1 = hashlib.sha1()
    sha1.update(user.id.encode('utf-8'))
    sha1.update(b':')
    sha1.update(passwd.encode('utf-8'))
    if user.passwd != sha1.hexdigest():
        raise APIValuelError('passwd', 'Invalid passwd.')
    r = web.Response()
    r.set_cookie(COOKIE_NAME, user2cookie(user, 86400), max_age=86400, httponly=True)
    user.passwd = '******'
    r.content_type = 'application/json'
    r.body = json.dumps(user, ensure_ascii=False).encode('utf-8')
    return r





_RE_EMAIL = re.compile(r'^[a-z0-9\.\_\-]+\@[a-z0-9\_\-]+(\.[a-z0-9\_\-]+){1,4}$')
_RE_SHA1 = re.compile(r'^[0-9a-f]{40}$')

@post('/api/users')
async def api_register_user(*, email, name, passwd):
    if not name or not name.strip():
        raise APIValuelError('name')
    if not email or not _RE_EMAIL.match(email):
        raise APIValuelError('email')
    if not passwd or not _RE_SHA1.match(passwd):
        raise APIValuelError('passwd')
    users = await User.findall('email=?', [email])
    if len(users) > 0:
        raise APIError('register:failed','email','Email is already in use!')
    uid = next_id()
    sha1_passwd = '%s:%s' % (uid,passwd)
    user = User(id=uid, name=name.strip(), email=email, passwd=hashlib.sha1(sha1_passwd.encode('utf-8')).hexdigest(),
                image='http://www.gravatar.com/avatar/%s?d=mm&s=120' % hashlib.md5(email.encode('utf-8')).hexdigest())
    await user.save()
    r = web.Response()
    r.set_cookie(COOKIE_NAME, user2cookie(user, 86400), max_age=86400, httponly=True)
    user.passwd = '******'
    r.content_type = 'application/json'
    r.body = json.dumps(user, ensure_ascii=False).encode('utf-8')
    return r


