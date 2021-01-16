from datetime import datetime


def header(name):
    print(name.ljust(20, '-'))


# now = date.today()
now = datetime.now()

header('Year')
print("%Y", now.strftime('%Y'))  # 年全称
print("%y", now.strftime('%y'))  # 年简称

header('Month')
print('%b', now.strftime('%b'))  # 月简称
print('%B', now.strftime('%B'))  # 月全称
print('%m', now.strftime('%m'))  # 月序号

header('Weekday')
print('%a', now.strftime('%a'))  # 周简称
print('%A', now.strftime('%A'))  # 周全称
print('%w', now.strftime('%w'))  # 周序号
print('%u', now.strftime('%u'))

header('Day')
print('%d', now.strftime('%d'))  # 日序号

header('Hour')
print('%H', now.strftime('%H'))  # 24小时
print('%I', now.strftime('%I'))  # 12小时

header('AM or PM')
print('%p', now.strftime('%p'))  # AM or PM

header('Minute')
print('%M', now.strftime('%M'))  # 分钟

header('Second')
print('%S', now.strftime('%S'))  # 秒钟

header('Micro Second')
print('%f', now.strftime('%f'))  # 微秒

header('UTC offset')
print('%z', now.strftime('%z'))
print('%Z', now.strftime('%Z'))

header('Day of the year')
print('%j', now.strftime('%j'))  # 一年中的第几天

header('Week of the year')
print('%U', now.strftime('%U'), 'Sunday as first day of the week')
print('%W', now.strftime('%W'), 'Monday as first day of the week')
print('%V', now.strftime('%V'), 'Monday as first day of the week')

header('appropriate date and time representation in current locale')
print('%c', now.strftime('%c'))
print('%x', now.strftime('%x'))
print('%X', now.strftime('%X'))

header('print %')
print('%%', now.strftime('%%'))
