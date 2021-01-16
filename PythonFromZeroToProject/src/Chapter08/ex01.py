# _*_ coding    : UTF8 _*_
# Author        : ZnYang
# Creation Time : 2021/1/15 16:35
# File Name     : ex01.py
# Dev Tool      : PyCharm


while True:
    c = input('input a char: ')
    if not c.isalnum():
        print('invalid neither number nor alphabet')
        break
    print(ord(c))
