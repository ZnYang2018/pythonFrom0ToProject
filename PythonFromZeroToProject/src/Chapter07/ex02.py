# _*_ coding    : UTF8 _*_
# Author        : ZnYang
# Creation Time : 2021/1/15 11:34
# File Name     : ex02.py
# Dev Tool      : PyCharm
while True:
    text = input('请输入要检测的字符串:\n')
    sign = input('请输入要统计的字符：\n')
    cnt = text.count(sign)
    print(f'字符{sign}出现次数为{cnt}次。\n')