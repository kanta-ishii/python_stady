'''
csvファイルを操作する
“r”：読み込み
“w”：書き込み（新規作成。同名のファイルがあれば上書き）
“x”：書き込み（新規作成。同名のファイルがあればエラー）
“a”：書き込み（追記。同名のファイルがあれば末尾に追記）
reader : 読み込む
    delimiter : 分割を指定する
    DictReader : ヘッダーをkeyとして読み込んでくれる
writer : 書き込む
'''

import csv
import pprint

'''読み込み用'''
with open('ファイル操作/csv/sample.csv', 'r') as f:
    # print(f.read())
    reader = csv.DictReader(f)
    l = [row for row in reader]
    print(l)

#一気に読んだりする
with open('ファイル操作/csv/sample.csv') as f:
    l = [[v for v in row] for row in csv.reader(f)]
    print(l)

#空白を指定して分割する、数字に変換したりする  ※ヘッダーがあったりString型の物があるとエラーに
with open('ファイル操作/csv/sample2.csv') as f:
    l = [[int(v) for v in row] for row in csv.reader(f, delimiter=' ')]
    print(l)

with open('ファイル操作/csv/sample.csv') as f:
    l = [row for row in csv.DictReader(f)]
    pprint.pprint(l)

print('====================')
#一行ずつ出力する
with open('ファイル操作/csv/sample.csv') as f:
    reader = csv.DictReader(f)
    for i in reader:
        print(i)
        import time
        time.sleep(1)



'''書き込み用'''
with open('ファイル操作/csv/書き込み用.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow([0, 1, 2])
    writer.writerow(['a', 'b', 'c'])