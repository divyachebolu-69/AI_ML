import numpy as np

a = np.array([[1, 2, 3],
              [4, 5, 6]])

print(a)
print(a.shape)
print(a.sum(axis=0))
print(a.sum(axis=1))