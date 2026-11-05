import pandas as pd
import numpy as np

df = pd.DataFrame({
    "Name":    ["Ravi", "Sita", "Anil", "Priya", "Kiran"],
    "Maths":   [78, 92, 65, 88, 45],
    "Physics": [82, 85, 70, 91, 60],
    "Chem":    [75, 90, 58, 84, 50]
})

df["Total"] = df[["Maths", "Physics", "Chem"]].sum(axis=1)
df["Average"] = df["Total"] / 3

conditions = [df["Average"] >= 85, df["Average"] >= 70, df["Average"] >= 55]
grades     = ["A", "B", "C"]
df["Grade"] = np.select(conditions, grades, default="Fail")

df["Rank"] = df["Total"].rank(ascending=False, method="min").astype(int)

print(df.sort_values("Rank"))