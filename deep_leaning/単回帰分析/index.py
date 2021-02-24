import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm

data = pd.read_csv('deep_leaning/単回帰分析/SimpleLinearRegression.csv')
data.describe()
# print(data)

y = data['GPA']
x1 = data['SAT']

plt.scatter(x1, y)
plt.xlabel('SAT', fontsize=20)
plt.ylabel('GPA', fontsize=20)
# plt.show()

x = sm.add_constant(x1)
results = sm.OLS(y,x).fit()
# results.summary()
print(results.summary())