# _*_ coding    : UTF8 _*_
# Author        : ZnYang
# Creation Time : 2021/1/8 23:31
# File Name     : sample01.py
# Dev Tool      : PyCharm

# '%[-][+][0][m][.n]格式化字符' % exp


# '%-d' 正数前无符号，负数前加负号
print('%-d' % -10)  # -10
print('%-d' % 10)  # 10

# '%-s' 左对齐
print('%-10s' % 'abc')  # abc_______

# '%+d' 正数前加正号，负数前加负号
print('%+d' % -10)  # -10
print('%+d' % 10)  # +10

# '%+s' 右对齐
print('%+10s' % 'abc')  # _______abc

# '%5d' '%5s' 占有宽度为5
# '%05d' 数字右对齐，用0填充空白处，正数前无符号，负数前加负号
print('%05d' % 10)  # 00010

# '%.5f' 小数点后保留5位
print('%.5f' % 1)  # 1.00000


