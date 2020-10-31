'''
[式 for 任意の変数名 in イテラブルオブジェクト]
'''

order = []
for i in range(5):
    order.append(i)
print(order)

#for文
order = [i for i in range(5)]
print(order)

order = [i*i for i in range(5)]
print(order)

#if文を絡ませる
order = [i for i in range(11) if i % 2 == 0]
print(order)