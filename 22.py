import pandas as pd
import numpy as np

df = pd.DataFrame({
    "Name":    ["Ravi", "Sita", "Anil", "Priya", "Kiran", "Lakshmi", "Mohan", "Anitha"],
    "Branch":  ["ECE", "CSE", "ECE", "CSE", "ECE", "CSE", "MECH", "MECH"],
    "City":    ["Rajahmundry", "Kakinada", "Vizag", "Rajahmundry",
                "Kakinada", "Vizag", "Rajahmundry", "Kakinada"],
    "Maths":   [78, 92, 65, 88, None, 95, 55, 72],
    "Physics": [82, 85, 70, 91, 60, 89, 48, 66],
    "Age":     [21, 22, 21, 20, 22, 21, 23, 22]
})