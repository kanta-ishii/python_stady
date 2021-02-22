'''
すべての要素を削除: clear()
指定した位置の要素を削除し、値を取得: pop()
指定した値と同じ要素を検索し、最初の要素を削除: remove()
インデックス・スライスで位置・範囲を指定して削除: del
条件を満たす複数の要素を一括で削除: リスト内包表記
'''

l = list(range(10))
l.clear()

l = list(range(10))
print(l.pop(0))

l = ['Alice', 'Bob', 'Charlie', 'Bob', 'Dave']
l.remove('Alice')

l = list(range(10))
del l[2:5]