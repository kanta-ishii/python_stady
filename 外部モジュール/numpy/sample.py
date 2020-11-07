import numpy as np

sample = np.array([1,2,3,4,5])
sample2 = np.array([[1,2,3,4,5],[6,7,8,9,10]])
sample3 = np.arange(start=0., stop=10., step=0.1)
tile = np.tile('A', 5)
tile2 = np.tile(0, 5)
zeros = np.zeros(4) #0を並べる(個数)
zeros2 = np.zeros([4,4])
ones = np.ones(4) #1づめも可能


print(
    sample,
    sample2,
    sample2[0,2:3],
    sample3,
    tile,
    tile2,
    zeros,
    zeros2,
    ones
)