# coding=utf-8
import datetime
while True:
    im_year = input('Input your birth year: ')
    now_year = datetime.datetime.now().year
    age = now_year - int(im_year)
    print(f'Your age is {age} year{("s" if age > 1 else "")} old')
    if age < 18:
        print('You are a minor')
    elif age < 66:
        print('You are a youth')
    elif age < 80:
        print('You are a middle-aged man')
    else:
        print('You are an elderly-aged man')
