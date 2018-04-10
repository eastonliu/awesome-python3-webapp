# !usr/bin/env python
# encoding:utf-8
"""
@project = awesome-python3-webapp
@file = config
@author = EastonLiu
@time = 2018/4/8 13:47
@Description:

"""

import www.config_default as config_default


class Dict(dict):
    def __init__(self, names=(), values=(), **kw):
        super().__init__(**kw)
        for k, v in zip(names,values):
            self[k] = v

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'DICT' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

def merge(defaults, override):
    r = {}
    for k, v in defaults.items():
        if k in override:
            if isinstance(v, dict):
                r[k] = merge(v, override[k])
            else:
                r[k] = override[k]
        else:
            r[k] = v
    return r

def toDict(d):
    D = Dict()
    for k, v in d.items():
        if isinstance(v, dict):
            D[k] = toDict(v)
        else:
            D[k] = v
    return D

configs = config_default.configs


try:
    import www.config_override as config_override
    configs = merge(configs, config_override.configs)
except ImportError:
    pass
configs = toDict(configs)


