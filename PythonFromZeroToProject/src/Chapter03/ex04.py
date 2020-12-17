# coding=utf-8
import datetime
import os
from time import sleep

while True:
    now = datetime.datetime.now()
        # .strftime("%Y年%m月%d日 %H时%M分%S秒")
    # date_time = datetime.datetime.now().strftime("%Y%m%d %H%M%S")
    print(f'现在时间是: {now.year}年{now.month}月{now.day}日 {now.hour}时{now.minute}分{now.second}秒')
    sleep(0.91)
    os.system('cls')
