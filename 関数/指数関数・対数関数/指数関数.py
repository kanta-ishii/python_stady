'''
ネイピア数
math.exp(x)はeのx乗 しかしmath.exp(x)とmath.e ** xは一緒ではなくてmath.exp(x)の方が正確
'''
import math

print(math.exp(2))
print(math.exp(2) == math.e**2)