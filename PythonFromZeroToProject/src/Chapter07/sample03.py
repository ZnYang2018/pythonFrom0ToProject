# _*_ coding    : UTF8 _*_
# Author        : ZnYang
# Creation Time : 2021/1/12 23:23
# File Name     : sample03.py
# Dev Tool      : PyCharm
import re

pattern = r'mr_\w+'
string = 'MR_SHOP mr_shop'
match = re.match(pattern, string, re.IGNORECASE)
print(match)

print('匹配值的起始位置：', match.start())
print('匹配值的结束位置：', match.end())
print('匹配位置的元组：', match.span())
print('要匹配的字符串：', match.string)
print('匹配数据：', match.group())

string2 = '项目名称MR_SHOP mr_shop'
match2 = re.match(pattern, string2, re.IGNORECASE)
print(match2)
print('=' * 80)

match = re.search(pattern, string, re.I)
print(match)
match2 = re.search(pattern, string2, re.I)
print(match2)
print('=' * 80)

match_list = re.findall(pattern, string, re.I)
print(match_list)
match_list2 = re.findall(pattern, string2, re.I)
print(match_list2)
print('=' * 80)

pattern = r'[1-9]{1,3}(\.[0-9]{1,3}){3}'
string3 = '127.0.0.1 192.168.1.66'
match3 = re.findall(pattern, string3)
print(match3)
