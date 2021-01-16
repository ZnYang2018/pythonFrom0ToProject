# _*_ coding    : UTF8 _*_
# Author        : ZnYang
# Creation Time : 2020/12/28 23:03
# File Name     : ex01.py
# Dev Tool      : PyCharm
L = [89, 98, 00, 75, 68, 37, 58, 90]
N = [i + 1900 if i != 0 else i + 2000 for i in L]
print(sorted(N))
