m = '''
任意の文字列の位置を取得: finds, rfind
正規表現ですべての結果を取得、カウント: re.findall, re.finditer
'''

#4番目にあることが帰ってくる 012345~
print(m.find('文字'))
#ない時は -1
print(m.find('jふぃえじふぇ'))

