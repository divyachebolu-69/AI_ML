import numpy as np

X = np.array([[1.0, 200.0, 3.0],
              [2.0, 220.0, 5.0],
              [3.0, 260.0, 9.0],
              [4.0, 300.0, 7.0]])

Z = (X - X.mean(axis=0)) / X.std(axis=0)

print(Z)
print("Column means:", Z.mean(axis=0).round(10))  
print("Column stds: ", Z.std(axis=0))             