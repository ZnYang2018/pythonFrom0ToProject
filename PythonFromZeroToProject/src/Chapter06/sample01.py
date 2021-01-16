# _*_ coding    : UTF8 _*_
# Author        : ZnYang
# Creation Time : 2020/12/28 22:39
# File Name     : sample01.py
# Dev Tool      : PyCharm

import datetime

l1 = list(range(10000000))
l2 = list(range(10000000))

start = datetime.datetime.now()
l3 = l1 + l2
end = datetime.datetime.now()
delta1 = (end - start).total_seconds()
print('+ spent', delta1, 'seconds')

start = datetime.datetime.now()
l1.extend(l2)
end = datetime.datetime.now()
delta2 = (end - start).total_seconds()
print('extend spent', delta2, 'seconds')
print('+ is shorter' if delta1 < delta2 else 'extend is shorter')
