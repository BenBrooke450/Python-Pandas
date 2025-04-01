



# https://www.w3resource.com/python-exercises/pandas/index-data-series.php


import pandas as pd
import numpy as np

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank'],
    'Age': [24, 27, 22, 32, 29, 24],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 'New York'],
    'Salary': [70000, 80000, 65000, 120000, 95000, 68000],
    'Experience': [2, 5, 1, 10, 7, 2]
}

df = pd.DataFrame(data)







"""
2. Write a Pandas program to convert a Panda module Series to Python list and it's type.
"""
list_name = list(df["Name"])

print(list_name)
#['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank']









"""
3. Write a Pandas program to add, subtract, multiple and divide two Pandas Series.
Sample Series: [2, 4, 6, 8, 10], [1, 3, 5, 7, 9]
"""

s_pd = pd.Series([2, 4, 6, 8, 10])
s_df_2 = pd.Series([1, 3, 5, 7, 9])

print(s_pd + s_df_2)
"""
0     3
1     7
2    11
3    15
4    19
"""


print(s_pd - s_df_2)
"""
0    1
1    1
2    1
3    1
4    1
"""









"""
4. Write a Pandas program to compare the elements of the two Pandas Series.
Sample Series: [2, 4, 6, 8, 10], [1, 3, 5, 7, 10]
"""












"""
5. Write a Pandas program to convert a dictionary to a Pandas series.
"""

dic1 = {'a': 100, 'b': 200, 'c': 300, 'd': 400, 'e': 800}

series = pd.Series(dic1)

print(series)
"""
a    100
b    200
c    300
d    400
e    800
"""









"""
7. Write a Pandas program to change the data type of given a column or a Series.
"""

s = pd.Series([100, 200, "python", 300.12, 400])

s_int = pd.to_numeric(s,errors='coerce')

print(s_int)
"""
0    100.00
1    200.00
2       NaN
3    300.12
4    400.00
"""












"""
11. Write a Pandas program to sort a given Series.
"""


data = {
    'Integer_Column': np.arange(1, 21),  # Integers from 1 to 20
    'Float_Column': np.linspace(0, 1, 20),  # Floats from 0 to 1 evenly spaced
    'String_Column': ['Row_' + str(i) for i in range(1, 21)],  # Strings like 'Row_1', 'Row_2', ...
    'Date_Column': pd.date_range('2025-01-01', periods=20, freq='D')  # Dates from 2025-01-01 onwards
}

df = pd.DataFrame(data)

df = df.sort_values("Integer_Column",ascending = False)

print(df)
"""
    Integer_Column  Float_Column String_Column Date_Column
19              20      1.000000        Row_20  2025-01-20
18              19      0.947368        Row_19  2025-01-19
17              18      0.894737        Row_18  2025-01-18
16              17      0.842105        Row_17  2025-01-17
15              16      0.789474        Row_16  2025-01-16
14              15      0.736842        Row_15  2025-01-15
13              14      0.684211        Row_14  2025-01-14
12              13      0.631579        Row_13  2025-01-13
11              12      0.578947        Row_12  2025-01-12
10              11      0.526316        Row_11  2025-01-11
9               10      0.473684        Row_10  2025-01-10
8                9      0.421053         Row_9  2025-01-09
7                8      0.368421         Row_8  2025-01-08
6                7      0.315789         Row_7  2025-01-07
5                6      0.263158         Row_6  2025-01-06
4                5      0.210526         Row_5  2025-01-05
3                4      0.157895         Row_4  2025-01-04
2                3      0.105263         Row_3  2025-01-03
1                2      0.052632         Row_2  2025-01-02
0                1      0.000000         Row_1  2025-01-01
"""










"""
12. Write a Pandas program to add some data to an existing Series.
"""





df.loc[18,"String_Column"] = "Row_24"

print(df.head(5))
"""
    Integer_Column  Float_Column String_Column Date_Column
19              20      1.000000        Row_20  2025-01-20
18              19      0.947368        Row_24  2025-01-19
17              18      0.894737        Row_18  2025-01-18
16              17      0.842105        Row_17  2025-01-17
15              16      0.789474        Row_16  2025-01-16
"""






print(df.iloc[0:4])
"""
    Integer_Column  Float_Column String_Column Date_Column
19              20      1.000000        Row_20  2025-01-20
18              19      0.947368        Row_24  2025-01-19
17              18      0.894737        Row_18  2025-01-18
16              17      0.842105        Row_17  2025-01-17
"""



print(df.iloc[0:4,1])
"""
19    1.000000
18    0.947368
17    0.894737
16    0.842105
"""












"""
13. Write a Pandas program to create a subset of a given series based on value and condition.
"""


df =  df[df["Integer_Column"] < 6]

print(df)
"""
   Integer_Column  Float_Column String_Column Date_Column
4               5      0.210526         Row_5  2025-01-05
3               4      0.157895         Row_4  2025-01-04
2               3      0.105263         Row_3  2025-01-03
1               2      0.052632         Row_2  2025-01-02
0               1      0.000000         Row_1  2025-01-01
"""





print(df.describe())
"""
       Integer_Column  Float_Column          Date_Column
count        5.000000      5.000000                    5
mean         3.000000      0.105263  2025-01-03 00:00:00
min          1.000000      0.000000  2025-01-01 00:00:00
25%          2.000000      0.052632  2025-01-02 00:00:00
50%          3.000000      0.105263  2025-01-03 00:00:00
75%          4.000000      0.157895  2025-01-04 00:00:00
max          5.000000      0.210526  2025-01-05 00:00:00
std          1.581139      0.083218                  NaN
"""



print(np.std(df["Float_Column"]))
#0.07443229275647868


print(np.mean(df["Float_Column"]))
#0.10526315789473684











"""
16. Write a Pandas program to get the items of a given series not present in another given series.
"""

s_1 = pd.Series(range(4,10))

s_2 = pd.Series(range(0,6))

print(np.intersect1d(s_1,s_2))
#[4 5]








"""
17. Write a Pandas program to get the items which are not common of two given series.
"""

print(np.setxor1d(s_1,s_2))
#[0 1 2 3 6 7 8 9]













"""
19. Write a Pandas program to calculate the frequency counts of each unique value of a given series.
"""

df["Count_values"] = df["Float_Column"].value_counts()










"""
20. Write a Pandas program to display most frequent value in a given series and replace everything else as 'Other' in the series.
"""

df = df.sort_values("Count_values")

top_values = list(df.iloc[0:2,-1])

df["Float_Column"] = np.where(df["Float_Column"].isin(top_values),df["Float_Column"],"Other")














"""
21. Write a Pandas program to find the positions of numbers that are multiples of 5 of a given series.
"""


i = 0
for n in pd.Series(range(0,50)):
    i = i + 1
    if n % 5 == 0:
        print(i)
"""
1
6
11
16
21
26
31
36
41
46
"""







"""
26. Write a Pandas program to compute difference of differences between consecutive numbers of a given series.
"""


x = ["01 Jan 2015", "10-02-2016", "20180307", "2014/05/06", "2016-04-12", "2019-04-06T11:20"]

x = pd.Series(x)
print(x)
"""
0         01 Jan 2015
1          10-02-2016
2            20180307
3          2014/05/06
4          2016-04-12
5    2019-04-06T11:20
"""

x = pd.to_datetime(x,format='mixed')
print(x)
"""
0   2015-01-01 00:00:00
1   2016-10-02 00:00:00
2   2018-03-07 00:00:00
3   2014-05-06 00:00:00
4   2016-04-12 00:00:00
5   2019-04-06 11:20:00
"""






from collections import Counter

color_series = pd.Series(["Red","Green","Blue","Yellow","Cyan","Magenta","Black","White","Orange","Purple"])
vowels = ["o","u","a","i","e"]

color_series.map(lambda c: sum([Counter(c.lower()).get(i, 0) for i in list('aeiou')]) >= 2)















"""
32. Write a Pandas program to find the positions of the values
    neighboured by smaller values on both sides in a given series.
"""


df = pd.DataFrame({'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
                   'Sales': [200, 220, 210, 300, 360, 310]})
print((df))
"""
  Month  Sales
0   Jan    200
1   Feb    220
2   Mar    250
3   Apr    300
4   May    280
5   Jun    310
"""

df['Shifted_Sales_down'] = df['Sales'].shift(1)
df['Shifted_Sales_up'] = df['Sales'].shift(-1)

print(df)
"""
  Month  Sales  Shifted_Sales_down  Shifted_Sales_up
0   Jan    200                 NaN             220.0
1   Feb    220               200.0             250.0
2   Mar    250               220.0             300.0
3   Apr    300               250.0             280.0
4   May    280               300.0             310.0
5   Jun    310               280.0               NaN
"""






df["Biggest_above_and_below"] = np.where((df['Sales'].shift(1) < df['Sales'])
                                         & (df['Sales'] > df['Sales'].shift(-1)),"Yes"," ")

print(df)
"""
  Month  Sales  Shifted_Sales_down  Shifted_Sales_up Biggest_above_and_below
0   Jan    200                 NaN             220.0                        
1   Feb    220               200.0             210.0                     Yes
2   Mar    210               220.0             300.0                        
3   Apr    300               210.0             360.0                        
4   May    360               300.0             310.0                     Yes
5   Jun    310               360.0               NaN        
"""





df["Biggest_above_and_below"] = df["Biggest_above_and_below"].replace(" ","Replaced blank space")

print(df)
"""
  Month  Sales  Shifted_Sales_down  Shifted_Sales_up Biggest_above_and_below
0   Jan    200                 NaN             220.0    Replaced blank space
1   Feb    220               200.0             210.0                     Yes
2   Mar    210               220.0             300.0    Replaced blank space
3   Apr    300               210.0             360.0    Replaced blank space
4   May    360               300.0             310.0                     Yes
5   Jun    310               360.0               NaN    Replaced blank space
"""





df.dropna(inplace=True)

print(df)
"""
   Month  Sales  Shifted_Sales_down  Shifted_Sales_up Biggest_above_and_below
1   Feb    220               200.0             210.0                     Yes
2   Mar    210               220.0             300.0    Replaced blank space
3   Apr    300               210.0             360.0    Replaced blank space
4   May    360               300.0             310.0                     Yes
"""














"""
33. Write a Pandas program to replace missing white 
    spaces in a given string with the most frequent character.
"""

df = pd.DataFrame({'Month': ['Jan', ' ', 'Mar', ' ', 'May', 'Jun'],
                   'Sales': [2, 2, 2, 3, 4, 4]})
print(df)
"""
  Month  Sales
0   Jan      2
1            2
2   Mar      2
3            3
4   May      4
5   Jun      4
"""





most_frequent_value = max(set(df["Sales"]), key=list(df["Sales"]).count)

df["Month"] = df["Month"].replace(" ",most_frequent_value)

print(df)
"""
  Month  Sales
0   Jan      2
1     2      2
2   Mar      2
3     2      3
4   May      4
5   Jun      4
"""













"""
37. Write a Pandas program to stack two given series vertically and horizontally.
"""

df_1 = pd.DataFrame({'Month': ['Jan', ' ', 'Mar', ' ', 'May', 'Jun'],
                   'Sales': [2, 2, 2, 3, 4, 4]})

df_2 = pd.DataFrame({'Month': ['Jan', ' ', 'Mar', ' ', 'May', 'Jun'],
                   'Sales': [2, 2, 2, 3, 4, 4]})


print(pd.concat([df_1, df_2], ignore_index=True, axis=0))
"""
   Month  Sales
0    Jan      2
1             2
2    Mar      2
3             3
4    May      4
5    Jun      4
6    Jan      2
7             2
8    Mar      2
9             3
10   May      4
11   Jun      4
"""







"""
38. Write a Pandas program to check the equality of two given series.
"""











"""
39. Write a Pandas program to find the index of the
    first occurrence of the smallest and largest value of a given series.
"""
series_1 = pd.Series(range(2,16))

df = pd.DataFrame(series_1, columns=['My_range_Name'])

max_1 = max(series_1)
min_1 = min(series_1)

condition_max = df['My_range_Name'] == max_1

condition_min = df['My_range_Name'] == min_1

print(df.index[condition_max])
#Index([13], dtype='int64')

print(df.index[condition_min])
#Index([0], dtype='int64')










