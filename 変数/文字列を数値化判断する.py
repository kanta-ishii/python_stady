#文字列が十進数字か判定: str.isdecimal()
s = '1234567890'
print('s =', s)
print('isdecimal:', s.isdecimal())
print('isdigit:', s.isdigit())
print('isnumeric:', s.isnumeric())

s = '１２３４５６７８９０'
print('s =', s)
print('isdecimal:', s.isdecimal())
print('isdigit:', s.isdigit())
print('isnumeric:', s.isnumeric())

s = '-1.23'
print('s =', s)
print('isdecimal:', s.isdecimal())
print('isdigit:', s.isdigit())
print('isnumeric:', s.isnumeric())


#文字列が数を表す文字か判定: str.isnumeric()
s = '\u00BD'
print('s =', s)
print('isdecimal:', s.isdecimal())
print('isdigit:', s.isdigit())
print('isnumeric:', s.isnumeric())

s = '\u2166'
print('s =', s)
print('isdecimal:', s.isdecimal())
print('isdigit:', s.isdigit())
print('isnumeric:', s.isnumeric())

s = '一二三四五六七八九〇'
print('s =', s)
print('isdecimal:', s.isdecimal())
print('isdigit:', s.isdigit())
print('isnumeric:', s.isnumeric())

s = '壱億参阡萬'
print('s =', s)
print('isdecimal:', s.isdecimal())
print('isdigit:', s.isdigit())
print('isnumeric:', s.isnumeric())