
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
