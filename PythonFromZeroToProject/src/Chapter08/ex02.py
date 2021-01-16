# _*_ coding    : UTF8 _*_
# Author        : ZnYang
# Creation Time : 2021/1/15 17:29
# File Name     : ex02.py
# Dev Tool      : PyCharm
import pytz
import datetime

now = datetime.datetime.now(pytz.utc)
print(now)
print(datetime.datetime.now())


def test(a, b=2, *c, d, e=2):
    ...

print(test.__defaults__)
test(1, 2, 3, 4, 5, d=6, e=7)
