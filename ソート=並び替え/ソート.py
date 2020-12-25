#リスト
org_list = [3, 1, 4, 5, 2]

'''昇順'''
org_list.sort()
print(org_list)

'''降順'''
org_list.sort(reverse=True)
print(org_list)

org_list = [3, 1, 4, 5, 2]

new_list = sorted(org_list)
print(org_list)
print(new_list)

new_list_reverse = sorted(org_list, reverse=True)
print(org_list)
print(new_list_reverse)

#文字列
org_str = 'cebad'

new_str_list = sorted(org_str)
print(org_str)
print(new_str_list)

new_str = ''.join(new_str_list)
print(new_str)

new_str = ''.join(sorted(org_str))
print(new_str)

new_str_reverse = ''.join(sorted(org_str, reverse=True))
print(new_str_reverse)

#タプル
org_tuple = (3, 1, 4, 5, 2)

new_tuple_list = sorted(org_tuple)
print(org_tuple)
print(new_tuple_list)

new_tuple = tuple(new_tuple_list)
print(new_tuple)
