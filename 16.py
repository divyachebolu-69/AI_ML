import numpy as np
x = np.array([1, 2, 3, 4])
y = np.array([10, 20, 30, 40])

print(x + y, x * y, x ** 2)
print(x.sum(), x.mean(), x.max(), x.min())

grid = np.array([[1, 2, 3], [4, 5, 6]])
print(grid.sum(axis=0))   
print(grid.sum(axis=1))   