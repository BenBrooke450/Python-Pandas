

import pandas as pd
import numpy as np

df = pd.DataFrame({'X':[78,85,96,80,86], 'Y':[84,94,89,83,86],'Z':[86,97,96,72,83]})

print(df)

"""
    X   Y   Z
0  78  84  86
1  85  94  97
2  96  89  96
3  80  83  72
4  86  86  83
"""










df_2 = pd.DataFrame({'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
                     'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
                     'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
                     'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']},
                    index = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'])

print(df_2)
"""
        name  score  attempts qualify
a  Anastasia   12.5         1     yes
b       Dima    9.0         3      no
c  Katherine   16.5         2     yes
d      James    NaN         3      no
e      Emily    9.0         2      no
f    Michael   20.0         3     yes
g    Matthew   14.5         1     yes
h      Laura    NaN         1      no
i      Kevin    8.0         2      no
j      Jonas   19.0         1     yes
"""










"""
3. Write a Pandas program to display a summary of the basic information about a specified DataFrame and its data.
"""

print(df_2.info())
"""
<class 'pandas.core.frame.DataFrame'>
Index: 10 entries, a to j
Data columns (total 4 columns):
 #   Column    Non-Null Count  Dtype  
---  ------    --------------  -----  
 0   name      10 non-null     object 
 1   score     8 non-null      float64
 2   attempts  10 non-null     int64  
 3   qualify   10 non-null     object 
dtypes: float64(1), int64(1), object(2)
memory usage: 400.0+ bytes
"""





