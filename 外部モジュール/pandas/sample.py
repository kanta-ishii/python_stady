import numpy as np
import pandas as pd


sample = np.array([1,2,3,4,5])
sample2 = np.array([1,2,3,4,5])
sample3 = np.array([6,7,8,9,10])

sample_pd = pd.DataFrame(
    {
        'col': sample,
        'col2': sample2,
        'col3': sample3
    }
)
print(sample_pd)