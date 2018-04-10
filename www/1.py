# !usr/bin/env python
# encoding:utf-8
"""
@project = awesome-python3-webapp
@file = 1
@author = EastonLiu
@time = 2018/4/4 17:14
@Description:

"""

import re
def count_smileys(arr):
#    a = ' '.join(arr)
#    print(re.findall('[:;][-~]?[)D]', a))
    return (len(re.findall('[:;][-~]?[)D]', ' '.join(arr))))

print(count_smileys([':)',':(',':D',':O','D:']))






