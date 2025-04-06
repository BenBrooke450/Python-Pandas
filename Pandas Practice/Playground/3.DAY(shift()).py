

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

df = df.sort_values(by = ['HouseAge','AveRooms'])

df["new_column"] = np.where(df['AveRooms'].shift(-1) < (df['AveRooms']/2),"Double_size_previous","Nope")

print(df.head(7))
"""
       MedInc  HouseAge   AveRooms  ...  Latitude  Longitude            new_column
12286  1.6250       1.0   3.000000  ...     33.86    -116.95                  Nope
3130   4.8750       1.0   5.533333  ...     35.08    -117.95                  Nope
18972  5.2636       1.0   7.694030  ...     38.23    -122.00                  Nope
19536  4.2500       1.0  20.125000  ...     37.65    -120.93  Double_size_previous
59     2.5625       2.0   2.771930  ...     37.82    -122.29                  Nope
15736  3.6437       2.0   3.319559  ...     37.78    -122.43                  Nope
17824  4.3750       2.0   4.420233  ...     37.39    -121.89                  Nope
"""














df = df[['MedInc', 'HouseAge', 'AveRooms', 'AveBedrms', 'Population', 'AveOccup']]

df["Avg_rooms_for_age"] = df.groupby("HouseAge")["AveRooms"].transform("mean")

df_Age_one = df.query("HouseAge == 1").copy()

print(df_Age_one)
"""
       MedInc  HouseAge   AveRooms  ...  Population  AveOccup  Avg_rooms_for_age
12286  1.6250       1.0   3.000000  ...         8.0  4.000000           9.088091
3130   4.8750       1.0   5.533333  ...        32.0  2.133333           9.088091
18972  5.2636       1.0   7.694030  ...       872.0  3.253731           9.088091
19536  4.2500       1.0  20.125000  ...       402.0  3.589286           9.088091

[4 rows x 7 columns]
"""










df_Age_one["Med_TEST"] = df_Age_one["MedInc"].shift(-1)
print(df_Age_one)
"""
       MedInc  HouseAge   AveRooms  ...  AveOccup  Avg_rooms_for_age  Med_TEST
12286  1.6250       1.0   3.000000  ...  4.000000           9.088091    4.8750
3130   4.8750       1.0   5.533333  ...  2.133333           9.088091    5.2636
18972  5.2636       1.0   7.694030  ...  3.253731           9.088091    4.2500
19536  4.2500       1.0  20.125000  ...  3.589286           9.088091       NaN
"""











df_Age_one["Med_cheap?"] = np.where(df_Age_one["MedInc"] < df_Age_one["MedInc"].shift(-1),
                                    "cheaper_than_next",
                                    np.where(df_Age_one["MedInc"] > df_Age_one["MedInc"].shift(-1),
                                    "not_cheaper_than_next",None))
print(df_Age_one)
"""
       MedInc  HouseAge  ...  Med_TEST             Med_cheap?
12286  1.6250       1.0  ...    4.8750      cheaper_than_next
3130   4.8750       1.0  ...    5.2636      cheaper_than_next
18972  5.2636       1.0  ...    4.2500  not_cheaper_than_next
19536  4.2500       1.0  ...       NaN                   None
"""




print(df_Age_one.to_string())
"""
        MedInc  HouseAge   AveRooms  AveBedrms  Population  AveOccup  Avg_rooms_for_age  Med_TEST             Med_cheap?
12286  1.6250       1.0   3.000000   1.000000         8.0  4.000000           9.088091    4.8750      cheaper_than_next
3130   4.8750       1.0   5.533333   1.000000        32.0  2.133333           9.088091    5.2636      cheaper_than_next
18972  5.2636       1.0   7.694030   1.279851       872.0  3.253731           9.088091    4.2500  not_cheaper_than_next
19536  4.2500       1.0  20.125000   2.928571       402.0  3.589286           9.088091       NaN                   None
"""


























