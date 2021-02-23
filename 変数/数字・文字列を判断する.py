import pprint
# int()で判断する方法
def is_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

'''
メソッドによる判別方法
    ・isdecimal()
    ・isdigt()
    ・isnumeric()
'''

pprint.pprint(
    # 数字のみの場合は全てTrue
    '1234'.isdecimal(),
    '1234'.isdigit(),
    '1234'.isnumeric(),
    # 英数字混合の場合はは全てFalse
    '1b34'.isdecimal(),
    '1b34'.isdigit(),
    '1b34'.isnumeric(),
    # 小数はピリオドが数字ではないためFalse
    '1.234'.isdecimal(),
    '1.234'.isdigit(),
    '1.234'.isnumeric(),
    # 全角数字も全てTrue
    '１'.isdecimal(),
    '１'.isdigit(),
    '１'.isnumeric()
    )
