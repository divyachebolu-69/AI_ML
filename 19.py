import pandas as pd

data = {
    "Name":    ["Ravi", "Sita", "Anil", "Priya", "Kiran", "Lakshmi"],
    "Branch":  ["ECE", "CSE", "ECE", "CSE", "ECE", "CSE"],
    "Maths":   [78, 92, 65, 88, None, 95],
    "Physics": [82, 85, 70, 91, 60, 89]
}

df = pd.DataFrame(data)
print(df)