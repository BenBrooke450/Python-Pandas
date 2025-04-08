

import pandas as pd
import numpy as np
from sklearn.datasets import load_iris, fetch_california_housing

housing = fetch_california_housing()

df = pd.DataFrame(housing.data, columns=housing.feature_names)

print(df)


print(df.iloc[1:3])
"""
   MedInc  HouseAge  AveRooms  ...  AveOccup  Latitude  Longitude
1  8.3014      21.0  6.238137  ...  2.109842     37.86    -122.22
2  7.2574      52.0  8.288136  ...  2.802260     37.85    -122.24

[2 rows x 8 columns]
"""




print(df.iloc[1:3,1:4])
"""
   HouseAge  AveRooms  AveBedrms
1      21.0  6.238137   0.971880
2      52.0  8.288136   1.073446
"""


