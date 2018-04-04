# !usr/bin/env python
# encoding:utf-8
"""
@project = awesome-python3-webapp
@file = orm
@author = EastonLiu
@time = 2018/4/4 14:16
@Description:

"""

import asyncio
import aiomysql
import logging
logging.basicConfig(level=logging.INFO)


async def create_pool(loop, **kw):
    logging.info("create database connection pool....")
    global __pool
    __pool = await aiomysql.create_pool(
        host=kw.get('host', 'localhost'),
        port=kw.get('port', '3306'),
        user=kw.get('user'),
        password=kw.get('password'),
        db=kw.get('db'),
        charset=kw.get('charset', 'utf8'),
        autocommit=kw.get('autocommit', 'True'),
        maxsize=kw.get('maxsize', 10),
        minsize=kw.get('minsize', 1),
        loop=loop
    )


async def select(sql, args, size=None):
    logging.info("SQL:", sql)
    global __pool
    with (await __pool.get()) as conn:
        cur = await conn.cursor(aiomysql.DictCursor)
        await cur.execute(sql.replace('?', '%s'), args or ())
        if size:
            rs = await conn.fetchmany(size)
        else:
            rs = await conn.fetchall()
        await conn.close()
        logging.info("rows returned:", len(rs))
        return rs


async def execute(sql, args, autocommit=True):
    logging.info("SQL", sql)
    with (await __pool.get()) as conn:
        if not autocommit:
            conn.begin()
        try:
            cur = await conn.cursor(aiomysql.DictCursor)
            await cur.execute(sql.replace('?', '%s'), args)
            affected = cur.rowcount
            if not autocommit:
                await conn.commit()
            await conn.close
        except BaseException:
            if not autocommit:
                await conn.rollback()
            raise
        return affected



