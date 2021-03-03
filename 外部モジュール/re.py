'''
ref
    ・https://docs.python.org/3/library/re.html
'''
import re


# 置換系
s = 'aaa@xxx.com bbb@yyy.com ccc@zzz.com'

print(re.sub('[a-z]*@', 'ABC@', s))
print(re.sub('[a-z]*@', 'ABC@', s, 2)) # countに最大値関数を指定できる
print(re.sub('[xyz]', '1', s)) # 複数の文字列を同じ文字列に置換
print(re.sub('aaa|bbb|ccc', 'ABC', s)) # ターンを|で区切るといずれかのパターンにマッチする
print(re.sub('([a-z]*)@', '\\1-123@', s))
print(re.sub('([a-z]*)@', r'\1-123@', s))


#半角小文字
lowerReg = re.compile(r'^[a-z]+$')
def islower(s):
    return lowerReg.match(s) is not None

#半角大文字
upperReg = re.compile(r'^[A-Z]+$')
def isupper(s):
    return upperReg.match(s) is not None

#半角英字
alphaReg = re.compile(r'^[a-zA-Z]+$')
def isalpha(s):
    return alphaReg.match(s) is not None

#半角数字
digitReg = re.compile(r'^[0-9]+$')
def isdigit(s):
    return digitReg.match(s) is not None

#半角英数字
alnumReg = re.compile(r'^[a-zA-Z0-9]+$')
def isalnum(s):
    return alnumReg.match(s) is not None

#半角英数字orアンダースコア
alnum_Reg = re.compile(r'^[a-zA-Z0-9_]+$')
def isalnum_(s):
    return alnum_Reg.match(s) is not None

#半角記号
symbolReg = re.compile(r'^[!-/:-@[-`{-~]+$')
def issymbol(s):
    return symbolReg.match(s) is not None

#ASCII文字
asciiReg = re.compile(r'^[!-~]+$')
def isascii(s):
    return asciiReg.match(s) is not None


# 文字列と「'」シングルクォーテーションが入っている文字を出力する
text = "don't touch it"
re.findall(r'[a-zA-Z\']+',text)