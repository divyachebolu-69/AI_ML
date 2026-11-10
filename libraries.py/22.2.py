import numpy as np
import pandas as pd
rng = np.random.default_rng(42)
arr = rng.integers(1, 100, size=(4, 3))

df2 = pd.DataFrame(arr, columns=["A", "B", "C"])
print(df2)
print(df2.to_numpy())   