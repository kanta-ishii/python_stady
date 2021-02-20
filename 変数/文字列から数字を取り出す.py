#正規表現操作モジュール 「re」を使う
'''
re.sub(第1引数, 第2引数, 第3引数)
    第1引数 : 文字列内で置換させたい文字列
    第2引数 : 置換後の文字列
    第3引数 : 対象の文字列
'''
from re import sub

s = '2020年の2月５日'
result = sub(r'\D', '', s)
print(result) #全角も半角抽出してくれる


#findall()を使う
from re import findall

s = '2020年の2月５日'
result = findall(r'\d+', s)
print(result)