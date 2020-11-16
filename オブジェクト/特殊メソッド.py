'''
object.__repr__(self)
object.__lt__(self, other)
object.__le__(self, other)
object.__eq__(self, other)
object.__ne__(self, other)
object.__gt__(self, other)
object.__ge__(self, other)
これらはいわゆる "拡張比較 (rich comparison)" メソッドです。
演算子シンボルとメソッド名の対応は以下の通りです
    object → __repr__に定義されたものが呼べ出される
    x<y   → x.__lt__(y) を呼び出します; 
    x<=y  → x.__le__(y) を呼び出します; 
    x==y  → x.__eq__(y) を呼び出します; 
    x!=y  → x.__ne__(y) を呼び出します; 
    x>y   → x.__gt__(y) を呼び出します; 
    x>=y  → x.__ge__(y) を呼び出します。
'''


class Num:
    def __init__(self,x):
        self.__x = x

    def __repr__(self):
        print('オブジェクト思考')

    def __lt__(self, other):
        return self.__x < other

    def __le__(self, other):
        return self.__x <= other

    def __eq__(self, other):
        return self.__x == other

    def __ne__(self, other):
        return self.__x != other

    def __gt__(self, other):
        return self.__x > other

    def __ge__(self, other):
        return self.__x >= other

x = Num(100)
print(
    x,
    x < 1000,
    x <= 10,
    x == 10,
    x != 10,
    x > 10,
    x >= 10
)