'''
.describe()
    表示名	        説明	                        Pandasで相当する関数
    count	        データの個数を表します。	      　DataFrame.count,Series.count
    mean	        数値データの平均を表します。	   　DataFrame.mean,Series.mean
    std	            数値データの標準偏差を表します       DataFrame.std, Series.std
    min	            最小値を表します。	               DataFrame.min,Series.min
    max	            最大値を表します。	               DataFrame.max,Series.max
    25%,50%,75%	    四分位数を表します。               DataFrame.quantile,Series.quantile
'''
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
import seaborn as sns
sns.set()

data = pd.read_csv('外部モジュール/pandas/sample.csv')
print(data)
data.head()
data.describe() # csvの中身の概要を出力してくれる


'''result.summary()
                            OLS Regression Results                            
==============================================================================
Dep. Variable:                  price   R-squared:                       0.745
Model:                            OLS   Adj. R-squared:                  0.742
Method:                 Least Squares   F-statistic:                     285.9
Date:                Mon, 22 Feb 2021   Prob (F-statistic):           8.13e-31
Time:                        15:30:34   Log-Likelihood:                -1198.3
No. Observations:                 100   AIC:                             2401.
Df Residuals:                      98   BIC:                             2406.
Df Model:                           1                                         
Covariance Type:            nonrobust                                         
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
const       1.019e+05   1.19e+04      8.550      0.000    7.83e+04    1.26e+05
size         223.1787     13.199     16.909      0.000     196.986     249.371
==============================================================================
Omnibus:                        6.262   Durbin-Watson:                   2.267
Prob(Omnibus):                  0.044   Jarque-Bera (JB):                2.938
Skew:                           0.117   Prob(JB):                        0.230
Kurtosis:                       2.194   Cond. No.                     2.75e+03
==============================================================================
'''
y = data['price']
x1 = data['size']
x = sm.add_constant(x1)
result = sm.OLS(y, x).fit()
print(result.summary())

