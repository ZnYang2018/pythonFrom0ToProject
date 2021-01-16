# _*_ coding    : UTF8 _*_
# Author        : ZnYang
# Creation Time : 2021/1/13 22:49
# File Name     : sample04.py
# Dev Tool      : PyCharm
import re

pattern = r'1[34578]\d{9}'
string = '中奖号码为：84978981 联系电话为：13611111111'
result = re.sub(pattern, '1XXXXXXXXXX', string)
print(result)

pattern2 = '[?|&]'
url = 'http://www.mingrisoft.com/login.jsp?username="mr"&pwd="mrsoft'
result2 = re.split(pattern2, url)
print(result2)