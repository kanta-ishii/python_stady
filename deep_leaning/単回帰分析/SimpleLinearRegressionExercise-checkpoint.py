import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from seaborn.rcmod import reset_defaults
import statsmodels.api as sm
import seaborn as sns
sns.set()

data = pd.read_csv('deep_leaning/単回帰分析/real_estate_price_size.csv')
# print(data)
data.head()
print(data.describe()) # csvの中身の概要を出力してくれる

y = data['price']
x1 = data['size']

plt.scatter(x1, y)
plt.xlabel('size', size=20)
plt.xlabel('price', size=20)
# plt.show()


'''回帰の実行'''
x = sm.add_constant(x1)
result = sm.OLS(y, x).fit()
print(result.summary())

plt.scatter(x1,y)
yhat = x1*223.1787+101900
fig = plt.plot(x1,yhat, lw=4, c='orange', label ='regression line')
plt.xlabel('Size', fontsize = 20)
plt.ylabel('Price', fontsize = 20)
plt.show()