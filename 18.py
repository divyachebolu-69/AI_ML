import pandas as pd

data = {
    "Item":  ["Rice", "Oil", "Sugar", "Milk"],
    "Price": [60, 150, 45, 30],
    "Qty":   [5, 2, 4, 10]
}

df = pd.DataFrame(data)
df["Total"] = df["Price"] * df["Qty"]    

print(df)
print(df[df["Total"] > 250])             