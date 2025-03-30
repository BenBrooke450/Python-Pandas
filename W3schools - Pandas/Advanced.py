

import numpy as np
import pandas as pd


data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank'],
    'Age': [24, 27, 22, 32, 29, 24],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 'New York'],
    'Salary': [70000, 80000, 65000, 120000, 95000, 68000],
    'Experience': [2, 5, 1, 10, 7, 2]
}



# Convert dictionary to DataFrame
df = pd.DataFrame(data)

df['Salary Rank'] = (df['Salary'].rank())

print(df["City"].value_counts())
