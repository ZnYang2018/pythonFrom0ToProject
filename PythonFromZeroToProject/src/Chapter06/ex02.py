# _*_ coding    : UTF8 _*_
# Author        : ZnYang
# Creation Time : 2021/1/6 14:48
# File Name     : ex02.py
# Dev Tool      : PyCharm
this_week = [4235, 10111, 8447, 9566, 9788, 8951, 9808]
last_week = [4235, 5612, 8447, 11250, 9211, 9985, 3783]
sum_week = []
for a, b in zip(this_week, last_week):
    sum = a + b
    sum_week.append(sum)
print(sum_week)
