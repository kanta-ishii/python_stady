'''
*と**が頭についていれば他の名前でも問題ない
    *args: 複数の引数をタプルとして受け取る
    **kwargs: 複数のキーワード引数を辞書として受け取る
'''
 
def args(*args):
    return args

def args_s(args1, args2, *args):
    return args1, args2, args

def args_m(args1, *args, args2):
    return args1, args, args2

def kwargs(**kwargs):
    return kwargs

d = {'kwargs1': 1, 'kwargs2': 2, 'arg1': 100, 'arg2': 200}
def kwargs_s(kwargs1, kwargs2, **kwargs):
    return kwargs1, kwargs2, kwargs

#最後に設定することしかできないため以下の文はエラーになる → 確かめる際はコメントアウトを外す
# def kwargs_m(kwargs1, **kwargs, kwargs2):
#     return kwargs1, kwargs, kwargs2


print(
    '*args単体\n',
    args(1, 2, 3, 4),

    '\n複数の引数 = *argsだけタプルに\n',
    args_s(1, 2, 3, 4, 5, 6, 7, 8, 9),

    '\n引数の中間に*argsを指定した場合\n',
    args_m(1, 2, 3, 4, 5, 6, 7, 8, args2=9),

    '\n**kwargs\n',
    kwargs(key1=1, key2=2, key3=3),

    '\n複数の引数\n',
    kwargs_s(0, 1, key1=1),

    '\n逆もできる\n',
    kwargs_s(**d)
)