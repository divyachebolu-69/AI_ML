import numpy as np

X = np.array([[1, 200, 3],
              [2, 220, 5],
              [3, 260, 9],
              [4, 300, 7]], dtype=float)

Z = (X - X.mean(axis=0)) / X.std(axis=0)
print(Z)