
import pandas as pd
import numpy as np
from sklearn.datasets import load_iris, fetch_california_housing

housing = fetch_california_housing()

df = pd.DataFrame(housing.data, columns=housing.feature_names)

print(df.columns)
"""
Index(['MedInc', 'HouseAge', 'AveRooms', 'AveBedrms', 'Population', 'AveOccup',
       'Latitude', 'Longitude'],
      dtype='object')
"""


print(df.shape)
#(20640, 8)


h = df.HouseAge
print(h.head(5))
"""
0    41.0
1    21.0
2    52.0
3    52.0
4    52.0
Name: HouseAge, dtype: float64
"""



#print(h.dtype())
#THIS WILL THROW AN ERROR AS h IS NO LONGER A DATAFRAME


print(type(h))
#<class 'pandas.core.series.Series'>


print(type(df))
#<class 'pandas.core.frame.DataFrame'>




h = df[["AveRooms"]]
print(type(h))
#<class 'pandas.core.frame.DataFrame'>


g = df["AveRooms"]
print(type(g))
#<class 'pandas.core.series.Series'>


print(g[1:5])
"""
1    6.238137
2    8.288136
3    5.817352
4    6.281853
"""




print(df.iloc[:, 2])
"""
Name: AveRooms, dtype: float64
0        6.984127
1        6.238137
2        8.288136
3        5.817352
4        6.281853
           ...   
20635    5.045455
20636    6.114035
20637    5.205543
20638    5.329513
20639    5.254717
"""



