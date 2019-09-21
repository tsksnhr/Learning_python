# 二次元配列

import numpy as np

a = np.array([[1,2,3],
            [4,5,6]])

print(a[0,1])
print(a[:,1])
print(a[0,:])

print("---")

print(a[1,1:])
print(a[1,:1])
print(a[1:,2])