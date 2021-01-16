# _*_ coding    : UTF8 _*_
# Author        : ZnYang
# Creation Time : 2020/12/26 22:49
# File Name     : ex02.py
# Dev Tool      : PyCharm

# 进制转换
num_str = input('请输入数字')
base_num = int(input('请输入进制'))
actual_number = int(num_str, base_num)
print('该数字为：')
print('16进制：', hex(actual_number))
print('10进制：', actual_number)
print('8进制：', oct(actual_number))
print('2进制：', bin(actual_number))
