
import numpy as np
import pandas as pd

df = pd.read_csv("/Users/benjaminbrooke/.cache/kagglehub/datasets/mirichoi0218/insurance/versions/1/insurance.csv")

df = pd.DataFrame(df)

df = df.head(10)


print(df.dtypes)
"""
age           int64
sex          object
bmi         float64
children      int64
smoker       object
region       object
charges     float64
dtype: object
"""









df['Age'] = df['Age'].astype(float)






df['charges_x2'] = df['charges'].apply(lambda x: x*2)



df['charges'] = df['charges'].apply(lambda x: x*2)



df[['age', 'charges']] = df[['age', 'charges']].applymap(lambda x: x + 1)



sampled_df = df.sample(n=3)



filtered_df = df[df['age'].isin([22, 23])]




df['Salary Rank'] = (df['Salary'].rank())
df = df.sort_values('Salary Rank')




