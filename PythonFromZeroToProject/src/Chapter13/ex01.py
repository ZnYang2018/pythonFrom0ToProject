# _*_ coding    : UTF8 _*_
# Author        : ZnYang
# Creation Time : 2021/1/16 22:28
# File Name     : ex01.py
# Dev Tool      : PyCharm
import re

seats = [[True] * 5 for i in range(13)]


def show_seat(row, col):
    if 1 <= row <= 13 and 1 <= col <= 5:
        if seats[row - 1][col - 1]:
            print('{}行{}列，有票'.format(row, col))
        else:
            print('{}行{}列，无票'.format(row, col))
    else:
        print('无效的座位号')


def order_seat(row, col):
    if 1 <= row <= 13 and 1 <= col <= 5:
        if seats[row - 1][col - 1]:
            seats[row - 1][col - 1] = False
            print('{}行{}列，订票成功！'.format(row, col))
        else:
            print('{}行{}列，无票，订票失败！'.format(row, col))
    else:
        print('无效的座位号，订票失败！')


def get_row_and_col():
    row_col_str = input('请输入行列号（1,1）：')
    row_str, col_str = re.split(',|，', row_col_str)
    row = int(row_str)
    col = int(col_str)
    return row, col


while True:
    opt = input('请输入（1.查询，2.订票，3.退出）：')
    if opt == '1':
        row, col = get_row_and_col()
        show_seat(row, col)
    elif opt == '2':
        row, col = get_row_and_col()
        order_seat(row, col)
    elif opt == '3':
        break
    else:
        print('无效的参数')
