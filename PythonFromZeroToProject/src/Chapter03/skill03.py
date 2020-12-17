from datetime import datetime, time
from datetime import date


def header(name):
    print(name.ljust(20, '-'))


# now = date.today()
now = datetime.now()

header('Year')
print("%Y", now.strftime('%Y'))
print("%y", now.strftime('%y'))

header('Month')
print('%b', now.strftime('%b'))
print('%B', now.strftime('%B'))
print('%m', now.strftime('%m'))

header('Weekday')
print('%a', now.strftime('%a'))
print('%A', now.strftime('%A'))
print('%w', now.strftime('%w'))
print('%u', now.strftime('%u'))

header('Day')
print('%d', now.strftime('%d'))

header('Hour')
print('%H', now.strftime('%H'))
print('%I', now.strftime('%I'))

header('AM or PM')
print('%p', now.strftime('%p'))

header('Minute')
print('%M', now.strftime('%M'))

header('Second')
print('%S', now.strftime('%S'))

header('Micro Second')
print('%f', now.strftime('%f'))

header('UTC offset')
print('%z', now.strftime('%z'))
print('%Z', now.strftime('%Z'))

header('Day of the year')
print('%j', now.strftime('%j'))

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
