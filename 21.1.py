import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.DataFrame({
    "Branch": ["ECE", "CSE", "ECE", "CSE", "ECE", "CSE", "MECH", "MECH"],
    "Marks":  [70, 88, 65, 92, 75, 85, 60, 68]
})

sns.barplot(data=df, x="Branch", y="Marks")
plt.title("Average Marks by Branch")
plt.show()