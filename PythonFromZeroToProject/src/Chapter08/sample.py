# _*_ coding    : UTF8 _*_
# Author        : ZnYang
# Creation Time : 2021/1/15 16:32
# File Name     : sample.py
# Dev Tool      : PyCharm
# 逢3过

for i in range(1, 100):
    if i % 3 == 0 or '3' in str(i):
        print('过')
    else:
        print(i)
