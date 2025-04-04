
import pandas as pd
from sklearn import datasets
import numpy as np

# Load the Iris dataset
iris = datasets.load_iris()

df = pd.DataFrame(iris.data, columns=iris.feature_names)

df["ceil_sepal"] = df["sepal length (cm)"].apply(np.ceil)

print(df)
"""
     sepal length (cm)  sepal width (cm)  ...  petal width (cm)  ceil_sepal
0                  5.1               3.5  ...               0.2         6.0
1                  4.9               3.0  ...               0.2         5.0
2                  4.7               3.2  ...               0.2         5.0
3                  4.6               3.1  ...               0.2         5.0
4                  5.0               3.6  ...               0.2         5.0
..                 ...               ...  ...               ...         ...
145                6.7               3.0  ...               2.3         7.0
146                6.3               2.5  ...               1.9         7.0
147                6.5               3.0  ...               2.0         7.0
148                6.2               3.4  ...               2.3         7.0
149                5.9               3.0  ...               1.8         6.0

[150 rows x 5 columns]
"""








df["floor_sepal"] = df["sepal length (cm)"].apply(np.floor)

print(df)
"""
    sepal length (cm)  sepal width (cm)  ...  ceil_sepal  floor_sepal
0                  5.1               3.5  ...         6.0          5.0
1                  4.9               3.0  ...         5.0          4.0
2                  4.7               3.2  ...         5.0          4.0
3                  4.6               3.1  ...         5.0          4.0
4                  5.0               3.6  ...         5.0          5.0
..                 ...               ...  ...         ...          ...
145                6.7               3.0  ...         7.0          6.0
146                6.3               2.5  ...         7.0          6.0
147                6.5               3.0  ...         7.0          6.0
148                6.2               3.4  ...         7.0          6.0
149                5.9               3.0  ...         6.0          5.0

[150 rows x 6 columns]
"""





df.drop(columns = {"floor_sepal","ceil_sepal"},inplace=True)

print(df)
"""
     sepal length (cm)  sepal width (cm)  petal length (cm)  petal width (cm)
0                  5.1               3.5                1.4               0.2
1                  4.9               3.0                1.4               0.2
2                  4.7               3.2                1.3               0.2
3                  4.6               3.1                1.5               0.2
4                  5.0               3.6                1.4               0.2
..                 ...               ...                ...               ...
145                6.7               3.0                5.2               2.3
146                6.3               2.5                5.0               1.9
147                6.5               3.0                5.2               2.0
148                6.2               3.4                5.4               2.3
149                5.9               3.0                5.1               1.8

[150 rows x 4 columns]
"""



print(df.columns)
"""
Index(['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)',
       'petal width (cm)'],
"""




df = df.dropna()

df["sepal_area"] = df["sepal length (cm)"] * df["sepal width (cm)"]

df["petal_area"] = df["petal length (cm)"] * df["petal width (cm)"]

print(df)
"""
     sepal length (cm)  sepal width (cm)  ...  sepal_area  petal_area
0                  5.1               3.5  ...       17.85        0.28
1                  4.9               3.0  ...       14.70        0.28
2                  4.7               3.2  ...       15.04        0.26
3                  4.6               3.1  ...       14.26        0.30
4                  5.0               3.6  ...       18.00        0.28
..                 ...               ...  ...         ...         ...
145                6.7               3.0  ...       20.10       11.96
146                6.3               2.5  ...       15.75        9.50
147                6.5               3.0  ...       19.50       10.40
148                6.2               3.4  ...       21.08       12.42
149                5.9               3.0  ...       17.70        9.18

[150 rows x 6 columns]
"""





df_1 = df["sepal length (cm)"] < 3
print(df_1)
"""
0      False
1      False
2      False
3      False
4      False
       ...  
145    False
146    False
147    False
148    False
149    False
Name: sepal length (cm), Length: 150, dtype: bool
"""







df = df[df["sepal length (cm)"] < 5]
print(df)
"""
     sepal length (cm)  sepal width (cm)  ...  sepal_area  petal_area
1                  4.9               3.0  ...       14.70        0.28
2                  4.7               3.2  ...       15.04        0.26
3                  4.6               3.1  ...       14.26        0.30
6                  4.6               3.4  ...       15.64        0.42
8                  4.4               2.9  ...       12.76        0.28
9                  4.9               3.1  ...       15.19        0.15
11                 4.8               3.4  ...       16.32        0.32
12                 4.8               3.0  ...       14.40        0.14
13                 4.3               3.0  ...       12.90        0.11
22                 4.6               3.6  ...       16.56        0.20
24                 4.8               3.4  ...       16.32        0.38
29                 4.7               3.2  ...       15.04        0.32
30                 4.8               3.1  ...       14.88        0.32
34                 4.9               3.1  ...       15.19        0.30
37                 4.9               3.6  ...       17.64        0.14
38                 4.4               3.0  ...       13.20        0.26
41                 4.5               2.3  ...       10.35        0.39
42                 4.4               3.2  ...       14.08        0.26
45                 4.8               3.0  ...       14.40        0.42
47                 4.6               3.2  ...       14.72        0.28
57                 4.9               2.4  ...       11.76        3.30
106                4.9               2.5  ...       12.25        7.65

[22 rows x 6 columns]
"""







df["count"] = df.apply(lambda row: row.sum(),axis=1)

print(df.head())
"""
   sepal length (cm)  sepal width (cm)  ...  petal_area  count
1                4.9               3.0  ...        0.28  24.48
2                4.7               3.2  ...        0.26  24.70
3                4.6               3.1  ...        0.30  23.96
6                4.6               3.4  ...        0.42  25.76
8                4.4               2.9  ...        0.28  21.94

[5 rows x 7 columns]
"""






df['classification'] = df['count'].apply(lambda x: 'High' if x > 25 else 'Low')

print(df.head(15))
"""
    sepal length (cm)  sepal width (cm)  ...  count  classification
1                 4.9               3.0  ...  24.48             Low
2                 4.7               3.2  ...  24.70             Low
3                 4.6               3.1  ...  23.96             Low
6                 4.6               3.4  ...  25.76            High
8                 4.4               2.9  ...  21.94             Low
9                 4.9               3.1  ...  24.94             Low
11                4.8               3.4  ...  26.64            High
12                4.8               3.0  ...  23.84             Low
13                4.3               3.0  ...  21.51             Low
22                4.6               3.6  ...  26.16            High
24                4.8               3.4  ...  27.00            High
29                4.7               3.2  ...  25.06            High
30                4.8               3.1  ...  24.90             Low
34                4.9               3.1  ...  25.19            High
37                4.9               3.6  ...  27.78            High

[15 rows x 8 columns]
"""












df['transformed_score'] = df['count'].apply(lambda x: x * 1.1 if x > 80 else x * 1.05)

print(df.head(10))
"""
    sepal length (cm)  sepal width (cm)  ...  classification  transformed_score
1                 4.9               3.0  ...             Low            25.7040
2                 4.7               3.2  ...             Low            25.9350
3                 4.6               3.1  ...             Low            25.1580
6                 4.6               3.4  ...            High            27.0480
8                 4.4               2.9  ...             Low            23.0370
9                 4.9               3.1  ...             Low            26.1870
11                4.8               3.4  ...            High            27.9720
12                4.8               3.0  ...             Low            25.0320
13                4.3               3.0  ...             Low            22.5855
22                4.6               3.6  ...            High            27.4680

[10 rows x 9 columns]
"""








df['classification_upper'] = df['classification'].apply(lambda x: x.upper())

print(df)







