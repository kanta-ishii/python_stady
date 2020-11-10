'''
    年        ＝ year
    月        ＝ month
    日        ＝ day
    時        ＝ hour
    分        ＝ minute
    秒        ＝ second
    マイクロ秒 ＝ microsecond
'''

import datetime


dt_now = datetime.datetime.now()

print(dt_now)
print(dt_now.strftime('%Y年%m月%d日 %H:%M:%S'))
print(dt_now.strftime('%Y%m%d %H%M%S'))
print(dt_now.isoformat())
print(dt_now.year)
print(dt_now.month)
print(dt_now.day)
print(dt_now.hour)
print(dt_now.minute)
print(dt_now.second)
print(dt_now.microsecond)

d_today = datetime.date.today()
print(d_today)
t_now = datetime.datetime.now().time()
print(t_now)
print(d_today.strftime('%Y%m%d'))
print(t_now.strftime('%H%M%S'))