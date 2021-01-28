# _*_ coding    : UTF8 _*_
# Author        : ZnYang
# Creation Time : 2021/1/17 21:36
# File Name     : sample01.py
# Dev Tool      : PyCharm

try:
    file = open('001.txt', 'r')
except FileNotFoundError as e:
    file = open('001.txt', 'w+')
    file.write("hasha")
    file.close()

