
"""
What is Pandas?

Pandas is a Python library used for working with data sets.

It has functions for analyzing, cleaning, exploring, and manipulating data.

The name "Pandas" has a reference to both "Panel Data",
    and "Python Data Analysis" and was created by Wes McKinney in 2008.

"""

import pandas as pd



mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}

myvar = pd.DataFrame(mydataset)

print(myvar)
"""
    cars  passings
0    BMW         3
1  Volvo         7
2   Ford         2
"""









"""
What is a Series?

A Pandas Series is like a column in a table.

It is a one-dimensional array holding data of any type.
"""

a = [1, 7, 2]

myvar = pd.Series(a)

print(myvar)
"""
0    1
1    7
2    2
"""



print(myvar[0])
#1





"""
Create Labels

With the index argument, you can name your own labels.

"""

a = [1, 7, 2]

myvar = pd.Series(a, index = ["x", "y", "z"])

print(myvar)
"""
x    1
y    7
z    2
"""







"""
Key/Value Objects as Series

You can also use a key/value object, like a dictionary, when creating a Series.

"""

calories = {"day1": 420, "day2": 380, "day3": 390}

myvar = pd.Series(calories)

print(myvar)
"""
day1    420
day2    380
day3    390
"""








"""
DataFrames

Data sets in Pandas are usually multi-dimensional tables, called DataFrames.

Series is like a column, a DataFrame is the whole table.
"""


data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

myvar = pd.DataFrame(data)

print(myvar)
"""
   calories  duration
0       420        50
1       380        40
2       390        45
"""











"""
Locate Row

As you can see from the result above, the DataFrame is like a table with rows and columns.

Pandas use the loc attribute to return one or more specified row(s)
"""

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

df = pd.DataFrame(data)

print(df.loc[0])
"""
calories    420
duration     50
"""


print(df.loc[[0, 1]])
"""
   calories  duration
0       420        50
1       380        40
"""










data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

df = pd.DataFrame(data, index = ["day1", "day2", "day3"])


print(df)
"""
      calories  duration
day1       420        50
day2       380        40
day3       390        45
"""


print(df.loc["day2"])
"""
calories    380
duration     40
Name: day2, dtype: int64
"""



df = pd.read_csv("/Users/benjaminbrooke/.cache/kagglehub/datasets/mirichoi0218/insurance/versions/1/insurance.csv")

print(df)
"""
Name: day2, dtype: int64
      age     sex     bmi  children smoker     region      charges
0      19  female  27.900         0    yes  southwest  16884.92400
1      18    male  33.770         1     no  southeast   1725.55230
2      28    male  33.000         3     no  southeast   4449.46200
3      33    male  22.705         0     no  northwest  21984.47061
4      32    male  28.880         0     no  northwest   3866.85520
...   ...     ...     ...       ...    ...        ...          ...
1333   50    male  30.970         3     no  northwest  10600.54830
1334   18  female  31.920         0     no  northeast   2205.98080
1335   18  female  36.850         0     no  southeast   1629.83350
1336   21  female  25.800         0     no  southwest   2007.94500
1337   61  female  29.070         0    yes  northwest  29141.36030

[1338 rows x 7 columns]
"""




print(df.head(10))
"""
   age     sex     bmi  children smoker     region      charges
0   19  female  27.900         0    yes  southwest  16884.92400
1   18    male  33.770         1     no  southeast   1725.55230
2   28    male  33.000         3     no  southeast   4449.46200
3   33    male  22.705         0     no  northwest  21984.47061
4   32    male  28.880         0     no  northwest   3866.85520
5   31  female  25.740         0     no  southeast   3756.62160
6   46  female  33.440         1     no  southeast   8240.58960
7   37  female  27.740         3     no  northwest   7281.50560
8   37    male  29.830         2     no  northeast   6406.41070
9   60  female  25.840         0     no  northwest  28923.13692
"""




print(df.tail())
"""
      age     sex    bmi  children smoker     region     charges
1333   50    male  30.97         3     no  northwest  10600.5483
1334   18  female  31.92         0     no  northeast   2205.9808
1335   18  female  36.85         0     no  southeast   1629.8335
1336   21  female  25.80         0     no  southwest   2007.9450
1337   61  female  29.07         0    yes  northwest  29141.3603
"""



print(df.info())
"""
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 1338 entries, 0 to 1337
Data columns (total 7 columns):
 #   Column    Non-Null Count  Dtype  
---  ------    --------------  -----  
 0   age       1338 non-null   int64  
 1   sex       1338 non-null   object 
 2   bmi       1338 non-null   float64
 3   children  1338 non-null   int64  
 4   smoker    1338 non-null   object 
 5   region    1338 non-null   object 
 6   charges   1338 non-null   float64
dtypes: float64(2), int64(2), object(3)
memory usage: 73.3+ KB
"""

















"""
Data Cleaning

Data cleaning means fixing bad data in your data set.

Bad data could be:
    Empty cells
    Data in wrong format
    Wrong data
    Duplicates


In this tutorial you will learn how to deal with all of them.
"""







"""
Remove Rows

One way to deal with empty cells is to remove rows that contain empty cells.

This is usually OK, since data sets can be very big, 
  and removing a few rows will not have a big impact on the result.
"""



new_df = df.dropna()

print(new_df.to_string())
"""
      age     sex     bmi  children smoker     region       charges
0      19  female  27.900         0    yes  southwest  16884.924000
1      18    male  33.770         1     no  southeast   1725.552300
2      28    male  33.000         3     no  southeast   4449.462000
3      33    male  22.705         0     no  northwest  21984.470610
4      32    male  28.880         0     no  northwest   3866.855200
5      31  female  25.740         0     no  southeast   3756.621600
6      46  female  33.440         1     no  southeast   8240.589600
7      37  female  27.740         3     no  northwest   7281.505600
8      37    male  29.830         2     no  northeast   6406.410700
9      60  female  25.840         0     no  northwest  28923.136920
10     25    male  26.220         0     no  northeast   2721.320800
11     62  female  26.290         0    yes  southeast  27808.725100
12     23    male  
"""






# If you want to change the original DataFrame, use the inplace = True argument:

df.dropna(inplace = True)

"""
Note: Now, the dropna(inplace = True) will NOT return a new DataFrame,
    but it will remove all rows containing NULL values from the original DataFrame.
"""






"""
Replace Empty Values

Another way of dealing with empty cells is to insert a new value instead.

This way you do not have to delete entire rows just because of some empty cells.

The fillna() method allows us to replace empty cells with a value:
"""

import pandas as pd

#Replace NULL values with the number "FILL_IN":
df.fillna("FILL_IN", inplace = True)











"""
Replace Only For Specified Columns

The example above replaces all empty cells in the whole Data Frame.

To only replace empty values for one column, specify the column name for the DataFrame:
"""

df["sex"] = df["sex"].fillna("FILL")


"""
df["sex"] = df["sex"].fillna("FILL")

This directly modifies the "sex" column in the original
 DataFrame, replacing any missing values (NaN) with the value "FILL".

It modifies the original DataFrame in-place and leaves the
 other columns in the DataFrame unaffected.
"""



"""
df = df["sex"].fillna("FILL")
This creates a new pandas Series with
 the "sex" column filled with the value
  "FILL" wherever there are missing values.

It doesn’t modify the original DataFrame,
 and you would need to reassign it to df
  for the changes to persist in the DataFrame.

This approach will return only the filled
 column and will not affect the rest of the DataFrame.
"""


















"""
Replace Using Mean, Median, or Mode

A common way to replace empty cells, is to calculate the mean,
    median or mode value of the column.

Pandas uses the mean() median() and mode() methods
  to calculate the respective values for a specified column:
"""


x = df["bmi"].mean()

df["bmi"] = df["bmi"].fillna(x)




x = df["bmi"].median()

df["bmi"] = df["bmi"].fillna(x)












"""
Convert Into a Correct Format

In our Data Frame, we have two cells with the wrong format. 
  Check out row 22 and 26, the 'Date' 
  column should be a string that represents a date:
"""
#df['Date'] = pd.to_datetime(df['Date'])

#print(df.to_string())















"""
For small data sets you might be able to replace the wrong
  data one by one, but not for big data sets.

To replace wrong data for larger data sets you can create some rules,
  e.g. set some boundaries for legal values, and replace any
   values that are outside of the boundaries.




Replacing Values

One way to fix wrong values is to replace them with something else.

In our example, it is most likely a typo, and the value should be 
  "45" instead of "450", and we could just insert "45" in row 7:
"""


#Set "Duration" = 45 in row 7:

df.loc[7, 'age'] = 45














"""
Another way of handling wrong data is to
  remove the rows that contains wrong data.

This way you do not have to find out what to
  replace them with, and there is a good chance you do not need them to do your analyses.

"""

"""
Loop through all values in the "Duration" column.

If the value is higher than 120, set it to 120:
"""

for x in df.index:
  if df.loc[x, "age"] > 120:
    df.loc[x, "age"] = 120













"""
Another way of handling wrong data is to remove the rows that contains wrong data.

This way you do not have to find out what to
 replace them with, and there is
  a good chance you do not need them to do your analyses.
"""

#Delete rows where "Duration" is higher than 120:

for x in df.index:
  if df.loc[x, "age"] > 120:
    df.drop(x, inplace = True)










"""
Removing Duplicates

To remove duplicates, use the drop_duplicates() method.
"""

df.drop_duplicates(inplace = True)











#SELECT()

print(df["age"])
"""
0       19
1       18
2       28
3       33
4       32
        ..
1333    50
1334    18
1335    18
1336    21
1337    61
"""




print(df[["sex","bmi"]])
"""
         sex     bmi
0     female  27.900
1       male  33.770
2       male  33.000
3       male  22.705
4       male  28.880
...      ...     ...
1333    male  30.970
1334  female  31.920
1335  female  36.850
1336  female  25.800
1337  female  29.070
"""










print(df[df['age'] > 25])
"""
      age     sex     bmi  children smoker     region      charges
2      28    male  33.000         3     no  southeast   4449.46200
3      33    male  22.705         0     no  northwest  21984.47061
4      32    male  28.880         0     no  northwest   3866.85520
5      31  female  25.740         0     no  southeast   3756.62160
6      46  female  33.440         1     no  southeast   8240.58960
...   ...     ...     ...       ...    ...        ...          ...
1329   52    male  38.600         2     no  southwest  10325.20600
1330   57  female  25.740         2     no  southeast  12629.16560
1332   52  female  44.700         3     no  southwest  11411.68500
1333   50    male  30.970         3     no  northwest  10600.54830
1337   61  female  29.070         0    yes  northwest  29141.36030
"""




group_df = df.groupby("sex").mean("age")
print(group_df)
"""
              age        bmi  children       charges
sex                                                 
female  39.515106  30.377749  1.074018  12569.578844
male    38.946667  30.943652  1.117037  13974.998864
"""





df = df.head(10)
print(df.sort_values("age"))
"""
1   18    male  33.770         1     no  southeast   1725.55230
0   19  female  27.900         0    yes  southwest  16884.92400
2   28    male  33.000         3     no  southeast   4449.46200
5   31  female  25.740         0     no  southeast   3756.62160
4   32    male  28.880         0     no  northwest   3866.85520
3   33    male  22.705         0     no  northwest  21984.47061
8   37    male  29.830         2     no  northeast   6406.41070
7   45  female  27.740         3     no  northwest   7281.50560
6   46  female  33.440         1     no  southeast   8240.58960
9   60  female  25.840         0     no  northwest  28923.13692
"""