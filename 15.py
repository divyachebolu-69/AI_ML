import numpy as np
arr = np.array([[10, 20, 30],
                [40, 50, 60],
                [70, 80, 90]])

print(arr[1, 2])         
print(arr[:, 0])       
print(arr[1:, :2])    

mask = arr > 40
print(arr[mask])    
arr[arr > 80] = 0      