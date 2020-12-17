import datetime

print('今日日期:', datetime.date.today())
print('今日:', datetime.datetime.today())
print('现在:', datetime.datetime.now())
print('现在日期是: ', datetime.datetime.now().strftime('%Y-%m-%d'))
print('现在时间是: ', datetime.datetime.now().strftime('%y-%m-%d %H:%M:%S'))
print('现在时间是: ', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S %A'))
print('现在时间是: ', datetime.datetime.now().strftime('%Y-%h-%d %H:%M:%S %A'))