import pandas as pd

customers = pd.DataFrame({"Age": [17, 22, 25, 31, 38, 45, 52, 60, 19, 28]})

customers["AgeGroup"] = pd.cut(
    customers["Age"],
    bins=[0, 18, 30, 45, 100],
    labels=["Teen", "Young", "Adult", "Senior"]
)

print(customers["AgeGroup"].value_counts())