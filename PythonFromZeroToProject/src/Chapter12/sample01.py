# _*_ coding    : UTF8 _*_
# Author        : ZnYang
# Creation Time : 2021/1/15 21:18
# File Name     : sample01.py
# Dev Tool      : PyCharm


class Bird(object):
    name = 'bird'

    def __init__(self):
        ...
        self.age = 1


b = object.__new__(Bird)
c = object.__new__(Bird)
print(id(b))
print(id(c))
print(dir(b))
print(b.name)
Bird.__init__(b)
print(dir(b))
print(b.age)
print(type(b))
print(b)
print(b.name)
# print(b.age)
c = Bird.__init__(b)
print(c)
