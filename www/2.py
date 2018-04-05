# !usr/bin/env python3
# -*- coding:utf-8 -*- 
"""
@project = awesome-python3-webapp
@file = 2
@author = EastonLiu
@time = 2018/4/4 23:43
@Description: 

"""


class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        print('name======', name, 'base=======', bases, 'attrs======', attrs)
        attrs['add'] = lambda self, value: self.append(value)
        print('name======', name, 'base=======', bases, 'attrs======', attrs)
        return type.__new__(cls, name, bases, attrs)


class MyList(list, metaclass=ListMetaclass):
    pass


if __name__ == '__main__':
    L = MyList()
    L.add(1)
    print(L)
