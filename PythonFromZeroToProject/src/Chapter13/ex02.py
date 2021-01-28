# _*_ coding    : UTF8 _*_
# Author        : ZnYang
# Creation Time : 2021/1/16 23:14
# File Name     : ex02.py
# Dev Tool      : PyCharm


# 推算日期
import datetime

days = int(input('输入间隔的天数：'))
now = datetime.datetime.now()
delta = datetime.timedelta(days)
new = now + delta
print(new)
