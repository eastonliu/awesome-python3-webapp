# !usr/bin/env python
# encoding:utf-8
"""
@project = awesome-python3-webapp
@file = app
@author = EastonLiu
@time = 2018/4/4 10:16
@Description:

"""

import logging
import asyncio
import os
import time
import json
from datetime import datetime
from aiohttp import web


def index(request):
    return web.Resource(body=b'<h1>Awesome</h1>')


async def init(loop):
    app = web.Application(loop=loop)
    app.router.add_route('GET', '/', index )
    srv = await loop.create_server(app.make_handler(), '127.0.0.1', 9001)
    logging.info("server started at http://127.0.0.1:9001")
    return srv

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()

