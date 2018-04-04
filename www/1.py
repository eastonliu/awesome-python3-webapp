# !usr/bin/env python
# encoding:utf-8
"""
@project = awesome-python3-webapp
@file = 1
@author = EastonLiu
@time = 2018/4/4 17:14
@Description:

"""


class User(Model):
    id = IntegerField('id')
    name = StringField('name')
    email = StringField('email')
    password = StringField('password')


class Field(object):

    def __init__(self, name, column_type):
        self.name = name
        self.column_type = column_type

    def __str__(self):
        return '<%s:%s>' % (self.__class__.__name__, self.name)


class StringField(Field):
    def __init__(self,name):
        super(StringField,self).__init__(name, 'varchar(100)')


class IntegerField(Field):
    def __init__(self,name):
        super(IntegerField,self).__init__(name, 'bigint')



