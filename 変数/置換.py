# 文字列を指定して置換: replace
s = 'one two one two one'

print(s.replace(' ', '-'))
print(s.replace(' ', ''))
print(s.replace('one', 'XXX'))
print(s.replace('one', 'XXX', 2)) # 最大置換回数を指定: 引数count
print(s.replace('one', 'XXX').replace('two', 'YYY'))


# 改行文字を置換
s_lines_multi = 'one\ntwo\r\nthree'

print(s_lines_multi.splitlines())
print('-'.join(s_lines_multi.splitlines()))


# 複数の文字を指定して置換: translate
s = 'one two one two one'

print(s.translate(str.maketrans({'o': 'O', 't': 'T'})))
print(s.translate(str.maketrans({'o': 'XXX', 't': None})))
print(s.translate(str.maketrans('ow', 'XY', 'n')))


# 正規表現で置換: re.sub, re.subn
import re
s = 'aaa@xxx.com bbb@yyy.com ccc@zzz.com'

print(re.sub('[a-z]*@', 'ABC@', s))
print(re.sub('[a-z]*@', 'ABC@', s, 2)) # countに最大値関数を指定できる
print(re.sub('[xyz]', '1', s)) # 複数の文字列を同じ文字列に置換
print(re.sub('aaa|bbb|ccc', 'ABC', s)) # ターンを|で区切るといずれかのパターンにマッチする
print(re.sub('([a-z]*)@', '\\1-123@', s))
print(re.sub('([a-z]*)@', r'\1-123@', s))
