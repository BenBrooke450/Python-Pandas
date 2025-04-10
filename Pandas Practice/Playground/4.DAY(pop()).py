




import pandas as pd
import numpy as np
from sklearn.datasets import load_iris, fetch_california_housing

housing = fetch_california_housing()

df = pd.DataFrame(housing.data, columns=housing.feature_names)

print(df)

df.pop("Longitude") # REMOVES INPLACE
# ALSO CAN ONLY REMOVE ONE AT A TIME

df.drop(columns = ["Latitude","AveOccup"],inplace=True) #NEEDS TO PUT INPLACE
#CAN HANDLE MULTIPLE



