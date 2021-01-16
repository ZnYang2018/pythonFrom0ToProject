# _*_ coding    : UTF8 _*_
# Author        : ZnYang
# Creation Time : 2021/1/8 23:56
# File Name     : sample02.py
# Dev Tool      : PyCharm

# {[index][: [ [fill] align] [sign] [#] [width] [.precision] [type] ]}

# {[index]} 索引位置
print('{1}, {0}, {0}'.format(0, 1))  # 1, 0, 0

# {:[ [fill]align ] [width] }   fill空白填充字符，align <左对齐 >右对齐 =数字右对齐 ^居中， width 字符串宽度
print('{:_<10}'.format('abc'))  # abc_______
print('{:_>10}'.format('abc'))  # _______abc
print('{:10}'.format(123))  # '       123'
print('{:_=10}'.format(123))  # _______123
print('{:_^10}'.format('abc'))  # ___abc____

# {: [sign]}    + 正数加正号，负数加负号；- 正数无符号，负数加负号；  （空格）正数加空格，负数加负号
print('{:+}'.format(10))  # +10
print('{:+}'.format(-10))  # -10
print('{:-}'.format(10))  # 10
print('{:-}'.format(-10))  # -10
print('{: }'.format(10))  #  10
print('{: }'.format(-10))  # -10

# {: [#]}   # 显示进制前缀 0b 0o或者0x
print('{:#b}'.format(10))   # 0b1010
print('{:b}'.format(10))    # 1010
print('{:#o}'.format(10))   # 0o12
print('{:o}'.format(10))    # 12
print('{:#x}'.format(10))   # 0xA
print('{:X}'.format(10))    # A

# {: [.precision]}  保留小数的位数
print('{:.4}'.format(1.2))  # 1.2
print('{:.4f}'.format(1.2))  # 1.2000
print('{:f}'.format(1.2))  # 1.200000

# {: [type]} 类型
