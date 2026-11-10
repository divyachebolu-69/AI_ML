import pandas as pd
data = {
    "name":   ["Ravi", "Sita", "Karthik", "Divya", "Anil"],
    "maths":  [78, 92, 65, 88, 70],
    "physics": [85, 88, 70, 90, 60],
    "city":   ["Hyd", "Vizag", "Hyd", "Rajahmundry", "Vizag"],
}
df = pd.DataFrame(data)

print(df)
print(df.shape)
print(df.columns.tolist())
df.info()
print(df.describe())