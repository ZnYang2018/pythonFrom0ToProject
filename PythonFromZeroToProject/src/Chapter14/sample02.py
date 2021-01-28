# _*_ coding    : UTF8 _*_
# Author        : ZnYang
# Creation Time : 2021/1/17 21:44
# File Name     : sample02.py.py
# Dev Tool      : PyCharm

file = open('002.txt', 'r+', encoding='utf-8')
r = file.read(10)
print(r)
file.write('hasash哈哈fsdfh')
file.close()