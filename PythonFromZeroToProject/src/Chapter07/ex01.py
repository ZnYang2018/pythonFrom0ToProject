# _*_ coding    : UTF8 _*_
# Author        : ZnYang
# Creation Time : 2021/1/13 23:00
# File Name     : ex01.py
# Dev Tool      : PyCharm
import re

string = '2018 Amazon Jeff Bezos 1120'
print('1' + '=' * 70)
print(string.replace('2018', ''))

print('2' + '=' * 70)
numbers = re.findall('\d', string)
print(''.join(numbers))

print('3' + '=' * 70)
words = string.split(' ')
new_string = ''
for i in range(len(words)):
    if words[i].isdigit():
        words[i] = f'[{words[i]}]'
print(' '.join(words))

print('4' + '=' * 70)
print(string.replace(' ', ''))

print('5' + '=' * 70)
words = string.split(' ')
new_string = ''
for i in range(len(words)):
    if words[i].isdigit():
        words[i] = str(int(words[i]) * 2)
print(''.join(words))

print('6' + '=' * 70)
bezos = '(bezos)'
string = '要么创新，要么杰夫·贝索斯会替你做'
index = string.find('贝索斯')
new_string = string[0:index + 3] + bezos + string[index + 3:]
print(new_string)
